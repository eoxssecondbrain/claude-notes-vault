---
thread_name: "scheduled-spam-detection-runs"
user: "raj"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

[SCHEDULED TASK RUN — 2026-09-02, Scheduled Email Spam Detection v9]

Fix-up pass: searched label:AI-SPAM in:inbox → 0 threads found (nothing to fix).

Normal run: labels AI-SPAM (Label_33) and AI-Reviewed (Label_37) already exist and have been applied extensively (53,735 messages under AI-Reviewed), so this was NOT treated as a first run.

Ran search_threads with query "-in:sent -in:chats -label:Label_33 -label:Label_37", pageSize 50, and paginated through 4 pages (~200 threads, matching the tool's resultCountEstimate of 201).

Finding: the -label:Label_33/-label:Label_37 exclusion in the query does not actually filter — nearly every thread returned already carries Label_37 (AI-Reviewed) on all its messages. Verified this by inspecting labelIds on every message in every returned thread across all 4 pages via jq. Out of ~200 threads returned, only ONE (thread 1a062cee78966544, "Re: Create a New Processing Module", from info.eoxs@gmail.com, dated 2026-09-02T15:48:40Z, the most recent thread in the mailbox excluding sent/chats) actually lacked both labels. All other ~199 threads across pages 2-4 were 100% already labeled (0 unlabeled messages each), confirming the mailbox is otherwise fully caught up and the query's label exclusion is unreliable/non-functional for these custom label IDs.

Classified the one new thread: sender info.eoxs@gmail.com (EOXS internal task-notification system), to: rajat@eoxs.com — matches skip-list rule 1 ("any eoxs address in To/Cc"). Classified NOT_SPAM, applied AI-Reviewed label. No further action.

Final report:
- Checked: 1 new thread (plus ~199 already-labeled threads inspected to confirm no gaps)
- SPAM/SUSPICIOUS: 0
- NOT_SPAM: 1 (AI-Reviewed applied)
- Moves by sub-label: none
- Fixed by fix-up pass: 0
- Moves confirmed by verification: n/a (no moves)
- MOVE_FAILED: none

Flagged to user via push notification: the search_threads label-exclusion filter (-label:Label_33/-label:Label_37) appears broken/unreliable — it returns already-labeled threads instead of excluding them. This run compensated by manually inspecting labelIds on every returned thread, but future runs relying on the query filter alone risk either reprocessing already-reviewed mail or missing genuinely new mail buried among stale results. Recommend investigating the Gmail connector's label-ID exclusion syntax, or switching this workflow to sort-by-recency + manual label inspection.
