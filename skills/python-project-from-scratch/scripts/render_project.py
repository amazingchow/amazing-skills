#!/usr/bin/env python3
"""Render the bundled Python project template with Jinja2."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

try:
    from jinja2 import Environment, StrictUndefined
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Jinja2 is required. Install it with `python3 -m pip install jinja2`."
    ) from exc

REQUIRED_KEYS = (
    "project_name",
    "project_description",
    "your_real_name",
    "your_email",
    "your_github_username",
)

SUPPORTED_CONFIG_SUFFIXES = {".toml", ".json", ".yaml", ".yml"}


class ConfigError(ValueError):
    """Raised when the project configuration is invalid."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render the bundled Python project template from a config file."
    )
    parser.add_argument(
        "--config",
        required=True,
        type=Path,
        help="Path to a TOML, JSON, or YAML config file.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Directory where the rendered project should be written.",
    )
    parser.add_argument(
        "--template-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "assets" / "project-template",
        help="Override the template directory. Defaults to the bundled project template.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow writing into an existing non-empty output directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the files that would be rendered without writing them.",
    )
    return parser.parse_args()


def load_config(config_path: Path) -> dict[str, Any]:
    if not config_path.exists():
        raise ConfigError(f"Config file not found: {config_path}")

    suffix = config_path.suffix.lower()
    if suffix not in SUPPORTED_CONFIG_SUFFIXES:
        supported = ", ".join(sorted(SUPPORTED_CONFIG_SUFFIXES))
        raise ConfigError(f"Unsupported config format '{suffix}'. Use one of: {supported}")

    if suffix == ".toml":
        if tomllib is None:  # pragma: no cover
            raise ConfigError("TOML parsing requires Python 3.11+.")
        with config_path.open("rb") as handle:
            data = tomllib.load(handle)
    elif suffix == ".json":
        data = json.loads(config_path.read_text(encoding="utf-8"))
    else:
        if yaml is None:
            raise ConfigError(
                "YAML config support requires PyYAML. Install it with "
                "`python3 -m pip install pyyaml` or use TOML/JSON."
            )
        data = yaml.safe_load(config_path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        raise ConfigError("Config file must contain a top-level object/dictionary.")

    return data


def normalize_package_name(project_name: str) -> str:
    package_name = re.sub(r"[^a-zA-Z0-9]+", "_", project_name.strip().lower())
    package_name = package_name.strip("_")
    if not package_name:
        raise ConfigError("Unable to derive package_name from project_name.")
    if package_name[0].isdigit():
        package_name = f"pkg_{package_name}"
    return package_name


def build_context(raw_config: dict[str, Any]) -> dict[str, Any]:
    context = dict(raw_config)

    missing = [key for key in REQUIRED_KEYS if not str(context.get(key, "")).strip()]
    if missing:
        raise ConfigError(f"Missing required config keys: {', '.join(missing)}")

    project_name = str(context["project_name"]).strip()
    context["project_name"] = project_name
    context["project_description"] = str(context["project_description"]).strip()
    context["your_real_name"] = str(context["your_real_name"]).strip()
    context["your_email"] = str(context["your_email"]).strip()
    context["your_github_username"] = str(context["your_github_username"]).strip()

    context.setdefault("package_name", normalize_package_name(project_name))
    context["package_name"] = normalize_package_name(str(context["package_name"]))
    context.setdefault("python_version", "3.12")
    context["python_version"] = str(context["python_version"]).strip()
    context.setdefault("minimum_python_version", context["python_version"])
    context["minimum_python_version"] = str(context["minimum_python_version"]).strip()
    context.setdefault("copyright_year", str(datetime.now().year))
    context["copyright_year"] = str(context["copyright_year"]).strip()

    return context


def build_environment() -> Environment:
    return Environment(
        autoescape=False,
        keep_trailing_newline=True,
        lstrip_blocks=False,
        trim_blocks=False,
        # Avoid collisions with shell syntax like `${#var}` in templates.
        comment_start_string="[#",
        comment_end_string="#]",
        undefined=StrictUndefined,
    )


def render_text(environment: Environment, template_text: str, context: dict[str, Any]) -> str:
    return environment.from_string(template_text).render(**context)


def render_relative_path(
    environment: Environment, relative_path: Path, context: dict[str, Any]
) -> Path:
    rendered_parts = [render_text(environment, part, context) for part in relative_path.parts]
    return Path(*rendered_parts)


def ensure_output_dir(output_dir: Path, overwrite: bool) -> None:
    if output_dir.exists():
        if not output_dir.is_dir():
            raise ConfigError(f"Output path is not a directory: {output_dir}")
        if any(output_dir.iterdir()) and not overwrite:
            raise ConfigError(
                f"Output directory is not empty: {output_dir}. Use --overwrite to continue."
            )
        return

    output_dir.mkdir(parents=True, exist_ok=True)


def render_tree(
    template_dir: Path,
    output_dir: Path,
    context: dict[str, Any],
    overwrite: bool,
    dry_run: bool,
) -> list[Path]:
    if not template_dir.exists():
        raise ConfigError(f"Template directory not found: {template_dir}")

    environment = build_environment()
    written_paths: list[Path] = []

    for source_path in sorted(template_dir.rglob("*")):
        relative_path = source_path.relative_to(template_dir)
        destination_path = output_dir / render_relative_path(environment, relative_path, context)

        if source_path.is_dir():
            if dry_run:
                print(f"mkdir {destination_path}")
            else:
                destination_path.mkdir(parents=True, exist_ok=True)
            continue

        if destination_path.exists() and not overwrite:
            raise ConfigError(
                f"Refusing to overwrite existing file without --overwrite: {destination_path}"
            )

        if dry_run:
            print(f"render {destination_path}")
            written_paths.append(destination_path)
            continue

        destination_path.parent.mkdir(parents=True, exist_ok=True)
        source_bytes = source_path.read_bytes()
        try:
            source_text = source_bytes.decode("utf-8")
        except UnicodeDecodeError:
            shutil.copy2(source_path, destination_path)
        else:
            rendered_text = render_text(environment, source_text, context)
            destination_path.write_text(rendered_text, encoding="utf-8")
            shutil.copystat(source_path, destination_path)
        written_paths.append(destination_path)

    return written_paths


def main() -> int:
    args = parse_args()

    try:
        config = build_context(load_config(args.config.resolve()))
        output_dir = args.output.resolve()
        template_dir = args.template_dir.resolve()
        ensure_output_dir(output_dir, args.overwrite)
        written_paths = render_tree(
            template_dir=template_dir,
            output_dir=output_dir,
            context=config,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
        )
    except ConfigError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    action = "Would render" if args.dry_run else "Rendered"
    print(f"{action} {len(written_paths)} files into {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
