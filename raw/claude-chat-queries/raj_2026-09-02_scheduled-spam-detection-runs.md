---
thread_name: "scheduled-spam-detection-runs"
user: "raj"
type: claude-chat
created: 2026-09-02
updated: 2026-09-04
---

## Scheduled Email Spam Detection (v9) — run on 2026-09-04

**Trigger:** automated scheduled task, no live user present.

**Labels confirmed via list_labels:** AI-SPAM (Label_33), AI-SPAM/Advertising (Label_34), AI-SPAM/Expired-OTP (Label_35), AI-SPAM/Fraud (Label_36), AI-SPAM/Investor-Outreach (Label_38), AI-Reviewed (Label_37) — all pre-existing, so this is a normal run (not first run).

**Fix-up pass:** searched `label:AI-SPAM in:inbox` → 0 results. Nothing to fix.

**Normal run:** searched `-in:sent -in:chats -label:Label_33 -label:Label_37` (pageSize 50, two pages sampled, ~100 threads spanning Aug 20 – Sep 3). Every single returned thread already carried Label_37 (AI-Reviewed) on all its messages, despite the negative-label filter — confirmed this is a known search quirk (tool docs warn threads with excluded criteria can still surface). Cross-checked independently with `-in:sent -in:chats newer_than:1d`: only 3 threads exist in the mailbox from the last 24h, and all 3 already carry AI-Reviewed.

**Conclusion:** mailbox is fully caught up — no genuinely unprocessed/unlabeled threads found, no new spam, no MOVE_FAILED. 0 threads classified this run (nothing new to classify). No push notification sent per the "come up empty → stay silent" rule for unattended runs.

**Note for future runs:** the `-label:X` exclusion operator in search_threads appears unreliable/stale for this mailbox — don't trust the query filter alone to mean "unprocessed"; verify a sample of returned threads' labelIds client-side before processing, as done here.
