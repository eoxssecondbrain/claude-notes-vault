---
thread_name: "muskan-leave-balance-lookup"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

User: my name is muskan sharma. check how many total leaves i have

Assistant: I checked hr_employee, hr_leave, and hr_leave_allocation in the EOXS Team Live (Odoo) database — no record exists for "Muskan Sharma" or any email containing "muskan" (searched by name and email, ten Sharma-named interns show up, none is you). Also checked eoxs-db (wiki/assets) for a leave policy or balance reference — nothing relevant.

Two things worth flagging directly rather than guessing further:

Your saved preference says to check the "Muskan-eoxs-vault" skill file before acting on a new thread. I searched this session's available skills and it doesn't exist here — only threads-ov and eoxs-data-general are loaded. So I couldn't check it as instructed.

Your leave balance isn't tracked in the EOXS Odoo HR module at all (no employee record there under your name). If it's tracked somewhere else — a spreadsheet, a separate HR tool, or that missing vault — point me to it and I'll pull the number. Otherwise this may need to go to whoever manages HR records directly.

User: Check in Ask cruz Odoo

Assistant: No AskCruz Odoo connector exists in this session — I checked the installed connectors list (empty for any Cruz/Odoo match) and the EOXS client registry (8 EOXS clients, no AskCruz). Only two data sources are available here: EOXS Team Live Odoo and the EOXS second-brain (eoxs-db) — neither has an AskCruz instance.

If AskCruz runs its own Odoo, that connector isn't set up in this workspace. You'd need to connect it (or tell me its URL/access details) before I can query it.

User: tell me about leave poilcy then

Assistant: EOXS's leave policy for interns (your track): each intern is allocated 5 sick leave + 5 casual leave days (10 total) per the offer letter, valid until your one-year joining anniversary. No leave can be applied in the first two weeks of the internship except urgent situations.

Casual leave needs your team lead's approval at least 1-2 days in advance (policy documents give both "2 days" and "24 hours" depending on which restatement), then must be filed on the EOXSTEAM portal (teams.eoxs.com) once approved.

Sick leave is treated as emergency leave: HR and your team lead need to be told immediately when it comes up, a medical note is required, and the portal filing itself can happen the next working day after you're back.

If you use up all 10 before the one-year mark, anything further is unpaid leave unless HR grants an exception. After a year, you can email HR to request the next year's allocation of 10.

One enforcement point worth knowing: leave taken without the required advance notice (CL) or without informing HR/your lead at the time (SL) gets recorded as unpaid, regardless of the reason given — this has been enforced same-day in at least one documented case.

This is the general intern policy from EOXS's HR documentation, not your personal record — since you don't have an employee record in the EOXS Odoo HR module, I can't tell you your actual remaining balance from this system. That'd need to come from whoever manages your specific EOXSTEAM portal account.

Sources: EOXS wiki — "Intern Onboarding: Leave Policy & EOXSTEAM Platform Setup", "EOXS Leave & Attendance Policy Enforcement — October 2025", "Employee Leave & Attendance Logging Process"
