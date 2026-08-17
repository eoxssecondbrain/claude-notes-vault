---
thread_name: "askcru-ae-hiring-india"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

## Turn 1

### User
So I'm considering hiring an A/E in India, and we posted a job on LinkedIn, and almost 300 applicants applied for that job. I want to use this thread to evaluate these people and see who gets qualified. Let's start with having a good understanding of what kind of skill, experience, and background we need to hire an A/E for AskCru. Some things which are a red flag for me are high Iteration, like the sales guys who have seven jobs in six years. They are a hard red flag are people with a high iteration (the people who have had six jobs in the last seven years, people who just stick in one job for one year and keep moving)? The people we will disqualify are the people who have had just big brand names, the kind of people who are always chasing brand names. Of course, we will even assess their resumes to see if they have the right skills for this role. And then after that, we will assess if they have had an American selling experience or they have worked with SMBs or not.

### Assistant
[Asked AskUserQuestion for rigor level: 5ft/10ft/50ft deep. User chose 50ft deep (Deep).]

Before the framework — a scope flag: this task (building a hiring rubric and screening ~300 applicants) doesn't cleanly sit under either skill you've defined. sales-strategist governs GTM/deal strategy, objection handling, and prospect-facing emails — not recruiting. raj-eoxs-vault gives me EOXS's data connectors, but none of them are an ATS — no resumes, no applicant tracker. I checked anyway: eoxs-db has no wiki page or record for "AskCru," and the teams-askcruz Odoo instance I have access to is a CRM/prospecting database (prospect job titles at target steel-distributor companies), not a recruiting system — it doesn't hold your 300 applicants. So I'm proceeding on general hiring-strategy judgment, grounded in one real data point I did find: a 2021 email describing EOXS's Enterprise AE role as selling ERP software to steel distributors in the American market. If AskCru is a different product or ICP than that, tell me and I'll adjust the rubric below.

Rubric for the A/E role

Must-have (screen in): Full-cycle, quota-carrying closing experience — not just SDR/BDR prospecting. US-market selling experience. SMB or mid-market motion experience relevant to your actual deal size. Quantified track record on the resume itself.

Hard red flags (auto-disqualify): High iteration / job-hopping (6+ jobs in 7 years, or 10-14 month stints with no external explanation). Brand-chasing without substance (logo-heavy, numbers-empty resumes).

Screening sequence: 1. Tenure/iteration pass. 2. Brand-chasing pass. 3. Skills/experience match. 4. US selling / SMB experience.

One thing worth stress-testing before you run 300 resumes through this: "job-hopping" as a hard red flag can also filter out strong people who left because of company failure, acquisition, or being laid off in a bad market. Worth having a secondary check before hard-disqualifying rather than auto-rejecting on tenure math alone.

Two things I need from you before I can actually run the 300 through this: confirm whether AskCru = the ERP-to-steel-distributors, American-market business, and share the applicant data.

## Turn 2 — Candidate 1: Rajan Rastogi

### User
[Uploaded resume PDF] Here is the first candidate. Give me a rating out of 10 and qualify or disqualify

### Assistant
Rating: 4/10 — disqualify (borderline, worth keeping in a "maybe" pile only if the applicant pool is thin).

Candidate: Rajan Rastogi, Delhi. B.E. Mechanical (2008), MBA Marketing (2017). Tenure math: 7 employers in 10 years (Digit 9.0, Billfree Labs, Emanation Group, FinTrans, SignalX, Cohora, Magnimus), three under 9 months clustered in 2020-2024, plus two multi-month unexplained gaps. Matches the iteration red flag pattern at a slightly less severe rate than the extreme case. No brand-chasing — all small/unknown companies. No quantified quota/ARR/deal-size numbers anywhere in 9 years of sales roles — only activity descriptions. US exposure present (Magnimus, SignalX target US) but never states he personally closed US deals vs. prospecting into them. Billfree's merchant-acquisition work is genuinely SMB-flavored. Unexplained ~8-year gap between B.E. (2008) and first job (2016). Net: real iteration concern matching your criterion, combined with zero quantified proof of results. Recommend disqualify, or hold as low-priority maybe only if SMB/merchant-acquisition angle strongly matches AskCru's ICP.

## Turn 3 — Candidate 2: Ipsita Sukanya

### User
[Uploaded resume PDF] Check this

### Assistant
Rating: 4/10 — disqualify for this role, though for a different reason than candidate 1.

