---
thread_name: "gmail-spam-detection-run-2026-09-04"
user: "raj"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# Scheduled Email Spam Detection (v9) — Run 2026-09-04

**Trigger:** automated scheduled task, no live user present.

**Setup:** Listed labels. Confirmed AI-Reviewed (Label_37, 53,722 msgs / 29,460 threads) and AI-SPAM (Label_33, 7 msgs / 6 threads) already exist and have prior history → this is a NORMAL RUN, not first run.

**Fix-up pass:** `label:Label_33 in:inbox` returned 0 threads. Nothing needed fixing.

**Normal run:** Query `-in:sent -in:chats -label:Label_33 -label:Label_37`, pageSize 50, paginated across 6 pages (300 threads total, spanning message dates from 2026-09-03 back to 2026-07-27).

Classification: every single one of the 300 threads had an eoxs.com/eoxsteam.com address as sender, recipient, or cc (expected, since this is the mailbox owner's own account) → all hit skip-list rule 1 ("any eoxs address in To/Cc") → classified NOT_SPAM → labeled AI-Reviewed (Label_37) via label_thread. Two label_thread calls transiently errored (Precondition check failed / service unavailable) and were retried successfully.

Zero threads were classified as SPAM/SUSPICIOUS in this run. No mark_thread_spam calls were made.

**Anomaly found, stopped and flagged rather than continuing indefinitely:** after 300 threads (6 pages), the search still had a `nextPageToken` and kept surfacing older and older threads (into late July 2026), while Gmail's `resultCountEstimate` stayed frozen at "201" throughout — clearly a stale/capped estimate, not the real remaining count. This means the "normal run" unprocessed backlog is much larger than expected for a routine incremental run. Two possible causes: (1) this task has a real backlog of old threads that were never labeled and needs several more runs (or a larger page budget) to catch up, or (2) something is causing already-reviewed old threads to keep re-matching the "-label:Label_37" exclusion (e.g. very long threads where a message beyond the 5-oldest preview window lacks the label). Did not attempt to process the full backlog in this single run — stopped at 300 threads to avoid an unbounded number of tool calls in one unattended session.

**Secondary observation worth flagging to Raj:** skip-list rule 1 ("any eoxs address in To/Cc") fires for essentially all mail in this mailbox, since Raj's own eoxs.com address is the recipient of nearly everything. In 300 consecutive threads sampled (including cold outreach, job applicants, conference marketing, external vendor mail), 100% hit this skip rule and zero reached the SPAM classification buckets. Historical totals confirm this: AI-Reviewed has 53,722 messages ever vs AI-SPAM only 7. Practical implication: this filter essentially cannot catch spam/advertising/investor-outreach that is sent directly to an eoxs.com/eoxsteam.com address — it only catches mail with zero eoxs addresses anywhere in the header, which is likely a small minority of what a real inbox would call spam. Flagged to Raj via push notification for a decision on whether the skip-list rule is intended to be this broad.

**Final report (per task step 10):**
- Checked: 300
- SPAM/SUSPICIOUS: 0 | NOT_SPAM: 300
- Moves by sub-label: none
- Fixed by fix-up pass: 0
- Moves confirmed by verification: N/A (no moves)
- MOVE_FAILED: none
- Backlog remaining: unknown, larger than one run's page budget — recommend follow-up run(s) or review of the exclusion-filter/backlog issue above.
