---
thread_name: "gmail-promo-otp-labeling"
user: "danish"
type: claude-chat
created: 2026-08-27
updated: 2026-09-03
---

**User (scheduled task prompt, 2026-09-03):**

Using the connected Gmail account, categorize today's promotional/marketing emails and one-time-use OTP/verification-code emails in the inbox by applying labels only — do not archive, trash, delete, or otherwise move any email out of the inbox.

Steps:
1. Call list_labels to see existing labels. If a label named "Promotional" does not exist, create it with create_label. If a label named "OTP" does not exist, create it with create_label. Note their label IDs.
2. Search for promotional/marketing mail from the last 24 hours: search_threads with query `in:inbox category:promotions newer_than:1d`. For every thread returned, apply the "Promotional" label with label_thread (skip any thread that already has it).
3. Search for OTP/verification-code mail from the last 24 hours: search_threads with query `in:inbox newer_than:1d subject:(OTP OR "one time password" OR "one-time password" OR "verification code" OR "security code" OR "login code" OR "sign-in code" OR passcode)`. For every thread returned, apply the "OTP" label with label_thread (skip any thread that already has it).
4. Do not touch any email that doesn't match one of these two searches. Do not unsubscribe, reply, forward, or send anything.
5. End with a one-line summary: how many threads were labeled "Promotional" and how many were labeled "OTP". Keep it to that one line — no other report is needed.

**Assistant:**

Checked labels via list_labels — "Promotional" (Label_13) and "OTP" (Label_14) already existed, so no create_label calls were needed.

Ran search_threads with `in:inbox category:promotions newer_than:1d` — 1 thread returned: threadId 1a067cc9e101217f, subject "Make your keyboard play your sounds" from hello@keychron.com. Applied label_thread with labelIds ["Label_13"] (Promotional).

Ran search_threads with `in:inbox newer_than:1d subject:(OTP OR "one time password" OR "one-time password" OR "verification code" OR "security code" OR "login code" OR "sign-in code" OR passcode)` — 0 threads returned. No OTP labels applied.

No emails were archived, trashed, deleted, moved, unsubscribed, replied to, or forwarded.

Summary: 1 thread labeled "Promotional", 0 threads labeled "OTP".
