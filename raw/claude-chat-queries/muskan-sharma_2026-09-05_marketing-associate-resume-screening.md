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

1. **Where do the 167 resumes live right now?**
   - Folder on my computer — PDFs/DOCs in a local folder; you'd add that folder via "Add folder" in the desktop app so I can read them directly.
   - Email inbox / Zoho — Attachments sitting in an inbox. I'd need to pull them via the EOXS email connector or you export them.
   - Google Drive / cloud folder — I'd need a connector or you download them into a local folder first.
   - ATS or job board — LinkedIn, Naukri, Indeed, or similar; I'd need an export or browser access.

2. **What are the screening criteria? I need a bar to score against, not a vibe.**
   - I have the JD — I'll paste it. You give me the job description and I derive must-haves, nice-to-haves, and disqualifiers from it.
   - I have explicit must-haves — You list the hard filters (years, skills, location, notice period, salary band) and I apply exactly those.
   - You propose the rubric, I approve — I draft a scoring rubric for a marketing associate at EOXS based on what I can find internally, you edit it before I run.

3. **What should the output be?**
   - Scored spreadsheet (xlsx) — One row per candidate: name, contact, score per criterion, total, tier (A/B/C/reject), one-line reason. Sortable, filterable.
   - Ranked shortlist only — Top N candidates with a short write-up each. Faster, but you lose visibility into who got cut and why.
   - Both — Full scored sheet plus a shortlist doc of the top tier with interview notes.

4. **Rigor level for the screening pass?**
   - 5 ft — Quick: Keyword/criteria match per resume, single pass, no cross-checking. Fastest for 167 files.
   - 10 ft — Verified: Same scoring, but every material claim (years of experience, titles, gaps) read off the actual resume text rather than a keyword hit. Flags inconsistencies.
   - 50 ft — Deep: Verified, plus adjacent signals: employment gaps, job-hopping, over/under-qualification, portfolio links checked where present, risk flags per candidate.

---

## User (answers)

- Source: **Folder on my computer**
- Criteria: **I have the JD — I'll paste it**
- Output: **"you will rate applicant out of 10 and qualify and disqualify"**
- Rigor: **50 ft — Deep**

---

## Assistant

Two blockers before I can run.

1. Connect the folder — click "Add folder" in the Claude desktop app and point it at the folder holding the 167 resumes. I'll get a notice here once it's added.
2. Paste the JD.

One more pick while you do that:

**[AskUserQuestion — craft level]**

**Craft level for the deliverable (the scored output file)?**
- Draft — Clean xlsx: one row per candidate, score /10, qualify/disqualify, reason, key flags. Sorted by score. Functional and presentable.
- Sketch — Bare table dump, no formatting. Fastest.
- Painting — Formatted xlsx with conditional colour bands by tier, per-criterion sub-scores, filters, a summary tab with funnel counts and criteria breakdown.
- Commissioned — Painting plus a separate shortlist doc with interview probe questions per A-tier candidate and a documented rubric page for audit/fairness defensibility.

---

## User (answer)

- Craft: **Draft**

---

## Assistant

**[Called get_device_info — device desktop-5ncsbpq reachable, connectedFolders: [] (none), platform win32. Home directories visible include Desktop, Documents, Downloads, OneDrive.]**

Your computer is reachable but no folder is connected yet. Tell me the folder path (e.g. `Downloads\Marketing Associate Resumes`) and I'll request access to just that one, or add it yourself via "Add folder" in the desktop app.

Then paste the JD.

Two things worth flagging before we run:

Resume screening at scale has a defensibility problem. If a rejected candidate or an internal review ever asks why someone was cut, "the AI scored them 4/10" is not an answer. I'll record the specific criterion each score came from so every decision traces back to something on the resume. Tell me if you want that.

Second — I'll score against what the JD states. I will not infer or score on age, gender, college tier as a proxy for ability, name, or location beyond a stated work-location requirement. If your JD includes something like that, I'll flag it rather than silently apply it.

Once the folder is live I'll do a quick inventory first (file count, formats, how many are scanned images needing OCR) before scoring, since 167 files at 50 ft depth is a real run and I'd rather know the shape of the data before committing.

---

## Assistant (waiting note)

Waiting on the folder and the JD.

---

## User

how will it work for 167 resume, do i need to open new chat after every 10-15resumes so that you can screen every resume without losing the authenticy

---

## Assistant

No. Stay in this chat. Splitting into new chats every 10-15 would make the output worse, not better — here's why, and how it actually works.

**How it works**

I don't hold 167 resumes in my head at once. The run is four stages:

1. **Extract.** A script converts all 167 files to plain text on your machine in one pass. No reading, no scoring, near-zero context used. This also tells me which files are scanned images that need OCR.

2. **Freeze the rubric.** Before any scoring, I write the rubric to a file on disk — the criteria derived from your JD, the weight of each, and what a 3 vs a 7 vs a 9 looks like. This file is the standard, and I re-read it at the start of every batch.

3. **Score in batches of ~15-20.** I read that batch's text, score against the rubric, and immediately write the rows to a results file on disk. Then I move to the next batch. The results live in the file, not in my context — so batch 9 costs the same as batch 1, and nothing degrades as we go.

4. **Calibration pass.** After all 167 are scored, I re-read the borderline band (roughly 5-7 out of 10) against the finished distribution and correct for drift. This is the step that catches "I was stricter on Monday's batch than Friday's."

**Why a new chat per batch would hurt**

The rubric-in-a-file is what keeps scoring consistent, but the judgment calls that aren't in the rubric — how much a specific agency background is worth, whether a certain kind of gap matters — accumulate as we go. A fresh chat loses those. You'd get 11 mini-screenings with 11 slightly different bars, and the rankings across batches wouldn't be comparable. That's the exact failure you're trying to avoid.

**The real risk**

It isn't context loss. It's rubric drift and false precision. A 10-point score implies a resolution that resumes don't actually support — the difference between a 6 and a 7 is often noise. I'd rather score to bands (strong / possible / no) and use the /10 as a sort key inside those bands. Tell me if you want it that way or strict /10 as you asked.

Second: I only see what's written down. A resume is a marketing document. At 50 ft I'll flag inconsistencies and unverifiable claims, but I can't tell you who's good — only who's worth 20 minutes of your time.

**One thing worth saying**

167 applicants for one associate role means the funnel is too wide, not that you have a great pipeline. Screening them is your job this week; the higher-leverage fix is upstream — 3-4 knockout questions in the application form would have cut this to 40 before anyone read a resume. Worth raising once this batch is done.

Still blocked on the folder path and the JD.

---

## Status / Next steps

- **Blocked on:** (a) folder access to the resume directory on desktop-5ncsbpq, (b) the JD text.
- **Agreed parameters:** 50 ft deep rigor · Draft craft · output = per-applicant rating out of 10 with qualify/disqualify decision.
- **Open question to user:** strict /10 as originally asked, vs bands (strong/possible/no) with /10 as an in-band sort key.
- **Planned execution model:** extract-to-text pass → freeze rubric to disk → score in batches of 15-20 writing results to disk incrementally → final calibration pass over the borderline band. All in one chat; no need to split conversations.
