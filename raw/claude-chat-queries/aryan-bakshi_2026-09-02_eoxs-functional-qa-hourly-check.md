---
thread_name: "eoxs-functional-qa-hourly-check"
user: "aryan-bakshi"
type: claude-chat
created: 2026-09-02
updated: 2026-09-03
---

[SCHEDULED TASK - AUTOMATED FIRING] This is an hourly automated check of the EOXS implementation task board (EOXS_Data_General MCP connector, the "eoxs-db" implementation_tasks tools). This session starts fresh with no memory of prior runs — follow this instruction exactly, without asking any clarifying questions.

1. Call list_implementation_tasks(stage="Functional QA") with no client filter, to get every task currently sitting in the Functional QA stage, across all clients.
2. For each task returned, call get_implementation_task(task_id) to get its full event history (includes stage-change history and attachment metadata).
3. In that event history, find the most recent event where event_type is "stage_change" and tracking_changes shows field "Stage" with new value "Functional QA". That event's event_time is when the task entered Functional QA.
4. Compare that event_time (UTC) to the current UTC time. If it falls within the last 60 minutes, this task counts as newly moved into Functional QA this run — regardless of who owns/is assigned to it, and regardless of who performed the move.
5. For every task newly moved this run, gather: task name, client name, full description, current owner, and every photo/video/link connected to it — image/video filenames from the task's attachments list, plus any URLs mentioned in its log_note event bodies (e.g. fathom.video call-recording links, image links, etc.).
6. If one or more tasks newly moved into Functional QA this run, write the final response listing each one, organized task by task, with all details from step 5 laid out clearly. This response is what the user will see and be notified about — make sure it stands alone (no reference to "earlier in this conversation", there isn't one).
7. If no tasks moved into Functional QA in the last 60 minutes, say so in one short line and stop — do not invent findings or repeat something from a previous run.
8. If the EOXS_Data_General connector or its tools are unavailable, or a call errors out, state that plainly in the final response instead of retrying repeatedly.
9. the scheduled task should stop automatically at 3 am ist and only work on weekdays

RESPONSE:
Checked at 2026-09-03T21:39 UTC. Three tasks are currently in Functional QA (all client discount-pipe-steel): "Sticker Descriptions - Bug" (id 30585, last moved to Functional QA 2026-07-23 12:07:20 UTC), "Customer Statement - Bug" (id 30583, last moved to Functional QA 2026-07-23 12:06:15 UTC), and "Payment Sent Emails on Bill Payment" (id 30555, last moved to Functional QA 2026-07-23 12:06:57 UTC). None entered Functional QA within the last 60 minutes — no tasks newly moved into Functional QA this run.

Note: trigger trig_0196wy2x5KSQeR1Vf4yYem7K ("EOXS Functional QA Hourly Alert") cron is "38 0-17,21-23 * * 1-5" (UTC), which already skips the 18:00-20:00 UTC window (23:30-01:30 IST) and runs Mon-Fri only — checked and left as-is since it already satisfies the "stop before ~3am IST, weekdays only" requirement from step 9.
