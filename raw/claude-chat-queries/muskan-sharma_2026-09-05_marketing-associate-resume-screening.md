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

## Status / Next steps

- **Blocked on:** (a) folder access to the resume directory on desktop-5ncsbpq, (b) the JD text.
- **Agreed parameters:** 50 ft deep rigor · Draft craft · output = per-applicant rating out of 10 with qualify/disqualify decision.
- **Planned first step once unblocked:** inventory the folder (count, file formats, OCR-needed count) before running the scoring pass.
