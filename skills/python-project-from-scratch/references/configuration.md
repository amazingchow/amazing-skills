# Configuration

Use `assets/examples/project-config.toml` as the canonical example.

## Supported Config Formats

- `.toml`
- `.json`
- `.yaml` or `.yml`

YAML support is optional and requires `PyYAML`. TOML and JSON work without extra parsing dependencies on modern Python.

## Required Keys

- `project_name`
- `project_description`
- `your_real_name`
- `your_email`
- `your_github_username`

## Optional Keys

- `package_name`
- `python_version`
- `minimum_python_version`
- `copyright_year`

## Derived Defaults

- Derive `package_name` from `project_name` by converting it to snake_case.
- Default `python_version` to `3.12`.
- Default `minimum_python_version` to `python_version`.
- Default `copyright_year` to the current year.

## Renderer Behavior

- Render file contents with Jinja2 using `StrictUndefined`, so missing variables fail fast.
- Render path names too, so directories such as `src/{{ package_name }}/` become real package paths.
- Refuse to write into a non-empty output directory unless `--overwrite` is set.
