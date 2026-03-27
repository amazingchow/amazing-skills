# Handoff Quality Bar

## Table of Contents

- What good handoffs preserve
- Section guidance
- Anti-patterns
- Final review checklist

## What Good Handoffs Preserve

A strong handoff lets the next agent continue without replaying the entire session. Preserve:

- The exact task goal and what "done" means.
- What has already been tried, changed, or verified.
- Decisions that were made and why they were made.
- The concrete artifacts involved: files, commands, logs, branches, tickets, URLs, outputs.
- The next highest-value action and what should be validated first.

## Section Guidance

### 1. 当前任务目标

- State the user-facing problem.
- State the expected output.
- State the finish line in operational terms.

### 2. 当前进展

- Capture completed analysis, code edits, experiments, and validation.
- Mention concrete file paths and commands where possible.
- Distinguish finished work from partial attempts.

### 3. 关键上下文

- Preserve requirements, constraints, user preferences, and assumptions.
- Record non-obvious environment facts that matter for continuation.
- Include decisions that would otherwise be rediscovered.

### 4. 关键发现

- Highlight the small number of facts that most changed the direction of work.
- Prefer root causes, design decisions, or validated eliminations over raw observations.

### 5. 未完成事项

- Sort by priority, not by chronology.
- Make each item actionable enough that the next agent can pick one up directly.

### 6. 建议接手路径

- Point to the first files, commands, logs, or pages worth opening.
- Tell the next agent what to verify before making more changes.
- Recommend the immediate next move, not a long project plan.

### 7. 风险与注意事项

- Call out brittle areas, misleading clues, duplicated-work traps, and rejected approaches.
- Mention anything that could cause an accidental overwrite, regression, or wasted investigation.

### 下一位 Agent 的第一步建议

- End with a single concrete action.
- Good example: "Open `/abs/path/service.py`, compare it to `/abs/path/test_service.py`, then rerun `pytest tests/test_service.py -k retry`."

## Anti-Patterns

- Do not write generic summaries like "worked on debugging."
- Do not omit artifact names when they are available.
- Do not bury the next action in a long retrospective.
- Do not pretend assumptions are confirmed facts.
- Do not restate every step chronologically if only three decisions matter.

## Final Review Checklist

- Can the next agent name the goal, current status, and finish line after one read?
- Can the next agent identify the exact files or commands to inspect first?
- Are the most important decisions and discoveries explicit?
- Are open questions clearly labeled as unknowns?
- Would reading the original chat still feel optional instead of required?
