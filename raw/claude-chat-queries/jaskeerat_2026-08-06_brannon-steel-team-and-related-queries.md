---
thread_name: "brannon-steel-team-and-related-queries"
user: "jaskeerat"
type: claude-chat
created: 2026-08-06
updated: 2026-08-06
---

# Chat Transcript: Brannon Steel Team & Related Vault Queries

**User:** Ankit Pachauri

---

**User:** Hey cruz how are you?
**Assistant:** (Introduced self as doing well, ready to help with vault queries.)

**User:** hey cruz what are you actually?
**Assistant:** Explained: Cruz is an AI assistant wired into EOXS's internal vault (emails, call transcripts, client records, invoices, tickets, wiki), synthesizing answers from real data with citations, not a generic chatbot.

**User:** Tell me something about this ticket number T07567
**Assistant:** Searched get_ticket and search_tickets for T07567, 07567, 7567, T7567 — no matches found in vault.

**User:** tell me something about this ticket number T06699
**Assistant:** Found: Ticket T06699 — Sabre Alloys, Subject "SO - 19752", Status Paid, assigned to Hashir Saleem, created 2026-04-01, closed 2026-07-28. Description: investigate why order stuck in "to invoice" status, suspected FRT (freight) line issue. No events/attachments logged.

**User:** how much is it paid?
**Assistant:** Could not find exact dollar amount for SO 19752 specifically. Searched invoices, wiki, emails for "19752" — no matches. Sabre Alloys' invoice history uses S00XXX numbering, not matching the "19752" ID in ticket. Noted EOXS Team Live DB (queryable) is EOXS's own instance, not Sabre Alloys' separate Odoo instance (sabre.eoxs.com), so direct DB query also came up empty.

**User:** Hiren and EOXS what this call is all about?
**Assistant:** Found 3 calls with "Hiren" (Hiren Jungi, Pragtech — hiren.jungi@pragtech.co.in): 2022-08-29 "Hiren" (13min), 2022-09-21 "Hiren" (17min), 2022-09-21 "Shubham and Hiren" (12min). All hosted by Rajat. All three have EMPTY transcript bodies (just title, no dialogue/summary/topics/action items captured).

**User:** can i have the transcript of this call?
**Assistant:** Confirmed no transcripts exist for any of the 3 Hiren calls — provided Fireflies recording URLs as alternative (bDFEIt5RdJ, QveXmCC0eB, d50O5yvks9).

**User:** Telll me about this call Robert Dunn and EOXS
**Assistant:** Found 13 calls titled "Robert Dunn and EOXS" (Jan 2024–Jan 2025) — a recurring weekly series. Pulled full details of most recent (2025-01-17, 7 min): Robert Dunn (rdunn@hiec.com, Stanford GSB alumni) — small talk about Colorado/Bay Area/Toronto weather, SoCal wildfires; call derailed when Raj apologized for being late (sick son) and rescheduled with Rajan for following week. Confirmed by Robert as "standing weekly call." Key topics: EOXS, product support, implementation, Colorado, California, rescheduling. Action item: Rajan to reschedule.

**User:** what this call is all about and i need a proper insight of this call even end to end description of this call
**Assistant:** Provided full end-to-end narrative breakdown of the Jan 17, 2025 Robert Dunn call in 6 acts: awkward open, introductions, confusion about who's on call, small talk (geography/weather/career background), current events tangent (wildfires), call derails and reschedules. Assessed: zero substantive business content, entirely relationship-maintenance chat cut short by personal emergency.

**User:** what this call is all about and i need a proper insight... Prakash Walthare and EOXS
**Assistant:** Searched extensively — NO call transcript exists for "Prakash Walthare and EOXS." Found only 2 calendar invite emails (raj_gmail and ron_gmail, both dated 2023-08-16) for a meeting scheduled Mon Aug 21, 2023, 12:00-12:30pm EDT (Toronto). No agenda, no transcript, no follow-up found. Checked list_calls for Aug 2023 (full month) — no matching entry. Wiki search found one indirect reference confirming this was an unremarkable calendar accept with "no substantive body text." Could not identify who Prakash Walthare is (role/company) — not a listed client contact.

**User:** what is the invoice about? INV/2025/0005
**Assistant:** Found via direct DB query (account_move table): INV/2025/0005 — Sabre Alloys, invoice date 2025-01-06, total $9,360.00, fully paid (amount_residual $0.00), posted, out_invoice. Line items: License Charges (0 qty/$0), License Charges - Dec (24 units × $425 = $8,160), Server Upgrade (1 × $1,200). Total $9,360. Assessed as routine monthly EOXS platform billing to Sabre Alloys.

**User:** what is the july month progress report of Jaskeerat Singh?
**Assistant:** Compiled from productivity monitoring emails + 1 call (no single formal "progress report" doc exists):
- Jul 21, 2026 email: flagged low productivity Mon 13 Jul & Thu 16 Jul. Rajat personally replied: "Jaskeerat, I have big hopes from you. I hope you will not disappoint. R."
- Jul 27, 2026 email: flagged low productivity Mon 20 Jul & Tue 21 Jul. Jaskeerat responded: was doing research/analysis + QA for Brannon (used phone to compare values, less keyboard/mouse activity); committed to using laptop more.
- Same productivity-flag template also sent to Ayan Dutta (Jul 27, flagging Jul 23) — team-wide pattern, not unique to Jaskeerat.
- July 31, 2026 Fathom call ("Impromptu Zoom Meeting," 1h23m): Jaskeerat actively involved in Odoo/O2-13 deployment work (frontend), admin/permission config, API cost discussion (Claude/API usage costed $20-23 so far), tied to Brannon Steel MTR AI work (referenced Brannon Steel MTR Samples task thread — scan-orientation extraction bug, flagged Jul 16, 2026, still unresolved).
- No formal "progress report" document found in vault searches.

