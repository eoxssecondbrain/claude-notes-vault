---
thread_name: "askcruz-sdr-toronto-hiring-screening"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-21
updated: 2026-08-21
---

USER:
So I'm considering hiring an A/E in India, and we posted a job on LinkedIn, and almost 300 applicants applied for that job. I want to use this thread to evaluate these people and see who gets qualified. Let's start with having a good understanding of what kind of skill, experience, and background we need to hire an A/E for AskCru. Some things which are a red flag for me are high Iteration, like the sales guys who have seven jobs in six years. They are a hard red flag are people with a high iteration (the people who have had six jobs in the last seven years, people who just stick in one job for one year and keep moving)? The people we will disqualify are the people who have had just big brand names, the kind of people who are always chasing brand names. Of course, we will even assess their resumes to see if they have the right skills for this role. And then after that, we will assess if they have had an American selling experience or they have worked with SMBs or not.
This was a standard prompt I had created for a hiring need in India for an AE. However, my requirement has changed now, and now I am looking for an SDR who has some experience in software. This is going to be in Toronto, so we have to make sure that we hire the right employee. We will go through their resume in a rigorous form and analyze if this person would be a good fit for an SDR role. I don't want someone with a lot of experience. What would be a great fit would be a person who has a good track record and is seasoned to be an AE in the next 6 to 12 months.
Also, be mindful that we are looking for someone who has a North American background or has lived in North America for more than 10 years. I see a lot of people here who are recent immigrants, and they would not be a good fit. If I have to hire an Indian in Toronto, I will rather hire an Indian in India.

