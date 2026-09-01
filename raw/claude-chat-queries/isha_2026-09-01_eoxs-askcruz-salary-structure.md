---
thread_name: "eoxs-askcruz-salary-structure"
user: "isha"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: Should i update employee data from here?

Assistant: Yes, this connection can do it — the employee directory is the one part of eoxs-db that's writable from here (create_employee, update_employee, deactivate_employee, reactivate_employee). Everything else in the system (emails, wiki, calls, tickets, invoices, CRM) is read-only, no exceptions.

Caveats before you do:

Writes go straight to the live employees table, immediately — no preview, no undo tool. A deactivation is a soft delete (record and history stay, just flagged inactive); there's no hard-delete anywhere.

I need the exact change stated explicitly ("update X's department to Y") — I won't write speculatively or infer it from context.

I'll confirm what I'm about to do before calling the write, every time, even for something small.

If it's a bulk change or something you're unsure about, safer to do it in whatever system is the actual source of truth for HR records and let this stay a read/reporting layer — your call on which fits the situation.

What's the change you want made?

User: could you please make an automation for me ?

Assistant: What kind of automation did you have in mind? A few common HR ones I could set up:

Recurring report — e.g. a weekly/monthly scheduled task that pulls something specific (pending leave requests, new joiners, offboarding status) and sends it to you at a set time.

Reminder/check-in — e.g. "remind me every Friday to review pending resignations" or a nudge before a probation period ends.

Data sync/update trigger — something tied to the employee directory write capability we just discussed (e.g. auto-flagging when someone's date_of_leaving passes).

Tell me what it should do, how often, and what you want delivered (a message here, a file, an email), and I'll set it up as a proper scheduled task rather than something that only runs while this chat is open.

User: Reminder/check-in — e.g. "remind me every Friday to review pending resignations" or a nudge before a probation period ends.
this will be required

Assistant: [Asked clarifying questions via AskUserQuestion: data-pull vs plain nudge for Friday reminder; timing; probation nudge lead time]

User answered: Pull actual data (Recommended); 10 PM IST; "on Friday only" (fold probation check into the same Friday reminder).

Assistant: Set up: a weekly scheduled task, "Friday HR Check-in: Resignations & Probation," firing every Friday at 10:00 PM IST. Each run will independently pull pending resignations and flag anyone nearing the end of their probation period, then send you a structured summary.

Two things to know:

It runs as a fresh session each time — it re-checks the eoxs-wiki-db access rules and re-queries live data every Friday, so it won't drift out of date.

Probation-end detection depends on whether that's actually tracked in the employee records (date_of_joining, notes, offer terms). If it isn't reliably there, the task will say "not tracked" rather than guess — worth confirming once you see the first run whether that field needs to be added to the employee directory for this to be useful long-term.

First run: this Friday, Sept 4, 10:00 PM IST.
