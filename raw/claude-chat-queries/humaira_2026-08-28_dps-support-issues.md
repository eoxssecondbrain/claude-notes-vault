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

User: No. I don't want exact tickets. I want you to look at tickets and tell me what issue they are having. And what can we do to solve these issues

Assistant: Looking at the last 90 days of DPS tickets (52 substantive issues, filtering out routine payment-reminder and Stripe-notification tasks), the pattern is not random — it's a handful of recurring product bugs plus one process gap, not 52 unrelated problems.

Theme by frequency, last 90 days:

| Issue | Count | Pattern | Fix |
|---|---|---|---|
| Sales order stuck showing "Quote" after confirmation | 6 | Reported Jun 24, Jun 26 ("this error again"), Jul 6, Jul 28 ("still occurring"), Aug 18, Aug 21 — unresolved for 2 months | Needs a real root-cause fix from dev, not another per-order patch. This is the most visible chronic bug — customer is explicitly calling out that it keeps recurring |
| Auto-reserve / reservation function | 4 | Jun 26 (only reserved 2 of 60 pcs), Aug 19 (new failure scenario), Aug 25 (reserve-by-warehouse missing after being "pushed live"), Aug 28 (fails on non-stock product lines) | This is a regression on a recently-shipped feature that's getting worse, not better. Treat as P1 — freeze further changes to reservation until root-caused, and regression-test warehouse-level reserve + non-stock line edge cases before next release |
| Delivered quantities showing zero, blocking invoicing | 3 | Aug 17, Aug 27, Aug 28 — all in the last 2 weeks, customer says it's "happening with all of the ones where I was getting the stock production error" | Accelerating and directly blocks DPS from invoicing (cash flow impact). Needs root-cause on the stock production error now, before it hits more orders |
| Packing list missing tags (shipper/packer forgot to add tag) | 9 | Steady stream, Jun–Aug, always phrased "packer/shipper forgot" | This is DPS's warehouse process, not an EOXS bug — but 9 times in 90 days suggests the packing workflow doesn't flag untagged bundles before a list is finalized. Worth proposing a checklist/warning in the packing UI rather than leaving it to memory |
| Contact merging fails | 3 | Jul 29, Aug 3, Aug 19 ("why does this never work?") | Customer frustration is visible in the language. Dev fix needed on the merge tool itself |
| Refund issued in Stripe but credit not reflected in EOXS | 3 | Jul 13, Jul 18, Aug 24 | Stripe refunds aren't syncing to the EOXS credit balance automatically — manual correction needed each time. Worth automating this sync |
| Isolated server errors (cancel picking, generate blanking tags, negative scrap weight) | 3 | One-off stack traces shown to the customer | Not a pattern by themselves, but exposing raw tracebacks to the customer is a bad look — worth a general error-handling sweep |

The account-admin requests (new users, license adjustments, permissions, warehouse setup) are routine and not really "issues" — I excluded those from the count above.

Bottom line: strip out the noise and DPS has 4 real, recurring product defects (quote-stuck, reservation, zero-delivered-qty, contact merge — 16 tickets) plus one operational gap (packing tags — 9 tickets). The reservation bug and the zero-delivered-qty/invoicing bug are both trending worse in just the last two weeks and both touch revenue directly (can't invoice, can't fulfill correctly) — those two are where I'd push engineering first. The quote-stuck bug is lower urgency but has been open longest and is visibly eroding customer patience.
