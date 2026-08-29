---
thread_name: "scheduled-email-spam-detection-runs"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

# Scheduled Email Spam Detection Run — 2026-08-29

This is an automated scheduled-task run (not an interactive chat with Raj), following the "Scheduled Email Spam Detection (v3)" prompt.

## Actions taken
- Step 0 repair pass: searched `label:AI-SPAM -in:spam` (incl. trash) — 0 orphaned threads found.
- Labels already existed (AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-Reviewed) — not a first run (AI-Reviewed had 10,845 threads already).
- Normal run query: `in:inbox -label:AI-SPAM -label:AI-Reviewed`, paginated across ~10 pages (~500 threads surveyed, all dated 2022 — a large historical backlog that predates consistent AI-Reviewed coverage).
- Applied the skip rule (any eoxs.com/eoxsteam.com address in sender/To/Cc → auto NOT_SPAM) to classify most surveyed threads.
- Fully processed and labeled 207 threads this run:
  - 204 labeled AI-Reviewed (NOT_SPAM — legitimate business correspondence, internal EOXS/3GM Steel implementation threads, newsletters, calendar/vendor mail, etc.)
  - 3 labeled AI-SPAM + AI-SPAM/Advertising and moved to Spam via mark_thread_spam:
    - `1808a927805bbb45` — "Dedicated Recruiter at a reasonable cost." (pamelaharrisr@yahoo.com, self-addressed bulk spam)
    - `1808a813d8271679` — duplicate of the same spam (theresadanielsr@yahoo.com)
    - `1825f9562b5c4a66` — bcc-blast spam, gibberish subject "sdytw", fake banquet invite (mikejordan9928@gmail.com)
- Verified via list_labels: AI-Reviewed threadsTotal 10,845 → 11,049 (+204); SPAM folder threadsTotal 1,459 → 1,462 (+3); INBOX threadsTotal 20,478 → 20,475 (-3). Counts reconcile.

## Notable finding
The backlog of unreviewed inbox threads is far larger than a typical "gap after downtime" — surveyed ~500 threads (all pre-2023) without exhausting the query; `resultCountEstimate` stayed pegged at "201" throughout (appears stale/inaccurate for this large a result set). Many hundreds/thousands of old inbox threads likely remain unlabeled and will surface again on future scheduled runs. Recommend either running this scheduled task more frequently for a while, or accepting it will take several runs to fully clear the historical backlog.

## Notification sent
Pushed a proactive notification to the user summarizing: 207 threads cleared, 3 spam moved, and the unexpectedly large backlog finding.
