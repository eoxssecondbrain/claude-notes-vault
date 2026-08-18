---
title: "EOXS Revenue & Financial Health Snapshots"
type: chat-summary
sources: [raw/claude-chat-queries/raj_2026-07-31_2026-revenue-monthly-lookup.md, raw/claude-chat-queries/raj_2026-07-31_sales-numbers-3yr-analysis.md, raw/claude-chat-queries/raj_2026-08-06_eoxs-payroll-salary-benchmark.md, raw/claude-chat-queries/raj_2026-07-29_eoxs-business-health-view-5ft.md, raw/claude-chat-queries/raj_2026-07-27_eoxs-sales-team-weekly-performance.md, raw/claude-chat-queries/raj_2026-07-29_eoxs-recent-news-5ft.md, raw/claude-chat-queries/raj_2026-07-29_eoxs-prospect-list.md]
created: 2026-07-27
updated: 2026-08-06
---

# EOXS Revenue & Financial Health Snapshots

_Seven Raj-initiated conversations (Jul 27–Aug 6, 2026) pulling EOXS's revenue, sales pipeline, payroll structure, and overall business-health picture against the $1M ARR goal._

## Summary

Across late July and early August 2026, Raj repeatedly probed EOXS's financial trajectory from different angles, and the numbers converge on a consistent story: revenue is real but flat-to-stalling, growth is not organic, and one client's unpaid AR is quietly inflating the headline 2026 number.

The **monthly lookup** (Jul 31) established 2026 posted revenue Jan–Jul at **$243,080.80** net (7 months, ~$35K/month average), against an implied $83K/month pace needed for $1M ARR — roughly 42% of target pace. April ($6,606) and June ($11,170) were dragged down by credit notes, not just low invoicing.

The **3-year deep-dive** (also Jul 31, same day, 50ft depth) refined this using gross vs. net figures and added trailing-12-month framing: TTM revenue (Aug 2025–Jul 2026) is **$391,288**, only marginally above calendar-2025's $374,750 — meaning growth has effectively stalled. Revenue by year: 2023 $80,511 (6 invoices), 2024 $265,640 (+230% YoY), 2025 $374,750 (+41% YoY), 2026 YTD $267,926 gross / $240,702 net. New-logo velocity collapsed from 6 new paying clients in 2025 to just 1 (Brannon Steel) in 2026 YTD. Two 2025 logos — R W Conklin and Bri-Steel — have gone dormant (no invoices since Mar/Jul 2025) and aren't being tracked as churn anywhere. Most critically: **Brannon Steel has never paid a single invoice** — all 8 invoices since Jan 7, 2026 are unpaid, $55,239 outstanding (~7 months overdue) — meaning real cash-basis 2026 revenue is closer to **$215K than the reported $268K**.

The **business-health view** (Jul 29, 5ft) sized the active client base independently via OV2 wiki data: ~$27K/month MRR across 8 clients (~$324K annualized), with 3 of the 5 biggest accounts (Sabre, Discount Pipe & Steel, PPC Metals) flagged HIGH churn risk in the vault — meaning ~60% of MRR sits in structurally at-risk accounts.

The **sales-team weekly-performance check** (Jul 27, 10ft) found the CRM (`crm_lead`) had gone dormant for stage/lead updates since ~Jul 15 despite real sales calls continuing in parallel (Taylor Steel, Collier Metals, etc.), and that `crm_phonecall` is a dead legacy table (last touch 2022). The only system activity that week was billing/renewal quotes against existing clients, not new-pipeline activity.

The **prospect-list conversation** (Jul 29) quantified CRM data quality directly: 252 total opportunities, ~196 "active," but 60-70% show $0 expected_revenue and haven't had a stage update since 2025 or earlier despite being flagged active — confirming the CRM is not a reliable pipeline signal. The same thread pulled the current ~60-person active-user roster (core staff, sales, dev, plus ~20 recent adds from the 50-person MBA intern cohort) and a "positive points" / "facts" rundown reiterating the 9-client base, Mucker Capital's $350K across 3 tranches (~12.16% equity), and founder salaries still deferred as of Jul 2026.

