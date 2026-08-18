---
title: "DPS (Discount Pipe & Steel) — Tickets, Licensing & Churn Signal"
type: chat-summary
sources: [raw/claude-chat-queries/raj_2026-07-27_dps-support-tickets-status.md, raw/claude-chat-queries/raj_2026-07-27_dps-austin-user-license-list.md, raw/claude-chat-queries/raj_2026-08-18_discount-pipe-amy-churn-signal.md]
created: 2026-07-27
updated: 2026-08-18
---

# DPS (Discount Pipe & Steel) — Tickets, Licensing & Churn Signal

_One-sentence description of what this cluster of conversations covers._

Three DPS-related threads over three weeks — live support/dev ticket status, an unresolved user-licensing dispute over two unbilled seats, and a fresh churn-risk signal from a client contact venting to a peer customer — that together sketch an account with open product pain and open billing friction at the same time.

## Summary

On 2026-07-27, Raj asked for DPS's support ticket status. OV2's own `search_tickets` tool returned only stale July/August 2025 tickets, so the assistant instead queried EOXS Teams Live's `project_task` table filtered to DPS's partner_id (502192), which reflects live dev/support Kanban state. Of 588 active tasks, 574 were effectively closed (Paid 409, Approved 198, Communicated 57); 14 remained genuinely open, notably: "Need Developer" item Re: S05460 - One Stop Metals Limited (opened 6/26, still unassigned as of 7/3); "QA Failed" on Balance Sheet Report (stalled since 4/16); and "Ready for Sandbox" on Fix Report Filters Not Persisting, a priority-1 item opened 1/8/2026 that only reached sandbox on 7/23/2026 — roughly a 6.5-month cycle time. A separately-remembered "packing-list scanner bug" (previously noted as held in sandbox pending a Change Document notification) could not be located anywhere in the current `project_task` table under that or related phrasing.

Same day, Raj asked about the last correspondence with Austin (DPS) regarding a user list Austin had requested, where support had flagged that two users — Tina Valdez and Jamie Vernon — were not being charged. The assistant found a June 11, 2026 "Licenses" thread and a July 22–24, 2026 "Re: Invoice / EOXS INV/2026/0283" thread; the July 24 support reply itemized Active Users (Billed) vs. Active Users (No License Fee), with Tina and Jamie in the unbilled category. Raj then had the assistant draft an email (signed as Ron, continuing Ron's role as Austin's contact on this topic) explaining that Tina and Jamie's seats were held off-bill on a temporary assumption that no longer holds since both are active users, and that they'll move to standard licensing starting the next invoice cycle. The assistant flagged that "next invoice cycle" was left vague and should be pinned to an actual invoice number/date before sending, since Austin is known to escalate methodically and push for itemized specifics.

On 2026-08-18, a new and more serious signal arrived: Ryan at Eastern States Steel (a peer EOXS client, not EOXS support) emailed Raj and Ron on 8/17 at 3:59 PM reporting that Amy at DPS had called him venting about reserve functionality and double-selling of inventory, saying DPS is "at their wits end" and contemplating switching systems. Ron replied same day at 5:18 PM, calling the frustration fair, committing to making reserve/double-sell fixes top priority this week with QA before deploy, and promising to reach out to Amy directly. The assistant flagged this as a churn escalation signal rather than a routine bug report — Amy venting to a peer client before going to a competitor is a materially different risk signal than a support ticket — and noted it lands on the same account as the still-unresolved Tina/Jamie billing dispute, meaning DPS currently has two live friction points simultaneously. As of this thread, it was unconfirmed whether anyone had actually called Amy yet, or whether Ron's "top priority this week" fix commitment was real or a de-escalation placeholder.

