---
thread_name: "dps-support-issues"
user: "humaira"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: Hi Can you please check and let me know what issue DPS having right now ?

Assistant: [Asked clarifying question via AskUserQuestion: "DPS (Discount Pipe & Steel) doesn't have a support-ticket/helpdesk table in the live database — so "issue" could mean a few different things. What do you want me to check?" Options: Overdue invoices/collections, Stuck orders/shipments, Open purchase orders/vendor issues, Something else.]

User selected: Support ticket

Assistant: DPS (Discount Pipe & Steel) currently has 7 open support tickets in the EOXS Support queue — not yet resolved (excludes "Communicated" and "Paid"/closed stages). Oldest first:

| Ticket | Opened | Stage | Issue |
|---|---|---|---|
| S05460 | Jun 26 (63d) | Need Developer | Auto-reserve only pulled 2 of 60 pcs bundles on a sales order line |
| Quote-02416 | Jul 28 (31d) | Need Developer | Sales order stuck showing as "quote" stage instead of confirmed |
| S06119 | Jul 31 (28d) | Need Developer | "Values making no sense" (vague description, needs follow-up) |
| S06569 | Aug 24 (4d) | Assigned | Stripe payment received but not showing up in the system |
| Ops Blockers | Aug 27 (1d) | Tickets (new) | Salespeople manually calculating weights, risk of incorrect sales orders |
| S06447 | Aug 28 (today) | Tickets (new) | Delivered quantities showing zero, blocking invoicing — stock production error |
| S06659 | Aug 28 (today) | Tickets (new) | Reservation function failing when adding a non-stock product line |

Three of these have sat in "Need Developer" for a month or longer with no movement since Aug 19 — that's the real backlog, not the two that opened today.

Sources: EOXS Teams Live (eoxs-teams) — project_task, project "EOXS Support," partner_id 502192.
