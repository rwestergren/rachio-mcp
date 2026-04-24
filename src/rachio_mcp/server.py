"""MCP server for Rachio sprinkler controllers via the reverse-engineered
Android gRPC API.

23 tools over stdio transport:

- Discovery (7): list_devices, get_device, list_zones, get_zone,
  get_calendar, get_active_alerts, get_weather
- Schedule CRUD (10): list_schedules, get_schedule, preview_schedule,
  create_schedule, update_schedule, delete_schedule, copy_schedule,
  run_schedule, skip_schedule, get_schedule_runs
- Live ops (6): stop_watering, start_zones, set_rain_delay,
  skip_current_zone, pause_watering, resume_watering

Tool return values are JSON strings with shape::

    {"status": "success", ...fields...}
    {"status": "error", "message": "..."}

Input params are plain function signatures with type hints; FastMCP auto-
generates the tool schema from signatures + docstrings. This matches the
style used in cronometer-api-mcp.
"""

from __future__ import annotations

import json
import logging
import os
import sys
from datetime import date
from typing import Any

import grpc
from mcp.server.fastmcp import FastMCP

from .client import RachioClient, RachioError

# MCP stdio reserves stdout for protocol messages; route logs to stderr.
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    stream=sys.stderr,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

mcp = FastMCP(
    "rachio_mcp",
    instructions=(
        "Rachio sprinkler-controller MCP using the reverse-engineered Android "
        "mobile gRPC API. Use list_devices and list_zones to discover hardware. "
        "Use list_schedules + get_schedule to inspect watering programs. Use "
        "preview_schedule to server-dry-run a proposed schedule — it returns "
        "the same Schedule proto that create_schedule would produce, including "
        "a human-readable summary — then call create_schedule to commit it. "
        "stop_watering, start_zones, set_rain_delay, skip_current_zone, "
        "pause_watering, and resume_watering manipulate the controller in real "
        "time. All IDs are UUIDs obtained from list_* tools. Times are local to "
        "the controller's timezone. All write operations affect the live "
        "Rachio account and physical sprinkler system."
    ),
)


# ----------------------------------------------------------------------
# Client accessor (lazy)
# ----------------------------------------------------------------------

_client: RachioClient | None = None


def _get_client() -> RachioClient:
    global _client
    if _client is None:
        _client = RachioClient()
    return _client


# ----------------------------------------------------------------------
# Response helpers
# ----------------------------------------------------------------------


def _ok(payload: dict[str, Any] | None = None, **extra: Any) -> str:
    """Wrap a successful response as ``{"status": "success", ...}``."""
    body: dict[str, Any] = {"status": "success"}
    if payload:
        body.update(payload)
    if extra:
        body.update(extra)
    return json.dumps(body, indent=2, default=str)


def _err(e: Exception) -> str:
    """Wrap an error as ``{"status": "error", "message": "..."}``.

    Maps the common gRPC status codes and client errors to actionable
    messages aimed at an LLM agent calling the tool.
    """
    if isinstance(e, RachioError):
        msg = str(e)
    elif isinstance(e, grpc.RpcError):
        code = e.code()  # type: ignore[attr-defined]
        details = e.details() or ""  # type: ignore[attr-defined]
        if code == grpc.StatusCode.UNAUTHENTICATED:
            msg = (
                "Rachio rejected the access token. Mint a fresh one with "
                "`rachio-mcp-token` and update RACHIO_ACCESS_TOKEN in your "
                "MCP client config."
            )
        elif code == grpc.StatusCode.NOT_FOUND:
            msg = (
                f"Resource not found: {details}. Use list_devices or "
                "list_schedules to discover valid IDs."
            )
        elif code == grpc.StatusCode.PERMISSION_DENIED:
            if not details:
                # Likely an outright-bad token; surface the same guidance as
                # UNAUTHENTICATED.
                msg = (
                    "Rachio rejected the access token (PERMISSION_DENIED). "
                    "Mint a fresh one with `rachio-mcp-token` and update "
                    "RACHIO_ACCESS_TOKEN."
                )
            else:
                msg = (
                    f"Permission denied: {details}. This account may not "
                    "own the requested resource."
                )
        elif code == grpc.StatusCode.INVALID_ARGUMENT:
            msg = (
                f"Invalid request: {details}. Check the parameter formats — "
                "times are HH:MM, dates are MM-DD for annual or YYYY-MM-DD "
                "otherwise, and days are like 'MON,WED'."
            )
        elif code == grpc.StatusCode.UNAVAILABLE:
            msg = (
                f"Rachio backend unavailable: {details}. Network issue or a "
                "temporary outage — retry in a moment."
            )
        elif code == grpc.StatusCode.DEADLINE_EXCEEDED:
            msg = "Request timed out. Rachio backend may be slow; try again."
        elif code == grpc.StatusCode.ALREADY_EXISTS:
            msg = f"Conflict: {details}. The resource already exists."
        else:
            msg = f"gRPC error {code.name}: {details}"
    else:
        msg = f"{type(e).__name__}: {e}"
    return json.dumps({"status": "error", "message": msg})


