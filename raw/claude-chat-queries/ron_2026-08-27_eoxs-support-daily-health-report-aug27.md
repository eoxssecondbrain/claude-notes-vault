---
thread_name: "eoxs-support-daily-health-report-aug27"
user: "ron"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

User: Run the EOXS Support daily health report and email it. This is a fully autonomous scheduled run — do not ask clarifying questions or wait for approval, just build and send the report.

1. Query the Teams_eoxs connector (EOXS Teams Live, Odoo): project_task where project_id = 76 (the "EOXS Support" project) and active = true. Join to project_task_type for stage name, res_partner (via partner_id) for client, res_users/res_partner for assignee.

2. Tracked open stages ONLY: Tickets, Assigned, Waiting for Client's Reply, Need Developer, QA, Ready for Live. Exclude Communicated, Paid, Approved entirely — those do not count as open, per standing instruction.

3. New-tickets window: tickets created in the trailing 24 hours ending at this run's send time (6:00 PM Eastern), i.e. since 6:00 PM Eastern the previous day. Among those, separately flag which have already moved out of the 6 tracked stages within that same window (e.g. into Communicated) — report those as "moved/resolved same day," not as still open.

4. For every ticket currently sitting in the 6 tracked stages (regardless of age), pull id, name, client, stage, create_date, date_last_stage_update, and full description. Compute age = now − create_date, and time in current stage = now − date_last_stage_update.

5. Strip HTML from each description and read it to understand what the ticket is actually about, in plain language — not the raw subject line.

6. Detect recurring patterns: within each client's tickets (open and newly created), find tickets that are the same underlying issue recurring — same error, same bug class, same complaint. Note how many instances, since when (date of the earliest instance), and whether the client's own words signal a repeat ("this error again," "still occurring," "happened before"). Flag any regression where a description references a fix that was supposedly already completed.

7. Assign each client a health status — Critical (red) / Watch (yellow) / Stable (green) — based on: presence of a recurring/systemic bug, explicit client-stated urgency or financial/revenue impact, backlog age, and open-ticket volume. Write one sentence of rationale per client explaining the call, not just a number.

8. Build a ranked "Developer priorities — work these today" list (roughly 5-6 items) across all clients: tickets that should be worked today specifically because they're financially/revenue-impactful, recurring/systemic (fixing root cause helps multiple tickets), explicitly time-sensitive per the client, or a fix that's built but stuck in a non-dev bottleneck (e.g. sitting in QA) and just needs pushing through. For each: ticket, client, what needs doing, why today, and who it's currently assigned to (or "Unassigned").

9. Data-quality check: for any ticket with no client (partner_id) tagged in Odoo, check whether the description content identifies a client anyway (e.g. an email signature "Sent by <Client> L.P."). If so, attribute it to that client in the report and note the tagging gap in the footer.

10. Build the report reusing the same visual format used on prior days' runs (or the reference artifact at https://claude.ai/code/artifact/0bfaff75-e19b-43d4-8cfe-2ed621d15893 if reachable): header (date + 24h window stated in Eastern time), client status strip (chips with status pill, new/open/oldest-age counts), the Developer Priorities table, then per-client cards ordered worst-health-first, each with: rationale sentence, stat line, "received today" table, "dormant/needs attention" table, and a full ticket detail table with Recurrence and Age columns. Keep the same tokens/palette/typography — this is a recurring report and should look identical day to day, only the data changes.

11. Delivery format: build the report as a standalone HTML document, then convert it to a PDF (use the pdf skill) so it opens as a proper document rather than a rendered email body. Send the email via the Gmail connector: from the authenticated ronn@eoxs.com account, to ronn@eoxs.com, subject "EOXS Support — Daily Client Health Report — <today's date, e.g. Aug 27 2026>". Keep the email body itself SHORT — a few sentences covering the client health one-liners and the developer priorities list only, nothing more — and attach the full PDF report as the actual document (base64-encoded in the attachments field, filename like "EOXS_Support_Daily_Health_Report_2026-08-27.pdf"). Do not put the full HTML report in htmlBody anymore; htmlBody can mirror the short plain-text body, or be omitted.

12. If the Teams_eoxs query fails or the board is unreachable, don't stay silent — send a short plain-text email to ronn@eoxs.com from ronn@eoxs.com explaining what failed instead of the full report.

Assistant: [Queried EOXS Teams Live (Odoo) via Teams_eoxs connector for project_task where project_id=76, active=true, joined to project_task_type/res_partner/res_users. Found 25 open tickets across 6 tracked stages (Tickets, Assigned, Waiting for Client's Reply, Need Developer, QA, Ready for Live) and 9 tickets created in the trailing 24h window (Aug 26 6pm ET - Aug 27 6pm ET), of which 2 remained open and 7 moved to Communicated/Paid/Need Discussion same-day.

Built a full daily client health report covering 6 clients:
- Discount Pipe & Steel — CRITICAL (5 open, 1 new, 62d oldest). Highest same-day ticket churn, a reservation bug that already caused a real stock-out sale (#7366), and repeat language across 3 tickets ("this error again", "still occurring", "aren't linking properly again").
- 3GM Steel — CRITICAL (2 open, 149d oldest, 97d longest no-touch). Same "no results to show" coil-ID bug on #6692 and #7312, 5 months unresolved, client ties it to getting paid.
- PPC Speciality Metals — CRITICAL (5 open, 177d oldest). Oldest backlog of any client, confirmed regression on #6476 (client says a previously "completed" fix broke again), plus unresolved sales-tax and P&L financial-accuracy bugs.
- Sabre Alloys — WATCH (7 open, 169d oldest). Highest ticket volume, a genuine financial/AR bug (#7495 payment terms auto-resetting NET60->NET30), but mostly single-instance feature work otherwise.
- Eastern States Steel — WATCH (3 open, 1 new, 120d oldest). A completed fix (#6976) sitting in QA 64 days; new printer connectivity ticket today.
- Greer Steel Company — STABLE (2 open, 105d oldest). Only feature requests, no urgency, though unassigned to a human for 3+ months.

Developer priorities (ranked): 1) DPS reservation bug #7366/#7845 (revenue-impactful, recurring). 2) 3GM coil bug #6692/#7312 (recurring, revenue-tied urgency). 3) ESS QA-stuck fix #6976 (bottleneck, needs push not new dev). 4) Sabre payment-terms bug #7495 (AR/financial risk). 5) Sabre Ready-for-Live fix #7035 (bottleneck, cheap win). 6) PPC tag-disappearance regression #6476 (confirmed regression, reopen and reassign).

Data-quality note: ticket #6891 has no partner_id tagged but its content describes an internal cross-client initiative, not a specific client issue, so it was excluded from per-client analysis rather than mis-attributed (footnoted in the report).

Built the report as HTML (attempted Chromium/weasyprint rendering, then switched to a reportlab-based PDF for a much smaller file size to make the email attachment transcription reliable), verified the PDF opens correctly as a 5-page document (pdftotext/pikepdf checks passed), and sent the email via Gmail (mcp__Gmail__send_message) from ronn@eoxs.com to ronn@eoxs.com, subject "EOXS Support — Daily Client Health Report — Aug 27 2026", with a short plain-text body summarizing client health one-liners and developer priorities, and the full PDF attached (base64-encoded, filename EOXS_Support_Daily_Client_Health_Report_2026-08-27.pdf). Confirmed send success (message id 1a0458033434a507, sizeEstimate 32441 bytes consistent with a properly-attached ~20KB PDF).]
