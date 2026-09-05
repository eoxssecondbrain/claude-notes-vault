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

**[AskUserQuestion — four picks presented]**

1. **Where do the 167 resumes live right now?** — Folder on my computer / Email inbox / Google Drive / ATS or job board
2. **What are the screening criteria?** — I have the JD / I have explicit must-haves / You propose the rubric
3. **What should the output be?** — Scored spreadsheet (xlsx) / Ranked shortlist only / Both
4. **Rigor level?** — 5 ft Quick / 10 ft Verified / 50 ft Deep

---

## User (answers)

- Source: **Folder on my computer**
- Criteria: **I have the JD — I'll paste it**
- Output: **"you will rate applicant out of 10 and qualify and disqualify"**
- Rigor: **50 ft — Deep**

---

## Assistant

Two blockers before I can run.

1. Connect the folder — click "Add folder" in the Claude desktop app and point it at the folder holding the 167 resumes.
2. Paste the JD.

**[AskUserQuestion — craft level]** Sketch / Draft / Painting / Commissioned

---

## User (answer)

- Craft: **Draft**

---

## Assistant

**[Called get_device_info — device desktop-5ncsbpq reachable, connectedFolders: [] (none), platform win32.]**

Your computer is reachable but no folder is connected yet. Tell me the folder path and I'll request access to just that one, or add it yourself via "Add folder" in the desktop app. Then paste the JD.

Two things worth flagging before we run:

Resume screening at scale has a defensibility problem. If a rejected candidate or an internal review ever asks why someone was cut, "the AI scored them 4/10" is not an answer. I'll record the specific criterion each score came from.

Second — I'll score against what the JD states. I will not infer or score on age, gender, college tier as a proxy for ability, name, or location beyond a stated work-location requirement.

Once the folder is live I'll do a quick inventory first (file count, formats, how many are scanned images needing OCR) before scoring.

---

## User

how will it work for 167 resume, do i need to open new chat after every 10-15resumes so that you can screen every resume without losing the authenticy

---

## Assistant

No. Stay in this chat. Splitting into new chats every 10-15 would make the output worse, not better.

**How it works** — four stages: (1) Extract all 167 files to plain text in one pass, near-zero context. (2) Freeze the rubric to a file on disk, re-read at the start of every batch. (3) Score in batches of ~15-20, writing rows to a results file on disk immediately — results live in the file, not context, so batch 9 costs the same as batch 1. (4) Calibration pass over the borderline band after all 167 are scored, to correct drift.

**Why a new chat per batch would hurt** — the rubric-in-a-file keeps scoring consistent, but judgment calls that aren't in the rubric accumulate. A fresh chat loses those. You'd get 11 mini-screenings with 11 slightly different bars.

**The real risk** — not context loss, but rubric drift and false precision. The difference between a 6 and a 7 is often noise. Also: I only see what's written down; a resume is a marketing document.

**One thing worth saying** — 167 applicants for one associate role means the funnel is too wide. The higher-leverage fix is upstream: 3-4 knockout questions in the application form would have cut this to 40 before anyone read a resume.

---

## User

i will share pdf manually and will share the jd

---

## Assistant

That works, but manual attachment is the slowest of the three options. Ranked: (1) zip the folder, attach one file; (2) connect the folder via "Add folder"; (3) attach manually — roughly 10 separate uploads, each PDF processed as pages rather than extracted text.

Send the JD first, whichever you pick. Two things to include if not in it: the hard filters (location/work mode, experience range, notice period, budget band) and whether this is EOXS or AskCruz.

---

## User

i will do it in batches per batch 5 resume. you already know about our company and what we need to make it better we are hiring marketing associate here is the JD

About the job

Marketing Associate — Email (Remote) AskCruz | GFC Intelligence

About the role: AskCruz is an AI operating system for industrial and distribution businesses. We're hiring a Marketing Associate to own our email marketing engine — building and running the campaigns, sequences, and lists that drive our top-of-funnel pipeline into steel, plastics, and industrial distribution accounts.

