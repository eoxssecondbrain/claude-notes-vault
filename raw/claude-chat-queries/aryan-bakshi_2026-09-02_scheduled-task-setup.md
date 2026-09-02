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
