---
thread_name: "askcruz-ae-india-hiring"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

USER (turn 1):
So I'm considering hiring an A/E in India, and we posted a job on LinkedIn, and almost 300 applicants applied for that job. I want to use this thread to evaluate these people and see who gets qualified. Let's start with having a good understanding of what kind of skill, experience, and background we need to hire an A/E for AskCru. Some things which are a red flag for me are high Iteration, like the sales guys who have seven jobs in six years. They are a hard red flag are people with a high iteration (the people who have had six jobs in the last seven years, people who just stick in one job for one year and keep moving)? The people we will disqualify are the people who have had just big brand names, the kind of people who are always chasing brand names. Of course, we will even assess their resumes to see if they have the right skills for this role. And then after that, we will assess if they have had an American selling experience or they have worked with SMBs or not.

[User also attached a document in turn 1 containing a pre-written draft response with a hiring rubric, claiming to have checked eoxs-db for "AskCru" and found none, and claiming teams-askcruz is CRM/prospecting data. Full document content:]

Before the framework — a scope flag: this task (building a hiring rubric and screening ~300 applicants) doesn't cleanly sit under either skill you've defined. sales-strategist governs GTM/deal strategy, objection handling, and prospect-facing emails — not recruiting. raj-eoxs-vault gives me EOXS's data connectors, but none of them are an ATS — no resumes, no applicant tracker. I checked anyway: eoxs-db has no wiki page or record for "AskCru," and the teams-askcruz Odoo instance I have access to is a CRM/prospecting database (prospect job titles at target steel-distributor companies), not a recruiting system — it doesn't hold your 300 applicants. So I'm proceeding on general hiring-strategy judgment, grounded in one real data point I did find: a 2021 email describing EOXS's Enterprise AE role as selling ERP software to steel distributors in the American market. If AskCru is a different product or ICP than that, tell me and I'll adjust the rubric below.

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

ASSISTANT (turn 1):
Before starting: this doesn't cleanly fit either skill I have defined. Sales-strategist governs GTM/deal strategy and prospect-facing work, not hiring. Raj-eoxs-vault gives me EOXS/AskCruz data connectors, but none of them are an ATS — there's no resume or applicant data in eoxs-db, eoxs-teams, or teams-askcruz. So I'm proceeding on general hiring judgment, and I'll only reach for a connector if you want me pulling AskCruz deal-size/ICP context to calibrate the SMB-experience criterion.