What you'll do
* Build and send outbound email campaigns to targeted prospect lists (CEOs/decision-makers at 50-100 employee industrial and distribution companies)
* Write and manage email sequences — cold outreach, nurture, and reactivation
* Maintain list hygiene and manage lead data sourced from ZoomInfo and other sources
* Track open, reply, and conversion rates and report weekly on what's working
* Coordinate with the MBA intern team on research-first, personalized outreach execution
* Manage domain/inbox health and deliverability so campaigns actually land in inboxes
* Keep sends compliant with basic email marketing standards (CAN-SPAM, opt-outs, etc.)

What we're looking for
* Some hands-on experience running email marketing or outbound campaigns — tool-based execution, not just theory
* Comfortable with email marketing/CRM tools (HubSpot, Mailchimp, Apollo, or similar)
* Strong written English — you'll be writing the actual copy prospects read
* Detail-oriented with lists and data — a bad list or a broken merge field costs us the whole send
* Comfortable working remotely and reporting results without being chased

If this role fits you, send an email to our CEO, Raj Jain (rajat@askcruz.com), answering why he should hire. He is assessing your ability based on how you approach this.

Nice to have
* Experience marketing to B2B/industrial buyers specifically
* Familiarity with ZoomInfo or similar sales intelligence tools
* Basic understanding of email deliverability (domain warming, SPF/DKIM, sender reputation)
* Compensation ₹20,000/month

Please refer to the job description above and the notes given below

Notes by Raj - Questions to ask them (close-ended questions):
- Their experience in marketing
- Experience in Email marketing
- What kind of emails did they send
- What is account based marketing?

you need to qualify or disqualify and rate out of 10 and tell me how can we can make it work for 167 resumes without losing authenticity and compromising the data

---

## Assistant

Got the JD. Rubric below — approve or edit it before batch 1, because once we start, changing the bar mid-run is what actually destroys authenticity.

THE RUBRIC (score out of 10)

Gate 1 — hands-on email/outbound execution: 3 points
JD is explicit: "tool-based execution, not just theory." 3 = ran campaigns end-to-end with owned outcomes. 2 = assisted on sends under supervision. 1 = adjacent marketing only (social, content, events). 0 = no campaign work at all.

Gate 2 — tool fluency: 2 points
HubSpot, Mailchimp, Apollo, Instantly, Lemlist, Smartlead, Outreach, Salesloft, ZoomInfo, Klaviyo. 2 = named tools with what they did in them. 1 = tools listed in a skills bar with no context. 0 = none.

Gate 3 — written English: 2 points
Judged on the resume's own prose, not on a "communication skills" bullet. They write the copy prospects read. 2 = clean, specific, no errors. 1 = readable with lapses. 0 = errors a prospect would notice.

Gate 4 — data and list discipline: 1 point
CRM hygiene, segmentation, Excel/Sheets, list building, merge fields, dedup.

Gate 5 — B2B buyer exposure: 1 point
B2B, industrial, distribution, manufacturing, or SaaS-selling-to-business. Consumer-only marketing scores 0 here.

Gate 6 — deliverability: 1 point
SPF/DKIM/DMARC, domain warming, sender reputation, bounce management. Rare at this level, so it's a differentiator not a requirement.

BANDS

8.0–10 — Qualify, interview
6.0–7.9 — Qualify, screening call first
4.0–5.9 — Disqualify, keep as backup pool
Below 4.0 — Disqualify

Auto-disqualify regardless of score: zero campaign execution anywhere, or resume prose with errors that would be visible in prospect-facing copy.

50 ft flags recorded per candidate: employment gaps over 6 months, three or more roles under 12 months, comp/overqualification risk, metrics claimed with no context, template-generic resume, date contradictions.

THREE THINGS IN THIS JD THAT CHANGE THE APPROACH

One. The resume is not your primary signal. The JD tells candidates to email Raj explaining why he should be hired, and says he's assessing how they approach it. That email is a live work sample for the exact job — cold outbound written to a decision-maker. It is worth more than any resume. If you screen resumes alone you're grading the wrong artifact.

