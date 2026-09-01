---
thread_name: "scheduled-email-spam-detection"
user: "raj"
type: claude-chat
created: 2026-08-31
updated: 2026-09-01
---

# Scheduled Email Spam Detection — 2026-09-01

**Trigger:** Scheduled task (v9 protocol), automated, no live user present.

**User prompt (scheduled, stored):** Run the Scheduled Email Spam Detection (v9) protocol — fix-up pass on label:AI-SPAM in:inbox, then a normal run classifying unlabeled mail into SPAM (with sub-labels) or NOT_SPAM per the skip-list/spam rules, and report counts.

**Assistant actions and findings:**

1. Called `list_labels` — confirmed AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-SPAM/Investor-Outreach, and AI-Reviewed all already exist (Label_33/34/35/36/38/37). Not a first run.

2. Fix-up pass: `search_threads` with `label:Label_33 in:inbox` — 0 results. No threads needed re-moving to Spam.

3. Normal run: attempted `search_threads` with query `-in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed` (the exact query specified by the protocol). This combined two-custom-label negation returned an empty `threads` array despite a non-zero `resultCountEstimate` that was unstable across identical repeated calls (1293, then 877, then 1139) — identified as a tool-level bug, not a real signal of zero results.

4. Worked around it: pulled the full `-label:AI-SPAM` pool alone (single-label negation works reliably, confirmed by cross-checking that AI-SPAM-labeled threads are correctly excluded). Paginated all 5 pages (~250 thread listings; `resultCountEstimate` held at 201 throughout). For every thread returned, inspected each message's `labelIds` for the presence of Label_37 (AI-Reviewed). Result: every single message in every thread already carried Label_37.

5. Conclusion: zero threads in the mailbox currently lack both AI-SPAM and AI-Reviewed — nothing new to classify this run. Mailbox is fully caught up.

**Final report:**
- Checked: 0 net-new emails requiring classification
- SPAM/SUSPICIOUS: 0 (Fraud: 0, Expired-OTP: 0, Advertising: 0, Investor-Outreach: 0)
- NOT_SPAM: 0
- Fix-up pass: 0 threads fixed
- Moves confirmed by verification: 0 (n/a — no moves made)
- MOVE_FAILED: none

**Flagged to Raj (push notification sent):** The Gmail search tool's combined two-custom-label negation query (`-label:X -label:Y`) is unreliable — it returns 0 actual threads paired with a bogus non-zero estimate that changes on repeat identical calls. This is exactly the query the v9 protocol specifies for every normal run, so if a future run trusts it without the manual cross-check performed here, it could silently under-report a real spam/review backlog as "nothing to do." No spam was actually missed this run — verified manually — but the underlying query mechanism needs attention.