Candidate: Ipsita Sukanya, Bengaluru. B.Tech CS&E, MBA (Marketing & HR). Tenure: Vyze Inc. (Aug 2019-Mar 2021, 19mo), Kapiva/Atret Retail (Jul 2021-present, ~5 years). Strong tenure — opposite of iteration red flag. Problem is fit: current 5+ year role is B2C consumer wellness telesales (Kapiva), not B2B enterprise software. Only relevant B2B/US experience is the 19-month Vyze stint, 4+ years stale, with one modest number ($6K/month target) and possible staffing/consulting flavor rather than SaaS. Kapiva's achievements are entirely qualitative, no numbers. Resume's skills lists read as buzzword-stuffing not matched by role detail. No brand-chasing. Net: strong tenure discipline (a genuine plus elsewhere) but wrong sales motion/buyer type for this role, and relevant B2B/US experience is old and unverified. Disqualify for the AskCru AE opening specifically.

## Turn 4 — Candidate 3: Shaun Sylvester

### User
[Uploaded resume PDF] check it.

### Assistant
Rating: 1.5/10 — clear disqualify.

Candidate: Shaun Sylvester, Bengaluru. BBA, Reva University. Tenure: Mycaptain (03/2023-05/2024, 14mo), Corizo (06/2024-10/2025, 16mo), Simplilearn (11/2025-02/2026, 3mo), Intellirose (05/2026-present, ~3.5mo, after a 3-month gap). 4 employers in 3.5 years, accelerating to two sub-4-month stints most recently — more severe than the pattern you flagged as hard red flag. A 3-month stint isn't enough time to deliver the claimed accomplishments, which reads as filler. Zero quantified numbers anywhere. No US market, SaaS, enterprise, or SMB signal anywhere — all four employers read as edtech/consumer sales. No brand-chasing (no recognizable names). Net: clearest disqualify so far — iteration alone justifies rejection, compounded by no quantified proof and no signal on the two criteria you want checked last.

## Turn 5 — Candidate 4: Pravin Sigtia

### User
[Uploaded resume PDF] check this

### Assistant
Rating: 8/10 — qualify, move to interview. Strongest of the four so far by a clear margin.

Candidate: Pravin Sigtia, Hyderabad. BCom, DOB 1990. Tenure: Monster (Internet Recruitment Consultant Feb 2011-Jun 2012, then promoted to Account Manager Jun 2012-Mar 2023 — nearly 11 years, one company), TargetBay (Assistant Sales Manager, Mar 2023-present, ~3.5 years). Two employers in 15 years — opposite of iteration red flag. Quantified results: 120-135% of quota multiple consecutive quarters, Top 5 Account Manager 8 consecutive years, 1,000+ demos, 20% increase in average deal size, 25% demo-to-close improvement, 18% renewal-rate improvement. US market explicit: "high-value enterprise clients across the U.S." for over a decade. Full-cycle closing explicitly described at both employers. Two verification items: his US experience is at Monster (ITES/recruitment, not software) — only 3.5 years is actual SaaS-company experience; and his current Assistant Sales Manager title includes people-management scope, so confirm he wants an IC AE role and align comp expectations. Also confirm SMB vs. enterprise fit since Monster book was "high-value enterprise." Net: clear qualify, worth a screening call.

## Turn 6 — Candidate 5: Shreyash Patil

### User
[Uploaded resume PDF] check this one

### Assistant
Rating: 6/10 — flagging as a genuine judgment call, because this one directly tests your own stated rule.

Candidate: Shreyash Patil. BBA (Jain University 2021), PG Program in Product Management (Duke, 2023). Tenure: Talent Titan (Jul 2022-Jun 2023, 1yr), Simplilearn (Jun 2023-Jan 2025, 1.7yr), 6-month unexplained gap, Globussoft (Jul 2025-present, ~1yr). Three jobs in four years, each ~12-20 months — close to a literal match for your stated hard red flag. Substance is the strongest in the batch: $35,000 revenue at Talent Titan, $200,000+ annual revenue and 157% of quota with $1,250 ACV at Simplilearn, $7,000 monthly quota at Globussoft, $250,000+ cumulative career revenue. Full-cycle closing explicitly and consistently claimed. Two things to weigh: resume never says "United States" — only Europe/Middle East/South Asia/APAC/Domestic, a real gap against your specific US criterion; and the resume is unusually complete/rubric-shaped (precise percentages, ACV, revenue, AI-workflow fluency via Claude/OpenAI) — worth one verification step (CRM screenshots or manager reference) before trusting numbers at face value. Recommendation: don't auto-disqualify on tenure alone, but don't advance past a screening call either — press on US exposure specifically, ask him to explain the job changes and gap, and ask him to substantiate the numbers.