The **recent-news check** (Jul 29, 5ft) found no genuine external press/news cycle on EOXS — only stale directory listings and an old Crunchbase entry — confirming that anything "recent" about EOXS lives only in internal vault data, not public record.

The **payroll benchmark research** (Aug 6, 50ft) is adjacent but directly relevant to financial health: it reconstructed EOXS's India payroll structure from Isha Bisht's recurring monthly digest emails (confirmed recurring since at least Sep 2025) plus scattered payslips/offer letters, producing a 6-level (L0–L5) compensation benchmark grid with fixed-base ranges, bonus structure, and standard contractual terms (non-compete, notice, bond/forfeiture, arbitration venue) per level.

## Tribal Knowledge Extracted
- **"5ft / 10ft / 50ft" as a standing depth-of-research vocabulary** — used across every thread in this cluster as shorthand for research rigor: 5ft = single-source quick read, 10ft = cross-verified against raw records, 50ft = deep with trend drivers/risks/blind spots. Not an EOXS business term but an established convention for how Raj scopes every analysis request. (source: raj_2026-07-31_sales-numbers-3yr-analysis.md; raj_2026-07-29_eoxs-business-health-view-5ft.md; raj_2026-07-27_eoxs-sales-team-weekly-performance.md; raj_2026-07-29_eoxs-prospect-list.md)
- **crm_lead "won" stage is not usable as a source of truth for deal count.** It shows only 1 won deal in 2024, 3 in 2025, 1 in 2026 YTD — wildly undercounting versus invoice-ledger ground truth. The correct workaround, discovered in this thread, is to derive new-client count from first-invoice date per client instead of CRM stage. (source: raj_2026-07-31_sales-numbers-3yr-analysis.md)
- **crm_phonecall is a dead/legacy table** (last touch 2022) — despite the plausible name, it is not a real call-activity source; Fireflies call transcripts (via OV2 `list_calls`) are the actual signal for live sales activity, and as of this thread are more accurate than the CRM itself. (source: raj_2026-07-27_eoxs-sales-team-weekly-performance.md)
- **Sale orders created by Humaira Zainab and Ayan Dutta are existing-client billing/renewal quotes, not new-business AE pipeline** — an undocumented disambiguation rule needed to correctly read the `sale_order` table in EOXS Teams Live; without it, renewal billing activity looks like new sales motion. (source: raj_2026-07-27_eoxs-sales-team-weekly-performance.md)
- **CRM `expected_revenue` field is unreliable as a pipeline-value indicator** — 60-70% of the 196 "active" opportunities show $0, and most haven't had a stage update since 2025 or earlier despite being flagged active=true. Any pipeline-value read must filter for genuinely populated, recently-touched records only. (source: raj_2026-07-29_eoxs-prospect-list.md)
- **Isha Bisht's monthly payroll digest email (subject pattern like "<Month> Excel Sheet", attachment only, no body text) is the standing/recurring payroll record-of-truth**, confirmed recurring back to at least Sep 2025 — but the vault's email tools can read email text, not attachment binaries, so the digest itself can't be opened directly; the workaround is reconstructing compensation from payslips, signed offer letters, and payroll-thread comments instead. (source: raj_2026-08-06_eoxs-payroll-salary-benchmark.md)
- **The "Misc Earning/Bonus" payroll line has no documented formula** — three Software Developers hired the same day, same fixed base (₹13,000 total), show bonus swings from ₹5,000 to ₹26,300 across different months with nothing on record explaining the variance. Flagged as the single biggest obstacle to fair salary benchmarking from EOXS's own records. (source: raj_2026-08-06_eoxs-payroll-salary-benchmark.md)
- **Interns get a 1-year non-compete; full-time employees get 5 years** — an initial research pass conflated these before being corrected mid-thread; the 5-year term is FTE-specific only. (source: raj_2026-08-06_eoxs-payroll-salary-benchmark.md)
- **Intern-to-FTE conversion carries a 2-year bond with a ₹40,000 early-exit penalty, plus a deferred ₹5,000/month accrual forfeited entirely if the employee leaves before one year** — an undocumented-outside-contracts retention mechanism standard across junior hires. (source: raj_2026-08-06_eoxs-payroll-salary-benchmark.md)
- **Dhrup Kumar Singh's comp is contractually locked to a long-horizon ladder**: ₹60k/mo (2024) → ₹80,000/mo (2026, per signed contract) → ₹90,000/mo "fixed and non-negotiable" from 2027 — directly relevant context since his raise review was open at the time of this thread. (source: raj_2026-08-06_eoxs-payroll-salary-benchmark.md)
- **Founder salaries (Raj, Ron, Ayan) are deferred until financial health warrants paying them** — all three unpaid as of Jul 2026, a fact not otherwise documented. (source: raj_2026-07-29_eoxs-prospect-list.md)