ASSISTANT:
This doesn't clearly match any of the listed skills — it's not an EOXS data query (eoxs-data-general doesn't apply), and threads-ov only governs saving this transcript, not the hiring task itself. Flagging that per your standing instruction, then proceeding on judgment.

Before building out the SDR screening framework, I need a few things locked down.

[Asked via AskUserQuestion tool, four questions:]

1. Applicant pool — "Are the ~300 LinkedIn applicants you mentioned the same pool you now want evaluated against SDR (Toronto) criteria, or is this a separate hiring search with its own applicants?"
   Options: Same 300, repurposed / Separate SDR pool / AE India is dead, SDR Toronto is the only active search now

2. Experience range — "You said 'not a lot of experience' but 'seasoned enough to become an AE in 6-12 months.' What years-of-experience band are you targeting for this SDR?"
   Options: 0-2 years / 1-3 years / 2-4 years

3. Rigor level — "This is a strategic task (defining the SDR screening framework and later scoring ~hundreds of resumes against it). Pick a rigor level:"
   Options: 5ft — Quick / 10ft — Verified / 50ft — Deep / 100ft — Staged

4. Craft level — "Once criteria are locked, I'll likely produce a written screening rubric/scorecard for you to use on resumes. What craft level for that deliverable?"
   Options: Sketch / Draft / Painting

USER (answers):
Applicant pool: "Separate SDR pool"
Experience range: "[No preference]"
Rigor level: "[No preference]"
Craft level: "[No preference]"

ASSISTANT:
Two things upfront: the SDR Toronto search is a separate, fresh applicant pool from the 300 AE India applicants — I'll leave the AE India evaluation on hold under its original AE criteria and treat this SDR Toronto framework as its own track. You had no preference on experience band, rigor, or craft level, so I picked defaults — flagged below, easy to override.

Defaults I'm running with:
- Experience band: 1-3 years, with a real SDR/BDR quota-carrying track record. Old enough to show they can actually sell, young enough to still want the promotion rather than resent still sitting in an SDR seat at that tenure.
- Rigor: 10ft (verified) — once real resumes come in, I check specifics (actual employer names, actual dates, actual quota numbers) against the resume itself rather than trusting a LinkedIn headline summary. A bad Toronto SDR hire is expensive relative to your 12-month AskCruz ARR target, worth the extra check.
- Craft: holding off on a polished scorecard file until you confirm the criteria below. No point building a document around criteria that might still change.

Carried over from your AE red flags, adapted for SDR:
- Job-hopping stays a hard disqualifier. Six jobs in seven years, or repeated ~1-year stints, out regardless of other strengths — that pattern predicts they leave right around the point you'd promote them to AE.
- Brand-name chasing gets reframed, not dropped. For an SDR the risk isn't the brand name itself, it's what kind of SDR work it produced. A resume that's all inbound-heavy SDR work at large, marketing-flush companies (Salesforce, HubSpot, etc.) with no outbound/cold-prospecting reps is a flag — AskCruz at your stage needs someone who can generate their own pipeline, not just book meetings that were handed to them. Ask directly in screening: did they source their own pipeline, or was it inbound-qualified for them?

New criteria for this brief:
- Software/SaaS sales experience specifically — not general sales, not real estate, insurance, or hardware. Needs to have sold to a technical or semi-technical buyer and understand a software sales motion.
- SMB vs enterprise: given AskCruz's ARR stage, SMB-motion experience (shorter cycles, higher velocity) is probably the better proxy over someone who only ran long enterprise cycles — but that depends on who AskCruz actually sells to. Share the ICP and I'll sharpen this instead of guessing.
- Legally eligible to work in Canada without sponsorship — confirm this explicitly and early, it's a hard practical filter regardless of anything else.

One place I want to push back before we bake it into a written scorecard: the "North American background, 10+ years, not a recent immigrant" criterion.

Citizenship, place of origin, and ethnic origin are explicitly protected grounds under the Ontario Human Rights Code, and immigration status carries separate protection under Canadian employment law. "Recent immigrant" as a written exclusion criterion sits almost exactly on top of "place of origin" and "citizenship" as protected grounds. If a rejected candidate ever files a complaint, a written rubric carrying that criterion is close to the worst evidence you could have created. I'm not a lawyer — if you want to run with a real background filter, get it reviewed by an employment lawyer before it's formalized anywhere in writing.

That said, the underlying business concern is legitimate, and most of what you're actually optimizing for can be captured through criteria that are about the job, not about origin:
- Idiomatic, native-level spoken and written English — testable directly in a phone screen, not inferable from a resume.
- Demonstrated experience actually selling to North American SMB buyers specifically — not just "worked in Canada," but built the instinct for how that buyer thinks and objects.
- An existing professional network and references in the Toronto market — concrete, askable, verifiable.

Those three get you most of the signal you're after without the exposure. I'd drop the raw "years in North America" line from anything written down.

Once you confirm or adjust the above — especially the background criterion — I'll build the one-page scorecard you'll actually run each resume against, and we can start feeding SDR candidates into this thread.

USER:
Here is the screening framework for the Toronto SDR role, built to your 50ft spec.
Hard disqualifiers — auto-reject regardless of resume strength
1. Under 10 years in North America, or a recent immigrant. This is a hard filter per your instruction, applied first, before any skills read.
2. No direct software/SaaS sales experience in an SDR/BDR outbound quota-carrying capacity. General sales experience (insurance, real estate, retail, agency) does not qualify, no matter how strong the numbers.
3. Severe job-hopping: roughly 5 or more jobs in 5-6 years, or a pattern of sub-12-month stints with no external explanation (acquisition, mass layoff, agency/contract work labeled as such). This mirrors the red flag you flagged for the original AE search and carries over here.
Scored criteria — for anyone who clears the disqualifiers
Seniority fit: you want someone gradeable into AE in 6-12 months, not a burned-out veteran. Ideal band is roughly 1-3 years of SDR/BDR experience with clear metrics. 5+ years still doing pure SDR work is a flag — either overqualified and will churn, or underperforming and got stuck.
Tenure quality: not just job count, but trajectory. Two solid 18-24 month stints with a promotion or expanded scope beats four 9-month stints even if the total years match.
Substance over brand: resumes that lean on logos (Salesforce, Google, etc.) without quota attainment, meetings-booked numbers, or pipeline-generated figures get flagged as brand-chasers per your original criteria. A no-name SaaS startup with hard numbers outranks a big name with none.
Outbound skill specifics: cadence tools used (Outreach, Salesloft, Apollo, HubSpot), call/email volume, meetings booked or pipeline sourced, quota attainment percentage where stated.
50ft-only risk flags, layered on top of the above:
Work authorization: since the NA-10-years filter is really a proxy for stability and likely work authorization, I will note where a resume/LinkedIn implies citizenship or PR status versus where it is ambiguous, so you are not relying on the proxy alone.
Career-story inconsistencies: unexplained gaps, overlapping employment dates, title inflation relative to company size, or a story that does not hold together across resume and LinkedIn.
Comp mismatch signals: if a candidate's trajectory or most recent title suggests they are pricing well above typical Toronto SDR comp, I will flag it rather than let it surface later as a rejected offer.
Company legitimacy: for employers I do not recognize, I will do a quick check on size and legitimacy where it materially affects how much weight to put on the claimed experience.
Output format per candidate: verdict of reject or proceed, the one or two decisive reasons, and any 50ft flags worth your attention. I will keep it tight so you can move through 61 of these without wading through prose.

ASSISTANT:
Framework is strong except for one piece I won't build: item 1, the recent-immigrant/under-10-years-in-North-America hard filter, applied first, before any skills read.

I flagged this last turn and you're reinstating it as a harder version — first-pass, before qualifications are even looked at, which is actually the worst version of it from a liability standpoint. Applying it before any job-related assessment makes it much harder to argue it's anything other than what it is: screening by citizenship and place of origin, both explicitly protected grounds under the Ontario Human Rights Code. I'm not going to build or run a screening pass that auto-rejects real applicants on that basis, regardless of how the instruction is framed. This isn't a rigor-level or craft-level choice, it's a line I'll hold.

The same issue shows up smaller in the 50ft risk flags: "note where a resume/LinkedIn implies citizenship or PR status." That's citizenship-inference again, just softer. Dropping that too.

What I'll do instead, same underlying business goal, defensible criteria:

Work authorization, factual not inferred: I'll flag where a candidate states they're legally authorized to work in Canada versus where that's unclear or requires sponsorship. That's an actual job requirement, checked directly, not backed into from tenure or immigration history.

NA-SMB selling experience and English fluency, as proposed last turn: these get you most of the real signal — someone who's actually sold to a North American SMB buyer and communicates like it — without touching a protected ground.

Everything else in your framework I'm running with as written: the job-hopping disqualifier, the SaaS/outbound-SDR-experience disqualifier, seniority band (1-3 yrs ideal, 5+ yrs still doing pure SDR is a flag), tenure-quality read (trajectory over raw job count), the brand-chasing reframe (substance over logos), outbound tool/metric specifics, career-story inconsistency checks, comp-mismatch flags, company-legitimacy checks, and the tight reject/proceed output format.

Send the resumes whenever you're ready and I'll start running them against this — minus item 1 and the citizenship-inference flag, plus the work-authorization/NA-SMB-experience swap above. If you want to push back on that swap specifically, say so — but I won't run the original version of item 1.
