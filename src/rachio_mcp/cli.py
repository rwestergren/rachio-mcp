"""Interactive CLI for minting a long-lived Rachio access token.

Exposed as the ``rachio-mcp-token`` console script. Performs the OAuth 2
password grant against oauth.rach.io once, prints a copy-pasteable token,
and exits. The returned token lasts ~25 years — set it once as
``RACHIO_ACCESS_TOKEN`` in your MCP client config and never hand the
rachio-mcp process a password again.

Usage:
    rachio-mcp-token                         # interactive prompts
    rachio-mcp-token --email you@ex.com      # preseed email, prompt password
    RACHIO_EMAIL=... RACHIO_PASSWORD=... rachio-mcp-token --json

Flags:
    --email EMAIL       Skip the interactive email prompt.
    --json              Emit a single JSON object; no banner. Useful for
                        piping into password managers or CI secret stores.
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
import sys
from datetime import datetime, timedelta, timezone

from .client import RachioError, mint_access_token


def _read_email(preseed: str | None) -> str:
    if preseed:
        return preseed.strip()
    env = os.environ.get("RACHIO_EMAIL")
    if env:
        return env.strip()
    if not sys.stdin.isatty():
        raise RachioError(
            "stdin is not a TTY and RACHIO_EMAIL is not set. "
            "Pass --email EMAIL or set RACHIO_EMAIL in the environment."
        )
    return input("Rachio email: ").strip()


def _read_password() -> str:
    env = os.environ.get("RACHIO_PASSWORD")
    if env:
        return env
    if not sys.stdin.isatty():
        raise RachioError(
            "stdin is not a TTY and RACHIO_PASSWORD is not set. "
            "Set RACHIO_PASSWORD in the environment or run "
            "rachio-mcp-token from an interactive shell."
        )
    return getpass.getpass("Rachio password: ")


def _format_banner(data: dict) -> str:
    token = data["access_token"]
    user_id = data.get("user_id", "")
    expires_in = int(data.get("expires_in") or 0)
    expiry_date = (
        datetime.now(tz=timezone.utc) + timedelta(seconds=expires_in)
        if expires_in
        else None
    )
    lines: list[str] = []
    lines.append("")
    lines.append("✓ Token obtained.")
    if user_id:
        lines.append(f"  user_id : {user_id}")
    if expiry_date:
        days = expires_in // 86400
        lines.append(
            f"  expires : {expiry_date.date().isoformat()} "
            f"({days:,} days — effectively permanent)"
        )
    lines.append("")
    lines.append("Set this in your MCP client config env block:")
    lines.append("")
    lines.append(f'    "RACHIO_ACCESS_TOKEN": "{token}"')
    lines.append("")
    lines.append("Or export in your shell:")
    lines.append("")
    lines.append(f"    export RACHIO_ACCESS_TOKEN='{token}'")
    lines.append("")
    lines.append(
        "If this token is ever revoked (password change, explicit "
        "logout, etc.), rerun `rachio-mcp-token` to mint a new one."
    )
    lines.append("")
    return "\n".join(lines)


def _format_json(data: dict) -> str:
    expires_in = int(data.get("expires_in") or 0)
    expires_at = (
        (datetime.now(tz=timezone.utc) + timedelta(seconds=expires_in)).isoformat()
        if expires_in
        else None
    )
    return json.dumps(
        {
            "access_token": data["access_token"],
            "user_id": data.get("user_id"),
            "expires_in": expires_in,
            "expires_at": expires_at,
        },
        indent=2,
    )


def mint_token(argv: list[str] | None = None) -> int:
    """Console entry point: prompt for credentials, mint a token, print it.

    Returns an exit code (0 on success, non-zero on error).
    """
    ap = argparse.ArgumentParser(
        prog="rachio-mcp-token",
        description=(
            "Mint a long-lived Rachio access token for use with rachio-mcp. "
            "Performs the OAuth password grant once; the resulting token "
            "is long-lived and can be set as RACHIO_ACCESS_TOKEN in your "
            "MCP client config."
        ),
    )
    ap.add_argument(
        "--email",
        help="Rachio account email. If omitted, reads RACHIO_EMAIL env var "
        "or prompts interactively.",
    )
    ap.add_argument(
        "--json",
        action="store_true",
        help="Emit a single JSON object with access_token, user_id, and "
        "expires_at; no banner. Suitable for piping to other tools.",
    )
    args = ap.parse_args(argv)

    try:
        email = _read_email(args.email)
        password = _read_password()
    except RachioError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    try:
        data = mint_access_token(email, password)
    except RachioError as e:
        print(f"Login failed: {e}", file=sys.stderr)
        return 1

    if args.json:
        print(_format_json(data))
    else:
        print(_format_banner(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(mint_token())
