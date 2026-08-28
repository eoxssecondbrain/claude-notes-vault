---
thread_name: "gmail-promo-otp-labeling-2026-08-28"
user: "danish"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: Using the connected Gmail account, categorize today's promotional/marketing emails and one-time-use OTP/verification-code emails in the inbox by applying labels only — do not archive, trash, delete, or otherwise move any email out of the inbox.

Steps:
1. Call list_labels to see existing labels. If a label named "Promotional" does not exist, create it with create_label. If a label named "OTP" does not exist, create it with create_label. Note their label IDs.
2. Search for promotional/marketing mail from the last 24 hours: search_threads with query `in:inbox category:promotions newer_than:1d`. For every thread returned, apply the "Promotional" label with label_thread (skip any thread that already has it).
3. Search for OTP/verification-code mail from the last 24 hours: search_threads with query `in:inbox newer_than:1d subject:(OTP OR "one time password" OR "one-time password" OR "verification code" OR "security code" OR "login code" OR "sign-in code" OR passcode)`. For every thread returned, apply the "OTP" label with label_thread (skip any thread that already has it).
4. Do not touch any email that doesn't match one of these two searches. Do not unsubscribe, reply, forward, or send anything.
5. End with a one-line summary: how many threads were labeled "Promotional" and how many were labeled "OTP". Keep it to that one line — no other report is needed.

Assistant: Called list_labels — found existing labels "Promotional" (Label_13) and "OTP" (Label_14) already present, no creation needed.

Searched `in:inbox category:promotions newer_than:1d` — 24 threads returned:
1a04861bb517e462, 1a048469baa6f2a2, 1a0483ef9e1b368d, 1a047de464792b40, 1a047cbe35fa4e14, 1a047b0ed1ff1e9f, 1a0479de3b8d46ee, 1a047611f498f39f, 1a0475553f66c63c, 1a0473612e79d426, 1a04706ae4e4a920, 1a046fe494dffece, 1a046fd81f8ce059, 1a046d2f3c71c9f0, 1a046d2861a3df5b, 1a046c925598726f, 1a046a6413f339db, 1a0468b899ffcf0f, 1a0465e3a6243860, 1a04641a20fa73f0, 1a045218ed86cfad, 1a044c2e1dbb40a1, 1a0448ba7d3e7ab8, 1a044736f6ffe2f2

Applied label_thread with Label_13 ("Promotional") to all 24 threads. Two calls (1a048469baa6f2a2, 1a047de464792b40) failed transiently with "service unavailable" and were retried successfully. All 24 confirmed labeled.

Searched `in:inbox newer_than:1d subject:(OTP OR "one time password" OR "one-time password" OR "verification code" OR "security code" OR "login code" OR "sign-in code" OR passcode)` — 0 threads returned. No OTP labels applied.

No emails were archived, trashed, deleted, or moved out of the inbox. No unsubscribe/reply/forward/send actions taken.

Final summary: 24 threads labeled "Promotional", 0 threads labeled "OTP".