## Key Points
- 2026 posted revenue Jan–Jul: $243,080.80 net (Jan $74,491, Feb $20,160, Mar $45,244, Apr $6,606, May $55,898, Jun $11,170, Jul $29,511). (raj_2026-07-31_2026-revenue-monthly-lookup.md)
- Trailing-12-month revenue (Aug 2025–Jul 2026): $391,288 across 71 invoices — ~39% of the $1M ARR/12mo goal. (raj_2026-07-31_sales-numbers-3yr-analysis.md)
- Yearly revenue: 2023 $80,511 → 2024 $265,640 (+230%) → 2025 $374,750 (+41%) → 2026 YTD $267,926 gross / $240,702 net. (raj_2026-07-31_sales-numbers-3yr-analysis.md)
- New paying clients by year: 2023: 1 (Morgan Hauser Steel, churned after 1 invoice); 2024: 2 (Sabre Alloys, Greer Steel); 2025: 6 (R W Conklin, Bri-Steel, Hansen Metallurgical, Discount Pipe & Steel, Eastern Steel Sales, PPC Speciality Metals); 2026 YTD: 1 (Brannon Steel). (raj_2026-07-31_sales-numbers-3yr-analysis.md)
- Brannon Steel: 8 invoices since Jan 7, 2026, $55,239 outstanding, none paid, ~7 months overdue as of Jul 31, 2026. (raj_2026-07-31_sales-numbers-3yr-analysis.md)
- 2026 total AR outstanding: $90,063 across 13 unpaid invoices; 2023-2025 collection history was 100% paid with zero residual. (raj_2026-07-31_sales-numbers-3yr-analysis.md)
- Active MRR snapshot (Jul 29, per OV2 wiki): ~$27K/month across 8 clients (~$324K annualized) — Sabre Alloys ~$10,970 (HIGH risk), 3GM Steel $4,759 (LOW risk), Discount Pipe & Steel $3,120 (HIGH risk), PPC Metals ~$2,750 (HIGH risk), Eastern States Steel ~$2,340 (MEDIUM risk), Ohio Strip/Greer $1,713, Brannon Steel ~$927, RW Conklin $450. (raj_2026-07-29_eoxs-business-health-view-5ft.md)
- CRM pipeline: 1,952 of ~2,400 active leads sit in one dead/unqualified stage; real distributed pipeline is a few hundred leads. (raj_2026-07-29_eoxs-business-health-view-5ft.md)
- Sales-team check (week of Jul 27): crm_lead showed zero touches since Jul 15 (12-day dormancy); real calls were happening (Taylor Steel/Rob Coppens Jul 21, Collier Metals Jul 20, etc.) but not logged as CRM stage moves. (raj_2026-07-27_eoxs-sales-team-weekly-performance.md)
- CRM prospect list: 252 total opportunities — 7 WON, ~34 LOST, ~15 Disqualified, ~196 open/active across 8 stages (Leads ~55, Unsure ~40, Intent ~35, Actions Pending ~20, Parked ~20, Discovery Call Done ~12, Client Proposal ~7, Rescheduled 1). (raj_2026-07-29_eoxs-prospect-list.md)
- Largest named open opportunities with real dollar values: Worthington Industries $4,154,400 (stale, 2022), Varsteel $484,400/$207,600, North Shore Steel $328,800, Coilplus $308,400, Three D Metals Canada $277,107, Excelsior Metals $394,320 (disqualified/dead), Superior Steel Supply $119,017, Titanium Industries $61,632, Farmers Copper $73,152. (raj_2026-07-29_eoxs-prospect-list.md)
- No genuine public news/press coverage of EOXS found as of Jul 29, 2026 — only stale directory profiles and an old Crunchbase seed-round listing. (raj_2026-07-29_eoxs-recent-news-5ft.md)
- Mucker Capital: $350K confirmed across 3 tranches, ~12.16% equity. (raj_2026-07-29_eoxs-prospect-list.md)
- MBA intern stipend: ₹10,000/month, 6-month contract, 50 interns deployed starting Aug 1, 2026 — sits at the upper end of documented historical intern precedent (₹7,000-10,000). (raj_2026-08-06_eoxs-payroll-salary-benchmark.md)
- Junior/intern-to-FTE career ladder: ₹18,000/mo Year 1 → ₹51,300/mo Year 5, with loyalty bonuses at years 3 and 5. (raj_2026-08-06_eoxs-payroll-salary-benchmark.md)
- Standard contract terms across nearly all hires: 5-year non-compete (no geographic limit, FTE only), 30-day notice (90 days for Dhrup Kumar Singh), Chandigarh/Delhi/Toronto arbitration venue. (raj_2026-08-06_eoxs-payroll-salary-benchmark.md)

