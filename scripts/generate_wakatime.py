#!/usr/bin/env python3
"""Generate the profile's WakaTime SVG cards using the authenticated API."""

from __future__ import annotations

import html
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API = "https://api.wakatime.com/api/v1"
RETRIES = 6
RETRY_DELAY = 15
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

PURPLE, LAVENDER = "#A78BFA", "#C4B5FD"
TEXT, MUTED, TRACK = "#E7E0F2", "#A79BB8", "#30283D"
PALETTE = [PURPLE, "#9476E8", "#8062D5", "#B9A0F5", "#7154B8", LAVENDER]
FONT = "Inter,Segoe UI,Arial,sans-serif"


class WakaTimeError(RuntimeError):
    """Raised when WakaTime data cannot be retrieved or parsed."""


def get_json(endpoint: str, token: str) -> tuple[int, dict[str, Any]]:
    request = Request(
        f"{API}/{endpoint}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "User-Agent": "NiZaMinius-GitHub-Profile/1.0",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            status, body = response.status, response.read().decode("utf-8")
    except HTTPError as error:
        status = error.code
        body = error.read().decode("utf-8", errors="replace")
        if status not in (202, 429, 500, 502, 503, 504):
            raise WakaTimeError(
                f"WakaTime returned HTTP {status} for {endpoint}. "
                "Check that the WAKATIME_API_KEY secret contains an OAuth token "
                "with the read_stats scope."
            ) from None
    except (URLError, TimeoutError) as error:
        raise WakaTimeError(f"Could not reach WakaTime API: {error}") from None

    try:
        return status, json.loads(body)
    except json.JSONDecodeError:
        raise WakaTimeError(f"WakaTime returned invalid JSON for {endpoint} (HTTP {status}).") from None


def fetch_data(endpoint: str, token: str) -> dict[str, Any]:
    last_data: dict[str, Any] | None = None
    for attempt in range(RETRIES):
        status, payload = get_json(endpoint, token)
        data = payload.get("data")
        if isinstance(data, dict):
            last_data = data
        retryable = status in (202, 429, 500, 502, 503, 504) or (
            isinstance(data, dict) and data.get("is_up_to_date") is False
        )
        if not retryable:
            if not isinstance(data, dict):
                raise WakaTimeError(f"Unexpected WakaTime response for {endpoint}: missing data object.")
            return data
        if attempt < RETRIES - 1:
            delay = RETRY_DELAY * (2 if status >= 400 else 1)
            print(f"WakaTime is refreshing {endpoint}; retrying in {delay}s ({attempt + 1}/{RETRIES - 1}).")
            time.sleep(delay)
    if last_data is not None:
        print(f"::warning::WakaTime refresh for {endpoint} did not finish; using latest returned data.")
        return last_data
    raise WakaTimeError(f"WakaTime did not return data for {endpoint}.")


def esc(value: Any) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def as_number(value: Any) -> float:
    try:
        result = float(value)
        return max(0.0, result)
    except (TypeError, ValueError):
        return 0.0


def pct(value: Any) -> str:
    value = as_number(value)
    return f"{value:.2f}%" if 0 < value < 0.1 else f"{value:.1f}%"


def short_name(value: Any, limit: int = 23) -> str:
    name = str(value or "Unknown")
    return name if len(name) <= limit else name[: limit - 1] + "…"


def metric_rows(items: list[dict[str, Any]], x: int, y: int, width: int) -> str:
    if not items:
        return f'<text x="{x}" y="{y + 4}" fill="{MUTED}" font-size="13" font-family="{FONT}">No recent data available</text>'
    rows = []
    for index, item in enumerate(items[:3]):
        row_y = y + index * 47
        value = as_number(item.get("percent"))
        bar = min(width, width * value / 100)
        rows.append(
            f'<text x="{x}" y="{row_y}" fill="{TEXT}" font-size="13" font-family="{FONT}">{esc(short_name(item.get("name")))}</text>'
            f'<text x="{x + width}" y="{row_y}" fill="{MUTED}" font-size="12" text-anchor="end" font-family="{FONT}">{pct(value)}</text>'
            f'<rect x="{x}" y="{row_y + 9}" width="{width}" height="5" rx="2.5" fill="{TRACK}" />'
            f'<rect x="{x}" y="{row_y + 9}" width="{bar:.2f}" height="5" rx="2.5" fill="{PURPLE}" />'
        )
    return "\n".join(rows)


def overview_svg(total: str, editors: list[dict[str, Any]], systems: list[dict[str, Any]], updated: str) -> str:
    editors = sorted(editors, key=lambda item: as_number(item.get("total_seconds")), reverse=True)
    systems = sorted(systems, key=lambda item: as_number(item.get("total_seconds")), reverse=True)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="238" viewBox="0 0 920 238" role="img" aria-labelledby="title desc">
  <title id="title">WakaTime coding overview</title>
  <desc id="desc">All-time coding time, editors and operating systems used during the last 30 days.</desc>
  <defs><linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="{PURPLE}"/><stop offset="100%" stop-color="{LAVENDER}"/></linearGradient></defs>
  <text x="28" y="32" fill="{PURPLE}" font-family="{FONT}" font-size="12" font-weight="700" letter-spacing="2.2">CODING OVERVIEW</text>
  <text x="892" y="32" fill="{MUTED}" font-family="{FONT}" font-size="11" text-anchor="end">UPDATED {esc(updated)}</text>
  <line x1="28" y1="49" x2="892" y2="49" stroke="{PURPLE}" stroke-opacity="0.28"/>
  <text x="30" y="83" fill="{MUTED}" font-family="{FONT}" font-size="11" font-weight="600" letter-spacing="1.3">TOTAL CODING TIME · ALL TIME</text>
  <text x="30" y="132" fill="{TEXT}" font-family="{FONT}" font-size="34" font-weight="700">{esc(total)}</text>
  <rect x="30" y="151" width="270" height="3" rx="1.5" fill="url(#accent)"/>
  <text x="30" y="180" fill="{MUTED}" font-family="{FONT}" font-size="12">Tracked by WakaTime since account creation</text>
  <line x1="347" y1="68" x2="347" y2="210" stroke="{PURPLE}" stroke-opacity="0.25"/>
  <text x="394" y="82" fill="{LAVENDER}" font-family="{FONT}" font-size="11" font-weight="700" letter-spacing="1.4">EDITORS · LAST 30 DAYS</text>
  {metric_rows(editors, 394, 111, 190)}
  <line x1="635" y1="68" x2="635" y2="210" stroke="{PURPLE}" stroke-opacity="0.25"/>
  <text x="665" y="82" fill="{LAVENDER}" font-family="{FONT}" font-size="11" font-weight="700" letter-spacing="1.4">OPERATING SYSTEMS · LAST 30 DAYS</text>
  {metric_rows(systems, 665, 111, 190)}
</svg>\n'''


def languages_svg(languages: list[dict[str, Any]], updated: str) -> str:
    languages = sorted(languages, key=lambda item: as_number(item.get("total_seconds")), reverse=True)[:10]
    height = 92 + max(1, len(languages)) * 31
    rows = []
    for index, language in enumerate(languages):
        y = 78 + index * 31
        value = as_number(language.get("percent"))
        width = min(560, 560 * value / 100)
        rows.append(
            f'<text x="30" y="{y + 12}" fill="{TEXT}" font-family="{FONT}" font-size="13">{esc(short_name(language.get("name"), 30))}</text>'
            f'<rect x="230" y="{y + 2}" width="560" height="10" rx="5" fill="{TRACK}"/>'
            f'<rect x="230" y="{y + 2}" width="{width:.2f}" height="10" rx="5" fill="{PALETTE[index % len(PALETTE)]}"/>'
            f'<text x="860" y="{y + 12}" fill="{LAVENDER}" font-family="{FONT}" font-size="12" text-anchor="end">{pct(value)}</text>'
        )
    if not rows:
        rows.append(f'<text x="30" y="91" fill="{MUTED}" font-family="{FONT}" font-size="13">No language statistics are available yet.</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="{height}" viewBox="0 0 920 {height}" role="img" aria-labelledby="title desc">
  <title id="title">WakaTime language distribution</title>
  <desc id="desc">Share of tracked coding time by language, all time.</desc>
  <text x="28" y="32" fill="{PURPLE}" font-family="{FONT}" font-size="12" font-weight="700" letter-spacing="2.2">LANGUAGES BY CODING TIME</text>
  <text x="892" y="32" fill="{MUTED}" font-family="{FONT}" font-size="11" text-anchor="end">ALL TIME · UPDATED {esc(updated)}</text>
  <line x1="28" y1="49" x2="892" y2="49" stroke="{PURPLE}" stroke-opacity="0.28"/>
  {''.join(rows)}
</svg>\n'''


def write_if_changed(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        print(f"Unchanged: {path.relative_to(ROOT)}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"Generated: {path.relative_to(ROOT)}")


def main() -> int:
    token = os.environ.get("WAKATIME_OAUTH_TOKEN") or os.environ.get("WAKATIME_API_KEY")
    if not token:
        print("::error::Missing OAuth token. Set the WAKATIME_API_KEY secret to a personal WakaTime OAuth access token.")
        return 1
    try:
        total = fetch_data("users/current/all_time_since_today", token)
        all_time = fetch_data("users/current/stats/all_time", token)
        recent = fetch_data("users/current/stats/last_30_days", token)
    except WakaTimeError as error:
        print(f"::error::{error}")
        return 1

    total_text = (total.get("text") or all_time.get("human_readable_total_including_other_language")
                  or all_time.get("human_readable_total") or "No tracked time yet")
    languages = all_time.get("languages") or []
    editors = recent.get("editors") or []
    systems = recent.get("operating_systems") or []
    if not all(isinstance(value, list) for value in (languages, editors, systems)):
        print("::error::Unexpected WakaTime response: expected language, editor and OS arrays.")
        return 1

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    write_if_changed(ASSETS / "wakatime-overview.svg", overview_svg(str(total_text), editors, systems, updated))
    write_if_changed(ASSETS / "wakatime-languages.svg", languages_svg(languages, updated))
    return 0


if __name__ == "__main__":
    sys.exit(main())
