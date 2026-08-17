---
thread_name: "askcru-ae-hiring-india"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

## User
So I'm considering hiring an A/E in India, and we posted a job on LinkedIn, and almost 300 applicants applied for that job. I want to use this thread to evaluate these people and see who gets qualified. Let's start with having a good understanding of what kind of skill, experience, and background we need to hire an A/E for AskCru. Some things which are a red flag for me are high Iteration, like the sales guys who have seven jobs in six years. They are a hard red flag are people with a high iteration (the people who have had six jobs in the last seven years, people who just stick in one job for one year and keep moving)? The people we will disqualify are the people who have had just big brand names, the kind of people who are always chasing brand names. Of course, we will even assess their resumes to see if they have the right skills for this role. And then after that, we will assess if they have had an American selling experience or they have worked with SMBs or not.

## Assistant

[Asked AskUserQuestion: "This is a strategic/analytical task (building a hiring rubric + evaluating ~300 applicants). What rigor level do you want?" with options 5ft deep (Quick), 10ft deep (Verified), 50ft deep (Deep). User selected: 50ft deep (Deep).]

Then queried eoxs-db (get_index, search_wiki for "AskCru"/"AskCru account executive" — both empty), searched eoxs-db emails (found one relevant 2021 email: "Fwd: Michael Page India" — EOXS Enterprise Account Executive role selling ERP software to Steel Distributors in the American market), and inspected the teams-askcruz Odoo instance (get_business_schema, list_tables, queried askcruz_job_position and hr_job) — confirmed this is a CRM/prospecting instance (prospect job titles at target companies) for a client/product called AskCruz, not a recruiting/ATS system, and does not contain the 300 LinkedIn applicants.

Skill-match flag: this task (defining a hiring rubric and screening ~300 job applicants) doesn't cleanly match sales-strategist (that skill governs GTM/deal strategy/objection handling/prospect emails, not recruiting) and isn't a straight EOXS-data lookup either — raj-eoxs-vault's connectors have no ATS/recruiting data. Proceeding on general hiring-strategy reasoning grounded in the one piece of EOXS context found (ERP software sold to steel distributors, American market, per the 2021 email), flagged as an assumption to confirm.

Flagged one clarifying point in text: whether "AskCru" is the same business as that 2021 EOXS Enterprise AE context (ERP to steel distributors, US market) — if AskCru is a different product/ICP, the rubric below needs correcting.

Delivered a hiring rubric for the India-based A/E role covering: hard disqualifiers (job-hop rate above one job per ~12-18 months sustained across recent history; resumes that are brand-name-heavy with no quantified quota/ARR/deal results), must-have criteria (full-cycle quota-carrying closing experience, not SDR-only; US-market selling experience — time zone overlap, buyer communication style, English fluency; SMB/mid-market motion experience relevant to AskCru's likely deal size), soft flags needing more evidence (12-18 month average tenure with plausible explanations; unexplained gaps), and the 4-step screening sequence matching the user's own stated order: (1) tenure/iteration screen, (2) brand-chasing screen, (3) skills/experience match, (4) US selling / SMB experience check. Ended by asking the user to confirm the AskCru product/ICP assumption and to share the applicant data (resumes or LinkedIn export) so actual screening can begin.
