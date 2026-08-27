---
thread_name: "gmail-promo-otp-labeling"
user: "danish"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

User: Using the connected Gmail account, categorize today's promotional/marketing emails and one-time-use OTP/verification-code emails in the inbox by applying labels only — do not archive, trash, delete, or otherwise move any email out of the inbox.

Steps:
1. Call list_labels to see existing labels. If a label named "Promotional" does not exist, create it with create_label. If a label named "OTP" does not exist, create it with create_label. Note their label IDs.
2. Search for promotional/marketing mail from the last 24 hours: search_threads with query `in:inbox category:promotions newer_than:1d`. For every thread returned, apply the "Promotional" label with label_thread (skip any thread that already has it).
3. Search for OTP/verification-code mail from the last 24 hours: search_threads with query `in:inbox newer_than:1d subject:(OTP OR "one time password" OR "one-time password" OR "verification code" OR "security code" OR "login code" OR "sign-in code" OR passcode)`. For every thread returned, apply the "OTP" label with label_thread (skip any thread that already has it).
4. Do not touch any email that doesn't match one of these two searches. Do not unsubscribe, reply, forward, or send anything.
5. End with a one-line summary: how many threads were labeled "Promotional" and how many were labeled "OTP". Keep it to that one line — no other report is needed.

Assistant: Called list_labels — no "Promotional" or "OTP" label existed. Created both via create_label (Promotional = Label_13, OTP = Label_14).

Searched `in:inbox category:promotions newer_than:1d` — 16 threads returned, none already labeled Promotional:
1a04349a31f9f700, 1a0434872821bd40, 1a043415d1491cd1, 1a04338dd7022b45, 1a0431947290f9c3, 1a0429da654e6b38, 1a0421d1491aaa0e, 1a041db9c9c56ac0, 1a0419477ed3259d, 1a0418583b730437, 1a0413832ce9a56c, 1a0409320e02c707, 1a03ee1463ed1a42, 1a03ea5bde782630, 1a03e9718d0fbcd5, 1a03e9342f91536a.

Applied label_thread with labelIds ["Label_13"] to all 16 threads — all succeeded.

Searched `in:inbox newer_than:1d subject:(OTP OR "one time password" OR "one-time password" OR "verification code" OR "security code" OR "login code" OR "sign-in code" OR passcode)` — 0 threads returned.

No emails were archived, trashed, deleted, or moved out of the inbox. No unsubscribe/reply/forward/send actions taken.

Summary: 16 threads labeled "Promotional", 0 threads labeled "OTP".
