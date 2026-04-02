A curated collection of reusable skills for AI coding agents.

Each skill packages practical instructions, workflows, and optional helper assets to make agents more consistent and effective in real projects.

This repository follows the [Agent Skills](https://agentskills.io/) format.

## Available Skills

| Skill | What It Does |
| --- | --- |
| `handoff-your-work` | Produces high-signal AI-to-AI handoff briefs that let a fresh agent continue work quickly. |
| `python-project-from-scratch` | Scaffolds a new `uv`-based Python project from a structured config file and bundled templates. |
| `python-unix-philosophy` | Applies Unix philosophy to Python design, refactoring, and code review decisions. |
| `sync-self-explanatory-docs` | Keeps Python architecture docs aligned with code across root, package, and module levels. |
| `ui-aesthetic-best-practices` | Turns reference websites or Figma boards into design systems, AI guardrails, and more original high-aesthetic UI directions. |

## Installation

```bash
npx skills add https://github.com/amazingchow/amazing-skills
```

## Usage

After installation, these skills become available to your agent automatically. The agent will invoke them when your task matches a skill's intent.

Example prompts:

```text
Initialize a Python project from this TOML config.
```

```text
Review this Python module using Unix philosophy principles.
```

```text
I refactored the package layout. Sync architecture docs with the code.
```

```text
Create a handoff brief for the next agent in ./260327-handoff.md.
```

```text
Use the UI aesthetic skill to turn these reference websites into a design system and a more original landing page direction.
```

## Skill Structure

Each skill directory can include:

- `SKILL.md`: Core instructions and workflow for the agent
- `scripts/`: Helper scripts for deterministic execution (optional)
- `references/`: Supplemental docs and checklists (optional)
- `assets/`: Templates or static resources (optional)

## License

MIT
