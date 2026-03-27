#!/usr/bin/env python3
"""Render a standard AI-to-AI handoff markdown scaffold."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

SECTION_TEMPLATE = """## 1. 当前任务目标

## 2. 当前进展

## 3. 关键上下文

## 4. 关键发现

## 5. 未完成事项

## 6. 建议接手路径

## 7. 风险与注意事项

## 下一位 Agent 的第一步建议
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a standard handoff markdown scaffold."
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output path. Supports the literal token {yymmdd}.",
    )
    parser.add_argument(
        "--date",
        help="Override date token with a yymmdd value such as 260327.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )
    return parser.parse_args()


def resolve_date(raw_date: str | None) -> str:
    if raw_date is None:
        return datetime.now().strftime("%y%m%d")
    if not re.fullmatch(r"\d{6}", raw_date):
        raise ValueError("--date must use yymmdd format, for example 260327")
    return raw_date


def expand_output_path(raw_output: str, yymmdd: str) -> Path:
    expanded = raw_output.replace("{yymmdd}", yymmdd)
    return Path(expanded).expanduser().resolve()


def write_template(output_path: Path, force: bool) -> None:
    if output_path.exists() and not force:
        raise FileExistsError(
            f"{output_path} already exists. Use --force to overwrite it."
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(SECTION_TEMPLATE, encoding="utf-8")


def main() -> int:
    args = parse_args()

    try:
        yymmdd = resolve_date(args.date)
        output_path = expand_output_path(args.output, yymmdd)
        write_template(output_path, args.force)
    except (ValueError, FileExistsError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
