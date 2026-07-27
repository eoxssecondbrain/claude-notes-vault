---
thread_name: "eoxs-sales-team-weekly-performance"
user: "raj"
type: claude-chat
created: 2026-07-27
updated: 2026-07-27
---

User: what is the weekly performance of eoxs team

Claude: [asked clarifying questions via ask_user_input_v0 - scope (dev/sales/interns/whole company) and week definition]

User: Sales team (pipeline movement, calls, deals worked this week) / This current week (in progress)

Claude: [offered rigor levels 5ft/10ft/50ft deep]

User: 10ft

Claude: [Read threads-ov and raj-eoxs-vault skills at thread start per user preference. Read sales-strategist skill since query touches pipeline motion. Queried EOXS Teams Live (crm_lead, crm_phonecall, sale_order, res_partner, res_users) and OV2 (list_calls) for July 2026.]

Findings:
- crm_lead: zero new leads, zero stage changes, zero record touches since Jul 27 (start of this week). More significantly, CRM's last genuine write_date/create_date touch across the whole table was Jul 15, 2026 - a ~12 day dormancy window predating this week.
- crm_phonecall table dead since 2022 - not a real call log.
- Cross-checked against OV2 Fireflies calls (list_calls month=2026-07): real sales conversations ARE happening in the trailing 2 weeks but not logged as CRM stage moves - Jul 17 Lawrence/Rajat, Jul 20 Collier Metals (MTR AI), Jul 21 Rob Coppens/Raj Taylor Steel discovery call, Jul 21 Robert/Claudia/Raj intro call, Jul 22 Jon and EOXS, Jul 23 Sabre inventory QA (implementation not sales).
- Only system activity logged today (Jul 27): 4 draft sale_order quotes (S00204-S00207) + 1 confirmed order (S00203, Jul 22, Brannon Steel $1,356), against existing clients (Sabre, Discount Pipe & Steel, PPC Speciality Metals, Eastern Steel Sales, Brannon Steel), created by Humaira Zainab and Ayan Dutta (implementation/ops staff) - existing-client billing/renewal quotes, NOT new-pipeline AE sales activity.
- Flagged risk: CRM has no reliable current pipeline visibility - real deal conversations aren't being logged as stage updates. This compounds the previously-known issue (from memory: 260-opportunity sweep found CRM stage names unreliable) - the gap isn't just naming inaccuracy, it's non-logging entirely. Raised open question of whether reps should log stage moves themselves or someone reconciles Fireflies calls into CRM weekly.

Sources cited: EOXS Teams Live (crm_lead, crm_phonecall, sale_order tables, live query Jul 27 2026) and OV2 list_calls (2026-07).

## Tribal Knowledge Extracted
- EOXS's internal Odoo CRM (crm_lead) has been effectively dormant for stage/lead updates since ~Jul 15, 2026, despite real sales calls continuing (Taylor Steel/Rob Coppens, Collier Metals, etc. in the following week) - meaning Fireflies call transcripts are currently a more accurate signal of live sales activity than the CRM itself.
- crm_phonecall table is legacy/unused (last touch 2022) - not a real data source for call activity, despite being a plausibly-named table.
- Sale orders created by Humaira Zainab and Ayan Dutta are existing-client billing/renewal quotes, not new-business AE pipeline - useful disambiguator for future "sales activity" queries against EOXS Teams Live sale_order table.

## Candidate OV2 Cross-References
- EOXS CRM data hygiene / stage-logging gap - could be relevant to an existing OV2 page on CRM audit / pipeline analysis (the 260-opportunity sweep, 4% hit rate) if one exists, as this extends that finding with a live dormancy data point.
