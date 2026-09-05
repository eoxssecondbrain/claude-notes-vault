---
thread_name: "marketing-associate-resume-screening"
user: "muskan-sharma"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

# Marketing Associate — Resume Screening (167 applicants)

**Thread:** marketing-associate-resume-screening
**Date:** 2026-09-05
**User:** Muskan Sharma (HR intern, EOXS) — muskan@askcruz.com

---

## User

can you help in screening resume of 167 job applicants of marketing associate

---

## Assistant

Before I start, four things I need. No folder is connected to this session yet and nothing's attached, so I can't see the resumes.

**[AskUserQuestion — four picks]** 1. Where do the resumes live? 2. What are the screening criteria? 3. What should the output be? 4. Rigor level?

---

## User (answers)

- Source: **Folder on my computer**
- Criteria: **I have the JD — I'll paste it**
- Output: **"you will rate applicant out of 10 and qualify and disqualify"**
- Rigor: **50 ft — Deep**

---

## Assistant

Two blockers: connect the folder, paste the JD. **[AskUserQuestion — craft level]**

Flagged: resume screening at scale has a defensibility problem — I'll record the specific criterion each score came from. And I'll score against what the JD states, not age, gender, college tier as ability proxy, name, or location beyond a stated work-location requirement.

---

## User (answer)

- Craft: **Draft**

---

## Assistant

**[get_device_info — desktop-5ncsbpq reachable, connectedFolders: [], win32]** Folder not connected. Tell me the path or use "Add folder". Then paste the JD.

---

## User

how will it work for 167 resume, do i need to open new chat after every 10-15resumes so that you can screen every resume without losing the authenticy

---

## Assistant

No. Stay in this chat. Four stages: extract all files to text in one pass; freeze the rubric to a file on disk and re-read it every batch; score in batches writing results to disk immediately (results live in the file, not context); calibration pass over the borderline band at the end.

A new chat per batch loses the accumulated judgment calls that aren't in the rubric — you'd get 11 mini-screenings with 11 slightly different bars.

Real risk is rubric drift and false precision, not context loss. Also: 167 applicants for one associate role means the funnel is too wide; the upstream fix is 3-4 knockout questions in the application form.

---

## User

i will share pdf manually and will share the jd

---

## Assistant

Ranked: (1) zip the folder, attach one file; (2) connect the folder; (3) attach manually. Send the JD first.

---

## User

i will do it in batches per batch 5 resume. [PASTED FULL JD — Marketing Associate — Email (Remote), AskCruz | GFC Intelligence]

Key JD contents: own the email marketing engine; outbound campaigns to CEOs/decision-makers at 50-100 employee industrial and distribution companies; cold outreach, nurture, reactivation sequences; list hygiene and ZoomInfo lead data; track open/reply/conversion, report weekly; coordinate with MBA intern team; manage domain/inbox health and deliverability; CAN-SPAM compliance. Looking for: hands-on email/outbound execution (tool-based, not theory); HubSpot/Mailchimp/Apollo or similar; strong written English; detail-oriented with lists and data; comfortable remote. Nice to have: B2B/industrial buyers, ZoomInfo, deliverability (domain warming, SPF/DKIM, sender reputation). Compensation ₹20,000/month.

Raj's notes — close-ended questions: their experience in marketing; experience in email marketing; what kind of emails did they send; what is account based marketing?

"you need to qualify or disqualify and rate out of 10 and tell me how can we can make it work for 167 resumes without losing authenticity and compromising the data"

---

## Assistant

THE RUBRIC (out of 10): G1 Execution 3 · G2 Tools 2 · G3 Written English 2 · G4 Data/list discipline 1 · G5 B2B exposure 1 · G6 Deliverability 1.
BANDS: ≥8.0 interview · 6.0–7.9 screening call · 4.0–5.9 backup pool (DQ) · <4.0 DQ.
AUTO-DQ: zero campaign execution anywhere, or resume prose with prospect-visible errors.
FLAGS: gap >6mo, 3+ roles <12mo, comp/overqualification risk, metrics without context, template-generic, date contradictions.

Three things in the JD that change the approach: (1) the email to Raj is a live work sample worth more than the resume; (2) ₹20,000/month means over-qualification is a retention risk, realistic target 0–2 yrs; (3) Raj's four questions belong in a screening call.

Authenticity at 167: drift (rubric-on-disk + calibration pass over the 5.0–7.0 band), halo (independent gate scoring, arithmetic total, visible sub-scores), unfalsifiable reasons (cite the resume line behind every score).

On data: this conversation auto-saves to a GitHub vault every turn. Chat tables use name + file number only; contact details stay in the local master file.

---

## User

The JD tells candidates to email Raj explaining why he should be hired, and says he'. no need to consider this point

---

## Assistant

