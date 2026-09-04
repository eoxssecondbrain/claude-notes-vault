---
thread_name: "scheduled-gmail-spam-detection-2026-09-04"
user: "raj"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

# Scheduled Email Spam Detection (v9) — Run 2026-09-04

**Trigger:** Scheduled task (automated), not a live user session.

## Setup
- Called `list_labels`: all required labels already exist — AI-SPAM (Label_33), AI-SPAM/Advertising (Label_34), AI-SPAM/Expired-OTP (Label_35), AI-SPAM/Fraud (Label_36), AI-SPAM/Investor-Outreach (Label_38), AI-Reviewed (Label_37). No labels created.
- AI-Reviewed already applied to 53,936 messages / 29,663 threads historically → this is a **normal run**, not a first run.

## Fix-up pass
- Query: `label:AI-SPAM in:inbox` → 0 threads returned. Nothing to fix.

## Tooling note
- Discovered that `-label:<LABEL_ID>` (e.g. `Label_37`) does NOT work for excluding by internal label ID in `search_threads` — it silently fails to filter. Using the label **display name** (e.g. `-label:AI-Reviewed`, `-label:AI-SPAM`) works correctly and was verified with a targeted test query. Also discovered `get_thread` and spam-folder searches (`in:spam`, `in:anywhere`, `label:SPAM`) return a permission error / empty results for threads inside Spam — this connector appears unable to read the Spam folder directly. Verification of a successful spam-move was done indirectly by confirming the thread no longer appears in an `in:inbox` search.

## Normal run
- Query: `-in:sent -in:chats -label:AI-SPAM -label:AI-Reviewed`, pageSize 50 → returned exactly 2 threads, no further pages (resultCountEstimate field is unreliable/rounded in this connector and was ignored in favor of actual returned items + absence of nextPageToken).

1. **Thread 1a06cdd6aa644fc8** — "Toll Processing Proposal - Sabre Alloys" from ronn@eoxs.com to michael@sabrealloys.com, tye@sabrealloys.com, dmgunderwood@gmail.com (cc rajat@eoxs.com).
   - Classification: Skip list — sender domain eoxs.com → **NOT_SPAM**.
   - Action: `label_thread` with AI-Reviewed (Label_37). Success.

2. **Thread 1a06cdb69381bca2** — "Sheenam has joined your Personal Meeting Room" from no-reply@zoom.us to rajat@eoxs.com.
   - Classification: Bucket 3 — Zoom Personal Meeting Room join ping → **SPAM (AI-SPAM/Advertising)**.
   - Action: `label_thread` with AI-SPAM + AI-SPAM/Advertising (Label_33, Label_34). Success.
   - `mark_thread_spam` called. Success (empty response, no error).
   - Verification: `get_thread` on this thread returned a permission error (connector cannot read Spam-folder threads). Fallback verification: searched `in:inbox from:no-reply@zoom.us subject:"joined your Personal Meeting Room"` → 0 results, confirming the thread is no longer in Inbox. Treated as confirmed given the connector's spam-folder access limitation.

## Final report
- Checked: 2
- SPAM/SUSPICIOUS: 1 (AI-SPAM/Advertising: 1)
- NOT_SPAM: 1
- Fixed by fix-up pass: 0
- Moves confirmed by verification: 1 (via inbox-absence; direct spam-folder lookup blocked by connector permission)
- MOVE_FAILED: none

## Outcome
Routine, low-volume run. No errors requiring escalation. No push notification sent per standing guidance (nothing anomalous, no failures, trivial volume).
