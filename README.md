# rachio-mcp

<!-- mcp-name: io.github.rwestergren/rachio-mcp -->

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) server for [Rachio](https://rachio.com/) sprinkler controllers, built on the reverse-engineered Android-app gRPC API.

The [public Rachio API](https://rachio.readme.io/) exposes only read-only access to schedules and a handful of single-action endpoints. This server instead talks to the same internal gRPC backend (`cloud.rach.io:443`) that the official mobile app uses, giving an agent the full set of operations: listing devices and zones, inspecting schedules, **creating and previewing new schedules**, updating and deleting them, starting and stopping manual zone runs, setting rain delays, and more.

> ⚠️ **Unofficial.** This server uses a reverse-engineered API. It works as of Rachio Android v4.21.18 and is not supported by Rachio. The schema can change without notice.

## Features

- **Devices and zones** — list controllers, sensors, and weather stations; inspect zone soil/nozzle/plant configuration and live state
- **Schedules** — list, read, preview (dry-run), create, update, delete, copy, run, and skip schedules
- **Live control** — stop watering, run specific zones manually, set rain delays, skip/pause/resume the currently-running zone
- **Context** — calendar of upcoming runs, recent/past run history, active alerts, observed/forecast weather readings

## Quick Start

### 1. Install [uv](https://docs.astral.sh/uv/)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Mint a long-lived access token

The MCP server itself never sees your Rachio password. Instead you mint a long-lived (~25-year) access token once, and supply only the token to the MCP client.

```bash
uvx --from rachio-mcp rachio-mcp-token
```

It will prompt for your Rachio email and password, then print a `RACHIO_ACCESS_TOKEN` value to paste into your MCP client config. The token remains valid until you change your password or explicitly log out from another device.

Or, if you'd rather have the commands on your PATH permanently, install once:

```bash
uv tool install rachio-mcp
```

Then `rachio-mcp-token` (and `rachio-mcp` itself) are available as regular commands.

For scripting (e.g. pipe into a password manager):

```bash
RACHIO_EMAIL=you@example.com RACHIO_PASSWORD=... \
    uvx --from rachio-mcp rachio-mcp-token --json | jq .access_token
```

### 3. Configure your MCP client

`uvx` downloads and runs the server on demand — no separate install step required.

#### OpenCode (`opencode.json`)

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "rachio": {
      "type": "local",
      "command": ["uvx", "rachio-mcp"],
      "environment": {
        "RACHIO_ACCESS_TOKEN": "{env:RACHIO_ACCESS_TOKEN}"
      },
      "enabled": true
    }
  }
}
```

#### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "rachio": {
      "command": "uvx",
      "args": ["rachio-mcp"],
      "env": {
        "RACHIO_ACCESS_TOKEN": "paste-your-token-here"
      }
    }
  }
}
```

If a tool call later returns a "token rejected" error, rerun `rachio-mcp-token` to mint a fresh one and update the config.

## Available Tools

24 tools over stdio transport.

### Discovery

| Tool | Description |
|------|-------------|
| `list_devices` | Every device on the account — controllers, sensors, weather stations |
| `get_device` | Full details + live state for a single device |
| `list_zones` | Zones configured on a controller, with agronomic metadata |
| `get_zone` | Full detail for a single zone |
| `get_calendar` | Scheduled runs + skip events for a date range |
| `get_run_history` | Observed recent/past zone-run telemetry plus calendar context |
| `get_active_alerts` | Unresolved alerts on a device or zone |
| `get_weather` | Observed + forecast weather readings for a location |

### Schedule CRUD

| Tool | Description |
|------|-------------|
| `list_schedules` | Filter by device, location, zone, or schedule id |
| `get_schedule` | Single schedule + its locations/devices |
| `preview_schedule` | **Dry-run** — returns the Schedule that `create_schedule` would produce, including the server-generated human-readable summary. Never persists |
| `create_schedule` | Create a new schedule |
| `update_schedule` | Partial-merge edit: name, enabled, timing/criteria, day restrictions, and per-zone add/update/remove |
| `delete_schedule` | Permanent, destructive |
| `copy_schedule` | Duplicate an existing schedule |
| `run_schedule` | Trigger an immediate run |
| `skip_schedule` | Skip or re-arm the next scheduled run |
| `get_schedule_runs` | Past runs + skip events for a schedule |

### Live controller ops

