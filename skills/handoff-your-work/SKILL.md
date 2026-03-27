---
name: handoff-your-work
description: Write a concrete AI-to-AI handoff brief when the current context is long, the user wants to continue in a fresh session, or Codex must summarize ongoing work for another agent. Use for requests such as "写交接文档", "交接给下一个 Agent", "resume this in a new chat", or "在 ./{yymmdd}-handoff.md 输出接手摘要". Preserve task goals, completed work, key decisions, file paths, commands, pending work, and next-step guidance.
---

# Handoff Your Work

Use this skill to leave the next agent with enough operational context to continue immediately instead of re-discovering the problem.

## Workflow

1. Confirm the output path.
   - If the user specifies `./{yymmdd}-handoff.md`, keep that pattern and expand it with `scripts/render_handoff_template.py`.
   - Otherwise write to the exact file path the user requested.
2. Reconstruct the working state before writing.
   - Inspect the active request, touched files, repo status, important commands, logs, failed attempts, and any partial outputs.
   - Prefer concrete evidence over narrative memory.
3. Create the scaffold before drafting.
   - Run `python3 scripts/render_handoff_template.py --output /absolute/path/to/{yymmdd}-handoff.md`.
   - Add `--force` only when you intentionally want to overwrite an existing draft.
4. Fill each section with transfer-ready detail.
   - `当前任务目标`: current problem, expected deliverable, and definition of done.
   - `当前进展`: work already completed, including analysis, code changes, experiments, and validations.
   - `关键上下文`: requirements, constraints, user preferences, assumptions, and decisions that should not be rediscovered.
   - `关键发现`: highest-signal conclusions, root-cause judgments, design calls, or anomalies.
   - `未完成事项`: remaining work, prioritized.
   - `建议接手路径`: exact files, commands, logs, pages, and the next verification target.
   - `风险与注意事项`: likely misreads, sensitive areas, dead ends, and duplicated-work traps.
   - `下一位 Agent 的第一步建议`: one concrete first move that gets momentum immediately.
5. Optimize for continuation, not storytelling.
   - Make the next action obvious.
   - State unknowns explicitly instead of guessing.
   - Name artifacts exactly as they exist on disk.
6. Perform a final quality pass.
   - Remove vague phrases such as "did some debugging" or "updated several files."
   - Ensure the next agent can answer "what changed, why, what is left, and where do I start?" without reading the old chat.

## Output Rules

- Write for another agent, not for the end user.
- Keep the user-provided heading structure exactly when one is given.
- Prefer compact, high-signal prose over retrospectives or process diaries.
- Include file paths, commands, branch names, errors, tickets, and artifacts when they matter.
- If no code was changed, say so plainly and focus on analysis, decisions, and next actions.
- If a fact is uncertain, label it as an assumption or an unverified lead.

## Commands

Scaffold the default filename for today:

```bash
python3 scripts/render_handoff_template.py --output "/absolute/path/to/workspace/{yymmdd}-handoff.md"
```

Overwrite an existing draft intentionally:

```bash
python3 scripts/render_handoff_template.py \
  --output "/absolute/path/to/workspace/260327-handoff.md" \
  --force
```

## Resources

- Use `scripts/render_handoff_template.py` to expand `{yymmdd}` and generate the required markdown scaffold deterministically.
- Read [references/handoff-quality-bar.md](references/handoff-quality-bar.md) when you need section-by-section guidance, anti-patterns, or a final review checklist.
