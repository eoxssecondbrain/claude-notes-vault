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
