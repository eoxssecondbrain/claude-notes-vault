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

1. **Where do the 167 resumes live right now?** (Folder on my computer / Email inbox / Google Drive / ATS or job board)
2. **What are the screening criteria?** (I have the JD — I'll paste it / I have explicit must-haves / You propose the rubric, I approve)
3. **What should the output be?** (Scored spreadsheet xlsx / Ranked shortlist only / Both)
4. **Rigor level?** (5 ft Quick / 10 ft Verified / 50 ft Deep)

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

**[AskUserQuestion — craft level]** Draft / Sketch / Painting / Commissioned

---

## User (answer)

- Craft: **Draft**

---

## Assistant

**[get_device_info — device desktop-5ncsbpq reachable, connectedFolders: [] (none), win32.]**

Your computer is reachable but no folder is connected yet. Tell me the folder path and I'll request access to just that one, or add it yourself via "Add folder".

Flagged: (a) defensibility — I'll record the specific criterion each score came from so every decision traces back to something on the resume; (b) I'll score against what the JD states, not age, gender, college tier as ability proxy, name, or location beyond a stated work-location requirement.

Planned first step: inventory the folder (count, formats, OCR-needed count) before scoring.

---

## User

how will it work for 167 resume, do i need to open new chat after every 10-15resumes so that you can screen every resume without losing the authenticy

---

## Assistant

No. Stay in this chat. Splitting into new chats every 10-15 would make the output worse, not better.

**How it works** — four stages: (1) Extract all 167 to plain text in one pass, near-zero context, also reveals which need OCR. (2) Freeze the rubric to a file on disk before any scoring; re-read at the start of every batch. (3) Score in batches of ~15-20, writing rows to disk immediately — results live in the file, not context, so batch 9 costs the same as batch 1. (4) Calibration pass over the borderline band after all 167, correcting for drift.

**Why a new chat per batch would hurt:** the judgment calls not captured in the rubric accumulate as we go. A fresh chat loses those — you'd get 11 mini-screenings with 11 slightly different bars, and rankings across batches wouldn't be comparable. That's the exact failure you're trying to avoid.

**The real risk** is rubric drift and false precision, not context loss. A 10-point score implies resolution resumes don't support; the difference between a 6 and a 7 is often noise. Also: I only see what's written down. A resume is a marketing document — I can tell you who's worth 20 minutes, not who's good.

**One thing worth saying:** 167 applicants for one associate role means the funnel is too wide. The higher-leverage fix is upstream — 3-4 knockout questions in the application form would have cut this to 40 before anyone read a resume.

---

## User

i will share pdf manually and will share the jd

---

## Assistant

That works, but manual attachment is the slowest of the three options.

**Best — zip the folder, attach one file.** One upload, I extract text from all 167 in one pass.
**Second — connect the folder.** Zero uploading; I can write results straight back into that folder.
**Third — attach manually.** Per-message file limit means ~10 separate uploads, each PDF processed as pages rather than extracted text.

Send the JD first whichever you pick — I'll build the rubric while files come across. Include the hard filters and whether this is EOXS or AskCruz.

---

## User

i will do it in batches per batch 5 resume. you already know about our company and what we need to make it better we are hiring marketing associate here is the JD

> **Marketing Associate — Email (Remote) | AskCruz | GFC Intelligence**
>
> **About the role:** AskCruz is an AI operating system for industrial and distribution businesses. We're hiring a Marketing Associate to own our email marketing engine — building and running the campaigns, sequences, and lists that drive our top-of-funnel pipeline into steel, plastics, and industrial distribution accounts.
>
> **What you'll do**
> - Build and send outbound email campaigns to targeted prospect lists (CEOs/decision-makers at 50-100 employee industrial and distribution companies)
> - Write and manage email sequences — cold outreach, nurture, and reactivation
> - Maintain list hygiene and manage lead data sourced from ZoomInfo and other sources
> - Track open, reply, and conversion rates and report weekly on what's working
> - Coordinate with the MBA intern team on research-first, personalized outreach execution
> - Manage domain/inbox health and deliverability so campaigns actually land in inboxes
> - Keep sends compliant with basic email marketing standards (CAN-SPAM, opt-outs, etc.)
>
> **What we're looking for**
> - Some hands-on experience running email marketing or outbound campaigns — tool-based execution, not just theory
> - Comfortable with email marketing/CRM tools (HubSpot, Mailchimp, Apollo, or similar)
> - Strong written English — you'll be writing the actual copy prospects read
> - Detail-oriented with lists and data — a bad list or a broken merge field costs us the whole send
> - Comfortable working remotely and reporting results without being chased
>
> If this role fits you, send an email to our CEO, Raj Jain (rajat@askcruz.com), answering why he should hire. He is assessing your ability based on how you approach this.
>
> **Nice to have**
> - Experience marketing to B2B/industrial buyers specifically
> - Familiarity with ZoomInfo or similar sales intelligence tools
> - Basic understanding of email deliverability (domain warming, SPF/DKIM, sender reputation)
> - **Compensation ₹20,000/month**

> Please refer to the job description above and the notes given below
>
> This position needs to be screened using Siv
>
> **Notes by Raj - Questions to ask them (close-ended questions):**
> - Their experience in marketing
> - Experience in Email marketing
> - What kind of emails did they send
> - What is account based marketing?

you need to qualify or disqualify and rate out of 10 and tell me how can we can make it work for 167 resumes without losing authenticity and compromising the data

---

## Assistant

**[Called get_index() — eoxs-db: 1,479 wiki pages, 30,536 email threads, 2,201 fireflies calls, 141 fathom calls, 8 clients, 824 implementation tasks. Called search_emails("Marketing Associate application email marketing", account="all").]**

**Key finding from the email search:** the `isha_zoho` inbox is receiving Naukri "Summary of Total Responses Received on <date>" digests containing per-applicant name, current role, years of experience, location, and key skills. Connected accounts visible: raj_gmail, ron_gmail, remya_gmail, support_zoho, isha_zoho. rajat@askcruz.com is not among them.

Read the JD. Before the rubric, three things in it change how this should run.

**The real filter is the email, not the resume**

The JD tells applicants to email rajat@askcruz.com arguing why he should be hired, and says he's assessing how they approach it. That is the actual test. A resume tells you someone lists "email marketing" as a skill; the email tells you whether they can write to a decision-maker — which is the entire job.

So the cheapest, highest-signal cut is free: of the 167, how many actually sent that email? If it's 40, you have your shortlist and 127 failed the first instruction. Screening 167 resumes before checking that is doing the expensive work first.

I can't see rajat@askcruz.com from here. Connected inboxes are raj_gmail, ron_gmail, remya_gmail, support_zoho and isha_zoho. Can you get me the list of who emailed Raj, or is that inbox connectable?

**Raj's four questions aren't resume criteria**

"Their experience in marketing" and "experience in email marketing" are visible on a resume. "What kind of emails did they send" and "what is account based marketing" are not — those are call or form questions. So the resume pass can only pre-qualify. Two of Raj's four can't be scored from a PDF, and I won't fake them.

**You already have structured applicant data**

The isha_zoho inbox is receiving Naukri "Summary of Total Responses Received" digests — name, current role, years of experience, location, key skills, per applicant. If these 167 came through Naukri, a large part of the screening data is already in the system in structured form, which is faster and more consistent than parsing 167 PDFs. Worth checking before you upload anything.

**Proposed rubric — approve or edit before I score anything**

Calibration note first: at ₹20,000/month you are not going to get three-year email marketers. If I score against the JD literally, almost everyone lands at 3/10 and the exercise tells you nothing. So the bar is calibrated to the realistic pool — the question is "has this person actually touched a sending tool", not "are they an expert".

Scoring, 10 points:

| Criterion | Points | What earns the top of the range |
|---|---|---|
| Email/outbound execution | 3 | Ran real campaigns or sequences; names the tool, the volume, or a result. Not "email marketing" in a skills list. |
| Tool fluency | 2 | HubSpot, Mailchimp, Apollo, Instantly, Lemlist, Outreach, Salesloft, ZoomInfo — named in a work context, not a course list |
| Written English (the resume itself) | 2 | Clean, specific, no template filler. The resume is the writing sample. |
| List and data discipline | 1.5 | CRM hygiene, segmentation, list building, merge fields, spreadsheet work |
| B2B / industrial relevance | 1 | B2B, manufacturing, distribution, industrial, or SMB SaaS buyers |
| Deliverability awareness | 0.5 | SPF, DKIM, domain warming, sender reputation — rare, treat as a bonus |

Bands:
- 8.0–10 — Qualify, interview
- 6.0–7.9 — Qualify, screening call with Raj's four questions
- 4.0–5.9 — Hold, revisit only if the top bands come up thin
- Below 4.0 — Disqualify

Auto-disqualify regardless of score: no email or outbound execution anywhere; multiple English errors in the resume itself; unavailable for remote; no contact details.

Flags reported but not scored: unexplained gaps over six months, three or more jobs in two years, claims with no tool or number attached, over-qualification that makes ₹20k a retention risk.

I score only against the JD. Not age, gender, college tier, name, or marital status. If a resume shows those, they're ignored, not weighted.

**On 167 without losing authenticity**

Batches of five means 34 rounds of back-and-forth. That's the plan most likely to fail — not because of quality, but because you'll abandon it around batch 12. Twenty per batch, nine rounds, is the same accuracy for a quarter of the effort. Or one zip and it's a single upload.

What keeps it authentic across whatever batch size:

The rubric above gets written to a file before batch one and re-read at the start of every batch. It doesn't drift because it isn't held in memory.

Every score gets a one-line justification quoting the actual resume — "Instantly.ai, 12k sends/month at Zenith" not "good email background". If a line can't be written, the score isn't defensible and gets flagged instead of guessed.

Results are appended to a file on disk after each batch, so batch 30 costs the same as batch 1 and nothing degrades.

After all 167, I re-read everything in the 5.0–7.0 band against the finished distribution and correct for drift. This is the step that catches me being harsher on Monday than Friday. Without it, batch-based scoring is not comparable across batches.

**On the data**

Resumes are PII — names, phone numbers, addresses. They stay in this session's sandbox and in your local folder. Nothing gets published to a shareable page, nothing goes to an external service. The output file lands in your folder, not in a link. If you want it somewhere shared later, that's your call to make explicitly, not my default.

**One thing I can't proceed on**

"This position needs to be screened using Siv" — I don't know what Siv is. Internal tool, vendor, a person, an acronym? It may change the whole workflow, so tell me before I build anything.

---

## Status / Next steps

- **Blocked on:** (a) what "Siv" is, (b) rubric approval, (c) the resume files.
- **Agreed parameters:** 50 ft deep rigor · Draft craft · rating out of 10 + qualify/disqualify.
- **Open recommendations to user:** check who actually emailed rajat@askcruz.com first (highest-signal, cheapest cut); check the Naukri digests in isha_zoho for structured applicant data before uploading PDFs; raise batch size from 5 to ~20 or use a single zip.
- **Execution model agreed:** rubric frozen to disk → score in batches writing results to disk incrementally → calibration pass over the 5.0–7.0 band at the end. One chat throughout.
- **Data handling:** resumes stay in session sandbox + user's local folder; no external publication of PII.
