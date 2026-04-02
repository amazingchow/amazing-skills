# Originality And Quality Bar

Use this reference when reviewing an existing design system, generated page concept, or implemented UI.

## Pass Criteria

The work is strong when most of these are true:

1. The system stands on its own.
   - Another agent can generate a page from the system and rules without seeing the original websites.
2. The page preserves mood without preserving composition.
   - The result feels related to the references, but not reconstructive.
3. The same system can support at least 3 pages.
   - Tokens, components, and patterns are reusable beyond one screen.
4. The rules are explicit.
   - Constraints are written as operational guardrails, not emotional feedback like "make it less ugly."
5. The visual quality comes from structure first.
   - Typography, spacing, layout, and hierarchy carry the experience before gradients, motion, or decorative effects.

## Failure Patterns

Flag these quickly:

- Single-source dependence: one reference clearly dominates structure and mood.
- Section cloning: the new page follows the source order or section composition too closely.
- Token theater: a token file exists, but the actual UI still uses arbitrary colors, sizes, and local overrides.
- Component drift: cards, tags, buttons, and inputs do not look like they belong to one family.
- Pattern collapse: every section turns into centered copy or a card grid.
- Decoration-first aesthetics: gradients, glassmorphism, glows, or imagery do most of the work because the structure is weak.
- Accent sprawl: multiple bright accents compete for priority on the same page.

## Originality Checks

Ask these questions:

1. If images and colors were removed, would the layout still feel distinct from the references?
2. Did the page change at least 3 of these: grid, proportions, whitespace rhythm, corner treatment, border strategy, shadow strategy?
3. Did the team avoid reusing source-brand copy, illustration logic, icon language, or hero composition?
4. Can you explain what was intentionally preserved versus intentionally discarded?

If any answer is "no", the page is still too derivative.

## Aesthetic Checks

Ask these questions:

1. Is there one dominant accent instead of many competing accents?
2. Does the page establish hierarchy through typography and spacing before decoration?
3. Do section transitions feel intentional rather than repetitive?
4. Do components share a recognizable family resemblance?
5. Is the hero or first screen visually tense enough without falling back to stock landing-page tropes?

## Repair Guidance

When the review fails, fix in this order:

1. Foundations
2. Semantic tokens
3. Component families
4. Section patterns
5. Page styling

Do not start with micro-polish if the failure is structural.
