#!/usr/bin/env python3
"""Copy the bundled design-system template into a target workspace."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the bundled design-system template into a target path."
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Absolute or relative output path for the copied design-system-template directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output path if it already exists.",
    )
    return parser.parse_args()


def remove_existing(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
        return
    path.unlink()


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parents[1]
    template_dir = skill_dir / "assets" / "design-system-template"
    output_dir = Path(args.output).expanduser().resolve()

    if not template_dir.is_dir():
        print(f"[ERROR] Missing template directory: {template_dir}", file=sys.stderr)
        return 1

    if output_dir.exists():
        if not args.force:
            print(
                f"[ERROR] Output already exists: {output_dir}. Use --force to overwrite.",
                file=sys.stderr,
            )
            return 1
        remove_existing(output_dir)

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(template_dir, output_dir)
    print(f"[OK] Scaffolded design-system template to: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
