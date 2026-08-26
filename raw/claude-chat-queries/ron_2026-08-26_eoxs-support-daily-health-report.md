---
thread_name: "eoxs-support-daily-health-report"
user: "ron"
type: claude-chat
created: 2026-08-26
updated: 2026-08-26
---

## User (scheduled routine trigger)

Run the EOXS Support daily health report and email it. This is a fully autonomous scheduled run — do not ask clarifying questions or wait for approval, just build and send the report.

1. Query the Teams_eoxs connector (EOXS Teams Live, Odoo): project_task where project_id = 76 (the "EOXS Support" project) and active = true. Join to project_task_type for stage name, res_partner (via partner_id) for client, res_users/res_partner for assignee.

2. Tracked open stages ONLY: Tickets, Assigned, Waiting for Client's Reply, Need Developer, QA, Ready for Live. Exclude Communicated, Paid, Approved entirely — those do not count as open, per standing instruction.

3. New-tickets window: tickets created in the trailing 24 hours ending at this run's send time (6:00 PM Eastern), i.e. since 6:00 PM Eastern the previous day. Among those, separately flag which have already moved out of the 6 tracked stages within that same window (e.g. into Communicated) — report those as "moved/resolved same day," not as still open.

4. For every ticket currently sitting in the 6 tracked stages (regardless of age), pull id, name, client, stage, create_date, date_last_stage_update, and full description. Compute age = now − create_date, and time in current stage = now − date_last_stage_update.

5. Strip HTML from each description and read it to understand what the ticket is actually about, in plain language — not the raw subject line.

6. Detect recurring patterns: within each client's tickets (open and newly created), find tickets that are the same underlying issue recurring — same error, same bug class, same complaint. Note how many instances, since when (date of the earliest instance), and whether the client's own words signal a repeat ("this error again," "still occurring," "happened before"). Flag any regression where a description references a fix that was supposedly already completed.

7. Assign each client a health status — Critical (red) / Watch (yellow) / Stable (green) — based on: presence of a recurring/systemic bug, explicit client-stated urgency or financial/revenue impact, backlog age, and open-ticket volume. Write one sentence of rationale per client explaining the call, not just a number.

8. Build a ranked "Developer priorities — work these today" list (roughly 5-6 items) across all clients: tickets that should be worked today specifically because they're financially/revenue-impactful, recurring/systemic (fixing root cause helps multiple tickets), explicitly time-sensitive per the client, or a fix that's built but stuck in a non-dev bottleneck (e.g. sitting in QA) and just needs pushing through. For each: ticket, client, what needs doing, why today, and who it's currently assigned to (or "Unassigned").

9. Data-quality check: for any ticket with no client (partner_id) tagged in Odoo, check whether the description content identifies a client anyway (e.g. an email signature "Sent by <Client> L.P."). If so, attribute it to that client in the report and note the tagging gap in the footer.

10. Build the report reusing the same visual format as the reference artifact at https://claude.ai/code/artifact/0bfaff75-e19b-43d4-8cfe-2ed621d15893 — read that artifact first (Artifact tool, action "read") to pull its exact HTML/CSS, then reuse its structure with today's data: header (date + 24h window stated in Eastern time), client status strip (chips with status pill, new/open/oldest-age counts), the Developer Priorities table, then per-client cards ordered worst-health-first, each with: rationale sentence, stat line, "received today" table, "dormant/needs attention" table, and a full ticket detail table with Recurrence and Age columns. Keep the same tokens/palette/typography — this is a recurring report and should look identical day to day, only the data changes.

