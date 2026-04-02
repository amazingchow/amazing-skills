---
name: browser-semantic-snapshot
description: Extract a webpage into a browser semantic snapshot derived from the accessibility tree instead of screenshots, then normalize it into a Claude Code or Codex-ready text format. Use when a user gives a URL and wants page structure, actionable elements, or browser state captured as compact text with stable refs; when Codex needs to reason about a page semantically; or when a page may require authentication and Codex must detect that a manual login is required before capture. Also use for requests like "给这个网页做语义快照", "把页面整理成 Claude/Codex 可用格式", or "先判断是否需要登录再抓页面结构".
---

# Browser Semantic Snapshot

Use this skill to capture what matters for machines: roles, names, states, values, and refs from the page accessibility tree. Prefer semantic structure over screenshots, because the goal is reliable reasoning and precise browser actions.

## Workflow

1. Open the user-provided URL in a browser context that can expose a semantic snapshot.
   - Prefer browser tools that expose the accessibility tree or a semantic/ARIA snapshot.
   - Wait for the meaningful page state, not just the first paint.
2. Decide whether the page is accessible or blocked by authentication.
   - Treat redirects to sign-in pages, auth walls, blank private shells, consent flows that block content, SSO interstitials, CAPTCHA, or missing private content as `login_required`.
   - If a useful page snapshot cannot be captured without login, stop and tell the user they must log in manually in that browser session before extraction.
   - If the conversation is in Chinese, deliver the same reminder in Chinese.
3. Capture the semantic snapshot instead of a screenshot.
   - Keep hierarchy, role, accessible name, state, value, and stable ref ids.
   - Do not replace a semantic snapshot with visual guesses.
   - Ignore CSS, spacing, and image styling unless the user explicitly asks for a visual audit.
4. Normalize the result into the canonical wrapper.
   - Include `source_url`, `final_url`, `page_title`, `auth_state`, `captured_at`, `notes`, and the raw snapshot body.
   - Preserve ref ids exactly as captured so downstream agents can reference them safely.
   - Trim repetitive noise only when it is clearly irrelevant; never delete actionable refs without noting the omission.
5. Deliver a Claude Code / Codex-ready block.
   - State that the content came from the accessibility tree, not a screenshot.
   - If the user also wants analysis or next actions, include the task above the snapshot and cite `[ref=...]` for any proposed interaction.
   - Use `scripts/render_semantic_snapshot_prompt.py` when a raw snapshot file already exists.

## Login Handling

- Use `login_required` when private content is unavailable, not only when a page literally says "Sign in".
- Never ask the user to paste credentials into chat.
- Ask the user to complete SSO, 2FA, CAPTCHA, or consent gates manually in the same browser session that will be used for extraction.
- After manual login, continue capture from that authenticated browser state instead of reopening a fresh session.

Read [references/auth-playbook.md](references/auth-playbook.md) when you need detailed heuristics or the exact reminder wording.

## Commands

Wrap an existing raw semantic snapshot into a Claude/Codex-ready prompt:

```bash
python3 scripts/render_semantic_snapshot_prompt.py \
  --url https://example.com/dashboard \
  --final-url https://example.com/dashboard \
  --page-title "Acme Dashboard" \
  --auth-state authenticated \
  --snapshot-file /absolute/path/to/raw-snapshot.txt \
  --task "Summarize the page and identify the primary call to action." \
  --output /absolute/path/to/browser-semantic-snapshot.md
```

Render the login-required reminder instead of a snapshot:

```bash
python3 scripts/render_semantic_snapshot_prompt.py \
  --url https://example.com/app \
  --auth-state login_required \
  --note "Redirected to the SSO sign-in page before app content loaded." \
  --output /absolute/path/to/browser-semantic-snapshot.md
```

## Resources

- Use `scripts/render_semantic_snapshot_prompt.py` to package raw snapshot text into the standard prompt wrapper or a login-required reminder.
- Read [references/format-spec.md](references/format-spec.md) for the canonical output format, field meanings, and normalization rules.
- Read [references/auth-playbook.md](references/auth-playbook.md) for authentication detection heuristics and how to ask the user to log in manually.
- Reuse [assets/templates/claude-codex-semantic-snapshot.md](assets/templates/claude-codex-semantic-snapshot.md) and [assets/templates/login-required-message.md](assets/templates/login-required-message.md) when drafting output by hand.
