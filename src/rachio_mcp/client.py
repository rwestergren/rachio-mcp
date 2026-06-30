"""Rachio mobile gRPC API client.

Reverse-engineered from the Rachio Android app (v4.21.18). Talks to
``cloud.rach.io:443`` over TLS-protected gRPC with an OAuth 2 bearer
token obtained via the Android app's hardcoded client credentials.

Auth flow (mirrors ``com.rachio.core.auth.OAuthHandler`` in the app):

1. ``POST https://oauth.rach.io/oAuth/token`` with ``grant_type=password``,
   ``username``, ``password``, ``client_id``, and ``client_secret`` from
   ``RachioCoreService.java:215``. Returns an access token (and a
   ``user_id`` field) that lives for many hours.
2. Every gRPC call carries ``authorization: Bearer <token>`` and
   ``client-version: v4 Android 4.21.18`` in the request metadata.

The token is kept in memory for the lifetime of the process. The gRPC
channel is lazily opened on first use and auto-retries once on
``UNAUTHENTICATED`` by re-running the OAuth grant.
"""

from __future__ import annotations

import logging
import os
import sys
from collections.abc import Callable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import grpc
import httpx
from google.protobuf import json_format
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.wrappers_pb2 import BoolValue, Int32Value, StringValue

# ---------------------------------------------------------------------------
# Generated protobuf stubs
#
# The stubs in ``rachio_mcp/proto`` are emitted by grpc-python with bare
# imports (``import core_pb2``) — convenient for us but they expect that
# directory to be on ``sys.path``. Rather than rewrite every import at
# generation time, we add the directory here once, then import the modules
# by their bare names. This is the same pattern the Android app's
# generated Kotlin uses.
# ---------------------------------------------------------------------------

_PROTO_DIR = Path(__file__).parent / "proto"
if str(_PROTO_DIR) not in sys.path:
    sys.path.insert(0, str(_PROTO_DIR))

import core_pb2  # noqa: E402
import device_service_pb2 as dev_svc  # noqa: E402
import device_service_pb2_grpc as dev_grpc  # noqa: E402
import location_service_pb2 as loc_svc  # noqa: E402
import location_service_pb2_grpc as loc_grpc  # noqa: E402
import schedule_criteria_pb2 as sc_pb  # noqa: E402
import schedule_restriction_criteria_pb2 as src_pb  # noqa: E402
import schedule_service_pb2 as svc  # noqa: E402
import schedule_service_pb2_grpc as svc_grpc  # noqa: E402
import schedule_zone_info_pb2 as szi_pb  # noqa: E402

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants extracted from the Android app
# ---------------------------------------------------------------------------

OAUTH_URL = "https://oauth.rach.io/oAuth/token"
OAUTH_CLIENT_ID = "rachio-android-2016-06-03"
OAUTH_CLIENT_SECRET = "c6304649-7d17-4484-a7c7-2211765a2300"
GRPC_TARGET = "cloud.rach.io:443"
CLIENT_VERSION = "v4 Android 4.21.18"

# ---------------------------------------------------------------------------
# Day-of-week name -> proto enum value.
# ---------------------------------------------------------------------------

DAY_NAMES: dict[str, int] = {
    "MON": core_pb2.MONDAY,
    "MONDAY": core_pb2.MONDAY,
    "TUE": core_pb2.TUESDAY,
    "TUESDAY": core_pb2.TUESDAY,
    "WED": core_pb2.WEDNESDAY,
    "WEDNESDAY": core_pb2.WEDNESDAY,
    "THU": core_pb2.THURSDAY,
    "THURSDAY": core_pb2.THURSDAY,
    "FRI": core_pb2.FRIDAY,
    "FRIDAY": core_pb2.FRIDAY,
    "SAT": core_pb2.SATURDAY,
    "SATURDAY": core_pb2.SATURDAY,
    "SUN": core_pb2.SUNDAY,
    "SUNDAY": core_pb2.SUNDAY,
}

SCHEDULE_TYPE_NAMES: dict[str, int] = {
    "FIXED": sc_pb.FIXED,
    "FLEX_MONTHLY": sc_pb.FLEX_MONTHLY,
    "FLEX_DAILY": sc_pb.FLEX_DAILY,
}


# ---------------------------------------------------------------------------
# Public exceptions
# ---------------------------------------------------------------------------


class RachioError(Exception):
    """Raised when a Rachio API call fails or credentials are missing."""


# ---------------------------------------------------------------------------
# Module-level helpers — used by the client AND by the token-minting CLI.
# ---------------------------------------------------------------------------


def mint_access_token(email: str, password: str) -> dict[str, Any]:
    """Perform the OAuth 2.0 password grant against oauth.rach.io.

    Returns the raw JSON response. Notable fields:
        access_token (str)
        refresh_token (str, not used by this project)
        user_id       (str, UUID)
        expires_in    (int, seconds; observed ~25 years)
        token_type    (str, always "Bearer")

    Raises RachioError on non-200 or missing access_token.
    """
    resp = httpx.post(
        OAUTH_URL,
        data={
            "grant_type": "password",
            "username": email,
            "password": password,
            "client_id": OAUTH_CLIENT_ID,
            "client_secret": OAUTH_CLIENT_SECRET,
        },
        headers={"Accept": "application/json"},
        timeout=20.0,
    )
    if resp.status_code != 200:
        raise RachioError(
            f"OAuth password grant failed ({resp.status_code}): {resp.text[:500]}"
        )
    data = resp.json()
    if not data.get("access_token"):
        raise RachioError(f"OAuth response missing access_token: {data}")
    return data


