# Auth Playbook

Use this reference when deciding whether a page is ready for semantic capture or requires manual login first.

## Mark As `login_required` When

- The page redirects to a sign-in, SSO, or identity-provider flow before useful content appears.
- The browser shows a private-app shell with no meaningful content until the user logs in.
- A CAPTCHA, MFA, passkey, or device approval gate blocks access.
- The expected application content is missing and the page instead shows auth prompts, access denied, or session expired messaging.
- A cookie or consent screen blocks content and cannot be completed safely by the agent.

## Manual Login Reminder

Use this wording, translated to the current conversation language when appropriate:

```text
This page needs authenticated browser access before I can capture a useful semantic snapshot. Please log in manually in the browser session that will be used for extraction, then tell me to continue.
```

Add a second sentence when relevant:

```text
If the page requires SSO, 2FA, CAPTCHA, or consent, please complete that flow manually in the same session as well.
```

## Guardrails

- Never ask the user to share credentials in chat.
- Never fabricate a private-page snapshot from search results, page source snippets, or screenshots.
- Do not reopen a fresh browser session after the user logs in unless they explicitly ask for it.
- If the authenticated content loads partially, note the limitation in `notes` and capture what is truly visible.

## After Login

1. Return to the intended page in the same authenticated browser session.
2. Wait for the private content to settle.
3. Capture the semantic snapshot.
4. Set `auth_state` to `authenticated`.
