---
thread_name: "gmail-spam-detection-scheduled-run-2026-08-30"
user: "raj"
type: claude-chat
created: 2026-08-30
updated: 2026-08-30
---

# Scheduled Email Spam Detection (v3) — Run 2026-08-30

**Trigger**: Automated scheduled task, no live user present.

**Step 0 (repair pass)**: Searched `label:AI-SPAM -in:spam` (includeTrash=true) — 0 orphaned threads found. Healthy.

**Run type**: Normal run (AI-Reviewed label already had 14,654+ threads applied historically → not a first run).

**Step 1**: Searched `in:inbox -label:AI-SPAM -label:AI-Reviewed`, paginated across 8 pages of 50. Discovered a very large historical backlog of inbox threads (dating back to 2020) that had never been labeled AI-Reviewed or AI-SPAM — far larger than the stale `resultCountEstimate` of 201 suggested.

**Processed this run**: 400 threads total.
- SPAM: 3 (all sub-labeled Advertising) — cold marketing/promotional emails with no eoxs.com address involved:
  1. "Are you frustrated with the results from your networking efforts?" (taz.sadhukhan@centricitynetwork.com)
  2. "Following up to schedule time to chat... Data 360 Business Bootcamp" (krystle.edullantes@data360.solutions)
  3. "FINAL CLEARANCE! 50% 60% & 70% off everything" (news@a.mango.com)
  All three: labeled AI-SPAM + AI-SPAM/Advertising, then immediately moved to Spam via mark_thread_spam (atomic, no separation between label and move).
- SUSPICIOUS: 0
- NOT_SPAM: 397 — labeled AI-Reviewed only. Vast majority matched the skip-list (eoxs.com/eoxsteam.com address present in sender/To/Cc, or calendar mail, or security notices, or payment/invoice mail). A handful were classified NOT_SPAM by content assessment even without an eoxs address present (e.g. legitimate Zoom/Google/BuildingLink/G Suite service notifications, ongoing personal correspondence) since they showed no phishing/marketing/fraud indicators.

**Outstanding**: Thousands of pre-2021 inbox threads remain unprocessed. Since labeled threads are permanently excluded from future normal-run searches, no work is lost or repeated — subsequent scheduled firings will continue clearing the backlog incrementally.

**User notified**: Yes, via push notification (3 spam moved + backlog discovery, since this materially changes what future runs will find/do).