Dropped. Resume-only scoring. Consequence: the score is entirely self-reported claims — treat the output as a triage list for who gets a call, not a ranking of who's good. Rubric stands. Send batch 1.

---

## User

[Uploaded 11.pdf–15.pdf] here is the first batch

---

## Assistant

**[Extracted all five with pdftotext -layout; real text layers, no OCR. Wrote RUBRIC.md and results.csv to /home/claude/screening/.]**

| File | Name | Exec /3 | Tools /2 | Eng /2 | Data /1 | B2B /1 | Deliv /1 | Total | Decision |
|---|---|---|---|---|---|---|---|---|---|
| 14 | Kajal Jakati | 3 | 2 | 2 | 1 | 1 | 1 | 10.0 | Qualify |
| 15 | Ragul Radhakrishnan | 3 | 2 | 2 | 1 | 1 | 1 | 10.0 | Qualify |
| 11 | Shakti Srivastava | 3 | 2 | 1 | 1 | 1 | 1 | 9.0 | Qualify |
| 13 | Anupama Singh | 2 | 1 | 1 | 0 | 1 | 0 | 5.0 | Disqualify |
| 12 | Sharan S. Bhadravathi | 0 | 0 | 1 | 0 | 0 | 0 | 1.0 | Disqualify |

14 — Kajal Jakati, Bengaluru, ~5 yrs. Built HONO's B2B SaaS email engine from scratch as sole owner, cold outbound to CHROs/CTOs/CFOs, Apollo + Instantly + HubSpot, only candidate naming SPF/DKIM/DMARC, domain warm-up and bounce management. Industry campaigns into manufacturing and BFSI — closest to your industrial ICP. Probe: Globussoft stint (15 months, "Email Marketing Specialist") claims LinkedIn Ads, Meta Ads, Power BI, SMS, ABM, deliverability and an A/B framework — wide scope for one role; ask what she personally executed.

15 — Ragul Radhakrishnan, Chennai, 7+ yrs. Cleanest written English, zero errors. Oracle Eloqua end-to-end, HubSpot, Mailchimp, Omnisend, Openprise dedup/enrichment. Fit gap: depth is lifecycle and nurture — welcome series, abandoned cart, reactivation, much of it B2C retail. Your role is cold outbound to industrial CEOs. Deliverability asserted in a skills bar, never demonstrated. "Senior Process Associate" at HTC is a services-delivery title — confirm he owns campaigns rather than executing tickets.

11 — Shakti Srivastava, Gorakhpur, 7+ yrs. Real ABM and outbound depth, Elastic Email sends, HubSpot–ZoomInfo integration, inbox-placement/spam-trap work at AnovIP. ZoomInfo is a JD nice-to-have he actually has. Marked down on written English: "ABM Statergy", "Report updation", "Created dashboard and report on HubSpot to get summarize report". Two gaps: 10 months in 2020, 5 months in 2025.

13 — Anupama Singh, Pune, ~7 months. MBA finishing 2026, real campaign execution at Pyxtech including email and lead nurture. Apollo.io listed with no evidence of use. No list hygiene, segmentation or CRM discipline. Out rather than borderline because of spacing and punctuation errors throughout — "market research ,campaign planning", "identification.Monitored" — the exact failure mode the JD warns about. Counterpoint: only one in the batch who would accept ₹20,000/month. Keep in backup pool.

12 — Sharan Shivaram Bhadravathi. Cover letter with no resume. No employer, tool, campaign or date. Auto-DQ. Check whether the resume page failed to attach.

The pattern: three of five score 9 or 10, all with five to seven years. None will take ₹20,000/month. The one person whose salary fits scored a 5.

---

## User

[Uploaded 16.pdf–20.pdf] 2 / Continue from where you left off.

---

## Assistant

Batch 2 scored.

| File | Name | Exec /3 | Tools /2 | Eng /2 | Data /1 | B2B /1 | Deliv /1 | Total | Decision |
|---|---|---|---|---|---|---|---|---|---|
| 18 | Amit Singh | 3 | 2 | 2 | 1 | 1 | 1 | 10.0 | Qualify |
| 20 | Rahul D Jadhav | 3 | 2 | 2 | 1 | 0 | 1 | 9.0 | Qualify |
| 16 | Suryadev Kumar Sah | 1 | 0 | 2 | 0 | 1 | 0 | 4.0 | Disqualify |
| 17 | Kanav Kundra | 0 | 1 | 2 | 1 | 1 | 0 | 4.0 | Disqualify |
| 19 | Nishtha Bhasin | 1 | 0 | 2 | 0 | 0 | 0 | 3.0 | Disqualify |