# ---------------------------------------------------------------------------
# gRPC auth metadata plugin
# ---------------------------------------------------------------------------


class _TokenAuth(grpc.AuthMetadataPlugin):
    """Per-call gRPC credentials plugin that adds the bearer token + the
    same ``client-version`` header the Android app sends."""

    def __init__(self, get_token: Callable[[], str]):
        self._get_token = get_token

    def __call__(self, context, callback):
        try:
            token = self._get_token()
        except Exception as e:  # surfaced to the caller as UNAVAILABLE
            callback((), e)
            return
        callback(
            (
                ("authorization", f"Bearer {token}"),
                ("client-version", CLIENT_VERSION),
            ),
            None,
        )


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------


class RachioClient:
    """Stateful client for the Rachio mobile gRPC API.

    Authentication is token-only: the caller must set ``RACHIO_ACCESS_TOKEN``
    in the environment. Mint a token once via ``rachio-mcp-token``; the
    resulting value lasts ~25 years (the same long-lived bearer token the
    Android app itself uses).

    The ``user_id`` for the token's owner is derived lazily on first use
    via ``LocationService.ListLocations``, which accepts only the bearer
    token as input.
    """

    def __init__(self) -> None:
        self._token: str | None = None
        self._user_id: str | None = None
        self._channel: grpc.Channel | None = None

    # ------------------------------------------------------------------
    # Auth
    # ------------------------------------------------------------------

    def login(self) -> None:
        """Load the pre-provisioned access token from the environment.

        Does NOT perform a password grant — that's a one-time operation
        handled by the ``rachio-mcp-token`` CLI. The MCP process itself
        only ever sees the token.
        """
        token = os.getenv("RACHIO_ACCESS_TOKEN")
        if not token:
            raise RachioError(
                "RACHIO_ACCESS_TOKEN is not set. Mint a long-lived token "
                "with `rachio-mcp-token` (or "
                "`uvx --from rachio-mcp rachio-mcp-token`) and set it as "
                "RACHIO_ACCESS_TOKEN in your MCP client's env block."
            )
        self._token = token
        logger.info("Rachio access token loaded from RACHIO_ACCESS_TOKEN")

    def _ensure_auth(self) -> None:
        if self._token is None:
            self.login()

    def _get_token(self) -> str:
        self._ensure_auth()
        assert self._token is not None
        return self._token

    @property
    def user_id(self) -> str:
        """Rachio user id (UUID) for the caller, derived lazily.

        The OAuth access token by itself does not include the user_id in
        any decodable form (it's just a UUID). We call
        ``LocationService.ListLocations`` on first access — it requires
        only the bearer token and returns ``location_summary[].owner.id``,
        which is the caller's user_id.
        """
        if self._user_id is not None:
            return self._user_id
        # Call ListLocations. Picks up the token via the auth metadata plugin.
        resp = self._call(
            self._location_stub().ListLocations,
            loc_svc.ListLocationsRequest(),
        )
        summaries = list(resp.location_summary)
        if not summaries:
            raise RachioError(
                "ListLocations returned no locations; cannot derive user_id. "
                "Check that your RACHIO_ACCESS_TOKEN belongs to an account "
                "that owns at least one Rachio controller."
            )
        owner_id = summaries[0].owner.id
        if not owner_id:
            raise RachioError(
                "ListLocations returned a location with no owner.id; "
                "cannot derive user_id."
            )
        self._user_id = owner_id
        logger.info("Derived user_id=%s from ListLocations", owner_id)
        return owner_id

    # ------------------------------------------------------------------
    # Channel + stub helpers
    # ------------------------------------------------------------------

    def _get_channel(self) -> grpc.Channel:
        if self._channel is None:
            composite = grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(),
                grpc.metadata_call_credentials(
                    _TokenAuth(self._get_token),
                    name="rachio-bearer",
                ),
            )
            self._channel = grpc.secure_channel(
                GRPC_TARGET,
                composite,
                options=[("grpc.keepalive_time_ms", 60_000)],
            )
        return self._channel

    def _device_stub(self) -> dev_grpc.DeviceServiceStub:
        return dev_grpc.DeviceServiceStub(self._get_channel())

    def _schedule_stub(self) -> svc_grpc.ScheduleServiceStub:
        return svc_grpc.ScheduleServiceStub(self._get_channel())

    def _location_stub(self) -> loc_grpc.LocationServiceStub:
        return loc_grpc.LocationServiceStub(self._get_channel())

    def close(self) -> None:
        """Close the gRPC channel. Safe to call multiple times."""
        if self._channel is not None:
            self._channel.close()
            self._channel = None

    # ------------------------------------------------------------------
    # Call helper with one-shot re-auth on UNAUTHENTICATED
    # ------------------------------------------------------------------

    def _call(
        self,
        rpc_callable: Callable,
        request,
        *,
        timeout: float = 30.0,
    ):
        """Invoke a unary gRPC RPC.

        UNAUTHENTICATED is terminal: the access token is provisioned
        externally (via ``rachio-mcp-token``) and cannot be refreshed
        without the user's password, which this process does not have.
        Callers should catch ``RachioError`` and surface the "mint a new
        token" message to the user.
        """
        self._ensure_auth()
        try:
            return rpc_callable(request, timeout=timeout)
        except grpc.RpcError as e:
            code = e.code()  # type: ignore[attr-defined]
            details = e.details() or ""  # type: ignore[attr-defined]
            # UNAUTHENTICATED is the canonical "bad token" code. Rachio's
            # backend, however, sometimes returns PERMISSION_DENIED for an
            # outright invalid/garbage token before even reaching the
            # per-RPC authorization layer. Treat both as terminal auth
            # failures with the same user-facing message.
            if code == grpc.StatusCode.UNAUTHENTICATED or (
                code == grpc.StatusCode.PERMISSION_DENIED and not details
            ):
                raise RachioError(
                    "Rachio rejected the access token "
                    f"({code.name}). The token may have been revoked by "
                    "the Rachio app, by a password change, or by explicit "
                    "logout from another device — or it may simply be "
                    "malformed. Mint a fresh one with `rachio-mcp-token` "
                    "and update RACHIO_ACCESS_TOKEN."
                ) from e
            raise

    # ------------------------------------------------------------------
    # Response -> dict
    # ------------------------------------------------------------------

    @staticmethod
    def _pb2dict(msg) -> dict:
        """Convert a protobuf message to a JSON-ready dict.

        ``always_print_fields_with_no_presence=True`` surfaces zero-valued
        proto3 scalar fields so callers can see every key, even when empty;
        ``preserving_proto_field_name=True`` keeps snake_case field names.
        """
        return json_format.MessageToDict(
            msg,
            preserving_proto_field_name=True,
            always_print_fields_with_no_presence=True,
        )

    # ==================================================================
    # Discovery
    # ==================================================================

    def list_devices(self) -> list[dict]:
        """Return all devices owned by the logged-in user.

        Includes sprinkler controllers, linked sensors, and virtual
        weather stations — callers should filter by ``type`` if they only
        want controllers.
        """
        req = dev_svc.ListDevicesRequest(owner_id=self.user_id)
        resp = self._call(self._device_stub().ListDevices, req)
        return [self._pb2dict(d) for d in resp.device]

    def get_device(self, device_id: str) -> dict:
        """Return rich device details plus live state.

        Merges ``GetDeviceDetails`` (static info: name, model, zones,
        linked sensor ids) with ``GetDeviceState`` (live state: standby,
        rain delay, current zone run, sensor RSSI) when the latter is
        available. Linked sensors and virtual weather stations don't have
        a device state record, so ``state`` may be ``None``.
        """
        stub = self._device_stub()
        details = self._call(
            stub.GetDeviceDetails, dev_svc.GetDeviceDetailsRequest(id=device_id)
        )
        out: dict[str, Any] = {"details": self._pb2dict(details)}
        which = details.WhichOneof("device")
        if which is not None:
            out["kind"] = which
        try:
            state = self._call(
                stub.GetDeviceState, dev_svc.GetDeviceStateRequest(device_id=device_id)
            )
            out["state"] = self._pb2dict(state)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:  # type: ignore[attr-defined]
                out["state"] = None
            else:
                raise
        return out

    def list_zones(
        self,
        device_id: str,
        *,
        include_extra: bool = False,
        include_moisture: bool = False,
    ) -> list[dict]:
        """List all zones for a device, with optional extra/moisture data."""
        req = dev_svc.ListZonesRequest(device_id=device_id)
        if include_extra:
            req.include_extra_data.value = True
        if include_moisture:
            req.include_moisture_data.value = True
        resp = self._call(self._device_stub().ListZones, req)
        return [self._pb2dict(z) for z in resp.zone_summary]

    def get_zone(self, zone_id: str, *, force_imperial: bool = True) -> dict:
        """Return full zone detail (soil, nozzle, crop, sun, slope, area, etc.)."""
        req = dev_svc.GetZoneDetailRequest(
            zone_id=zone_id, force_imperial=force_imperial
        )
        resp = self._call(self._device_stub().GetZoneDetail, req)
        return self._pb2dict(resp.zone_summary)

    def get_calendar(
        self,
        device_id: str,
        start: datetime | date | None = None,
        end: datetime | date | None = None,
    ) -> dict:
        """Return scheduled runs + skip events for a date range.

        Defaults to a 14-day window starting today.
        """
        start = start or date.today()
        end = (
            end or date.today().replace(day=min(28, date.today().day))
            if False
            else None
        )
        if end is None:
            end = date.today()
            # 14 days ahead
            end = (
                datetime.combine(start, datetime.min.time())
                if isinstance(start, date)
                else start
            )
            end = end.replace()  # placeholder; overridden below
        # Normalise to UTC datetimes
        start_dt = _to_utc(start)
        end_dt = _to_utc(end) if end else start_dt
        if end_dt <= start_dt:
            # expand to 14 days
            from datetime import timedelta

            end_dt = start_dt + timedelta(days=14)

        req = dev_svc.GetCalendarRequest(device_id=device_id)
        _set_ts(req.start_time, start_dt)
        _set_ts(req.end_time, end_dt)
        resp = self._call(self._device_stub().GetCalendar, req)
        return self._pb2dict(resp)

    def get_run_history(
        self,
        device_id: str,
        start: datetime | date | None = None,
        end: datetime | date | None = None,
    ) -> dict:
        """Return recent completed/started runs and skips for a controller.

        Defaults to the last 7 days through tomorrow, so today's completed
        watering is included without the caller having to specify dates.
        """
        from datetime import timedelta

        start = start or date.today() - timedelta(days=7)
        end = end or date.today() + timedelta(days=1)
        start_dt = _to_utc(start)
        end_dt = _to_utc(end)
        if end_dt <= start_dt:
            raise RachioError("end must be after start")

        req = dev_svc.GetCalendarRequest(device_id=device_id)
        _set_ts(req.start_time, start_dt)
        _set_ts(req.end_time, end_dt)
        resp = self._call(self._device_stub().GetCalendar, req)
        out = self._pb2dict(resp)
        out["calendar_runs"] = out.pop("runs", [])
        last_zone_runs = self.get_last_zone_runs(device_id)
        actual_zone_runs = []
        for zone_run in last_zone_runs:
            run_start = _parse_utc_timestamp(zone_run.get("last_run_start_time"))
            if run_start is None:
                continue
            run_end = (
                _parse_utc_timestamp(zone_run.get("last_run_end_time")) or run_start
            )
            if start_dt <= run_end and run_start < end_dt:
                actual_zone_runs.append(zone_run)
        actual_zone_runs.sort(key=lambda z: z.get("last_run_start_time", ""))

        out["range"] = {
            "start": start_dt.isoformat(),
            "end": end_dt.isoformat(),
        }
        out["actual_zone_runs"] = actual_zone_runs
        out["history_note"] = (
            "actual_zone_runs is controller-observed watering telemetry. "
            "calendar_runs and skips are Rachio calendar events and may not "
            "include every completed scheduled run. Observed telemetry is "
            "limited to the latest run per zone."
        )
        return out

    def get_last_zone_runs(self, device_id: str) -> list[dict]:
        """Return the last observed run state for each zone on a controller."""
        req = dev_svc.GetLastZoneRunStateRequest(device_id=device_id)
        resp = self._call(self._device_stub().GetLastZoneRunState, req)
        return [self._pb2dict(z) for z in resp.last_zone_run_states]

    def get_active_alerts(
        self,
        device_id: str | None = None,
        zone_id: str | None = None,
    ) -> list[dict]:
        """Get active (unresolved) alerts for a device or zone.

        Exactly one of ``device_id`` or ``zone_id`` must be provided.
        """
        if (device_id is None) == (zone_id is None):
            raise RachioError("Provide exactly one of device_id or zone_id")
        req = dev_svc.GetActiveAlertsRequest()
        if device_id:
            req.device_id.CopyFrom(core_pb2.StringList(id=[device_id]))
        else:
            req.zone_id.CopyFrom(core_pb2.StringList(id=[zone_id]))
        resp = self._call(self._device_stub().GetActiveAlerts, req)
        return [self._pb2dict(a) for a in resp.alerts]

    def get_weather(
        self,
        location_id: str,
        start: date | None = None,
        end: date | None = None,
    ) -> dict:
        """Return weather observations + forecast for a location.

        Defaults to a 7-day window ending 7 days from today.
        """
        from datetime import timedelta

        start = start or date.today() - timedelta(days=3)
        end = end or date.today() + timedelta(days=7)
        req = loc_svc.GetWeatherByLocationRequest(location_id=location_id)
        req.start_date.year, req.start_date.month, req.start_date.day = (
            start.year,
            start.month,
            start.day,
        )
        req.end_date.year, req.end_date.month, req.end_date.day = (
            end.year,
            end.month,
            end.day,
        )
        resp = self._call(self._location_stub().GetWeatherByLocation, req)
        return self._pb2dict(resp)

    # ==================================================================
    # Schedule CRUD
    # ==================================================================

    def list_schedules(
        self,
        *,
        device_id: str | None = None,
        location_id: str | None = None,
        zone_id: str | None = None,
        schedule_id: str | None = None,
    ) -> list[dict]:
        """List schedules matching a filter. Exactly one filter is required."""
        provided = sum(
            x is not None for x in (device_id, location_id, zone_id, schedule_id)
        )
        if provided != 1:
            raise RachioError(
                "Provide exactly one of device_id, location_id, zone_id, schedule_id"
            )
        req = svc.GetSchedulesRequest()
        if device_id:
            req.device_id.CopyFrom(core_pb2.StringList(id=[device_id]))
        elif location_id:
            req.location_id.CopyFrom(core_pb2.StringList(id=[location_id]))
        elif zone_id:
            req.zone_id.CopyFrom(core_pb2.StringList(id=[zone_id]))
        elif schedule_id:
            req.schedule_id.CopyFrom(core_pb2.StringList(id=[schedule_id]))
        resp = self._call(self._schedule_stub().GetSchedules, req)
        return [self._pb2dict(s) for s in resp.schedule]

    def get_schedule(self, schedule_id: str) -> dict:
        """Return a schedule plus the locations/devices it runs on."""
        schedules = self.list_schedules(schedule_id=schedule_id)
        if not schedules:
            raise RachioError(f"schedule {schedule_id} not found")
        out: dict[str, Any] = {"schedule": schedules[0]}
        loc_resp = self._call(
            self._schedule_stub().GetLocationsAndDevicesForSchedule,
            svc.GetLocationsAndDevicesForScheduleRequest(schedule_id=schedule_id),
        )
        out["locations_and_devices"] = self._pb2dict(loc_resp)
        return out

    def preview_schedule(
        self,
        *,
        name: str,
        schedule_type: str = "FIXED",
        zones: list[dict],
        start_time: str | None = None,
        start_sun: str | None = None,
        days: list[str] | None = None,
        annual_start: str | None = None,
        annual_end: str | None = None,
        smart_cycle: bool = False,
        cycle_soak: bool = False,
        cycle_time_seconds: int | None = None,
        soak_time_seconds: int | None = None,
        zone_delay_time_seconds: int | None = None,
        rain_delay_enabled: bool = True,
        freeze_delay_enabled: bool = True,
        wind_delay_enabled: bool = False,
        climate_skip: bool = True,
        seasonal_shift: bool = False,
    ) -> dict:
        """Server-side dry-run of CreateSchedule. Returns the Schedule
        proto (including the generated human-readable ``summary``) without
        persisting anything. Same fields as ``create_schedule``.

        ``zones``: list of dicts with keys ``device_id``, ``zone_id``,
        ``watering_time`` (seconds), and optional ``order_id``.
        """
        criteria, restriction, zone_infos = self._build_schedule_parts(
            schedule_type=schedule_type,
            zones=zones,
            start_time=start_time,
            start_sun=start_sun,
            days=days,
            annual_start=annual_start,
            annual_end=annual_end,
            smart_cycle=smart_cycle,
            cycle_soak=cycle_soak,
            cycle_time_seconds=cycle_time_seconds,
            soak_time_seconds=soak_time_seconds,
            zone_delay_time_seconds=zone_delay_time_seconds,
            rain_delay_enabled=rain_delay_enabled,
            freeze_delay_enabled=freeze_delay_enabled,
            wind_delay_enabled=wind_delay_enabled,
            climate_skip=climate_skip,
            seasonal_shift=seasonal_shift,
        )
        req = svc.PreviewScheduleRequest(
            name=name,
            schedule_criteria=criteria,
            schedule_restriction_criteria=restriction,
            zone_info=zone_infos,
        )
        resp = self._call(self._schedule_stub().PreviewSchedule, req)
        return self._pb2dict(resp.schedule)

    def create_schedule(
        self,
        *,
        name: str,
        schedule_type: str = "FIXED",
        zones: list[dict],
        enabled: bool = True,
        start_time: str | None = None,
        start_sun: str | None = None,
        days: list[str] | None = None,
        annual_start: str | None = None,
        annual_end: str | None = None,
        smart_cycle: bool = False,
        cycle_soak: bool = False,
        cycle_time_seconds: int | None = None,
        soak_time_seconds: int | None = None,
        zone_delay_time_seconds: int | None = None,
        rain_delay_enabled: bool = True,
        freeze_delay_enabled: bool = True,
        wind_delay_enabled: bool = False,
        climate_skip: bool = True,
        seasonal_shift: bool = False,
    ) -> dict:
        """Create a new schedule. Persists to the Rachio backend.

        Recommendation: call ``preview_schedule`` with the same arguments
        first and review the returned ``summary`` before committing.
        """
        criteria, restriction, zone_infos = self._build_schedule_parts(
            schedule_type=schedule_type,
            zones=zones,
            start_time=start_time,
            start_sun=start_sun,
            days=days,
            annual_start=annual_start,
            annual_end=annual_end,
            smart_cycle=smart_cycle,
            cycle_soak=cycle_soak,
            cycle_time_seconds=cycle_time_seconds,
            soak_time_seconds=soak_time_seconds,
            zone_delay_time_seconds=zone_delay_time_seconds,
            rain_delay_enabled=rain_delay_enabled,
            freeze_delay_enabled=freeze_delay_enabled,
            wind_delay_enabled=wind_delay_enabled,
            climate_skip=climate_skip,
            seasonal_shift=seasonal_shift,
        )
        req = svc.CreateScheduleRequest(
            name=name,
            schedule_criteria=criteria,
            schedule_restriction_criteria=restriction,
            zone_info=zone_infos,
            enabled=BoolValue(value=enabled),
        )
        resp = self._call(self._schedule_stub().CreateSchedule, req)
        return self._pb2dict(resp.schedule)

    # Sentinel distinguishing "argument not supplied" (leave unchanged)
    # from an explicit value, including ``None`` where that is meaningful.
    _UNSET: Any = object()

    def _get_schedule_proto(self, schedule_id: str):
        """Fetch the raw ``Schedule`` protobuf message (not a dict).

        Used by ``update_schedule`` so it can merge changes onto the
        schedule's existing ``schedule_criteria`` / restriction / zone
        state, since the gRPC ``UpdateScheduleRequest`` carries those as
        whole (non-nullable) sub-messages rather than per-field patches.
        """
        req = svc.GetSchedulesRequest()
        req.schedule_id.CopyFrom(core_pb2.StringList(id=[schedule_id]))
        resp = self._call(self._schedule_stub().GetSchedules, req)
        if not resp.schedule:
            raise RachioError(f"schedule {schedule_id} not found")
        return resp.schedule[0]

    def update_schedule(
        self,
        schedule_id: str,
        *,
        name: str | None = None,
        enabled: bool | None = None,
        # --- criteria (timing / behaviour) ---
        schedule_type: str | None = None,
        start_time: str | None = _UNSET,
        start_sun: str | None = _UNSET,
        days: list[str] | None = _UNSET,
        annual_start: str | None = _UNSET,
        annual_end: str | None = _UNSET,
        smart_cycle: bool | None = None,
        cycle_soak: bool | None = None,
        cycle_time_seconds: int | None = None,
        soak_time_seconds: int | None = None,
        zone_delay_time_seconds: int | None = None,
        rain_delay_enabled: bool | None = None,
        freeze_delay_enabled: bool | None = None,
        wind_delay_enabled: bool | None = None,
        climate_skip: bool | None = None,
        seasonal_shift: bool | None = None,
        # --- zones ---
        zones: list[dict] | None = None,
        zone_ids_to_remove: list[str] | None = None,
    ) -> dict:
        """Partial-merge update of an existing schedule.

        Only the arguments you pass are changed; everything else is
        preserved by reading the current schedule first and overlaying
        your changes onto its existing criteria, restriction criteria,
        and zone list before sending a single ``UpdateSchedule`` RPC.

        Notes:
          * ``schedule_type``, the delay/skip booleans, smart-cycle,
            cycle-soak and the *_seconds timers map onto
            ``schedule_criteria``.
          * ``start_time`` and ``start_sun`` are mutually exclusive (a
            proto ``oneof``); passing one clears the other. Passing
            ``None`` explicitly leaves the existing start setting alone.
          * ``days`` replaces the day-of-week restriction wholesale.
          * ``zones`` upserts zone entries (matched on
            ``device_id`` + ``zone_id``); ``zone_ids_to_remove`` deletes
            zones by id. Both are optional and additive to the existing
            zone set.
        """
        current = self._get_schedule_proto(schedule_id)
        req = svc.UpdateScheduleRequest(schedule_id=schedule_id)

        if name is not None:
            req.name.CopyFrom(StringValue(value=name))
        if enabled is not None:
            req.enabled.CopyFrom(BoolValue(value=enabled))

        criteria_touched = any(
            v is not None
            for v in (
                schedule_type,
                smart_cycle,
                cycle_soak,
                cycle_time_seconds,
                soak_time_seconds,
                zone_delay_time_seconds,
                rain_delay_enabled,
                freeze_delay_enabled,
                wind_delay_enabled,
                climate_skip,
                seasonal_shift,
            )
        ) or any(
            v is not self._UNSET
            for v in (start_time, start_sun, days, annual_start, annual_end)
        )

        if criteria_touched:
            criteria = sc_pb.ScheduleCriteria()
            criteria.CopyFrom(current.schedule_criteria)

            if schedule_type is not None:
                st_key = schedule_type.upper()
                if st_key not in SCHEDULE_TYPE_NAMES:
                    raise RachioError(
                        f"schedule_type must be one of {list(SCHEDULE_TYPE_NAMES)}, "
                        f"got {schedule_type!r}"
                    )
                criteria.schedule_type = SCHEDULE_TYPE_NAMES[st_key]
            if smart_cycle is not None:
                criteria.smart_cycle = smart_cycle
            if cycle_soak is not None:
                criteria.cycle_soak = cycle_soak
            if cycle_time_seconds is not None:
                criteria.cycle_time = cycle_time_seconds
            if soak_time_seconds is not None:
                criteria.soak_time = soak_time_seconds
            if zone_delay_time_seconds is not None:
                criteria.zone_delay_time = zone_delay_time_seconds
            if rain_delay_enabled is not None:
                criteria.rain_delay_enabled = rain_delay_enabled
            if freeze_delay_enabled is not None:
                criteria.freeze_delay_enabled = freeze_delay_enabled
            if wind_delay_enabled is not None:
                criteria.wind_delay_enabled = wind_delay_enabled
            if climate_skip is not None:
                criteria.climate_skip = climate_skip
            if seasonal_shift is not None:
                criteria.seasonal_shift = seasonal_shift

            if annual_start is not self._UNSET:
                criteria.ClearField("annual_start_date")
                if annual_start:
                    m, d = _parse_mmdd(annual_start)
                    criteria.annual_start_date.month = m
                    criteria.annual_start_date.day = d
            if annual_end is not self._UNSET:
                criteria.ClearField("annual_end_date")
                if annual_end:
                    m, d = _parse_mmdd(annual_end)
                    criteria.annual_end_date.month = m
                    criteria.annual_end_date.day = d

            # start_end_time oneof: a supplied start_time/start_sun
            # replaces whatever was there.
            st_supplied = start_time is not self._UNSET and start_time is not None
            ss_supplied = start_sun is not self._UNSET and start_sun is not None
            if st_supplied and ss_supplied:
                raise RachioError("provide at most one of start_time or start_sun")
            if st_supplied:
                criteria.ClearField("start_end_time")
                h, m = _parse_hhmm(start_time)
                tl = core_pb2.TimeList()
                t = tl.time.add()
                t.hour = h
                t.minute = m
                criteria.start_time_set.CopyFrom(tl)
            elif ss_supplied:
                criteria.ClearField("start_end_time")
                criteria.start_sun_time = start_sun.upper()

            req.schedule_criteria.CopyFrom(criteria)

        if days is not self._UNSET:
            restriction = src_pb.ScheduleRestrictionCriteria()
            restriction.CopyFrom(current.schedule_restriction_criteria)
            restriction.ClearField("day_of_week_constraint")
            if days:
                restriction.day_of_week_constraint.extend(
                    [_parse_day(name) for name in days]
                )
            req.schedule_restriction_criteria.CopyFrom(restriction)

        if zones:
            existing_by_key = {(z.device_id, z.zone_id): z for z in current.zone_info}
            for idx, z in enumerate(zones, start=1):
                try:
                    device_id = z["device_id"]
                    zone_id = z["zone_id"]
                except KeyError as e:
                    raise RachioError(
                        f"zone entry missing key {e}; required: device_id, zone_id"
                    ) from e
                base = existing_by_key.get((device_id, zone_id))
                zi = szi_pb.ScheduleZoneInfo()
                if base is not None:
                    zi.CopyFrom(base)
                else:
                    zi.device_id = device_id
                    zi.zone_id = zone_id
                    zi.order_id = idx
                if "watering_time" in z:
                    zi.watering_time = int(z["watering_time"])
                elif base is None:
                    raise RachioError(f"new zone {zone_id} requires watering_time")
                if "order_id" in z:
                    zi.order_id = int(z["order_id"])
                if "flex_aggression_coefficient" in z:
                    zi.flex_aggression_coefficient = float(
                        z["flex_aggression_coefficient"]
                    )
                if "flex_runtime_coefficient" in z:
                    zi.flex_runtime_coefficient = float(z["flex_runtime_coefficient"])
                req.zone_info_to_add_or_update.append(zi)

        if zone_ids_to_remove:
            req.zone_ids_to_remove.extend(zone_ids_to_remove)

        resp = self._call(self._schedule_stub().UpdateSchedule, req)
        return self._pb2dict(resp.schedule)

    def delete_schedule(self, schedule_id: str) -> bool:
        """Delete a schedule. Destructive — this cannot be undone."""
        req = svc.DeleteScheduleRequest(schedule_id=schedule_id)
        resp = self._call(self._schedule_stub().DeleteSchedule, req)
        return bool(resp.deleted)

    def copy_schedule(self, schedule_id: str) -> dict:
        """Create a duplicate of an existing schedule."""
        req = svc.CopyScheduleRequest(schedule_id=schedule_id)
        resp = self._call(self._schedule_stub().CopySchedule, req)
        return self._pb2dict(resp.schedule)

    def run_schedule(self, schedule_id: str) -> list[str]:
        """Start an immediate run of the given schedule. Returns the
        list of device_ids the run was dispatched to."""
        req = svc.RunScheduleRequest(schedule_id=schedule_id)
        resp = self._call(self._schedule_stub().RunSchedule, req)
        return list(resp.device_id)

    def skip_schedule(self, schedule_id: str, disabled: bool) -> dict:
        """Toggle the skip-next-run state for a schedule.

        ``disabled=True`` skips the schedule's next scheduled run; setting
        it back to ``False`` re-arms it."""
        req = svc.SetSkipRequest(schedule_id=schedule_id, disabled=disabled)
        resp = self._call(self._schedule_stub().SetSkip, req)
        return self._pb2dict(resp.skip)

    def get_schedule_runs(
        self,
        schedule_id: str,
        start: datetime | date | None = None,
        end: datetime | date | None = None,
    ) -> dict:
        """Return past scheduled runs + skip events for a schedule.

        Defaults to the last 30 days.
        """
        from datetime import timedelta

        start = start or (date.today() - timedelta(days=30))
        end = end or date.today()
        start_dt = _to_utc(start)
        end_dt = _to_utc(end)
        req = svc.GetScheduleRunsRequest(schedule_id=schedule_id)
        _set_ts(req.start_time, start_dt)
        _set_ts(req.end_time, end_dt)
        resp = self._call(self._schedule_stub().GetScheduleRuns, req)
        return self._pb2dict(resp)

    # ==================================================================
    # Live controller operations
    # ==================================================================

    def stop_watering(self, device_id: str) -> None:
        """Stop all watering in progress on the device."""
        req = dev_svc.StopWateringRequest(device_id=device_id)
        self._call(self._device_stub().StopWatering, req)

    def start_zones(
        self,
        device_id: str,
        zones: list[dict],
        *,
        cycle_soak: bool = False,
        cycle_duration_seconds: int | None = None,
        soak_duration_seconds: int | None = None,
    ) -> int:
        """Start a manual run of one or more zones in sequence.

        ``zones`` is a list of ``{"zone_number": int, "duration": seconds}``.
        Returns the ``manual_schedule_id`` so callers can track the run.
        """
        if not zones:
            raise RachioError("start_zones requires at least one zone")
        req = dev_svc.SetManualScheduleRequest(
            device_id=device_id, cycle_soak=cycle_soak
        )
        for z in zones:
            run = req.runs.add()
            run.zone_number = int(z["zone_number"])
            run.duration = int(z["duration"])
        if cycle_duration_seconds is not None:
            req.cycle_duration.CopyFrom(Int32Value(value=cycle_duration_seconds))
        if soak_duration_seconds is not None:
            req.soak_duration.CopyFrom(Int32Value(value=soak_duration_seconds))
        resp = self._call(self._device_stub().SetManualSchedule, req)
        return int(resp.manual_schedule_id)

    def set_rain_delay(self, device_id: str, expiration: datetime | str | int) -> None:
        """Set a rain-delay window for the device.

        ``expiration`` accepts a ``datetime``, an ISO-8601 string, or a
        Unix epoch (seconds). Pass ``expiration=0`` or a time in the past
        to cancel an existing rain delay.
        """
        if isinstance(expiration, (int, float)):
            dt = datetime.fromtimestamp(float(expiration), tz=timezone.utc)
        elif isinstance(expiration, str):
            dt = datetime.fromisoformat(expiration)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
        else:
            dt = (
                expiration
                if expiration.tzinfo
                else expiration.replace(tzinfo=timezone.utc)
            )
        req = dev_svc.SetRainDelayRequest(device_id=device_id)
        _set_ts(req.rain_delay_expiration, dt)
        self._call(self._device_stub().SetRainDelay, req)

    def skip_current_zone(self, device_id: str) -> dict:
        """Skip to the next zone in the currently-running schedule."""
        req = dev_svc.SkipForwardZoneRunRequest(device_id=device_id)
        resp = self._call(self._device_stub().SkipForwardZoneRun, req)
        return self._pb2dict(resp)

    def pause_watering(self, device_id: str, seconds: int) -> dict:
        """Pause the currently-running zone for ``seconds``."""
        req = dev_svc.PauseZoneRunRequest(device_id=device_id, seconds_paused=seconds)
        resp = self._call(self._device_stub().PauseZoneRun, req)
        return self._pb2dict(resp)

    def resume_watering(self, device_id: str) -> dict:
        """Resume a paused zone run."""
        req = dev_svc.ResumeZoneRunRequest(device_id=device_id)
        resp = self._call(self._device_stub().ResumeZoneRun, req)
        return self._pb2dict(resp)

    # ==================================================================
    # Builders
    # ==================================================================

    def _build_schedule_parts(
        self,
        *,
        schedule_type: str,
        zones: list[dict],
        start_time: str | None,
        start_sun: str | None,
        days: list[str] | None,
        annual_start: str | None,
        annual_end: str | None,
        smart_cycle: bool,
        cycle_soak: bool,
        cycle_time_seconds: int | None,
        soak_time_seconds: int | None,
        zone_delay_time_seconds: int | None,
        rain_delay_enabled: bool,
        freeze_delay_enabled: bool,
        wind_delay_enabled: bool,
        climate_skip: bool,
        seasonal_shift: bool,
    ) -> tuple[
        sc_pb.ScheduleCriteria,
        src_pb.ScheduleRestrictionCriteria,
        list[szi_pb.ScheduleZoneInfo],
    ]:
        # --- ScheduleCriteria ---
        st_key = schedule_type.upper()
        if st_key not in SCHEDULE_TYPE_NAMES:
            raise RachioError(
                f"schedule_type must be one of {list(SCHEDULE_TYPE_NAMES)}, got {schedule_type!r}"
            )
        criteria = sc_pb.ScheduleCriteria(
            schedule_type=SCHEDULE_TYPE_NAMES[st_key],
            rain_delay_enabled=rain_delay_enabled,
            freeze_delay_enabled=freeze_delay_enabled,
            wind_delay_enabled=wind_delay_enabled,
            climate_skip=climate_skip,
            seasonal_shift=seasonal_shift,
            smart_cycle=smart_cycle,
            cycle_soak=cycle_soak,
        )
        if annual_start:
            m, d = _parse_mmdd(annual_start)
            criteria.annual_start_date.month = m
            criteria.annual_start_date.day = d
        if annual_end:
            m, d = _parse_mmdd(annual_end)
            criteria.annual_end_date.month = m
            criteria.annual_end_date.day = d
        if cycle_time_seconds is not None:
            criteria.cycle_time = cycle_time_seconds
        if soak_time_seconds is not None:
            criteria.soak_time = soak_time_seconds
        if zone_delay_time_seconds is not None:
            criteria.zone_delay_time = zone_delay_time_seconds
        # start_end_time is a oneof — set exactly one side.
        if start_time and start_sun:
            raise RachioError("provide at most one of start_time or start_sun")
        if start_time:
            h, m = _parse_hhmm(start_time)
            tl = core_pb2.TimeList()
            t = tl.time.add()
            t.hour = h
            t.minute = m
            criteria.start_time_set.CopyFrom(tl)
        elif start_sun:
            criteria.start_sun_time = start_sun.upper()

        # --- ScheduleRestrictionCriteria ---
        restriction = src_pb.ScheduleRestrictionCriteria()
        if days:
            restriction.day_of_week_constraint.extend(
                [_parse_day(name) for name in days]
            )

        # --- ScheduleZoneInfo[] ---
        if not zones:
            raise RachioError("schedule requires at least one zone")
        zone_infos: list[szi_pb.ScheduleZoneInfo] = []
        for idx, z in enumerate(zones, start=1):
            try:
                device_id = z["device_id"]
                zone_id = z["zone_id"]
                watering_time = int(z["watering_time"])
            except KeyError as e:
                raise RachioError(
                    f"zone entry missing key {e}; required: device_id, zone_id, watering_time"
                ) from e
            zi = szi_pb.ScheduleZoneInfo(
                device_id=device_id,
                zone_id=zone_id,
                order_id=int(z.get("order_id", idx)),
                watering_time=watering_time,
            )
            if "flex_aggression_coefficient" in z:
                zi.flex_aggression_coefficient = float(z["flex_aggression_coefficient"])
            if "flex_runtime_coefficient" in z:
                zi.flex_runtime_coefficient = float(z["flex_runtime_coefficient"])
            zone_infos.append(zi)

        return criteria, restriction, zone_infos


