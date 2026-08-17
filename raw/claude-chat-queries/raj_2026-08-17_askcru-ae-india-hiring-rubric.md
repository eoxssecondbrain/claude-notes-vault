---
thread_name: "askcru-ae-india-hiring-rubric"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

User: So I'm considering hiring an A/E in India, and we posted a job on LinkedIn, and almost 300 applicants applied for that job. I want to use this thread to evaluate these people and see who gets qualified. Let's start with having a good understanding of what kind of skill, experience, and background we need to hire an A/E for AskCru. Some things which are a red flag for me are high Iteration, like the sales guys who have seven jobs in six years. They are a hard red flag are people with a high iteration (the people who have had six jobs in the last seven years, people who just stick in one job for one year and keep moving)? The people we will disqualify are the people who have had just big brand names, the kind of people who are always chasing brand names. Of course, we will even assess their resumes to see if they have the right skills for this role. And then after that, we will assess if they have had an American selling experience or they have worked with SMBs or not.

[Attached document from user, pasted as reference context — appears to be a prior AI response on the same topic:]
This is a strategic/analytical task (building a hiring rubric + evaluating ~300 applicants). What rigor level do you want?
50ft deep (Deep)

Used 3 integrations, loaded tools
Used 3 integrations, loaded tools
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

Tenure/iteration pass — reject high-iteration resumes first. This is a cheap, high-signal filter that cuts volume fast.
Brand-chasing pass — reject logo-heavy, numbers-empty resumes.
Skills/experience match — full-cycle closing, sales methodology, relevant industry/vertical experience (ERP, B2B software, manufacturing/distribution is a bonus, not a requirement).
US selling / SMB experience — the final differentiator once the pool is down to people who've already cleared 1-3.
One thing worth stress-testing before you run 300 resumes through this: "job-hopping" as a hard red flag can also filter out strong people who left because of company failure, acquisition, or being laid off in a bad market — not because they're flaky. Worth having a secondary check (LinkedIn "About" section, or a quick screening question) before hard-disqualifying rather than auto-rejecting on tenure math alone, since that's the rule most likely to cost you a good candidate by mistake.

Two things I need from you before I can actually run the 300 through this: confirm whether AskCru = the ERP-to-steel-distributors, American-market business, and share the applicant data (resumes or the LinkedIn applicant export) so I can start scoring against this rubric.

Assistant: Scope flag: this task (hiring rubric + screening ~300 applicants) doesn't cleanly fit sales-strategist (that governs GTM/deal strategy, not recruiting) or raj-eoxs-vault (that's EOXS data access — relevant only if the applicant data lives in one of those systems, which I checked, it doesn't). I checked eoxs-db for an AskCruz-specific ICP or role definition — none exists (only an EOXS classic-ERP ICP asset). So the rubric below is built on general hiring judgment plus your stated criteria, not on internal data, because there isn't internal data to pull for this.

Carrying forward the rigor level from the pasted thread: 50ft deep. Say the word if you want a different level for this thread specifically.

Refined rubric, in your stated screening order:

Pass 1 — Iteration/tenure (hard red flag, reject first)
6+ jobs in 7 years, or repeated 10-14 month stints with no visible external cause, is disqualifying on its own. Rationale holds: AE ramp is typically 3-6 months, so someone who leaves annually was either still learning the seat or bailing before results showed. One caveat I'd keep from before — a quick LinkedIn "About" check for acquisition/layoff/shutdown language before hard-rejecting, since that's the rule most likely to cost a good candidate by mistake. Your call whether that check is worth the time at 300-applicant volume or whether you'd rather eat the false-positive rate for speed.

Pass 2 — Brand-chasing (hard red flag, reject second)
Resume is a list of recognizable logos with no attached numbers ("responsible for enterprise accounts," "drove revenue growth," zero quota/ARR/win-rate figures). A strong resume that happens to include a known logo AND has numbers is not this — the flag is logos as the entire pitch, not logos at all.

Pass 3 — Skills/experience match
Full-cycle, quota-carrying closing experience (not SDR/BDR-only prospecting), relevant sales methodology, quantified track record on the resume itself. ERP/B2B SaaS/manufacturing-distribution background is a plus, not a requirement.

Pass 4 — US selling experience or SMB experience
You framed this as "or," not "and" — worth confirming that's intentional. If either signal alone qualifies, this pass is more lenient than pass 3. If you actually want both, say so and I'll tighten it to an AND. This is also where I need one thing from you before I can screen accurately: what's AskCruz's actual ICP — enterprise or SMB-heavy? That changes what "SMB experience" even means as a filter, and I don't have it documented anywhere internally to infer it.

Two blockers before I can run the 300:
1. AskCruz ICP confirmation (enterprise vs SMB, deal size range) — not in the vault, only you have this.
2. The actual applicant data — resumes or the LinkedIn applicant export. Nothing resembling 300 AE applicants exists in eoxs-teams or teams-askcruz; you'll need to share the file or paste the export.
