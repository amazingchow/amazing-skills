---
name: python-project-from-scratch
description: Scaffold a new uv-based Python project from the bundled starter template and a structured config file. Use when asked to initialize or bootstrap a Python project, create project files such as pyproject.toml, Makefile, README.md, and src/tests from metadata, or render Jinja2 placeholders from a TOML, JSON, or YAML config. Also use for requests like "初始化 Python 项目", "搭建 Python 项目骨架", or "用配置文件渲染模板".
---

# Init Python Project

Use this skill to turn a small project brief into a ready-to-run Python repository.

## Workflow

1. Collect the project metadata in a config file. Prefer `assets/examples/project-config.toml`.
2. Render the bundled template with `scripts/render_project.py`.
3. In the generated project directory, initialize git with `git init` and switch to `master` using `git checkout -B master`.
4. Copy the generated `pre-commit` hook file into `.git/hooks/pre-commit`, then make it executable with `chmod +x .git/hooks/pre-commit`.
5. Review the generated repository and adjust dependencies or docs only if the user asked for extra customization.
6. When the environment allows it, finish by running `make install`, `make format`, and `make test` inside the generated project.

## Commands

Render into a new directory:

```bash
python3 scripts/render_project.py \
  --config /absolute/path/to/new-project/project-config.toml \
  --output /absolute/path/to/new-project
```

Overwrite an existing scaffold when the user explicitly wants regeneration:

```bash
python3 scripts/render_project.py \
  --config /absolute/path/to/existing-project/project-config.toml \
  --output /absolute/path/to/existing-project \
  --overwrite
```

After rendering, bootstrap git and install the local pre-commit hook:

```bash
cd /absolute/path/to/new-project
git init
git checkout -B master
cp pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Defaults

- Derive `package_name` from `project_name` when it is omitted.
- Default `python_version` to `3.12`.
- Default `minimum_python_version` to `python_version`.
- Default `copyright_year` to the current year.

## Resources

- Use `scripts/render_project.py` for deterministic rendering of both file contents and path names that contain Jinja2 placeholders.
- Use `assets/project-template/` as the source template tree.
- Read `references/configuration.md` only when you need the supported config keys, file formats, or renderer behavior.
