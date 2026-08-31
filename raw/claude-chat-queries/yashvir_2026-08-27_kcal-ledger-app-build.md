---
thread_name: "kcal-ledger-app-build"
user: "yashvir"
type: claude-chat
created: 2026-08-27
updated: 2026-08-31
---

## Continued — "not working" bug report and root-cause fix

**User:** "it's not working, it's not tracking"

**Assistant:** Asked diagnostic questions (what exactly happens on "Estimate with AI", was the API key saved) — answer: "Nothing happens at all" + key was saved. Investigated and found the real root cause: pages published via the Artifact tool run in a sandbox that silently blocks outbound fetch/XHR to arbitrary external hosts (confirmed via the Artifact tool's own documented CSP: "fetch/XHR/WebSocket... blocked, with no visible error" to any host outside the CDN allowlist). The direct `fetch()` to api.openai.com was never leaving the page — no API key troubleshooting could have fixed it. This was a design mistake in the v2 rebuild, not a user setup issue.

Loaded the `artifact-capabilities` skill to find the real fix: `claude.use("sample")`, the platform's first-party capability for a published page to ask Claude directly — no API key, no external network call, works inside the same sandbox that blocks arbitrary fetches. Presented the user two real options (switch to Claude via `sample`, recommended; or ship as a downloaded local HTML file to preserve literal OpenAI calls outside the sandbox, losing the persistent link). User chose: switch to Claude, keep the link.

Rebuilt `estimateFood()` to call `window.claude.use("sample")` → `sample.json(prompt, {modelTier:"quick"})` instead of fetch to OpenAI; removed all API-key state/UI (DEFAULT_STATE.apiKey, Settings API-key field, key-gating on the Estimate button, no-key banner) since none of it is needed anymore. Added a full error-code-to-copy map for the `sample` capability's documented error codes (not_granted, rate_limited, session_expired, refused, etc.) and a graceful fallback banner for when `window.claude` is absent entirely (e.g. the page saved and opened outside claude.ai).

Found and fixed a second real bug while in there: `logState.error` was being set on estimate failure but `paintInput()` never actually rendered it anywhere — so even before the sandbox issue, a failed estimate looked identical to "nothing happening," just silently reverting to the input screen. Added a proper error banner.

Tested the full flow with Playwright, mocking `window.claude.use("sample")` to simulate the real platform capability: verified success path (review screen populates, correct prompt sent), failure path (error banner now actually renders), manual-entry fallback still works, and the graceful "AI estimates only work on claude.ai" message when `window.claude` is entirely absent (simulating a saved/downloaded copy of the page). Screenshot-checked the day view for visual regressions from the edits — clean, footer now reads "Estimates from Claude."

Republished the same artifact URL with `capabilities: {sample: {}}` declared (required for the page to be granted the capability at open time), full changelog in the publish note explaining the root cause and both fixes.
