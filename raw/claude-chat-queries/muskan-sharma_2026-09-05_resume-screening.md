---
thread_name: "resume-screening"
user: "muskan-sharma"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

User: can you help in screening resume of job applicants and its 160+ candidiates

Assistant: This is an HR/recruiting task, not a sales or EOXS-business-data query, so it doesn't clearly fall under sales-strategist or the eoxs-data-general (raj-eoxs-vault) skill — flagging that per your rule rather than assuming. I'll treat it as a standalone task, unless the resumes themselves live inside EOXS systems (e.g. arrived as email attachments), in which case eoxs-data-general's read-only connector would be the way to pull them.

Before I start on 160+ resumes, I need two things in plain text from you (not a button pick):

1. The role and either a job description or a clear list of must-have / nice-to-have criteria — years of experience, specific skills, education, location, anything else that should filter candidates. This is the single biggest lever on screening quality; vague criteria produce a useless screen no matter how carefully I read each resume.
2. Confirmation of how the resumes will actually reach me (upload them as files here is the most reliable route for 160+ files).

Separately, three quick picks below will settle the mechanics.

[Interactive question widget shown to user:]
Q1: Where are the 160+ resumes?
Options: Uploading as files here / Email inbox (EOXS connector) / Google Drive / another link / Not gathered yet

Q2: What output do you want from the screen?
Options: Ranked/scored list / Yes / Maybe / No buckets / Top N shortlist only / Full sheet with notes per candidate

Q3: Rigor level for the screening logic itself?
Options: 5ft - quick keyword/criteria pass / 10ft - verified read against JD / 50ft - deep, also flags red flags/gaps / 100ft - staged, delivered in batches

User: Q: Where are the 160+ resumes?
A: Uploading as files here

Q: What output do you want from the screen?
A: Full sheet with notes per candidate

Q: Rigor level for the screening logic itself?
A: 50ft - deep, also flags red flags/gaps

Assistant: Rigor set: 50 ft — deep, verified read of each resume against criteria, plus flags for red flags and gaps. Output: full sheet with notes per candidate.

Still missing, and blocking the start:

1. The role and the actual criteria — job description or your own must-have / nice-to-have list (experience, skills, education, location, whatever matters). No sheet without this to screen against.
2. The resume files — none have come through yet. Upload them here; batches are fine if 160+ won't fit in one go.

One more quick pick, since the output is a formatted deliverable — craft level for the sheet.

[Interactive question widget shown to user:]
Q: Craft level for the candidate sheet?
Options: Sketch - bare structure, no polish / Draft - clean, functional, presentable / Painting - custom, detail-checked / Commissioned - full polish, edge cases covered

User: Q: Craft level for the candidate sheet?
A: Draft - clean, functional, presentable

Assistant: Craft level locked: Draft.

Two items are still outstanding and nothing can start without them:

1. Job description or must-have/nice-to-have criteria for the role — paste it or list it out.
2. The resume files — checked, none have landed here yet. Upload them (batches are fine).

Send both and I'll begin the screen.

User: i will send them later . now im just trying to find if you can help, if yes then how

Assistant: Yes, this is well within scope. Here's how it works once you send the JD/criteria and files:

1. You upload the resumes (PDF/docx, individually or in a batch/zip) plus the job description or criteria list.
2. I read each resume against the criteria — required skills, experience level, education, location, whatever you specify.
3. At 50 ft rigor, I don't just keyword-match: I check the actual content, flag red flags (employment gaps, job-hopping, mismatched titles vs claimed seniority, inflated claims, missing basics the JD requires) and adjacent risks you didn't explicitly ask about but that affect fit.
4. I compile it into one xlsx sheet — one row per candidate, columns for name, key qualifications, fit against each major criterion, red flags/gaps, and an overall verdict (or ranking, depending on what you want in the final column). Draft craft level means it's clean and usable, not a design exercise.

Practical notes for 160+ resumes:

- If they're all in one zip, that's easiest — I extract and process in one pass.
- If formats vary (PDF, docx, scanned images), scanned/image-only resumes take longer since they need OCR — flag if any are like that.
- For a set this size I'll likely process and report in batches so you can sanity-check the approach on the first 20-30 before I run the rest, rather than surface one giant sheet at the end with a systemic error baked in. Your call whether you want that checkpoint or a single final pass.

Send the JD and files whenever you're ready.

User: i will share it in pdf format and how will you process 167 candidates resume without losing authenticity

Assistant: For born-digital PDFs (text-based, not scanned image), I extract the actual text directly — no OCR guessing, no paraphrasing at the extraction stage. Whatever the resume states is what goes into the sheet.

Fidelity safeguards specific to this job:

- No inference beyond what's written. If a resume says "familiar with Excel," it gets recorded as stated — not upgraded to "advanced" or expanded into related skills the candidate didn't claim.
- Experience is calculated from the actual employment history listed, not from a claimed summary line. If someone writes "5 years experience" but the listed jobs only total 3, that gap gets flagged as a discrepancy rather than silently accepted or silently corrected.
- Every fit/no-fit call against your criteria traces back to something written in that specific resume. If the information needed for a criterion just isn't there, the sheet says "not stated" — not a guessed yes or no.
- Names, titles, companies, and dates are copied verbatim, not reworded or summarized, so nothing drifts across 167 separate extractions.

The real risk case is scanned/image-only PDFs with no extractable text layer — those need OCR, which can misread digits in dates or garble names. If any of your 167 are scans rather than typed/exported PDFs, I'll flag those specific rows so you know which ones need a manual glance instead of trusting OCR output at the same confidence as clean text.

At this volume I'll also work in batches of roughly 20-30 rather than one long uninterrupted run — that way if something in my extraction logic is off, it shows up on batch one instead of silently repeating across all 167.