**User:** How much is the incentive does jaskeerat get on brannon?
**Assistant:** IMPORTANT CORRECTION: The ₹10,000 incentive found in vault ("Incentive for Brannon upsell and Cold call conversion," email dated 2026-07-28, raj_gmail) belongs to **Ayan Dutta**, NOT Jaskeerat Singh. Found via Collier Metals wiki page cross-reference. No incentive record exists anywhere for Jaskeerat Singh tied to Brannon Steel — searched emails, wiki, calls extensively. Jaskeerat's role on Brannon is operational/QA (MTR Samples task thread, scan bug fixes), distinct from Ayan Dutta's sales/upsell incentive role. Also found unrelated David Brannon (batch-12 email archive) — a different person/prospect from SMU trade show, NOT Brannon Steel the client — flagged as a false-lead distinction.

**User:** how many people have worked in brannon steel project?
**Assistant:** Compiled from Brannon Steel entity page, CRM Record, Implementation Huddles (Jun 2026 + Mar-Jun 2026 call log), MTR Samples Task Thread, Ticket T06332:

Confirmed EOXS team members on Brannon Steel:
1. **Rajat Jain (Raj)** — sales lead, met David Brannon at SMU Steel Summit Sept 2025, EOXS Account Owner
2. **Scott Begin** — salesperson, closed deal Jan 20, 2026
3. **Ayan Dutta ("Ayaan")** — core implementation, Nov 11 2025 scoping call, owns Ticket T06332 (MTR Inventory Module, QA Passed), June 2026 huddles
4. **Jaskeerat Singh** — implementation/data-analyst, QA on MTR samples, flagged scan-orientation bug Jul 16 2026

Ambiguous/unresolved mentions:
- "Kirat" and "Nasker" — named in June 2026 huddles alongside Ayaan, possibly aliases (Kirat could = Jaskeerat) — not confirmed
- deepaksaxena192837@gmail.com — appears in Mar-Jun 2026 call log archive but role/affiliation explicitly flagged as unverified/unidentified in the wiki

Client-side (Brannon Steel) contacts for context: David Brannon (Owner), Kevin Brannon (K.R.), Manish Trivedi (Head of Ops/tech lead), Ranim/Raneem Fallaha (APQP Manager, primary tester), plus unnamed team members (Sean, Farin, CAD operators).

Assessment: 4 confirmed EOXS individuals by name, with caveat that most June 2026 huddle transcripts (13 of 14) were metadata-only with no actual dialogue captured, so additional attendees may exist undocumented by name. Offered to dig further into "Kirat"/"Nasker" aliases if needed.

**User:** Daily Team Work Summary for EOXS
**Assistant:** Compiled from most recent vault data (current date: Aug 6, 2026). No single formal "daily summary" document exists — reconstructed from emails, calls, and implementation task backlog for Aug 1-5, 2026:

CALLS:
- Aug 5: "Training the new sales person" (Ron J + Folabi Odunaiya, new AE hire) — substantive sales training call covering ERP vs CRM basics, AI value prop demo using Eastern Steel Sales as example (4-second data synthesis pitch)
- Aug 3: Three internal calls (KPI on Build Team, Update on this explanation, EOXS google presence) between Rajat/Ron/Sheenam — all with empty transcripts (title only)
- Aug 1-3: Recurring "Zoom link" calls (Rajat + rajat@prata.ca) — no transcripts
- Aug 3: Yoga Class - Kids (personal, non-work)

EMAILS:
- Aug 1: Hashir Saleem status update to Rajat — Sabre Iris Testing completed (210 questions verified), Banking Reports Excel bug fixed for Sabre Alloys/Juan
- Aug 1: New Seat request from Discount Pipe & Steel (Austin Rayzor) — Spencer Graves license added, completed same day
- Aug 3: Ex-Employment Verification request (Akshay Raina, from Macronix HR)
- Aug 1: SMU Steel Summit related emails, Brainstorming session invite for Aug 6

IMPLEMENTATION BACKLOG (standing snapshot, not day-specific):
- Discount Pipe & Steel: ~60 active tasks, most owned by Amy Rayzor/Tina Valdez (requirements stage) and Hashir Saleem/Dhrup/Nijamuddin (dev/QA stages). Advanced items: "No. of Pcs discrepancy" (In Developer Review), "Sales Order Status Not Updating" (Code QA), "Unable to Confirm Packing List" (DPS Sandbox Review, High priority)
- Eastern States Steel: ~13 active tasks. Most advanced: "Processing Error" (On Live, Deepak Shandilya)

Assessment: Aug 5 most substantive day (sales training); Aug 1 showed two closed-loop wins (Sabre Iris testing + DPS license provisioning); Discount Pipe & Steel is the most active client engagement based on backlog volume. No per-person daily standup log exists in vault.

## Key Vault Facts Established
- Brannon Steel: EOXS's first Canadian client (Brampton, Ontario) and first non-ERP AI-only engagement (MTR AI product). Won Jan 20, 2026. Implementation fee $14,400 CAD one-time + $1,240 CAD/month (~$927 USD). Legacy ERP: Microsoft Business Central. Contract flagged with contradictions (3-year vs 1-year term; monthly billing not matching invoices).
- Sabre Alloys: long-running client with regular monthly EOXS licensing invoices (~$425/seat).
- Jaskeerat Singh and Ayan Dutta are both EOXS team members working on Brannon Steel, in different capacities (technical/QA vs. sales/incentive).
- Discount Pipe & Steel and Eastern States Steel are currently the most active implementation clients by open task volume (as of Aug 2026 snapshot).
- Current vault "present" date context: Aug 6, 2026.
