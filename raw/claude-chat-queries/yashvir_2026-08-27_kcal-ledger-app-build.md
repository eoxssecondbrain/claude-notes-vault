---
thread_name: "kcal-ledger-app-build"
user: "yashvir"
type: claude-chat
created: 2026-08-27
updated: 2026-08-31
---

## Continued — zero-calorie bug fix, then "still same," then diagnostics build

**User:** [screenshot: logged "Aalo parantha" item with 0 kcal / 0g all macros, saved successfully]. "are you sure you've fixed the root cause?"

**Assistant:** Correctly identified this as a NEW, separate bug from the sandbox/CORS one: the item name parsed fine but numeric fields all defaulted to 0. Root cause: `estimateFood()`'s item-mapping only accepted one exact key name per field (kcal/protein_g/carbs_g/fat_g); anything Claude phrased differently (e.g. "calories" instead of "kcal", or a string like "320 kcal") silently became 0 via `Number(undefined)||0`. Fixed: added multi-key-name fallback (`pickNum` trying several likely variants) plus numeric extraction from strings via regex; strengthened the prompt with a concrete worked JSON example. Also added a genuine safety net since LLM output format can never be 100% guaranteed: any item still at 0 kcal after parsing is now flagged in the review screen with a red border + "came back as 0 — enter this by hand" note (clears live once fixed), plus a banner at the top — so this exact failure mode (silently saving zeros) can't happen unnoticed again regardless of cause. Tested against alternate key names, a genuine all-zero response, and totally garbage/unparseable values via Playwright + a mocked window.claude.sample — all handled correctly, screenshotted the warning UI. Republished (v4).

**User:** "still same."

**Assistant:** Asked a clarifying question (what specifically is still wrong, had they reloaded) rather than guess a third time.

**User:** Did not answer the multiple-choice directly — instead: "i give you 2 hours do the testing repeatedly and finish the product" (a directive to stop asking and just get it working autonomously).

**Assistant:** Recognized the real constraint: this session cannot access the user's actual claude.ai runtime/browser to observe what's actually failing, so further guessing wastes the user's time. Re-read the artifact-capabilities `claude.d.ts` contract closely and found a documented, non-obvious platform behavior: when a published page is opened as its own standalone top-level tab (vs. embedded inside the claude.ai app/conversation as "a viewer"), `claude.use(...)` currently resolves `null` for every capability — a platform-level limitation, not something fixable in the page's code. This is a strong candidate for what the user is actually hitting if they're opening the app via a saved/bookmarked link rather than staying inside the conversation.

Rather than guess a specific fix, built real diagnostics into the app: (1) a background self-check on load (`runAiDiagnostics`) using `window.top !== window.self` to detect standalone-vs-framed, plus whether `window.claude` exists and whether `claude.use("sample")` resolves non-null — all free, no consent prompt; (2) a proactive, specific warning banner in the Log Food sheet if any check fails, naming the actual reason (not connected to Claude at all / opened as a standalone tab / unavailable in this view) rather than waiting for a failed attempt; (3) a new "AI estimates" section in Settings with a live status line and a "Test AI connection" button that fires one real `sample()` call and reports the exact outcome — success with real numbers, or the precise failure reason; (4) every AI error now appends its raw error code in parentheses for precise diagnosis instead of only friendly copy.

Verified via Playwright across three scenarios (no window.claude at all / framed-in-an-iframe-but-disconnected / top-level-tab-with-working-mock) that each shows the correct specific message and, critically, that the diagnostic banners are advisory only — they never block a legitimately-working path (confirmed the mocked estimate still completes successfully even when the standalone-tab warning is showing). Re-ran the full prior regression suite (settings, AI log, manual log, week/month views, delete/undo) to confirm nothing broke. Republished (v5) and asked the user to run Settings → "Test AI connection" and report the exact result, since that now gives a definitive answer instead of another guess.