This is a strategic task (building a screening framework you'll apply to ~300 people), so per your rule, pick a rigor level:

5ft — I give you the rubric now from general hiring judgment (what "good A/E" looks like, red flag logic, screening sequence). No verification, fast.

10ft — Same rubric, but I first pull real AskCruz context (deal size, actual ICP — SMB vs enterprise steel/ERP-adjacent, what "American selling experience" should mean here) from teams-askcruz/eoxs-teams so the criteria are calibrated to your actual pipeline, not generic AE theory.

50ft — 10ft plus I stress-test your two hard-red-flag rules before we lock them in (job-hopping, brand-chasing) — where they're right, where they'd false-positive on a good candidate, and what a cheap secondary check would look like — before we run 300 resumes through it.

One thing worth flagging now regardless of level: job-hopping as a hard auto-disqualify will filter out people whose 1-year stints were caused by company failure, acquisitions, or mass layoffs rather than flakiness. That's a real cost if you make it a hard filter with no override. Worth deciding now whether it's hard-disqualify or heavily-weighted-but-checkable before we touch the 300.

Which level, and do you have the resumes/LinkedIn export ready to share once we lock the rubric?

USER (turn 2):
50ft

ASSISTANT (turn 2):
[Read threads-ov and raj-eoxs-vault skills; then queried OV2:get_index, OV2:search_wiki (multiple queries: "AskCruz ICP target customer profile", "AskCruz TAM SAM SOM", "AskCruz", "AskCruz pricing tiers platform fee per user", "AskCruz MRR ARR target signed clients Sabre 3GM", "AskCruz positioning Company Brain overview", "Account Executive AE hire job description", "LinkedIn job posting Account Executive India AskCruz", "screening applicants LinkedIn 200 candidates three sales roles", "Toronto SDR India SDR India AE screening system Ontario"), OV2:list_assets, OV2:search_emails (x2), Ask cruz:get_business_schema, Ask cruz:query (project_task where project_id=9 "Hiring Funnels"), OV2:get_client_profile("3GM Steel"). No text response given yet at this point — proceeded directly into turn 3 after user pasted rubric text again.]

USER (turn 3, pasted verbatim, matching the rubric text from the turn-1 attached document):
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

ASSISTANT (turn 3):
Correction to the rubric before we lock it — what I found changes one of your four screening criteria materially.

What's actually verified

No ATS anywhere. teams-askcruz has an emp_training_* module but it's empty (0 rows) — it's an unused internal training-course addon, not an applicant tracker. Confirmed: nothing in eoxs-db, eoxs-teams, or teams-askcruz holds your 300 applicants. That part of the earlier draft was right.

AskCruz's real motion isn't "cold American SMB acquisition." Every live AskCruz deal I found in the wiki is an upsell into an existing EOXS steel client relationship, not a new-logo cold sale: 3GM Steel (proposal already accepted), Sabre Alloys, Ohio Strip Steel, Collier Metals (came in via referral), Three D Metals. The one exception is a single legal-services prospect being tested as a new vertical. Source: OV2 wiki search on "AskCruz," cross-checked against 3GM Steel's client profile which shows an accepted AskCruz proposal email dated Aug 2026.

Deal size is small, consistent with SMB, not enterprise. Signed MRR you already have: Sabre Alloys $5K/month, 3GM Steel $2K/month — roughly $24K-$60K ARR per account. That validates the SMB-motion assumption in the draft rubric. What it doesn't validate is the assumption that this AE will be doing outbound cold-calling into unknown American SMBs — the actual pattern so far is closing warm expansion inside accounts EOXS already has relationships with.

No AE-specific job requisition exists in the system. The only related hiring-funnel record I found (teams-askcruz, project "Hiring Funnels") is for a different role — "0 to 1 SDR," created Aug 12, 2026 — with your own bar language: 2-3+ years experience, strong US calling and B2B SaaS/software sales experience, prioritize immediate joiners. That's a real data point on what you've already deemed acceptable for an adjacent India-based sales hire, but it's SDR, not AE, and it's not the posting you actually used for the 300 applicants.

What this changes in the rubric

Must-have #2 (US-market selling) and #3 (SMB experience) were written as if this is outbound new-business hunting. Given the real pipeline is mostly expansion/upsell into existing relationships, add a criterion the draft didn't have: demonstrated experience growing revenue within an existing account (upsell, cross-sell, renewal-and-expand) — that skill set matters as much as cold US SMB closing for the deals actually in motion right now. Someone who's only ever done net-new logo hunting may be a worse fit than someone with strong expansion-motion experience, even if the latter has less "pure closing" volume.

Everything else in the draft — job-hopping as a hard filter with a secondary check before auto-reject, brand-chasing as a flag only when logos substitute for numbers, quantified-track-record requirement, and the four-pass screening order — holds up. I have no data that contradicts any of it.

Two blind spots I can't close without you

I don't have the actual LinkedIn job posting text — if it names specific requirements (quota size, tools, years of experience) that should anchor the rubric over my inference. Can you paste it or point me to where it lives?

I don't have the 300 applicants. Once you share resumes or the LinkedIn applicant export, I'll score against this rubric — adjusted for the expansion-motion finding above, unless you tell me the AE is meant to build new-logo pipeline that just hasn't happened yet, in which case the original SMB/cold-outbound framing is the right one and I'll revert to it.
