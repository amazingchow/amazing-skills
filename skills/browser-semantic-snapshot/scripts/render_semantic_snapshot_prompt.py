#!/usr/bin/env python3
"""Render a browser semantic snapshot into a Claude/Codex-ready prompt."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

VALID_AUTH_STATES = {"public", "authenticated", "login_required", "unknown"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Wrap a raw browser semantic snapshot in a standard format for Claude Code or Codex."
        )
    )
    parser.add_argument("--url", required=True, help="Original source URL.")
    parser.add_argument("--final-url", help="Final URL after redirects.")
    parser.add_argument("--page-title", default="unknown", help="Current page title.")
    parser.add_argument(
        "--auth-state",
        choices=sorted(VALID_AUTH_STATES),
        default="unknown",
        help="Access state observed while capturing the page.",
    )
    parser.add_argument(
        "--snapshot-file",
        help="Path to a text file containing the raw semantic snapshot.",
    )
    parser.add_argument(
        "--task",
        help="Optional task for the downstream agent, such as summarizing or locating actions.",
    )
    parser.add_argument(
        "--note",
        action="append",
        default=[],
        help="Optional note to include in the output. Repeat for multiple notes.",
    )
    parser.add_argument(
        "--captured-at",
        help="UTC timestamp in ISO 8601 format. Defaults to the current UTC time.",
    )
    parser.add_argument(
        "--output",
        help="Write the rendered prompt to this file instead of stdout.",
    )
    return parser.parse_args()


def load_snapshot(path_value: str | None) -> str:
    if not path_value:
        return ""
    path = Path(path_value).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Snapshot file not found: {path}")
    return path.read_text().rstrip("\n")


def resolve_timestamp(raw_timestamp: str | None) -> str:
    if raw_timestamp:
        return raw_timestamp
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def render_notes(notes: list[str]) -> list[str]:
    if not notes:
        return ["notes: none"]
    lines = ["notes:"]
    lines.extend(f"- {note}" for note in notes)
    return lines


def render_login_required(args: argparse.Namespace, captured_at: str) -> str:
    lines = [
        "This page needs authenticated browser access before I can capture a useful semantic snapshot. Please log in manually in the browser session that will be used for extraction, then tell me to continue.",
        "",
        "If the page requires SSO, 2FA, CAPTCHA, or consent, please complete that flow manually in the same session as well.",
        "",
        "<browser-page-semantic-snapshot-status>",
        f"source_url: {args.url}",
        f"final_url: {args.final_url or args.url}",
        f"page_title: {args.page_title}",
        "auth_state: login_required",
        f"captured_at: {captured_at}",
    ]
    lines.extend(render_notes(args.note))
    lines.append("</browser-page-semantic-snapshot-status>")
    return "\n".join(lines) + "\n"


def render_snapshot_prompt(args: argparse.Namespace, captured_at: str, snapshot: str) -> str:
    lines = [
        "You are given a browser page semantic snapshot extracted from the accessibility tree, not a screenshot.",
        "Use element refs exactly as written when proposing clicks, fills, assertions, or navigation.",
    ]

    if args.task:
        lines.extend(["", "Task", args.task])

    lines.extend(
        [
            "",
            "<browser-page-semantic-snapshot>",
            f"source_url: {args.url}",
            f"final_url: {args.final_url or args.url}",
            f"page_title: {args.page_title}",
            f"auth_state: {args.auth_state}",
            f"captured_at: {captured_at}",
        ]
    )
    lines.extend(render_notes(args.note))
    lines.append("snapshot:")
    lines.extend(snapshot.splitlines())
    lines.append("</browser-page-semantic-snapshot>")
    return "\n".join(lines) + "\n"


def write_output(rendered: str, output_path: str | None) -> None:
    if not output_path:
        sys.stdout.write(rendered)
        return
    path = Path(output_path).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered)


def main() -> int:
    args = parse_args()
    captured_at = resolve_timestamp(args.captured_at)

    try:
        snapshot = load_snapshot(args.snapshot_file)
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    if args.auth_state == "login_required":
        rendered = render_login_required(args, captured_at)
        write_output(rendered, args.output)
        return 0

    if not snapshot.strip():
        print(
            "[ERROR] --snapshot-file is required unless --auth-state login_required.",
            file=sys.stderr,
        )
        return 1

    rendered = render_snapshot_prompt(args, captured_at, snapshot)
    write_output(rendered, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
