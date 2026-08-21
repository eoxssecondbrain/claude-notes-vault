---
thread_name: "askcruz-toronto-sdr-hiring"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-21
updated: 2026-08-21
---

## User (turn 1)

So I'm considering hiring an A/E in India, and we posted a job on LinkedIn, and almost 300 applicants applied for that job. I want to use this thread to evaluate these people and see who gets qualified. Let's start with having a good understanding of what kind of skill, experience, and background we need to hire an A/E for AskCru. Some things which are a red flag for me are high Iteration, like the sales guys who have seven jobs in six years. They are a hard red flag are people with a high iteration (the people who have had six jobs in the last seven years, people who just stick in one job for one year and keep moving)? The people we will disqualify are the people who have had just big brand names, the kind of people who are always chasing brand names. Of course, we will even assess their resumes to see if they have the right skills for this role. And then after that, we will assess if they have had an American selling experience or they have worked with SMBs or not.
This was a standard prompt I had created for a hiring need in India for an AE. However, my requirement has changed now, and now I am looking for an SDR who has some experience in software. This is going to be in Toronto, so we have to make sure that we hire the right employee. We will go through their resume in a rigorous form and analyze if this person would be a good fit for an SDR role. I don't want someone with a lot of experience. What would be a great fit would be a person who has a good track record and is seasoned to be an AE in the next 6 to 12 months.
Also, be mindful that we are looking for someone who has a North American background or has lived in North America for more than 10 years. I see a lot of people here who are recent immigrants, and they would not be a good fit. If I have to hire an Indian in Toronto, I will rather hire an Indian in India.

## Assistant (turn 1)

This is a hiring-evaluation task for AskCruz (not an EOXS data question), so the eoxs-data-general connector doesn't apply here — flagging that per your standing instruction rather than silently skipping it. Threads-ov is the only skill in play, and I'll save the transcript at the end as usual.

Before I build the SDR qualification framework, I need a few decisions from you — this is a strategic/analysis task, so per your standing rule I'm gating on rigor level, and I want 95% clarity before drafting criteria you'll use to screen ~300 people.

[Asked via AskUserQuestion tool, four questions:]

1. What rigor level for this hiring-criteria + candidate evaluation work?
   Options: 5ft deep — Quick / 10ft deep — Verified / 50ft deep — Deep / 100ft deep — Staged

2. What counts as the 'software experience' you want in this SDR?
   Options: SDR/sales inside a software company (Recommended) / Any role inside a software company / Open to tech-adjacent industries

3. Work authorization requirement for this Toronto hire?
   Options: Must already have Canadian work rights (Recommended) / Not a hard filter, assess case by case / Unsure — flag it per candidate

4. How much total experience should this SDR have?
   Options: 1-2 years total (early signal, not fresh grad) / 2-3 years total (some quota-carrying experience) / Let me propose a range based on typical SDR-to-AE timelines (Recommended)

## User (turn 2, via AskUserQuestion)

Rigor level: "50ft deep — Deep"
Software experience: "SDR/sales inside a software company (Recommended)"
Work authorization: "[No preference]"
Target experience: "Let me propose a range based on typical SDR-to-AE timelines (Recommended)"

## Assistant (turn 2)

Noting the assumption I'm making since your answer to the work-authorization question came back blank: I'm treating "must have Canadian work rights" as the default hard filter (citizen/PR/valid open work permit, no sponsorship) — correct me if you actually want to consider sponsorship or unclear-status candidates.

## The tension in what you're asking for

You want someone with "not a lot of experience" who's also "seasoned enough to be AE-ready in 6-12 months." The data says these two things pull against each other, and it's worth seeing before we set the filter.

SDR ramp-to-full-quota alone takes 3.2-5.7 months industry-wide, higher for SaaS specifically (Dialfyne, 2026). And on promotion timing specifically: SDRs promoted to AE before 11 months in seat had a 55% failure rate as AEs; SDRs with 16+ months of experience dropped that to 6% (Visdum SDR-to-AE Roadmap). Early-stage startups (which AskCruz is) do typically promote fastest — 6-12 months — but that's measured from when someone starts being a productive SDR, not from zero.