# ---------------------------------------------------------------------------
# Module-level helpers
# ---------------------------------------------------------------------------


def _parse_mmdd(s: str) -> tuple[int, int]:
    parts = s.split("-")
    if len(parts) != 2:
        raise RachioError(f"expected MM-DD, got {s!r}")
    try:
        return int(parts[0]), int(parts[1])
    except ValueError as e:
        raise RachioError(f"invalid MM-DD: {s!r}") from e


def _parse_hhmm(s: str) -> tuple[int, int]:
    parts = s.split(":")
    if len(parts) != 2:
        raise RachioError(f"expected HH:MM, got {s!r}")
    try:
        return int(parts[0]), int(parts[1])
    except ValueError as e:
        raise RachioError(f"invalid HH:MM: {s!r}") from e


def _parse_day(name: str) -> int:
    key = name.strip().upper()
    if key not in DAY_NAMES:
        raise RachioError(f"unknown day: {name!r}. Use MON/TUE/WED/THU/FRI/SAT/SUN")
    return DAY_NAMES[key]


def _to_utc(d: datetime | date) -> datetime:
    """Coerce a date or naive/aware datetime to an aware UTC datetime."""
    if isinstance(d, datetime):
        return (
            d.astimezone(timezone.utc) if d.tzinfo else d.replace(tzinfo=timezone.utc)
        )
    # A bare date becomes midnight UTC on that day.
    return datetime(d.year, d.month, d.day, tzinfo=timezone.utc)


def _set_ts(pb_ts: Timestamp, dt: datetime) -> None:
    """Populate a google.protobuf.Timestamp from an aware datetime."""
    pb_ts.FromDatetime(dt.astimezone(timezone.utc))


def _parse_utc_timestamp(value: str | None) -> datetime | None:
    """Parse a protobuf JSON timestamp into an aware UTC datetime."""
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