def _parse_date(s: str | None) -> date | None:
    return date.fromisoformat(s) if s else None


# ======================================================================
# Discovery
# ======================================================================


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def list_devices() -> str:
    """List all Rachio devices on the account.

    Includes sprinkler controllers (type = CONTROLLER_GEN1/2/3 or
    CONTROLLER_VIRTUAL), linked sensors (SENSOR_LINKED, e.g. rain/flow
    sensors wired into a controller), wireless flow sensors
    (WIRELESS_FLOW_SENSOR), and virtual weather stations
    (WEATHER_STATION_VIRTUAL). Filter by ``type`` client-side if you only
    want the irrigation controllers.

    Returns a JSON object with ``devices`` — a list of device summaries
    including ``id``, ``type``, ``name``, ``location_id``, and
    ``geo_point``. Use ``get_device`` for full details.
    """
    try:
        return _ok(devices=_get_client().list_devices())
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def get_device(device_id: str) -> str:
    """Get full details + live state for a single device.

    Combines the static device info (model, serial, firmware, linked
    sensors, USDA hardiness zone, Koppen climate code, etc.) with live
    state (current zone run, standby, rain delay status). Linked sensors
    and virtual weather stations don't have a live-state record, so the
    ``state`` field will be ``null`` for those.

    Args:
        device_id: Device UUID from list_devices.
    """
    try:
        return _ok(_get_client().get_device(device_id))
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def list_zones(
    device_id: str,
    include_extra: bool = False,
    include_moisture: bool = False,
) -> str:
    """List all zones configured on a controller.

    Each zone summary includes ``zone_detail`` (soil type, nozzle type,
    crop/plant, available water, root depth, slope, sun exposure, area,
    enabled flag, zone number) and ``zone_state`` (live state if any).

    Args:
        device_id: Controller UUID (must be a CONTROLLER_GEN* device).
        include_extra: Ask the server to populate extra diagnostic fields.
        include_moisture: Include per-zone moisture data.
    """
    try:
        return _ok(
            zones=_get_client().list_zones(
                device_id,
                include_extra=include_extra,
                include_moisture=include_moisture,
            )
        )
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def get_zone(zone_id: str, force_imperial: bool = True) -> str:
    """Get full zone detail + live state.

    Returns a single zone's agronomic configuration (soil, nozzle,
    crop/plant, root depth, efficiency, etc.) and any live state.

    Args:
        zone_id: Zone UUID from list_zones.
        force_imperial: If true, units are returned in imperial (inches,
            sqft). If false, metric is used.
    """
    try:
        return _ok(_get_client().get_zone(zone_id, force_imperial=force_imperial))
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def get_calendar(
    device_id: str,
    start: str | None = None,
    end: str | None = None,
) -> str:
    """Return scheduled runs and skip events for a device in a date range.

    Useful for 'what's going to water this week?' or 'what did Rachio
    actually run last weekend?'. The response includes both ``runs``
    (with per-zone durations and start times) and ``skips`` (climate-
    skip, rain-delay, manual skips).

    Args:
        device_id: Controller UUID.
        start: Start date, ISO YYYY-MM-DD (default: today).
        end: End date, ISO YYYY-MM-DD (default: today + 14 days).
    """
    try:
        return _ok(
            _get_client().get_calendar(
                device_id,
                start=_parse_date(start),
                end=_parse_date(end),
            )
        )
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def get_active_alerts(
    device_id: str | None = None,
    zone_id: str | None = None,
) -> str:
    """Return unresolved alerts for a device or a specific zone.

    Alerts include things like low flow, high current, freeze skip,
    rain skip, hardware faults. Exactly one of device_id or zone_id
    must be supplied.

    Args:
        device_id: Controller UUID to query alerts for.
        zone_id: Zone UUID to query alerts for.
    """
    try:
        return _ok(
            alerts=_get_client().get_active_alerts(device_id=device_id, zone_id=zone_id)
        )
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def get_weather(
    location_id: str,
    start: str | None = None,
    end: str | None = None,
) -> str:
    """Return observed + forecast weather readings for a location.

    Each reading includes temperature range, precipitation (observed and
    probability of), humidity, wind, and ET (evapotranspiration). Used
    by Rachio's climate-skip logic.

    Args:
        location_id: Location UUID (from a device's ``location_id`` field).
        start: Start date, ISO YYYY-MM-DD (default: today - 3 days).
        end: End date, ISO YYYY-MM-DD (default: today + 7 days).
    """
    try:
        return _ok(
            _get_client().get_weather(
                location_id,
                start=_parse_date(start),
                end=_parse_date(end),
            )
        )
    except Exception as e:
        return _err(e)