## Tribal Knowledge Extracted
- OV2's `search_tickets` tool is unreliable for DPS — it only surfaces stale 2025 ticket data. Current/live ticket-equivalent status for DPS must be pulled from EOXS Teams Live's `project_task` table filtered by partner_id, not OV2's ticket tool. (source: raw/claude-chat-queries/raj_2026-07-27_dps-support-tickets-status.md)
- DPS's partner_id in EOXS Teams Live is 502192 — needed to filter `project_task`/`res_partner` queries to this account. (source: raw/claude-chat-queries/raj_2026-07-27_dps-support-tickets-status.md)
- A previously-tracked "packing-list scanner bug fix held in sandbox pending Change Document notification" (known from prior memory/context) is no longer traceable in the current `project_task` table under that or related phrasing — either resolved, renamed, or tracked elsewhere; flagged as worth reconciling with Raj/Ron directly rather than assumed fixed. (source: raw/claude-chat-queries/raj_2026-07-27_dps-support-tickets-status.md)
- Standing informal billing convention at DPS: certain seats can be marked "Not Billable - Instructions from Raj" as an annotation, and there is a now-standard itemized Active-Users-Billed vs. Active-Users-No-License-Fee list sent per invoice — this is how the Tina/Jamie unbilled-seat issue was originally surfaced. (source: raw/claude-chat-queries/raj_2026-07-27_dps-austin-user-license-list.md)
- Ron is DPS's established point of contact for licensing/billing correspondence with Austin (not Raj directly) — outbound emails on this topic are drafted and signed as Ron to preserve continuity with prior threads. (source: raw/claude-chat-queries/raj_2026-07-27_dps-austin-user-license-list.md)
- Read on Austin's communication style (informal client-relationship knowledge, not written anywhere else): he escalates methodically and pushes for itemized detail, so any billing-change email to him needs to lead with a clear "why now" rationale and a concrete invoice reference rather than an unexplained unilateral notice. (source: raw/claude-chat-queries/raj_2026-07-27_dps-austin-user-license-list.md)
- A client contact venting to a peer client (rather than to EOXS support) is treated internally as a distinct, more severe churn-escalation signal than a normal bug report — the reasoning being that the client is shopping the frustration around the client network before shopping it to competitors. This is an informal risk-triage heuristic, not a documented policy. (source: raw/claude-chat-queries/raj_2026-08-18_discount-pipe-amy-churn-signal.md)

## Key Points
- 2026-07-27: DPS had 588 active tasks in EOXS Teams Live; 574 closed/handled (Paid 409, Approved 198, Communicated 57), 14 genuinely open.
- 2026-07-27: "Fix Report Filters Not Persisting" (priority 1) opened 1/8/2026, didn't reach Ready for Sandbox until 7/23/2026 (~6.5 months).
- 2026-07-27: "Balance Sheet Report" has been QA Failed and stalled since 4/16/2026.
- 2026-07-27: "Re: S05460 - One Stop Metals Limited" task opened 6/26/2026, unassigned as of 7/3/2026 (Need Developer stage).
- 2026-06-11 and 2026-07-22–24: correspondence trail on DPS user licensing; July 24 support reply itemized Tina Valdez and Jamie Vernon as active but unbilled users.
- 2026-07-27: Draft email prepared (signed as Ron) to notify Austin that Tina and Jamie's licenses move to standard billing "starting next invoice cycle" — invoice number/date still needed before sending as of this thread.
- 2026-08-17, 3:59 PM: Ryan (Eastern States Steel) emailed Raj and Ron that Amy (DPS) called him venting about reserve functionality and double-selling of inventory, and that DPS is considering switching systems.
- 2026-08-17, 5:18 PM: Ron replied committing to make reserve/double-sell fixes top priority this week (QA before deploy) and to contact Amy directly — unconfirmed as of this thread whether that outreach or the fix timeline had actually happened.

## Sources
- raw/claude-chat-queries/raj_2026-07-27_dps-support-tickets-status.md — Live DPS dev/support ticket status pulled from EOXS Teams Live project_task (OV2's ticket tool found stale).
- raw/claude-chat-queries/raj_2026-07-27_dps-austin-user-license-list.md — Correspondence review on DPS's unbilled Tina Valdez/Jamie Vernon seats and drafting of an email to Austin about moving them to standard billing.
- raw/claude-chat-queries/raj_2026-08-18_discount-pipe-amy-churn-signal.md — Eastern States Steel's Ryan reporting Amy (DPS) venting about reserve/double-sell issues and considering switching systems; flagged as a churn escalation signal.

## Candidate OV2 Cross-References
- Discount Pipe & Steel (DPS) client entity page — the unresolved ~6.5-month cycle-time issue on "Fix Report Filters Not Persisting" and the untraceable packing-list scanner bug are operational process gaps worth a pointer.
- Discount Pipe & Steel (DPS) client entity page — the Tina Valdez/Jamie Vernon licensing dispute has a concrete drafted outbound action (email to Austin) pending an invoice date, worth a pointer once sent.
- Discount Pipe & Steel (DPS) client entity page — the Amy churn-escalation signal (venting to a peer client, reserve/double-sell functionality complaint, considering switching systems) is a materially new risk signal worth flagging on the account page, especially combined with the concurrent billing friction.