So a true first-time SDR with no prior software sales background is a bad match for a 6-month AE timeline — you'd be promoting into the failure zone. The way to actually get what you want is to hire someone who already has some prior SDR/BDR time elsewhere, so AskCruz's clock only has to cover ramp plus a proof window, not the whole learning curve from scratch.

## Recommended experience band

Roughly 1-3 years total professional experience, of which 6-18 months should be direct SDR/BDR (quota-carrying, outbound) experience at a software/SaaS company specifically. That's "not a lot" relative to a seasoned AE hire, but enough prior seat time that the 6-12 month AE clock is realistic rather than a bet against the base rate above.

## Hard filters (disqualify without further review)

- Legal authorization to work in Canada, no sponsorship (see assumption note above)
- Direct SDR, BDR, or inside-sales experience at a software/SaaS company — not just "worked at a software company," actual outbound/pipeline-gen sales experience there
- Total experience in the 1-3 year band above, not a senior AE or 5+ year sales veteran (overqualified, will be a flight risk once you can't promote them fast enough or pay AE-level comp)

## Strong-fit signals

- Quota attainment stated with actual numbers, not just "top performer"
- Some full-cycle exposure — even partial ownership of a closed deal, not purely qualify-and-hand-off
- No more than one or two prior SDR stops (see red flags below for why this threshold, not a stricter one)
- Resume/application itself is well-written and specific — for an SDR, the application is a writing and prospecting-message sample

## Red flags — recalibrated for SDR, not copied from your AE criteria

Your AE red flag (six jobs in seven years) doesn't transfer directly. SDR is structurally a short-tenure role industry-wide: median tenure is 14-18 months and annual turnover is 34%, roughly triple other industries (Dialfyne). A candidate with two SDR stints of 12-18 months each is following the normal pattern for this role, not job-hopping.

What's actually a red flag at the SDR level:

- Three or more stints under 6-9 months each — that's churning faster than the role's own ramp time, meaning they likely never became productive before leaving or being let go
- SDR/BDR at three-plus companies over 3+ years with zero promotion anywhere — this directly contradicts what you're hiring for. If nobody has promoted them yet, there's a real chance you won't either
- Brand-name-only resumes with short (3-6 month) stints at those brands and no specifics — same "chasing logos" pattern you flagged for the AE role, still applies here

## The North America background criterion — flag this before we build it in

This is the one place I'd push back directly rather than just operationalize what you said. The Ontario Human Rights Code, section 5(1), explicitly lists citizenship, place of origin, ethnic origin, and ancestry as protected grounds in employment (OHRC). "Years lived in North America" and "recent immigrant" are functionally proxies for citizenship and place of origin — screening candidates out on that basis, or documenting it as a rejection reason, is real exposure to a human rights complaint in Ontario, not just an optics problem. I'm not a lawyer and this isn't legal advice, but the risk is concrete enough that I don't think you should build it into the screening criteria as stated.

The underlying business need is legitimate, though: you need someone who can actually sell to North American software buyers, read their objections, and ideally already has some network in your ICP. That's assessable through lawful proxies you're already using elsewhere in this framework:

- Direct prior experience selling to US/Canada B2B software buyers — an experience fact, already covered by your software-SDR hard filter
- A live discovery-call or cold-call role-play at interview stage, scored on communication and objection-handling — assesses the actual skill, not a demographic proxy
- Relevance of their existing professional network to your ICP, which you can see from LinkedIn connections/past employer overlap — again a fact about their work history, not their origin

I'd drop "recent immigrant" and "time in North America" as resume-screening criteria entirely and move the real check — can they actually sell to a North American buyer — to the live interview stage where you're testing the skill directly. Practically this gets you the same outcome (someone who can sell into your market) without the exposure.

## One more adjacent thing worth knowing

34% annual SDR turnover market-wide means retention risk here is baked into the role, not just a function of who you screen in. Whoever you hire has a real chance of leaving within 18 months regardless of how tight the screen is — worth planning the ramp/comp/promotion path with that in mind rather than treating a good hire as a solved problem once they sign.

## Proposed screening process for the 300 applicants

1. Hard filter pass — work authorization, software SDR/BDR experience specifically, 1-3 year experience band. Fast elimination.
2. Red flag pass — churn pattern, SDR-capped pattern, brand-chasing.
3. Score what's left on quota evidence, full-cycle exposure, and application quality.
4. Shortlist goes to a live sales-communication assessment at interview — this is where NA-buyer fluency actually gets tested, lawfully.

Confirm or adjust this and I'll start working through resumes against it once you share them.

Sources:
- SDR to AE: The 12-Month Promotion Roadmap — https://www.visdum.com/blog/sdr-to-ae-roadmap
- SDR Statistics 2026: Ramp Time, Quota & Turnover - Dialfyne — https://dialfyne.com/sdr-statistics
- Relevant Code provisions | Ontario Human Rights Commission — https://www.ohrc.on.ca/en/policy-discrimination-and-language/relevant-code-provisions
- Hire a temporary foreign worker - Canada.ca — https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada/hire-temporary-foreign.html

## User (turn 3)

i will be screening the SDR candidate not AE so be mindfull while screening

## Assistant (turn 3)

Good flag — a couple of things in my last framework leaned AE, not SDR, and worth fixing before you start screening.

## What I got wrong (correcting it)

I listed "quota attainment stated with actual numbers" and "full-cycle exposure, some ownership of a closed deal" as strong-fit signals. Those read like AE metrics. SDR and AE are scored on different things: SDRs are measured on meetings held (excluding no-shows) and pipeline value from opportunities the AE accepted, not closed revenue — dials and emails are diagnostic, not the actual target. AEs are measured on bookings against quota, win rate, deal size, and cycle length. The one shared number is opportunity acceptance rate — what percentage of the SDR's booked meetings the AE actually accepts as qualified, since that's what stops the SDR from just farming volume (ORM, SDR vs AE Sales Metrics).

Practical effect on how you screen: if a resume brags about "closed revenue" or "quota attainment" without saying meetings/pipeline, that's either an AE-flavored resume padding an SDR title, or a red flag for role confusion — not evidence of a strong SDR.

## Corrected screening lens for SDR resumes specifically

Strong-fit signals — look for these framed in SDR terms:

- Meetings held (not just booked) against a stated target, ideally with the target named
- Pipeline generated / opportunities accepted by AEs, with a number
- Sequence/cadence tool fluency named explicitly — Outreach, Salesloft, Apollo, ZoomInfo, HubSpot, Salesforce — this is a real skill gap between someone who's done the job and someone who hasn't
- Message quality — the application itself, cold email samples if provided, LinkedIn outreach style

Downgrade, don't require:

- Full-cycle or closing exposure — nice bonus if present, but most SDRs never get this, so requiring it will wrongly filter out otherwise strong candidates
- "Quota attainment" phrased vaguely without units — ask what quota, in what unit, before crediting it

For the "AE-ready in 6-12 months" trajectory judgment specifically, look for consistency of meeting-held attainment over multiple quarters plus a rising or high opportunity-acceptance rate, not prior closing experience. High activity with low acceptance rate is a volume-chaser, not someone who's ready to own a full cycle soon — that's the person who'll fail the promotion, per the 55% failure stat from last time.

Everything else from the earlier framework — the experience band, the work-auth default, the job-hop recalibration, and dropping the North America/immigration criterion in favor of a live communication assessment — still stands. Send resumes whenever you're ready.

Sources:
- SDR vs AE Sales Metrics: What to Measure for Each Role | ORM — https://orm-tech.com/blog/sdr-vs-ae-sales-metrics

## User (turn 4)

[Uploaded resume PDF: Siddhant Yadav]
check the first candidate and rate out of 10, qualify or disqualify

## Assistant (turn 4)

## Candidate: Siddhant Yadav

Merit score (skills/experience/background, work authorization set aside): 7/10
Verdict: Disqualify — fails the work-authorization hard filter as currently set

## Why disqualify first

Location is Gurgaon, India, and nothing on the resume indicates Canadian citizenship, PR, an existing work permit, or even a stated relocation plan. Under the default we agreed on last time — must already have Canadian work rights, no sponsorship — this fails before the merit review even starts. I'm flagging this loudly rather than quietly dropping him, because if 300 applicants came in against a Toronto posting, a meaningful chunk are probably India-based like this one, and whether that's an automatic disqualifier depends on something only you can answer.

## Merit breakdown (for if work-auth turns out not to be a blocker)

Software/SaaS experience: Real and relevant. Dancing Numbers is a SaaS product (QuickBooks/Xero data-import tool), and he's selling it B2B into US and UK markets — that's a genuine, lawful signal for "can this person sell to a North American buyer," which is exactly the proxy we agreed to use instead of screening on immigration status.

Experience band: About 2.3 years in the role (Apr 2024-present) plus a 1-month internship. Fits inside the 1-3 year band, though the role reads as full-cycle (demos, objection handling, renewals/closing) rather than pure top-of-funnel SDR — more AE-adjacent than the target profile, which is actually a decent trajectory signal for "AE-ready in 6-12 months" but means the title doesn't map cleanly to what you're hiring for.

Tenure/stability: One job, still current after 2+ years. Zero job-hop red flag.

Brand-chasing: None — smaller, lesser-known companies, no logo-chasing pattern.

SDR-specific evidence: Weak. No quantified meetings-held, pipeline-generated, or connect-rate numbers anywhere — just generic phrasing ("drive lead generation," "consistent pipeline of qualified prospects"). This is exactly the metric gap we said to watch for.

Resume quality: Two sets of near-duplicate bullets under the Marketing Intern role (both "Executed field marketing campaigns..." and "Collaborated with cross-functional teams..." appear twice with near-identical wording). Reads like unedited AI-assisted output — worth weighing since we're treating the application itself as a writing/attention-to-detail sample.

[Asked via AskUserQuestion:] This candidate (and likely a chunk of the 300) is India-based with no visible Canadian work rights. Is the Toronto SDR role open to relocation/sponsorship, or local-hire only?
Options: Local hire only (Recommended default) / Open to relocation/sponsorship / Case-by-case — flag it, don't auto-disqualify

## User (turn 5, via AskUserQuestion)

Relocation policy: "Local hire only (Recommended default)"

## User (turn 5, mid-turn upload)

[Uploaded resume PDF: Priya Jadon]
check this

## Assistant (turn 5)

## Update: Siddhant Yadav — final verdict

Confirmed disqualify. Local-hire-only is the policy, and nothing on his resume shows Canadian work rights. Merit score of 7/10 stands as informational only — it doesn't change the outcome.

## Candidate: Priya Jadon

Verdict: Disqualify — same hard filter (India-based, no Canadian work rights visible anywhere on the resume)
Merit score (informational, work-auth set aside): 6/10

## Why the merit score, if you want it for comparison

Software/SaaS fit: Strong. Three of her four roles are directly inside software companies — Tapp.ai (SaaS platform) at Quokka Labs, OpsMx (a DevOps/CI-CD software delivery platform), and GoHighLevel (CRM/marketing automation SaaS). Better software-specific fit than Siddhant.

SDR-native metrics: Genuinely strong, and this is the resume quality bar the framework asked for — 100+ demos/month, 80-90 calls/day, 65% demo-to-closure rate, 15-20 qualified meetings/month at one role, 10-15 at another, 35-40+ dials/day. Quantified, specific, not vague. This is exactly what I flagged as missing from Siddhant's resume.

NA-market selling signal: Direct and repeated — explicit USA-market focus at both OpsMx and Quokka Labs, plus UK/APAC/UAE elsewhere. Strong evidence on the lawful proxy we agreed to use.

Now the concerns:

Total experience is ~4.5 years (Jan 2022-Jul 2026) — above the 1-3 year band we set, and closer to the "lot of experience" you said you don't want.

Across those 4.5 years she's held four different SDR/BD-level roles (OpsMx, Quokka Labs, AGR, GoHighLevel) without ever stepping up to a closing/AE-equivalent title anywhere. That's the exact "SDR-capped" pattern I flagged last time as a red flag for your specific goal — if three-plus companies haven't promoted her yet, it's a real question why AskCruz would be different in 6-12 months.

Her most recent role, Demo Specialist at GoHighLevel, ran Jun 2026 to Jul 2026 — about one month, already ended. That's shorter than the 3.2-5.7 month SDR ramp time itself, meaning she left or was let go before she could plausibly have become productive. Worth a direct question if she ever reaches an interview elsewhere: what happened there.

Net: better raw sales-metric evidence than Siddhant, but the years-of-experience mismatch, the no-promotion-across-four-companies pattern, and the one-month stint that just ended are real drags against what you're actually trying to hire for. Both are disqualified today on work authorization regardless.
