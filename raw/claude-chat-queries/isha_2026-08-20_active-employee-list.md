---
thread_name: "active-employee-list"
user: "isha"
type: claude-chat
created: 2026-08-20
updated: 2026-08-28
---

[Full thread continues from prior saves through 2026-08-28. Latest exchange:]

User: you can re confirm that from eoxs team and ask cruz teams portal

Assistant: [Searched HR_MCP wiki for "AskCruz", fetched relevant wiki pages (AskCruz Mailbox Rollout, Sebastian Roa Viertel, Kartikey Tripathi work-log, EOXS Internship Extend-Relieve Cycle), fetched the actual AskCruz mailbox rollout email (id 62110) listing 42 recipient addresses, and queried the live EOXS Team Odoo database's hr_employee table (341 records) via Eoxs_team connector.]

I checked the live EOXS Team Odoo HR system (hr_employee table, 341 records — a completely independent source from the eoxs-wiki-db I've been using) and also the AskCruz mailbox rollout email. Results, most important first:

Kartikey Tripathi, Mahesh Mudiraj, and Arshad Malik show as active in Odoo right now, directly contradicting the eoxs-wiki-db record that has them deactivated since 2026-08-18. This is independent corroboration for your original claim — I'd recommend reactivating these three.

Anjali Singh and Aaryan Mehra show as inactive in Odoo too — matching the eoxs-wiki-db deactivation, not your pasted list. Two independent systems now agree these two are correctly inactive, so I'd hold off reactivating them unless you have a specific reason to override both records.

Kashish Chauhan isn't in Odoo at all, so I can't corroborate either way there.

The bigger issue: none of the 21 people I just created (Radhesh Tinani through Kushali Chauhan) appear anywhere in the live Odoo HR system — zero footprint. Sebastian Roa Viertel's absence makes sense since the wiki explicitly documents him as a contractor through SRV Consulting, not an EOXS employee. But the other 20 having no trace in the company's actual HR system is worth pausing on — either they're too new to have been entered into Odoo yet, or this needs a second look before treating them as confirmed active headcount.

On Parshant Sharma and Harsh Yadav being two different people each: Odoo only has one "Harsh Yadav" record and zero "Parshant Sharma" records. This doesn't disprove your claim, but Odoo can't corroborate it either — I still need department/role/email for the second person of each name before I can create distinguishable records.

Given the Odoo evidence, do you want me to: reactivate Kartikey Tripathi, Mahesh Mudiraj, and Arshad Malik now? And separately, should I leave the 21 new records as-is, or hold on treating them as confirmed until you verify against whatever source told you they're active (since neither eoxs-wiki-db nor Odoo had them before I created them)?

User: ok

Assistant: Reactivating Kartikey Tripathi, Mahesh Mudiraj, and Arshad Malik based on the Odoo corroboration.

[Called reactivate_employee for ids 52, 63, 17 — all succeeded]

All three reactivated — Kartikey Tripathi, Mahesh Mudiraj, Arshad Malik are active again. Active headcount is now 68.

Still unresolved and untouched: Anjali Singh and Aaryan Mehra stay inactive (both systems agree), Kashish Chauhan is unconfirmed either way, the 21 newly created employees remain in the system but unverified against Odoo, and the second Parshant Sharma / second Harsh Yadav still need department, role, and email before I can create them.