## Turn 7 — Candidate 6: Shiv Sharma

### User
[Uploaded resume PDF] check this

### Assistant
Rating: 6/10 — qualify with reservations, for a different reason than the tenure-driven flags on earlier resumes.

Candidate: Shiv Sharma, Noida. Graduate — Shobhit University. Tenure: Impressico (Jun 2013-Mar 2015, 21mo), Finoit (Apr 2015-Dec 2016, 20mo), Friends Color Images (Jan 2017-Oct 2017, 9mo), Batia Software/ProProfs (Nov 2017-present, ~8yr9mo). Four employers across 13 years, last nine at one company — cleanly clears the iteration red flag, longest single-employer tenure in the batch so far. US/SMB experience present but old and a different motion: 2013-2016 "SME IT companies in the US and Canada," but that was IT-services/offshoring partner development, not product sales, and ended ~10 years ago. Current 9-year ProProfs role is inbound-lead conversion (15 demos/week, consistent 30% close rate) with no outbound-prospecting language and no revenue/quota figures despite the long tenure. No brand-chasing. Net: excellent stability, real if dated US/SMB exposure, decent conversion metric — but dominant recent experience is inbound order-taking, not outbound hunting, which may be the wrong motion for this role. Recommend a screening call on one question: has he ever built his own outbound pipeline from scratch?

## Turn 8 — Candidate 7: Aswan Basha I

### User
[Uploaded resume PDF] check this

### Assistant
Rating: 1/10 — clear disqualify, not close.

Candidate: Aswan Basha I. B.Com Computer Applications (2019-2022), MBA Finance & Marketing (2022-2024), PG Diploma Import & Export (2022-2024). Total actual sales experience: a 2-month internship (Mohib Shoes, 2022) plus one year as BDE at Ediglobe (2023-2024) — about 14 months, all entry/support-level language. Most recent two years (2024-2026, current) are "Freelance Product Designer" doing UI/UX work — unrelated field, not sales. Resume self-identifies as seeking "a remote BDE, Inside Sales or SDR role" — wrong seniority level entirely for an AE opening. No quantified results, no US market, no enterprise/SaaS signal, no evidence of owning a sales cycle through close. Net: entry-level SDR profile with a two-year gap in an unrelated field. Disqualify — not worth a screening call for this requisition.

## Turn 9 — Candidate 8: Rohit Rana

### User
[Uploaded resume PDF] check this

### Assistant
Rating: 5/10 — borderline, recommend a verification call before deciding either way.

Candidate: Rohit Rana, Greater Noida. B.Com (Hons) 2018. Tenure: Daurcom (Sr. Customer Success Manager, 02/02/2019-07/08/2023, ~4.5yr), NetCom (Sr. Partner Account Manager, 06/Nov/2023-05/Jan/2026, ~26mo). Only two employers across ~7 years — strong stability. One flag: 7-month gap since Jan 2026, unexplained, worth asking about. Real question is role type, not tenure: Daurcom years were pure Customer Success (onboarding, retention, adoption, NPS — no prospecting/closing language). NetCom claims full funnel including closing but the "Partner Account Manager" title and heavy Cisco/Microsoft co-selling emphasis suggests channel/partnership management more than direct net-new hunting — worth confirming he's personally sourced and closed deals vs. managed partner-referred relationships. US/segment signal: reasonably strong but partly inferred (Daurcom explicitly "mid-market US clients"; NetCom references SLG/DOD/CPG/FSI, standard US GTM shorthand, implying a US-centric book though never stated directly). Both roles skew mid-market/enterprise ("Fortune 500 accounts" at NetCom), not SMB — a real gap if AskCru's ICP is SMB-heavy. Net: solid tenure and plausible US enterprise exposure, decent metrics (mostly retention/adoption, not sales-attainment) — recommend a screening call centered on hunter-vs-account-manager distinction, plus the gap.

## Turn 10 — Candidate 9: Ridaiy Ajrawat

### User
[Uploaded resume PDF] check this

### Assistant
Rating: 3/10 — disqualify for this AE opening, though the underlying skill set is real and might fit a different requisition.