11. Send the report by email using the Gmail connector: from the authenticated ronn@eoxs.com account, to ronn@eoxs.com, subject "EOXS Support — Daily Client Health Report — <today's date, e.g. Aug 27 2026>". Pass the full built HTML as htmlBody (inline all CSS, no external assets other than Google Fonts links if used) and a short plain-text version as body (client health one-liners + the developer priorities list only, so it's readable if HTML fails to render).

12. If the Teams_eoxs query fails or the board is unreachable, don't stay silent — send a short plain-text email to ronn@eoxs.com from ronn@eoxs.com explaining what failed instead of the full report.

## Assistant

[Loaded raj-eoxs-vault and threads-ov skills per standing preference. Attempted to read the reference artifact via Artifact tool action "read" — failed: the session's network allowlist blocks *.frame.claudeusercontent.com and the gateway read path was unavailable for this artifact. Proceeded to build the report to the brief's spec instead of pixel-matching the unreachable reference, noting this in the report footer.]

[Queried Teams_eoxs (EOXS Teams Live, Odoo) via get_business_schema/describe_table/query tools:
- Confirmed project_task, project_task_type, res_partner, res_users schemas.
- Ran a stage-distribution GROUP BY for project_id=76, active=true: Paid 1383, Communicated 396, Need Developer 16, Tickets 4 (fluctuated to 1 on re-check — live board), Assigned 3, Waiting for Client's Reply 2, Approved 2, Ready for Live 1, QA 1.
- Pulled two consistent snapshots: (a) all tickets currently in the 6 tracked stages (24 rows) with full descriptions, and (b) all tickets created since 2026-08-25 22:00 UTC (6:00 PM ET previous day) — 15 rows — to compute the new-tickets window and flag same-day moves out of tracked stages.
- Computed age and stage-age in days for each of the 24 open tracked tickets via a small Python script against a fixed "now" of 2026-08-26 22:00 UTC (6:00 PM ET report send time).]

Findings:

**New tickets in the 24h window (15 total):** 1 still open in a tracked stage (#7836, Discount Pipe & Steel, Tickets — a $3,569 payment-received notification). 14 moved/resolved same day: 5 for Sabre Alloys (#7837, #7827, #7822, #7821, #7820 — all moved to Communicated or Resolved) and 9 for Discount Pipe & Steel (#7833, #7832, #7831, #7830, #7829, #7828, #7826, #7825, #7819 — moved to Communicated or Resolved).

**24 tickets currently open in tracked stages**, broken down by client: PPC Specialty Metals 5, Sabre Alloys 7, 3GM Steel 2, Eastern States Steel 2, Greer Steel Company 2, Discount Pipe & Steel 5 (including #7836 from today's window). One ticket, #6891 ("Develop Client Support Module with Call Scheduling," Assigned, 131 days old, assigned to Ron), has no partner_id and no client identifiable from its description — it reads as an internal product initiative, not a client ticket, so it was excluded from client-level counts and flagged in the report footer as a data-quality note.

**Recurring patterns / regressions detected:**
- Discount Pipe & Steel: an active regression on packing-list/transfer processing (theoretical-weight error, manual-reserve failure) surfaced across at least 5 tickets in one day (#7826, #7829, #7830, #7831, #7833), with the client explicitly saying "this error again" (x2) and "I hope the new update from last week didn't mess something up with that fix" — a direct reference to a previously-completed fix regressing. A separate SO "stage" bug (#7523) was also flagged by the client as "still occurring."
- Sabre Alloys: a receiving-by-foot-instead-of-piece defect inflating price and cutting GP appeared twice same-day with identical wording (#7837, #7827), alongside three same-day inventory-adjustment GL correction requests (#7822, #7821, #7820) likely downstream of the same root cause. Separately, Ron himself flagged a payment-terms bug (invoices auto-resetting NET60 accounts to NET30) as needing a system-wide fix 34 days ago (#7495) — still open.
- 3GM Steel: a "no results to show" coil-add bug recurs across two tickets 79 days apart (#6692, 148 days old; #7312, 69 days old), with the more recent instance carrying explicit revenue/time urgency (11 loads blocked, customer payment terms tied to invoicing).
- PPC Specialty Metals: no recurring bug detected, but the worst backlog age of any client — all 5 open tickets have sat in Need Developer 53–176 days with no forward movement. One (#6476) references a prior "disappearing tags" issue that was supposedly already fixed.
- Eastern States Steel: a completed dev fix (#6976, control-tag width-mapping) has been stuck in QA for 63 days — a pure bottleneck, not a dev-capacity issue.
- Greer Steel Company: two routine, low-urgency feature/customization requests, no recurrence, no urgency language.

**Health calls:** Sabre Alloys — Critical (systemic UOM/GP defect, Ron-flagged systemic payment-terms bug still open, 168-day-old oldest ticket, 133-day-old high-priority infra ask). Discount Pipe & Steel — Critical (active regression hitting fulfillment operations 5x in one day, explicit client repeat-language). 3GM Steel — Watch (recurring bug with revenue urgency but low volume). PPC Specialty Metals — Watch (no recurrence/urgency but worst backlog age, 5 tickets 53–176 days stale). Eastern States Steel — Watch (fix stuck in QA 63 days). Greer Steel Company — Stable (routine, low-severity backlog only).

**Developer priorities built (6 items):** (1) DPS packing-list/transfer regression root-cause (#7830/#7833/#7831/#7829/#7826), (2) Sabre receiving-UOM/GP defect (#7837/#7827), (3) Sabre systemic payment-terms fix (#7495), (4) Eastern States Steel QA-stuck fix (#6976), (5) 3GM Steel recurring coil bug with revenue urgency (#7312), (6) DPS SO-stage bug flagged as "still occurring" (#7523).

Built the full HTML report (header, client status strip with status-pill chips, Developer Priorities table, six per-client cards ordered worst-health-first — Sabre, DPS, 3GM, PPC, Eastern States, Greer — each with rationale sentence, stat line, received-today table, dormant/needs-attention table [30+ days in current stage], and a full ticket-detail table with Age and Recurrence columns), plus a plain-text fallback (client health one-liners + developer priorities list). Footer notes: scope/stage definitions, the #6891 data-quality gap, the unreachable reference-artifact caveat, and a live-data snapshot caveat (the board changed stage under us mid-query, confirming it's actively worked in near-real-time by SupportAI/agents).

Sent the email via Gmail send_message: from the authenticated ronn@eoxs.com account, to ronn@eoxs.com, subject "EOXS Support — Daily Client Health Report — Aug 26 2026", htmlBody = full report, body = plain-text summary. Send succeeded (message id 1a0403a3190d100f).
