---
thread_name: "active-employee-list"
user: "isha"
type: claude-chat
created: 2026-08-20
updated: 2026-09-04
---

User: "so lakshit Singh 3rd sep dhruv maheshwari himanshu radhesh himanshu V 1 sep left"

Assistant: Loaded eoxs-wiki-db skill (fresh MCP reconnect this turn). Looked up each name in HR_MCP — Lakshit Singh (id 125), Dhruv Maheshwari (id 117), Himanshu Kumar (id 121), Radhesh Tinani (id 116). Asked user to clarify "Himanshu V" — confirmed it's the same person as Himanshu Kumar, not a 5th person. Then confirmed the write plan explicitly before acting (per skill's mandatory confirmation rule) — user confirmed "Yes, deactivate all 4."

Action taken: deactivate_employee called for all 4:
- Lakshit Singh (id 125) → date_of_leaving 2026-09-03, status inactive
- Dhruv Maheshwari (id 117) → date_of_leaving 2026-09-01, status inactive
- Himanshu Kumar (id 121) → date_of_leaving 2026-09-01, status inactive
- Radhesh Tinani (id 116) → date_of_leaving 2026-09-01, status inactive

All 4 writes succeeded (live environment, hr identity). Reported back to user with confirmed status/dates.

Still pending from earlier in session (not actioned, awaiting user decision):
(a) Kashish Chauhan deactivation reversal question
(b) Anjali Singh / Dhrup reactivation override question (Odoo + wiki both say inactive)
(c) Fardeen vs Mohd Fardeen same-name-different-email ambiguity
(d) 6 stale/likely-corrupted employee emails (Jaskeerat, Kriti Jain, Arpita, Humaira Zainab, Aryan Bakshi, Maria Naeem) not yet corrected.
