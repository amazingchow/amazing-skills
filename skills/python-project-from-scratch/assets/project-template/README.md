# {{ project_name }}

{{ project_description }}

## Quick Start

1. Install `uv`.
2. Run `make init`.
3. Run `make test`.
4. Run `make run`.

## Project Layout

```text
.
|-- src/{{ package_name }}/
|-- tests/
|-- pyproject.toml
`-- Makefile
```

## Development

- Format code with `make format`
- Lint with `make lint`
- Run tests with `make test`
- Run pre-commit hooks with `make pre-commit`

## Publishing Notes

- Package name: `{{ package_name }}`
- Python version: `>= {{ minimum_python_version }}`
- Repository owner: `{{ your_github_username }}`
