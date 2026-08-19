---
thread_name: "gmail-marketing-cleanup-automation"
user: "danish"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

User: i wan to create an automation where all spam and marketing emails gets labelled and moved to a different folder where i can review and delete it at once

Assistant: [Read threads-ov and eoxs-data-general skill files as required for new threads. Noted this task does not match eoxs-data-general (not an EOXS data question) — proceeding as a Gmail automation task, no specific skill match, per user preference to flag unclear/no-match skill routing before proceeding.]

Assistant: [Checked available Gmail MCP tools — confirmed there is no create_filter tool, so true "set and forget" filtering requires either a native Gmail filter (via browser automation) or a recurring scheduled Claude task using the Gmail MCP tools.]

Assistant asked via AskUserQuestion:
1. How should this run? (Native Gmail filter / Scheduled Claude task / Both) — User picked: Scheduled Claude task
2. What should count as "spam and marketing"? (Promotions + bulk marketing / Promotions only / Broader incl. Social+Updates) — User picked: Promotions + bulk marketing
3. Should existing inbox also be swept now? (Both - clean up existing too / Going forward only) — User picked: Both — clean up existing mail too

Assistant: Created a new Gmail label "Marketing Review" (label ID Label_12, orange color preset).

Assistant: Ran backlog cleanup — searched `in:inbox category:promotions` (~201 matching threads across the ~13,293-thread inbox), and for each thread called label_thread (add Label_12) + unlabel_thread (remove INBOX) to move it out of the inbox into the Marketing Review label for batch review/deletion. Gmail API had intermittent "service currently unavailable" errors throughout: handled by re-querying `in:inbox category:promotions` repeatedly (this naturally surfaces anything that failed, since successfully processed threads no longer match `in:inbox`) and retrying failures across three passes (201 → 45 → 1 remaining), until the backlog was fully cleared. Final verification search returned 0 remaining `in:inbox category:promotions` threads.

Assistant: Created a recurring scheduled task ("Marketing Email Sweep", trigger ID trig_01DcCg8C1AJUMGx5zCzTMXdo) via create_trigger, cron `30 2 * * *` UTC = 8:00 AM IST daily, next run 2026-08-20T02:30 UTC. The task prompt instructs a fresh session each day to: search `in:inbox (category:promotions OR unsubscribe)`, label matches with Label_12 and archive (remove INBOX), skip anything that looks transactional/important (OTPs, receipts, statements, boarding passes, password resets) even if matched, retry once on transient API errors then skip, and stay silent unless something notable happened (persistent errors or 100+ threads in one run). Notifications set to push:false, email:false (silent).

Assistant final summary to user: Set up "Marketing Review" label as the review folder. Swept and archived the full existing backlog of promotional/marketing email out of the inbox into that label (started at ~201 matching threads, now 0 remain in the inbox). Created a daily scheduled task (8:00 AM IST) that will keep sweeping new marketing/promotional mail into the same label going forward, while leaving transactional mail (OTPs, receipts, statements) alone. User can open the "Marketing Review" label in Gmail anytime to review and bulk-delete.