# ======================================================================
# Schedule CRUD
# ======================================================================


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def list_schedules(
    device_id: str | None = None,
    location_id: str | None = None,
    zone_id: str | None = None,
    schedule_id: str | None = None,
) -> str:
    """List schedules matching exactly one filter.

    ``device_id``: all schedules on a controller.
    ``location_id``: all schedules at a property (across devices).
    ``zone_id``: all schedules that include a given zone.
    ``schedule_id``: fetch a single schedule by id (1-element result).

    Exactly one argument must be supplied.
    """
    try:
        return _ok(
            schedules=_get_client().list_schedules(
                device_id=device_id,
                location_id=location_id,
                zone_id=zone_id,
                schedule_id=schedule_id,
            )
        )
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def get_schedule(schedule_id: str) -> str:
    """Get a single schedule plus the locations/devices it runs on.

    Returns ``schedule`` (the full Schedule proto — criteria, restriction
    criteria, zone list, runtime flags, enabled state, summary) plus
    ``locations_and_devices`` (which property and controllers it spans).

    Args:
        schedule_id: Schedule UUID from list_schedules.
    """
    try:
        return _ok(_get_client().get_schedule(schedule_id))
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def preview_schedule(
    name: str,
    zones: list[dict],
    schedule_type: str = "FIXED",
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
) -> str:
    """Server-side dry-run of create_schedule. Does NOT persist anything.

    Returns the same Schedule that create_schedule would produce,
    including the server-generated human-readable ``summary`` like
    'Every Monday and Thursday at 5:00 AM'. Always call this first and
    verify the summary + zone breakdown before calling create_schedule.

    Args:
        name: Schedule display name, e.g. "Summer Lawn".
        zones: List of zone entries. Each must be a dict with keys:
            ``device_id`` (str), ``zone_id`` (str),
            ``watering_time`` (int seconds), optionally
            ``order_id`` (int, defaults to list position + 1),
            ``flex_aggression_coefficient`` (float, flex only),
            ``flex_runtime_coefficient`` (float, flex only).
        schedule_type: FIXED (default), FLEX_MONTHLY, or FLEX_DAILY.
        start_time: Daily start time HH:MM, e.g. "05:00". Use this for
            fixed clock-time schedules.
        start_sun: "SUNRISE" or "SUNSET" to anchor to solar time
            instead of a clock time. Provide at most one of start_time
            or start_sun.
        days: Days of week for FIXED schedules, e.g. ["MON", "THU"].
            Names accept MON/TUE/WED/THU/FRI/SAT/SUN (case-insensitive).
            Omit for schedules that run every day within the date window.
        annual_start: Recurring-yearly window start, MM-DD (e.g. "06-15"
            for mid-June). Use for seasonal schedules.
        annual_end: Recurring-yearly window end, MM-DD.
        smart_cycle: Let Rachio auto-calculate cycle and soak based on
            each zone's soil/slope/nozzle.
        cycle_soak: Enable manual cycle + soak. Combine with
            cycle_time_seconds and soak_time_seconds.
        cycle_time_seconds: Length of each watering cycle (seconds).
        soak_time_seconds: Rest interval between cycles (seconds).
        zone_delay_time_seconds: Delay between zones in the sequence.
        rain_delay_enabled: Skip runs after significant rain.
        freeze_delay_enabled: Skip runs when temp drops below freezing.
        wind_delay_enabled: Skip runs during high wind.
        climate_skip: Skip runs when climate/ET data suggests enough
            moisture is present.
        seasonal_shift: Seasonally adjust runtimes up/down.
    """
    try:
        return _ok(
            _get_client().preview_schedule(
                name=name,
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
        )
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    }
)
def create_schedule(
    name: str,
    zones: list[dict],
    schedule_type: str = "FIXED",
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
) -> str:
    """Create a new schedule. Persists to the Rachio backend.

    Strongly recommended: call ``preview_schedule`` with the same
    arguments first and review the returned ``summary`` before calling
    this. Every argument has the same meaning as in preview_schedule;
    see that tool's docstring for field details.

    Args:
        name: Schedule display name.
        zones: List of zone entries; see preview_schedule for shape.
        schedule_type: FIXED, FLEX_MONTHLY, or FLEX_DAILY.
        enabled: Whether the schedule starts enabled (default true).
        start_time: Daily start time HH:MM.
        start_sun: "SUNRISE" or "SUNSET".
        days: Days of week, e.g. ["MON", "WED", "FRI"].
        annual_start: Annual window start MM-DD.
        annual_end: Annual window end MM-DD.
        smart_cycle: Let Rachio auto-calculate cycle/soak.
        cycle_soak: Enable manual cycle+soak.
        cycle_time_seconds: Cycle length in seconds.
        soak_time_seconds: Soak duration in seconds.
        zone_delay_time_seconds: Delay between zones.
        rain_delay_enabled: Enable rain-delay skipping.
        freeze_delay_enabled: Enable freeze-delay skipping.
        wind_delay_enabled: Enable wind-delay skipping.
        climate_skip: Enable climate/ET skipping.
        seasonal_shift: Enable seasonal runtime adjustment.
    """
    try:
        return _ok(
            schedule=_get_client().create_schedule(
                name=name,
                schedule_type=schedule_type,
                zones=zones,
                enabled=enabled,
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
        )
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    }
)
def update_schedule(
    schedule_id: str,
    name: str | None = None,
    enabled: bool | None = None,
) -> str:
    """Partial update of an existing schedule.

    Currently supports renaming and toggling enabled/disabled. To change
    criteria, days, or zones, delete + recreate the schedule.

    Args:
        schedule_id: Schedule UUID to update.
        name: New display name (optional).
        enabled: New enabled state (optional).
    """
    try:
        return _ok(
            schedule=_get_client().update_schedule(
                schedule_id, name=name, enabled=enabled
            )
        )
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": True,
        "idempotentHint": False,
        "openWorldHint": True,
    }
)
def delete_schedule(schedule_id: str) -> str:
    """Permanently delete a schedule. This cannot be undone.

    Args:
        schedule_id: Schedule UUID to delete.
    """
    try:
        deleted = _get_client().delete_schedule(schedule_id)
        return _ok(deleted=deleted, schedule_id=schedule_id)
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    }
)
def copy_schedule(schedule_id: str) -> str:
    """Duplicate an existing schedule. Returns the new Schedule.

    Useful for creating seasonal variants from an existing template —
    copy, then update_schedule to rename.

    Args:
        schedule_id: Schedule UUID to copy.
    """
    try:
        return _ok(schedule=_get_client().copy_schedule(schedule_id))
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    }
)
def run_schedule(schedule_id: str) -> str:
    """Start an immediate run of the schedule right now.

    Returns the list of device_ids the run was dispatched to.

    Args:
        schedule_id: Schedule UUID to run.
    """
    try:
        device_ids = _get_client().run_schedule(schedule_id)
        return _ok(device_ids=device_ids)
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def skip_schedule(schedule_id: str, disabled: bool) -> str:
    """Toggle the skip-next-run flag on a schedule.

    ``disabled=true`` skips the schedule's next run; ``disabled=false``
    re-arms it. Applies only to the next occurrence.

    Args:
        schedule_id: Schedule UUID.
        disabled: True to skip next run, False to re-enable it.
    """
    try:
        return _ok(skip=_get_client().skip_schedule(schedule_id, disabled))
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def get_schedule_runs(
    schedule_id: str,
    start: str | None = None,
    end: str | None = None,
) -> str:
    """Return past runs + skips for a schedule in a date range.

    Useful for auditing 'did my Summer Lawn actually water last week?'.

    Args:
        schedule_id: Schedule UUID.
        start: Start date ISO YYYY-MM-DD (default: today - 30 days).
        end: End date ISO YYYY-MM-DD (default: today).
    """
    try:
        return _ok(
            _get_client().get_schedule_runs(
                schedule_id,
                start=_parse_date(start),
                end=_parse_date(end),
            )
        )
    except Exception as e:
        return _err(e)


