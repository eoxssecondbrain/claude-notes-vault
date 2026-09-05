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

Ranked: (1) zip the folder, attach one file; (2) connect the folder; (3) attach manually — ~10 uploads, each PDF processed as pages rather than extracted text. Send the JD first.

---

## User

i will do it in batches per batch 5 resume. [PASTED FULL JD — Marketing Associate — Email (Remote), AskCruz | GFC Intelligence]

Key JD contents: own the email marketing engine; outbound campaigns to CEOs/decision-makers at 50-100 employee industrial and distribution companies; write cold outreach, nurture, reactivation sequences; list hygiene and ZoomInfo lead data; track open/reply/conversion and report weekly; coordinate with MBA intern team; manage domain/inbox health and deliverability; CAN-SPAM compliance. Looking for: hands-on email/outbound execution (tool-based, not theory); HubSpot/Mailchimp/Apollo or similar; strong written English; detail-oriented with lists and data; comfortable remote. Instruction to candidates: email CEO Raj Jain (rajat@askcruz.com) on why he should hire. Nice to have: B2B/industrial buyers, ZoomInfo, deliverability (domain warming, SPF/DKIM, sender reputation). Compensation ₹20,000/month.

Raj's notes — close-ended questions to ask: their experience in marketing; experience in email marketing; what kind of emails did they send; what is account based marketing?

"you need to qualify or disqualify and rate out of 10 and tell me how can we can make it work for 167 resumes without losing authenticity and compromising the data"

---

## Assistant

THE RUBRIC (out of 10): G1 Execution 3 · G2 Tools 2 · G3 Written English 2 · G4 Data/list discipline 1 · G5 B2B exposure 1 · G6 Deliverability 1.
BANDS: ≥8.0 interview · 6.0–7.9 screening call · 4.0–5.9 backup pool (DQ) · <4.0 DQ.
AUTO-DQ: zero campaign execution anywhere, or resume prose with prospect-visible errors.
FLAGS: gap >6mo, 3+ roles <12mo, comp/overqualification risk, metrics without context, template-generic, date contradictions.

Three things in the JD that change the approach: (1) the email to Raj is a live work sample worth more than the resume; (2) ₹20,000/month means over-qualification is a retention risk, realistic target 0–2 yrs; (3) Raj's four questions belong in a screening call, not the resume score.

Authenticity at 167: drift (fixed by rubric-on-disk + calibration pass over the 5.0–7.0 band), halo (fixed by independent gate scoring, arithmetic total, visible sub-scores), unfalsifiable reasons (fixed by citing the resume line behind every score).

On data: this conversation auto-saves to a GitHub vault every turn. Chat tables will use name + file number only; contact details stay in the local master file.

---

## User

The JD tells candidates to email Raj explaining why he should be hired, and says he'. no need to consider this point

---

## Assistant

Dropped. Resume-only scoring, no email signal, no penalty for not emailing Raj. Consequence: the score is entirely self-reported claims — treat the output as a triage list for who gets a call, not a ranking of who's good. Rubric stands. Send batch 1.

---

## User

[Uploaded 11.pdf, 12.pdf, 13.pdf, 14.pdf, 15.pdf] here is the first batch

---

## Assistant

**[Extracted all five PDFs to text with pdftotext -layout; all had real text layers, no OCR needed. Wrote RUBRIC.md and results.csv to /home/claude/screening/.]**

Batch 1 scored. All five extracted as real text, no OCR needed.

| File | Name | Exec /3 | Tools /2 | Eng /2 | Data /1 | B2B /1 | Deliv /1 | Total | Decision |
|---|---|---|---|---|---|---|---|---|---|
| 14 | Kajal Jakati | 3 | 2 | 2 | 1 | 1 | 1 | 10.0 | Qualify |
| 15 | Ragul Radhakrishnan | 3 | 2 | 2 | 1 | 1 | 1 | 10.0 | Qualify |
| 11 | Shakti Srivastava | 3 | 2 | 1 | 1 | 1 | 1 | 9.0 | Qualify |
| 13 | Anupama Singh | 2 | 1 | 1 | 0 | 1 | 0 | 5.0 | Disqualify |
| 12 | Sharan S. Bhadravathi | 0 | 0 | 1 | 0 | 0 | 0 | 1.0 | Disqualify |