## Sources
- raw/claude-chat-queries/raj_2026-07-31_2026-revenue-monthly-lookup.md — Monthly 2026 posted-revenue breakdown (Jan-Jul, $243K total) plus a bar chart, run against the $1M ARR pace goal.
- raw/claude-chat-queries/raj_2026-07-31_sales-numbers-3yr-analysis.md — 50ft deep 3-year revenue/deal-count analysis, uncovering the CRM won-stage unreliability workaround, new-logo velocity collapse, and Brannon Steel's unpaid-AR distortion of 2026 revenue.
- raw/claude-chat-queries/raj_2026-08-06_eoxs-payroll-salary-benchmark.md — 50ft reconstruction of India payroll structure from Isha's digest emails and scattered records, producing a leveled (L0-L5) compensation benchmark grid.
- raw/claude-chat-queries/raj_2026-07-29_eoxs-business-health-view-5ft.md — 5ft overall business-health view: MRR concentration, churn risk on 3 of top 5 accounts, and CRM pipeline mostly junk.
- raw/claude-chat-queries/raj_2026-07-27_eoxs-sales-team-weekly-performance.md — 10ft weekly sales-activity check that surfaced CRM dormancy since Jul 15 and the sale_order renewal-vs-new-business disambiguation.
- raw/claude-chat-queries/raj_2026-07-29_eoxs-recent-news-5ft.md — 5ft external web search for EOXS press/news (none found) plus a follow-up on the 3GM Steel/Travis Lane IRIS pitch (no vault record yet).
- raw/claude-chat-queries/raj_2026-07-29_eoxs-prospect-list.md — Full CRM prospect-list breakdown (252 opportunities), active employee roster pull, and multiple 5ft "positive points"/"facts" rundowns of EOXS overall.

## Candidate OV2 Cross-References
- Brannon Steel — the $55,239 unpaid-AR finding (8/8 invoices unpaid since Jan 2026) is a concrete, dated fact that likely belongs as a pointer on Brannon Steel's OV2 client page if one exists, since it materially changes their real 2026 revenue contribution.
- EOXS CRM data hygiene / stage-logging gap — this cluster adds two more dated data points (Jul 15 dormancy, 60-70% of opportunities with $0 expected_revenue) to what may already be a known CRM-reliability issue on an existing OV2 page.
- R W Conklin Steel / Bri-Steel Manufacturing dormancy — both are 2025-acquired logos with no invoices in 12+ months; worth a pointer on their OV2 pages if they're not already flagged as at-risk/dormant there.
- EOXS payroll/compensation benchmark — if OV2 maintains any HR or org-structure page, a pointer to this vault's payroll benchmark grid (L0-L5) would be relevant for future hiring/raise decisions.
