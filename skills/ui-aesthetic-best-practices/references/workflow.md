# Workflow

Use this reference when the task needs the full end-to-end sequence instead of just a single template.

## Entry Modes

### 1. Start from websites

Use this path when the user says "参考这个网站做一个更有审美的 UI" or provides a handful of URLs.

1. Gather 3-5 references, not 1.
2. Assign each source one main job.
   - typography rhythm
   - color mood
   - card hierarchy
   - whitespace density
   - illustration direction
3. Build a Figma reference board.
4. Remove source-branding artifacts before extracting rules.
5. Extract the system before drafting any production page.

### 2. Start from a Figma reference board

Use this path when the board already exists and the user wants Codex to help direct AI or Figma MCP.

1. Read `assets/design-system-template/utils/FIGMA_MCP_SYSTEM_PROMPT.md`.
2. Ask the AI or MCP workflow to summarize each source separately before merging the style language.
3. Force the output into these buckets:
   - `foundations/colors`
   - `foundations/typography`
   - `foundations/spacing-radius-shadow-motion`
   - `tokens/semantic`
   - `components`
   - `patterns`
   - `prompts-rules`
4. Reject any output that maps one source page section-by-section.

### 3. Start from an existing UI that feels weak

Use this path when the user already has a page or app, but it feels generic, copied, or inconsistent.

1. Audit the current UI against the originality and quality bar.
2. Identify which layer is actually broken:
   - `foundations`: color, type, spacing, radius, shadow, motion
   - `tokens/semantic`: missing semantics or hard-coded values
   - `components`: weak family resemblance or one-off variants
   - `patterns`: repetitive section structure or no composition logic
3. Repair the lowest broken layer first.
4. Only polish visuals after the system is coherent again.

## Recommended Sequence

### Phase A. Build the reference board

Target outcome:
- multiple sources
- clear source responsibilities
- de-branded visual samples

Stop and repair if:
- one source dominates the whole board
- the board still looks like a direct brand collage
- you cannot explain what to keep versus discard

### Phase B. Write the design system

Target outcome:
- clear `foundations/`
- semantic token map
- reusable component families
- reusable section patterns

Author the layers in this order:
1. foundations
2. semantic tokens
3. components
4. patterns

Why this order matters:
- foundations define the visual grammar
- tokens stabilize usage
- components reuse the stabilized tokens
- patterns stop the page from collapsing into repeated component piles

### Phase C. Write AI guardrails

Target outcome:
- a project-specific `CLAUDE.md` or Cursor rule
- explicit originality boundaries
- token and component reuse policy

The rules should answer:
- What mood should be preserved?
- What must never be copied?
- Which system layers must be used first?
- What output proof must the AI provide?

### Phase D. Produce a demo board

Target outcome:
- token palette
- type combinations
- 6-10 key components
- 2-3 section patterns
- 1 sample page

Do not skip this phase when the user wants strong aesthetics. It is the fastest way to catch derivative or over-styled decisions before implementation.

### Phase E. Produce business UI

Target outcome:
- 2-3 viable page directions
- one selected direction refined for production

Require every direction to explain:
- tokens used
- components reused
- patterns used
- at least 3 deliberate changes from the references

## Repair Loop

When a generated page still feels off, use this order:

1. Check whether the system is incomplete.
2. Check whether the page is ignoring the system.
3. Check whether the patterns are too generic.
4. Check whether aesthetics depend on decoration instead of structure.

If the answer is "yes" to any earlier step, repair that step instead of adding more styling noise.
