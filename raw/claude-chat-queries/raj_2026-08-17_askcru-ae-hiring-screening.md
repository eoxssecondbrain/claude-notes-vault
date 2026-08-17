---
thread_name: "askcru-ae-hiring-screening"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

Human: So I'm considering hiring an A/E in India, and we posted a job on LinkedIn, and almost 300 applicants applied for that job. I want to use this thread to evaluate these people and see who gets qualified. Let's start with having a good understanding of what kind of skill, experience, and background we need to hire an A/E for AskCru. Some things which are a red flag for me are high Iteration, like the sales guys who have seven jobs in six years. They are a hard red flag are people with a high iteration (the people who have had six jobs in the last seven years, people who just stick in one job for one year and keep moving)? The people we will disqualify are the people who have had just big brand names, the kind of people who are always chasing brand names. Of course, we will even assess their resumes to see if they have the right skills for this role. And then after that, we will assess if they have had an American selling experience or they have worked with SMBs or not.                                                                                                Before the framework — a scope flag: this task (building a hiring rubric and screening ~300 applicants) doesn't cleanly sit under either skill you've defined. sales-strategist governs GTM/deal strategy, objection handling, and prospect-facing emails — not recruiting. raj-eoxs-vault gives me EOXS's data connectors, but none of them are an ATS — no resumes, no applicant tracker. I checked anyway: eoxs-db has no wiki page or record for "AskCru," and the teams-askcruz Odoo instance I have access to is a CRM/prospecting database (prospect job titles at target steel-distributor companies), not a recruiting system — it doesn't hold your 300 applicants. So I'm proceeding on general hiring-strategy judgment, grounded in one real data point I did find: a 2021 email describing EOXS's Enterprise AE role as selling ERP software to steel distributors in the American market. If AskCru is a different product or ICP than that, tell me and I'll adjust the rubric below.

Rubric for the A/E role

Must-have (screen in):

Full-cycle, quota-carrying closing experience — not just SDR/BDR prospecting. You need someone who has owned a number and closed against it, not just booked meetings.

US-market selling experience — sold to US buyers, worked US time zones, communicates the way American buyers expect (directness, written follow-up discipline, objection handling in English at native-adjacent fluency). This matters more than pedigree because your buyer is American even though the hire is in India.

SMB or mid-market motion experience relevant to your actual deal size. This only screens correctly once we confirm AskCru's ICP — enterprise-only experience can be a mismatch for an SMB-heavy pipeline (different sales cycle, different objection set, different decision-maker access) even from strong sellers.

Quantified track record on the resume itself — quota attainment %, ARR/deal size closed, win rate, ramp time. A resume with no numbers is a resume you can't evaluate on merit alone.

Hard red flags (auto-disqualify):

High iteration / job-hopping. Your instinct is correct and it's a legitimate hard filter, not just a preference: someone with 6+ jobs in 7 years, or a pattern of 10-14 month stints with no external explanation (acquisition, layoff, company shutdown), has not demonstrated they can survive a normal sales ramp-and-build cycle. In an AE role that typically takes 3-6 months to ramp, someone who leaves every 12 months was likely still learning the job when they left, or leaving before results showed — neither is a signal you want.

Brand-chasing without substance. A resume that's a list of recognizable logos with vague bullet points ("responsible for enterprise accounts," "drove revenue growth") and no attached numbers is someone who optimized for the name on the resume, not for provable performance. This is different from someone who worked at a known company AND has quantified results — that's a plus, not a flag. The flag is brand names as the whole pitch.

Screening sequence (matches the order you described):

1. Tenure/iteration pass — reject high-iteration resumes first. This is a cheap, high-signal filter that cuts volume fast.
2. Brand-chasing pass — reject logo-heavy, numbers-empty resumes.
3. Skills/experience match — full-cycle closing, sales methodology, relevant industry/vertical experience (ERP, B2B software, manufacturing/distribution is a bonus, not a requirement).
4. US selling / SMB experience — the final differentiator once the pool is down to people who've already cleared 1-3.

One thing worth stress-testing before you run 300 resumes through this: "job-hopping" as a hard red flag can also filter out strong people who left because of company failure, acquisition, or being laid off in a bad market — not because they're flaky. Worth having a secondary check (LinkedIn "About" section, or a quick screening question) before hard-disqualifying rather than auto-rejecting on tenure math alone, since that's the rule most likely to cost you a good candidate by mistake.

Two things I need from you before I can actually run the 300 through this: confirm whether AskCru = the ERP-to-steel-distributors, American-market business, and share the applicant data (resumes or the LinkedIn applicant export) so I can start scoring against this rubric.

Assistant: This doesn't fit sales-strategist (that's GTM/deal work) or raj-eoxs-vault cleanly (recruiting isn't in eoxs-db/eoxs-teams/teams-askcruz) — flagging that per your instruction rather than guessing my way through it. I'm proceeding on general hiring judgment.

Before I build the actual scoring pass on 300 resumes, pick a rigor level:

5ft — quick: apply the rubric mechanically (tenure math, brand-name check, keyword match on skills/US-selling/SMB) and hand you a sorted shortlist fast. Misses nuance like "job-hopping with a legitimate reason."

10ft — verified: same, but every borderline case (ambiguous tenure, unclear US-exposure) gets a second look before I disqualify or advance them, not just a rule applied blind.

50ft — deep: verified, plus I flag pattern risks across the whole pool (e.g. if 200 of 300 are pure SDR/BDR with no closing experience, that's a sourcing problem, not a screening problem, and worth telling you before you burn time reading resumes) and surface anything else material I notice going through them.

Two things I still need before any of this runs:

1. Confirm AskCru = AskCruz, the AI ops platform (askcruz.com) — different ICP/deal size than the EOXS steel-ERP AE role, which changes what "right experience" means for question 3 (SMB motion, deal size, sales cycle).
2. The applicant data — resumes or the LinkedIn applicant export.
