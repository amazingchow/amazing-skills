# Format Spec

Use this reference when turning a browser accessibility tree into the final text that Claude Code or Codex will consume.

## Canonical Wrapper

```md
You are given a browser page semantic snapshot extracted from the accessibility tree, not a screenshot.
Use element refs exactly as written when proposing clicks, fills, assertions, or navigation.

Task
[insert the user's task, or omit this section if none was given]

<browser-page-semantic-snapshot>
source_url: https://example.com
final_url: https://example.com/dashboard
page_title: Acme Dashboard
auth_state: authenticated
captured_at: 2026-04-02T08:15:00Z
notes:
- cookie banner already dismissed
- left nav collapsed by default
snapshot:
- document "Acme Dashboard"
  - banner
    - link "Acme" [ref=s1]
    - button "Open user menu" [ref=s2]
  - main
    - heading "Revenue overview" [level=1]
    - button "Create report" [ref=s3]
</browser-page-semantic-snapshot>
```

## Field Rules

- `source_url`: the original URL supplied by the user.
- `final_url`: the final navigated URL after redirects. If unknown, repeat `source_url`.
- `page_title`: the current document title when known. Use `unknown` if unavailable.
- `auth_state`: one of `public`, `authenticated`, `login_required`, or `unknown`.
- `captured_at`: ISO 8601 timestamp in UTC when the snapshot or access check happened.
- `notes`: concise operational context. Use `notes: none` when there is nothing worth calling out.
- `snapshot`: the semantic tree itself.

## Normalization Rules

- Preserve indentation and parent-child structure.
- Preserve ref ids exactly as captured.
- Keep role, accessible name, state, level, checked status, expanded state, and input value when available.
- Keep actionable elements even if they look visually repetitive.
- Drop raw styling chatter, CSS classes, layout coordinates, and image pixel details.
- If you omit repeated low-value items, say so in `notes` with a short count and rationale.

## Delivery Rules

- Explain that the snapshot came from the accessibility tree rather than a screenshot.
- When asking another agent to interact with the page, cite `[ref=...]` directly.
- Do not invent refs, states, or page structure that are not present in the captured tree.
- Do not claim a private page was captured if authentication blocked access.