Candidate: Ridaiy Ajrawat, Mumbai. Tenure: LocoNav (Sep 2017-Aug 2018, 11mo, ops not sales) → ~11mo gap → OYO Rooms (Jul 2019-Feb 2021, 19mo, BDM) → MakeMyTrip/Goibibo (Mar 2021-Aug 2022, 17mo) → Infotelligent (Aug 2022-Nov 2023, 15mo, SDR→Sr SDR) → Sprinto (Nov 2023-Dec 2024, 13mo, Sr SDR) → VWO/Wingify (Jan 2025-Jan 2026, 12mo, Sr SDR) → Stamina.io (Mar-Apr 2026, explicitly freelance, 1-2mo). 7 employers in 9 years, most recent four landing at ~12-13 months each before collapsing to a 1-2 month freelance stint — close to a textbook match for your hard red flag, the clearest case yet. Underlying problem: his actual AE-title, full-cycle-closing experience is only that 1-2 month freelance stint on tiny $999 TCV deals (~$4K ACV) — everything from Aug 2022-Jan 2026 was SDR/Senior SDR (pipeline generation, not closing). His summary's "5+ years as SDR, Senior SDR and Account Executive" framing overstates real closing experience. Positives: last three roles show direct, current, consistent US/North America and SMB-to-mid-market exposure, real methodology fluency (BANT/SPIN/MEDDPICC), and honest (not inflated) quota numbers (75-80%, 9/12). MakeMyTrip numbers (₹5.8L to ₹19L/month in 6 months) show execution ability outside SaaS. Net: disqualify for the AE opening on iteration plus the AE-title-vs-track-record gap; worth a second look if AskCru ever opens an SDR/BDR requisition.

Running tally after 9 candidates: qualify — Pravin Sigtia (8/10). Borderline/verify — Shreyash Patil (6/10), Shiv Sharma (6/10), Rohit Rana (5/10). Disqualify — Rajan Rastogi (4/10), Ipsita Sukanya (4/10), Shaun Sylvester (1.5/10), Aswan Basha (1/10), Ridaiy Ajrawat (3/10).

## Turn 11 — Candidate 10: Arnold Stanley Dias

### User
[Uploaded resume PDF] check this

### Assistant
Rating: 7.5/10 — qualify, move to screening call. Strongest overall candidate in the batch on substance, with two specific things to verify.

Candidate: Arnold Stanley Dias. BCOM (listed as "Pursuing"). Tenure mapped: Flair IT Group (Jun 2012-Sep 2016, 4.25yr, though duties described are travel/holiday sales, not IT — a mismatch worth asking about), Agile CRM/Mantra Technologies (Oct 2016-Oct 2019, 3yr, B2B CRM sales Europe/Middle East), Customer Dynamics India (Nov 2019-Aug 2020, 9mo, channel/partner-marketing), 7-month gap, CloudFulcrum (Mar 2021-Aug 2021, 5mo), Electroneek Robotics (Mar 2022-Sep 2022, 6mo, RPA APAC), 4-month gap, Vee Phoenix/Doctor Alliance (Jan 2023-Aug 2025, 2yr8mo, US healthcare compliance SaaS), and a current 12-month gap since Aug 2025. Bimodal pattern: two long stable/high-performing runs (Flair IT, Agile CRM, Doctor Alliance) bookending a rougher 2019-2022 stretch plausibly tied to pandemic-era layoffs — worth confirming, not assuming. Biggest open item: the current 12-month gap needs a direct explanation. Substance is the strongest in the batch: repeated, specific, multi-employer quantified results — $550K+ ARR closed in year one at Doctor Alliance (handling Enterprise Accounts across the US), $22K closed in 25 days plus $150K pipeline in 50 days at Electroneek (highest revenue in region for the quarter), doubled territory MRR over 2.7 years at Agile CRM while overachieving monthly quota. Cleanest match on the two check-last criteria: Doctor Alliance is explicitly "US Healthcare," with him "handling only Enterprise Accounts across the US" and separately "managed accounts across small, medium, and enterprise levels" — direct, current, explicit confirmation of both US and SMB-through-enterprise experience. Net: strongest substance in the batch; advance via screening call focused on the 2019-2022 volatility and the current 12-month gap before treating this as a top candidate.

Running tally after 10 candidates: qualify — Arnold Dias (7.5/10), Pravin Sigtia (8/10). Borderline/verify — Shreyash Patil (6/10), Shiv Sharma (6/10), Rohit Rana (5/10). Disqualify — Rajan Rastogi (4/10), Ipsita Sukanya (4/10), Ridaiy Ajrawat (3/10), Shaun Sylvester (1.5/10), Aswan Basha (1/10).