| Tool | Description |
|------|-------------|
| `stop_watering` | Stop whatever is running |
| `start_zones` | Start one or more zones manually by zone number + duration |
| `set_rain_delay` | Defer all schedules until a given time |
| `skip_current_zone` | Skip to the next zone in the active run |
| `pause_watering` | Pause the current zone for N seconds |
| `resume_watering` | Resume a paused run |

All `device_id`, `zone_id`, `schedule_id`, and `location_id` parameters are UUIDs obtained from the `list_*` tools. Dates use `YYYY-MM-DD` (or `MM-DD` for annual-recurring schedules); times use `HH:MM`.

## Recommended Workflow for Schedule Changes

1. `list_devices` → pick your controller
2. `list_zones(device_id=...)` → note each zone's id and `zone_number`
3. `list_schedules(device_id=...)` and `get_schedule(schedule_id=...)` → understand what's already configured
4. `preview_schedule(...)` → dry-run your proposed schedule. Read the returned `summary` string and the per-zone breakdown
5. `create_schedule(...)` (same arguments) → commit
6. `get_schedule(schedule_id=<new>)` → confirm
7. `delete_schedule(schedule_id=<new>)` → rollback if needed

`preview_schedule` is safe to call repeatedly — it never writes anything.

To edit an existing schedule instead of recreating it, use `update_schedule`. It performs a partial merge: read the schedule with `get_schedule`, then pass only the fields you want to change (name, enabled, timing/criteria, `days`, or `zones`/`zone_ids_to_remove`). Omitted fields are left untouched.

## How It Works

This server talks to `cloud.rach.io:443` over TLS-protected gRPC, the same backend used by the Rachio Android app. Authentication uses the OAuth 2 password grant against `oauth.rach.io/oAuth/token` with the Android app's hardcoded client credentials.

The gRPC `.proto` definitions were recovered by decompiling the Rachio Android APK (v4.21.18) with jadx, extracting the embedded `FileDescriptorProto` payloads from the generated Java classes, and round-tripping them through `protoc` to produce clean `.proto` source. Pre-compiled Python stubs for the 40-odd messages/services used by the 23 MCP tools ship in `src/rachio_mcp/proto/`.

Regenerate those stubs any time the app's proto surface changes:

```bash
scripts/build_protos.sh
```

The stub generator reads from `reverse-engineering/protos/`, which is not shipped in the wheel but is kept alongside the source for future updates.

## Python API

The MCP server wraps a standalone client you can use directly:

```python
from rachio_mcp import RachioClient

c = RachioClient()

# Discovery
for d in c.list_devices():
    print(d["type"], d["id"], d.get("name"))

# Preview a proposed schedule
preview = c.preview_schedule(
    name="Fall Lawn",
    schedule_type="FIXED",
    zones=[
        {"device_id": "<controller>", "zone_id": "<zone>", "watering_time": 1200},
    ],
    start_time="06:00",
    days=["WED"],
    annual_start="09-16",
    annual_end="11-15",
    smart_cycle=True,
)
print(preview["summary"])

# Commit
created = c.create_schedule(name="Fall Lawn", ...)
print("created", created["id"])

# Rollback
c.delete_schedule(created["id"])
```

The client reads `RACHIO_ACCESS_TOKEN` from the environment, derives the user's `user_id` lazily on first use (via `LocationService.ListLocations`), and keeps both in memory for the lifetime of the process. Nothing is written to disk.

## Environment

| Variable | Required | Description |
|----------|----------|-------------|
| `RACHIO_ACCESS_TOKEN` | Yes | Long-lived bearer token minted by `rachio-mcp-token`. Valid for ~25 years unless revoked. |
| `LOG_LEVEL` | No | Python logging level (default: INFO). Logs go to stderr; stdio transport's stdout is reserved for the MCP protocol. |

### Minting a token (one-time setup)

| Variable | Used by | Description |
|----------|---------|-------------|
| `RACHIO_EMAIL` | `rachio-mcp-token` only | Rachio account email. If unset, `rachio-mcp-token` prompts interactively. |
| `RACHIO_PASSWORD` | `rachio-mcp-token` only | Rachio account password. If unset, `rachio-mcp-token` prompts interactively with a masked input. |

Neither `RACHIO_EMAIL` nor `RACHIO_PASSWORD` is ever read by the MCP server itself — they exist only to feed the one-time token-mint CLI.

## Transport

stdio only. Remote HTTP with OAuth 2.1 is not supported in v0.1.

## License

MIT — see [LICENSE](LICENSE).