14 — Kajal Jakati, Bengaluru, ~5 yrs. Strongest technical match in the batch. Built HONO's B2B SaaS email engine from scratch as sole owner, cold outbound to CHROs/CTOs/CFOs, Apollo + Instantly + HubSpot, and the only candidate who names SPF/DKIM/DMARC, domain warm-up and bounce management explicitly. Ran industry-specific campaigns into manufacturing and BFSI — closest thing in this batch to your industrial ICP.
Probe: the Globussoft stint (15 months, "Email Marketing Specialist") claims LinkedIn Ads, Meta Ads, Power BI, SMS, ABM, deliverability and an A/B framework. That's a wide scope for one specialist role in 15 months. Ask what she personally executed versus what the team did.

15 — Ragul Radhakrishnan, Chennai, 7+ yrs. Cleanest written English of the five, zero errors. Deep ESP experience: Oracle Eloqua end-to-end, HubSpot, Mailchimp, Omnisend, plus Openprise for dedup and enrichment.
Fit gap worth knowing: his depth is lifecycle and nurture — welcome series, abandoned cart, reactivation, a lot of it B2C retail. Your role is cold outbound to industrial CEOs. Different muscle. Deliverability is asserted in a skills bar but never demonstrated in a bullet. Also "Senior Process Associate" at HTC is a services-delivery title, so confirm whether he owns campaigns or executes tickets someone else scopes.

11 — Shakti Srivastava, Gorakhpur, 7+ yrs. Real ABM and outbound depth, Elastic Email sends, HubSpot–ZoomInfo integration, and inbox-placement/spam-trap work at AnovIP — directly relevant to your deliverability requirement. ZoomInfo experience is a JD nice-to-have he actually has.
Marked down on written English: "ABM Statergy", "Report updation", "Created dashboard and report on HubSpot to get summarize report". For a role where he writes the copy prospects read, that matters. Two gaps: 10 months in 2020, 5 months in 2025.

13 — Anupama Singh, Pune, ~7 months. MBA finishing 2026, doing real campaign execution at Pyxtech including email and lead nurture. Apollo.io is listed but with no evidence of what she did in it. No list hygiene, segmentation or CRM discipline anywhere.
The reason she's out rather than borderline: the resume has spacing and punctuation errors throughout — "market research ,campaign planning", "identification.Monitored". The JD says a broken merge field costs you the whole send. That's the exact failure mode this signals.
Counterpoint you should weigh: she is the only one in this batch who would actually accept ₹20,000/month. Keep her in the backup pool rather than rejecting outright.

12 — Sharan Shivaram Bhadravathi. Submitted a cover letter with no resume. No employer named, no tool, no campaign, no dates. Auto-disqualified on zero evidence of execution.
One check before you reject: it's possible the resume page failed to attach. If your source folder has a second file for this candidate, send it and I'll rescore.

The pattern you should be watching

Three of five score 9 or 10, and all three have five to seven years of experience. None of them will take ₹20,000/month. Kajal is a current Email Marketing Manager; Ragul and Shakti are seven-year specialists. Market for that profile in India is several times your budget.

So the real output of this batch isn't three qualified candidates. It's one signal: your top scorers are people who will decline, and the one person whose salary expectation fits scored a 5.

If that pattern holds through the next few batches, the constraint isn't screening quality — it's that the role is priced for a fresher and attracting seniors. Worth raising with Raj early rather than after you've screened 167 and shortlisted twelve people who all say no.

I'll keep scoring as-is and track it. If it repeats by batch four, I'd suggest a second scoring pass that weights affordability, so you get a shortlist of people who'll actually accept.

Running file is on my side; I'll build the xlsx once all batches are in. Send batch 2.

---

## Status / Next steps

- **Screened so far: 5 of 167.** Qualified 3 (files 14, 15, 11), disqualified 2 (13 backup pool, 12 auto-DQ).
- **Working files:** /home/claude/screening/RUBRIC.md (frozen rubric), /home/claude/screening/results.csv (running master), /home/claude/screening/txt/ (extracted resume text).
- **Rubric locked:** Execution 3 · Tools 2 · Written English 2 · Data discipline 1 · B2B exposure 1 · Deliverability 1. Qualify ≥ 6.0.
- **Open item:** file 12 may be a missing-resume upload — verify source folder before final reject.
- **Emerging signal to watch:** top scorers are 5–7 yr seniors who will not accept ₹20,000/month; the only affordable candidate scored 5.0. Re-assess by batch 4; may warrant an affordability-weighted second pass.
- **Deliverable plan:** xlsx built after all batches, plus calibration pass over the 5.0–7.0 band.
- **Next:** batch 2 (files 16–20 presumably).
