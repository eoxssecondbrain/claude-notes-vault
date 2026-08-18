---
thread_name: "kriti-jain-intro"
user: "jaskeerat"
type: claude-chat
created: 2026-08-18
updated: 2026-08-18
---

User: My full name is Kriti Jain, I go by Kriti — remember that.

Assistant: Got it, Kriti — saved.

User: What's my job title and department, based on what you can see?

Assistant: Innovation Cell · AI Engineer — that's what shows in the monthly performance summaries (July and June 2026) that list you by name and department.

User: Who do I report to, and who reports to me?

Assistant: In eoxs-teams (Odoo, current by definition): no manager set (parent_id is null), and nobody has you set as their manager. Nobody reports to you.

One flag: Odoo lists your job title as "Marketing Intern" in the "Marketing/OPS Team" department — that conflicts with the "Innovation Cell · AI Engineer" title showing in the July/June performance summary emails from eoxs-db. Since Odoo is the live HR record, it wins per the data hierarchy, but the mismatch itself is worth noting rather than picking silently — it looks like your Odoo employee record hasn't been updated to match your actual role.

User: ok so, i report to sheenam first of all. i was hired as a marketing intern on 25th may but then they changed my position to software developer intern and i started as a software developer intern. then on 12th may i got full time offer on 12th may as an AI Engineer . remember that for the context and update the information you have.

Assistant: Saved: reporting line to Sheenam, and the hire history (Marketing Intern May 25 → Software Developer Intern → full-time AI Engineer offer).

One thing before I lock it in: you said the full-time AI Engineer offer was "on 12th May" — but that's before your May 25 Marketing Intern hire date. That's likely a typo for a different month or year. What's the actual offer date?

Also worth flagging: Odoo's hr_employee record for you still shows "Marketing Intern" in "Marketing/OPS Team" with no manager set. None of this — Sheenam as manager, the move to Software Developer Intern, the AI Engineer promotion — is reflected there. That's a live HR data gap on their end, not something I can fix since the connector is read-only.