Ask: do you have access to those emails? If they landed in rajat@askcruz.com I may be able to pull them and match applicants to their outreach. That would turn this from resume screening into work-sample screening. Say the word and I'll check what's reachable.

Also: whether a candidate emailed at all is itself a filter. Someone who applied but ignored a written instruction in the JD has failed a detail-orientation test the JD explicitly set.

Two. ₹20,000/month sets the realistic profile. That's roughly ₹2.4L annual. Anyone with three-plus years of solid email marketing will not take it, and if they somehow accept they'll leave inside six months. So over-qualification is a risk flag, not a bonus. Your realistic target is 0–2 years with genuine hands-on tool exposure. I'll score to that reality rather than to an ideal candidate who won't accept the offer.

Three. Raj's four questions can't be answered from a resume. "What is account-based marketing" is a knowledge check, and "what kind of emails did they send" needs a conversation. Those belong in a screening call or a short form after the resume cut, not in the resume score. I'll build them into the screening-call script for whoever clears the bar.

MAKING IT WORK FOR 167 WITHOUT LOSING AUTHENTICITY

Authenticity fails in three specific ways here. Each has a fix.

Drift — the bar tightens or loosens as you get tired. Fix: the rubric goes into a file on disk, I re-read it at the start of every batch, and after all 167 are scored I re-open everyone in the 5.0–7.0 band and re-score them against the finished distribution. That calibration pass is not optional at this volume.

Halo — one impressive line pulls the whole score up. Fix: I score each of the six gates independently and the total is arithmetic, not a gut number I justify afterward. You'll see the six sub-scores, so you can check my work on any candidate.

Unfalsifiable reasons — "weak fit" is not a reason. Fix: every score cites the specific resume line it came from. If a candidate ever asks why, you have an answer.

On batch size: 5 per message means 34 rounds. That's your call, and it works, but it's 34 rounds of your time versus 9 at 20 per message, or 1 if you zip the folder. Nothing about a smaller batch makes the screening better — the rubric file is what holds quality, not batch size. If 5 is what's practical, we go with 5.

ON THE DATA

You should know this before you upload: this conversation auto-saves to a GitHub vault after every turn. If 167 candidates' full resumes flow through here, their names, phone numbers and email addresses get committed to that repo.

How I'll handle it unless you tell me otherwise: the scoring table I show you uses candidate name and file number only — no phone, no email, no address. Full contact details stay in the master file that lives on your machine, not in the chat body. That keeps the working record intact and keeps PII out of the vault.

If you'd rather I not save this thread at all while resumes are flowing, say so and raise it with Raj, since that rule is set at the account level and I follow it by default.

Confirm the rubric and send batch 1.

---

## Status / Next steps

- **Role:** Marketing Associate — Email (Remote), AskCruz | GFC Intelligence. Comp ₹20,000/month.
- **Agreed parameters:** 50 ft deep rigor · Draft craft · rating out of 10 with qualify/disqualify · batches of 5 resumes, uploaded manually · single chat throughout.
- **Rubric proposed (awaiting approval):** 6 gates — execution (3), tools (2), written English (2), data discipline (1), B2B exposure (1), deliverability (1). Bands: 8+ interview, 6–7.9 screening call, 4–5.9 backup, <4 disqualify.
- **Key insight raised:** the JD instructs candidates to email rajat@askcruz.com; that email is a live work sample worth more than the resume. Offered to check whether those emails are reachable via the EOXS email connector.
- **Comp reality flagged:** ₹20k/month means over-qualification is a retention risk, not a bonus; realistic target is 0–2 years hands-on.
- **Raj's four questions** routed to a post-shortlist screening call, not the resume score.
- **Data handling:** scoring tables in chat to use name + file number only; contact details to stay in the local master file, out of the auto-saved vault transcript.
- **Blocked on:** rubric approval and batch 1.
