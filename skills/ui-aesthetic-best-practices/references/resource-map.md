# Resource Map

Use this file to load only the bundled resource that matches the current task.

## Scaffold a project workspace

- Use `scripts/scaffold_design_system.py`.
- Source template: `assets/design-system-template/`

## Build or audit a reference board

- Read `assets/design-system-template/utils/REFERENCE_BOARD_CHECKLIST.md`.
- Use it to verify source count, de-branding, abstraction quality, and copy risk.

## Extract a system from Figma with MCP

- Read `assets/design-system-template/utils/FIGMA_MCP_SYSTEM_PROMPT.md`.
- Use it when the input artifact is a Figma reference board rather than raw websites.

## Fill the design-system folders

Read only the layer you are actively authoring:

- Colors: `assets/design-system-template/foundations/colors/README.md`
- Typography: `assets/design-system-template/foundations/typography/README.md`
- Spacing, radius, shadow, motion: `assets/design-system-template/foundations/spacing-radius-shadow-motion/README.md`
- Semantic tokens: `assets/design-system-template/tokens/semantic/README.md`
- Components: `assets/design-system-template/components/README.md`
- Patterns: `assets/design-system-template/patterns/README.md`

## Write AI rules

- Claude guardrails template: `assets/design-system-template/prompts-rules/CLAUDE.template.md`
- Cursor rule template: `assets/design-system-template/prompts-rules/cursor-ui-design.mdc`

Use these after the design system exists. Do not write AI rules against raw references alone.

## Generate page directions from the system

- Read `assets/design-system-template/utils/UI_PROMPT_TEMPLATE.md`.
- Use it to force the AI to propose multiple original directions before refining one.

## Review a demo board before implementation

- Read `assets/design-system-template/utils/DEMO_BOARD_CHECKLIST.md`.
- Use it to judge system completeness, originality, and expandability.
