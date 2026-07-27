---
thread_name: "sabre-alloys-mrr-lookup"
user: "raj"
type: claude-chat
created: 2026-07-27
updated: 2026-07-27
---

# Sabre Alloys MRR Lookup

**User:** what's Sabre's MRR?

**Assistant:** Sabre Alloys' MRR is $10,970/month (28 users, up from a starting $4,080/month at 12 users), per the OV2 Sabre Alloys entity page (updated 2026-07-22) and corroborated by an internal batch note citing $10K MRR in the Feb 2026 outage settlement figures.

Context flagged:
- Billing has slipped to 30+ days in arrears — $10,970 is contracted MRR, not necessarily on-time collections.
- Separate $1,000/month settlement liability (25 months, from Feb 2026 outage) is owed BY EOXS to Sabre, not revenue.
- Proposed "IRIS Pro" AI add-on at $1,000/month floated 2026-07-02, pending Sabre approval — not yet included in the $10,970 figure.

**User:** who is charles white and what is his role in this company?

**Assistant:** Charles White is a management/executive-level contact at Sabre Alloys (client, not EOXS). Email cwhite@sabrealloys.com. Not the primary contact (that's Tye Webb, COO), but more operationally involved than title suggests — main Fireflies call contact for Sabre, directly involved in server migration and processing-speed escalations, and the recurring voice behind escalating packing-list-to-invoice quantity-mismatch complaints. 117 total interactions (109 email threads + 8 calls). Uses the Executive Dashboard module.

**User:** whats ppc's open ticket's count right now?

**Assistant:** Queried EOXS Teams Live (project_task table) live, filtered to PPC Metals' partner_id (502410). 411 active tasks total. Used Odoo's fold=true marker on project_task_type as the actual "closed" indicator (rather than guessing from stage names like "Paid"/"Approved"). Result: 360 closed (Paid: 207, Approved: 115, Communicated-folded: 38), 49 open.

Open breakdown: Communicated (not closed) 16, Need Developer 8, Ready for Sandbox 7, Task Pool 7, Assigned 5, Waiting for Client's Reply 2, Raj questions 1, QA Passed 1, Resolved 1, QA Failed 1.

Flagged caveat: "Resolved" and "QA Passed" (1 each) aren't marked fold=true in this instance despite being logically near-done, so they're counted as open here — may need reclassification depending on use case. This is EOXS's internal tracker for PPC, not PPC's own ticketing (PPC has no individual client MCP).

**User:** who is jessica at 3gm steel

**Assistant:** Jessica Worley — primary contact at 3GM Steel, Director of Supply Chain Management (promoted from Office Administrator). jessica@3gmsteel.com. Signed the EOXS contract July 31, 2025. Highest-volume 3GM contact (449 threads), dominant day-to-day power user (product creation, variants, leads, CRM). Actually with 3GM since ~March 2022 as Office Administrator, day-to-day EOXS point of contact well before formal contract signing. Was on maternity leave from ~June 2024 (long handoff to Jerrica Eldridge/Shanan Shaver started Jan 2024). Absorbed Shanan Shaver's price-guideline duties after Shanan's Jan 2026 departure. Recurring friction point: repeatedly requesting expanded self-service system access, including CCO-level parity for Travis Lane (Mar 2026 request).

**User:** what's dps's last invoice amount?

**Assistant:** Queried EOXS Teams Live account_move table live, filtered to Discount Pipe & Steel's partner_id (502192), type=out_invoice. Last invoice: INV/2026/0283, dated 2026-06-30, $3,510.00, posted. Noted recent invoice amounts have fluctuated month to month (not flat recurring): $4,700 (Jun 2), $3,120 (May), $2,730 (Apr), $5,620 (Mar). Flagged that this predates the AltDigital consultant seat billing change (Tina Valdez, Jamie Vernon) currently in motion per standing account notes.

**User:** when did greer steel last have a support ticket opened

**Assistant:** Queried EOXS Teams Live project_task table live, filtered to Greer Steel partner records (101167/101168/502210). Last ticket opened 2026-07-21: "Fix Google Maps Customer Selection Error" (task #7480), stage=Assigned (still open). Noted OV2's synthesized snapshot was stale (last synced ticket dated mid-April) vs. live data. Greer has had 5 tickets in the last two months (May 27 - Jul 21), steady low-volume cadence.

**User:** whats brannon steel's contact value ?

**Assistant:** Checked EOXS Teams Live crm_lead table live for David Brannon (id 18788, matches OV2's raw_path). CRM "Expected Revenue" field (the literal "value" field in Odoo CRM) shows $0.00 — flagged as stale/unfilled CRM data, not the real deal size, consistent with the vault's broader "CRM stage/value figures are unreliable" pattern. Provided actual contract economics instead: $14,400 CAD implementation fee (one-time, split/reissued across multiple sales orders), monthly recurring stated as $1,240 CAD/month flat but actually invoiced at $1,200 CAD/month in July 2026 (~3% unreconciled discrepancy), ~$20,592 CAD billed to date through May 2026 plus a new $1,356 July invoice and $3,051 additional-development charge. Flagged that Brannon Steel was carrying a multi-month AR backlog as of 2026-07-22 (May/June subscription invoices plus an Implementation HST invoice unpaid). Asked user to clarify if "contact value" meant something else (lifetime revenue, ARR, contact-specific attribution).

**User:** what is the name with which this thread got saved in this vault?

**Assistant:** Confirmed thread_name: sabre-alloys-mrr-lookup. Full path: raw/claude-chat-queries/raj_2026-07-27_sabre-alloys-mrr-lookup.md

**User:** why did you not save the last message?

**Assistant:** Acknowledged missed mandatory save after the Brannon Steel response; corrected by saving full transcript including that exchange.
