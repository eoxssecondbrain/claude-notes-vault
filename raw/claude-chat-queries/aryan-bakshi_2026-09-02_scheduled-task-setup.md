---
thread_name: "scheduled-task-setup"
user: "aryan-bakshi"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

**User:** I want to set up a scheduled task. Briefly explain how scheduled tasks work in Cowork, then ask me a few questions to figure out what I'd like Claude to do and when it should run.

**Assistant:** Scheduled tasks in Cowork run on a cron schedule (or a one-time timestamp) and each firing starts a completely fresh session — it has no memory of this conversation, so the prompt has to be a fully self-contained instruction. Results come back as a new session the user reviews independently; Claude can optionally send a push notification or email when a run finishes something noteworthy. A task can optionally be bound to a specific computer if it needs local device access (files, browser, apps on that machine) — that binding is set once at creation and can't be added later.

A few things I need to nail down before creating one:

[AskUserQuestion tool call with three questions:]
1. "How often should this task run?" (Frequency) — options: Daily, Weekly / specific weekdays, One-time, Other custom schedule
2. "Does the task need access to your computer (local files, browser, apps), or can it run entirely in the cloud?" (Device access) — options: Cloud only, Needs my computer, Not sure
3. "Should it notify you when a run finishes?" (Notifications) — options: Push notification (Recommended), Push and email, No notification

**User's answers:** Frequency = "Daily", Device access = "Cloud only", Notifications = "Push notification (Recommended)"

**Assistant:** Good, that gives me the shape: daily, cloud-only, push notification on completion. Two things left before I can create it:

1. What exactly should the task do each time it fires? (e.g. pull a report, check something and flag issues, draft something, send a summary — give me the actual instruction as you'd want it written for a session with no memory of this conversation)
2. What time of day (IST) should it run?

**User:** so what i wanted the scheduled task on is for you to access the eoxs task board  from the mcp connectors and see which tasks are under my name ( under my name means the tasks in which i am either assigned or am in ownership off) on in the functional qa stage on the board
check those tasks every hour and send me a notification if there are any new tasks that were pushed to functioncal qa stage in the last hour (doesnt matter if i am in assigned or in ownership of the latest moved task, if it was moved in the last hour i want the notification)

and in the notification i also want the name of the task, details of the task and any photos/ videos/links that are in the log note of the said task

**Assistant:** Created. It runs every hour (anchored at :38 past the hour, so next run is 2026-09-02 14:38 UTC / 8:08 PM IST) with push notifications on.

Each run: pulls every task currently in Functional QA across all clients, checks each one's stage-change history for a transition into Functional QA within the last 60 minutes, and if found, reports task name, client, description, owner, and any photos/videos/links from attachments and log notes. No match in a given hour means a quiet one-line "nothing moved" and no real notification.

One thing worth flagging: the push notification is a system-generated summary of the run's output, not something I template directly — so the phone alert will likely be a condensed version, with the full task details (links, description, attachments) sitting in that run's session for you to open. If you want the full detail in the push text itself, that's not something these tools guarantee.

[Trigger created via create_trigger tool: name "EOXS Functional QA Hourly Alert", cron_expression "38 * * * *" (hourly), trigger_id trig_0196wy2x5KSQeR1Vf4yYem7K, notifications: push=true, requires_local_device=false. Full prompt text stored in the trigger:

"This is an hourly automated check of the EOXS implementation task board (EOXS_Data_General MCP connector, the "eoxs-db" implementation_tasks tools). This session starts fresh with no memory of prior runs — follow this instruction exactly, without asking any clarifying questions.

1. Call list_implementation_tasks(stage="Functional QA") with no client filter, to get every task currently sitting in the Functional QA stage, across all clients.
2. For each task returned, call get_implementation_task(task_id) to get its full event history (includes stage-change history and attachment metadata).
3. In that event history, find the most recent event where event_type is "stage_change" and tracking_changes shows field "Stage" with new value "Functional QA". That event's event_time is when the task entered Functional QA.
4. Compare that event_time (UTC) to the current UTC time. If it falls within the last 60 minutes, this task counts as newly moved into Functional QA this run — regardless of who owns/is assigned to it, and regardless of who performed the move.
5. For every task newly moved this run, gather: task name, client name, full description, current owner, and every photo/video/link connected to it — image/video filenames from the task's attachments list, plus any URLs mentioned in its log_note event bodies (e.g. fathom.video call-recording links, image links, etc.).
6. If one or more tasks newly moved into Functional QA this run, write the final response listing each one, organized task by task, with all details from step 5 laid out clearly. This response is what the user will see and be notified about — make sure it stands alone (no reference to "earlier in this conversation", there isn't one).
7. If no tasks moved into Functional QA in the last 60 minutes, say so in one short line and stop — do not invent findings or repeat something from a previous run.
8. If the EOXS_Data_General connector or its tools are unavailable, or a call errors out, state that plainly in the final response instead of retrying repeatedly."]