# ======================================================================
# Live controller operations
# ======================================================================


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def stop_watering(device_id: str) -> str:
    """Stop all watering currently in progress on the device.

    If nothing is running, this is a no-op.

    Args:
        device_id: Controller UUID.
    """
    try:
        _get_client().stop_watering(device_id)
        return _ok(stopped=True, device_id=device_id)
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    }
)
def start_zones(
    device_id: str,
    zones: list[dict],
    cycle_soak: bool = False,
    cycle_duration_seconds: int | None = None,
    soak_duration_seconds: int | None = None,
) -> str:
    """Start a manual run of one or more zones in sequence.

    ``zones`` is a list of ``{"zone_number": <int>, "duration": <seconds>}``.
    ``zone_number`` is the 1-based hardware slot visible on the controller
    (not the zone UUID). Find it via ``list_zones`` -> each entry's
    ``zone_detail.zone_number``.

    Args:
        device_id: Controller UUID.
        zones: List of ``{zone_number, duration}`` dicts.
        cycle_soak: Apply cycle-and-soak to the run.
        cycle_duration_seconds: Cycle length when cycle_soak is true.
        soak_duration_seconds: Soak gap when cycle_soak is true.
    """
    try:
        run_id = _get_client().start_zones(
            device_id,
            zones,
            cycle_soak=cycle_soak,
            cycle_duration_seconds=cycle_duration_seconds,
            soak_duration_seconds=soak_duration_seconds,
        )
        return _ok(manual_schedule_id=run_id, device_id=device_id)
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    }
)
def set_rain_delay(device_id: str, expiration: str) -> str:
    """Set a rain-delay expiration for the device.

    The device will not run any schedules until the given time. Pass an
    ISO-8601 datetime (``2026-05-01T00:00:00Z``) or ``1970-01-01T00:00:00Z``
    to cancel an existing delay.

    Args:
        device_id: Controller UUID.
        expiration: ISO-8601 datetime when the delay expires.
    """
    try:
        _get_client().set_rain_delay(device_id, expiration)
        return _ok(device_id=device_id, expiration=expiration)
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    }
)
def skip_current_zone(device_id: str) -> str:
    """Skip to the next zone in the currently-running schedule.

    Does nothing if no schedule is running.

    Args:
        device_id: Controller UUID.
    """
    try:
        return _ok(_get_client().skip_current_zone(device_id))
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    }
)
def pause_watering(device_id: str, seconds: int) -> str:
    """Pause the currently-running zone for ``seconds``.

    Use resume_watering to continue before the pause expires; otherwise
    the run resumes automatically after ``seconds`` elapse.

    Args:
        device_id: Controller UUID.
        seconds: How long to pause (1 to 3600).
    """
    try:
        return _ok(_get_client().pause_watering(device_id, seconds))
    except Exception as e:
        return _err(e)


@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    }
)
def resume_watering(device_id: str) -> str:
    """Resume a paused zone run.

    Args:
        device_id: Controller UUID.
    """
    try:
        return _ok(_get_client().resume_watering(device_id))
    except Exception as e:
        return _err(e)


# ----------------------------------------------------------------------
# Entrypoint (stdio only)
# ----------------------------------------------------------------------


def main() -> None:
    """Run the MCP server over stdio.

    stdio is the only supported transport for v0.1. Remote HTTP with
    OAuth 2.1 will be added later if there's demand.
    """
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