18 — Amit Singh, Hyderabad, 4 yrs at AgileEngine. Best functional match across both batches. Ran cold outbound on Instantly — the exact tool category your role needs — plus domain setup, ESP configuration, email warming and DKIM/SPF/DMARC done himself, not listed as a buzzword. Zoho CRM workflows and segmentation. Two things to probe: no numbers anywhere on the resume across four years ("increased open rates and CTR" with no figure) — ask for actual open and reply rates on his last campaign; and the resume gives almost no prose to judge writing on, so ask for a cold email sample before interviewing. Left AgileEngine April 2026, out about four months.

20 — Rahul D Jadhav, Mumbai, 5 yrs at Uplers/Mavlers. Cleanest writing of the ten, real deliverability discipline (99% inbox rate, ESP warmup, Email on Acid pre-send testing), genuine depth in Klaviyo and Iterable. Scored 9 but the fit is weaker than the number: every account named is B2C — Business Insider, Line Friends, a supermarket chain. His entire career is lifecycle marketing to opted-in subscriber lists: welcome flows, abandoned cart, win-back. Your role is cold outbound to industrial CEOs who never subscribed to anything. Different jobs that share tools. Strong at sending mechanics, untested at the part that generates your pipeline.

16 — Suryadev Kumar Sah, Bengaluru. "Email Marketing" appears once, in a skills bar. Not one bullet in six roles describes an email campaign. Actual work is school partnerships, lead generation and social media. No ESP, no CRM. Separate concern: five roles since 2021 including a one-month stint at Smart Learn and two five-month stints.

17 — Kanav Kundra, Amritsar. Auto-disqualified. Business analyst and project manager — Oracle ERP implementations, penetration-testing project management. HubSpot appears, but used to post project status updates, not to run campaigns. The Dabur "marketing internship" was two months of retail field work. Also a declared twelve-month career break through 2025, then three months at Breachlock ending April 2026, unemployed since. Wrong function regardless.

19 — Nishtha Bhasin, Noida. BBA fresher, three internships of one to two months each, all support-level. No email marketing anywhere. Tools are Excel, PowerPoint and Canva. Worth flagging: MaxView Now is dated June–July 2025 and PeopleBridge is also dated June–July 2025 — two full-time internships at two companies in the same two months. Might be genuine parallel part-time work, might be padding. For a role where accuracy in a list is the core requirement, an unexplained overlap on your own resume is a bad sign.

Running position: 10 of 167

Five qualified, five disqualified. But the qualifiers' experience is 7, 5, 7, 4, 5 years. Every single one.

Ten resumes in, the number of candidates who both clear the bar and would plausibly accept ₹20,000/month is zero. Not low — zero. The three people whose salary expectations fit scored 5.0, 4.0 and 3.0.

That's no longer a small sample. It's a consistent structural result: the screening is working correctly while the funnel is broken. You will finish 167 resumes with a clean, defensible shortlist of a dozen people who decline the offer.

Second pattern, quieter but real: of the five qualifiers, two (Ragul and Rahul) are B2C lifecycle marketers, not cold-outbound operators. So the effective shortlist for the job as written is three, not five.

What I'd do with this: stop and take it to Raj now, at 10 resumes, rather than at 167. The question isn't "who's good" — it's which of these you're actually buying:

- ₹20,000/month buys a fresher you train. Then the rubric is wrong: drop the execution requirement, weight written English and detail-orientation, hire for trainability. I can rescore on that basis.
- The role needs someone who can run outbound unsupervised from day one. Then the budget is wrong, and the number is probably ₹45,000–70,000/month for the Amit Singh profile.

Screening 157 more resumes against a bar the budget can't buy is the low-leverage path. Twenty minutes with Raj resolves it.

Tell me which way it goes and I'll adjust the rubric. If you want me to keep going as-is in the meantime, say so and send batch 3 — I'll keep tracking both scores so nothing is wasted either way.

---

## Status / Next steps

- **Screened: 10 of 167.** Qualified 5 (files 11, 14, 15, 18, 20). Disqualified 5 (12, 13, 16, 17, 19). Average score 6.5.
- **Working files:** /home/claude/screening/RUBRIC.md (frozen rubric), /home/claude/screening/results.csv (running master, 10 rows), /home/claude/screening/txt/ (extracted text).
- **Qualifier experience profile: 7, 5, 7, 4, 5 years — zero affordable qualifiers at ₹20,000/month.**
- **Secondary finding:** two of five qualifiers (15 Ragul, 20 Rahul) are B2C lifecycle marketers with no cold-outbound experience. Effective shortlist is 3, not 5.
- **Escalation raised to user:** take the budget-vs-bar mismatch to Raj now rather than after 167. Two paths offered — rescore for trainability at ₹20k, or revise budget to ₹45–70k for the proven-operator profile.
- **Open item:** file 12 may be a missing-resume upload — verify source folder before final reject.
- **Awaiting:** user decision on rubric direction, and batch 3 (files 21–25).
