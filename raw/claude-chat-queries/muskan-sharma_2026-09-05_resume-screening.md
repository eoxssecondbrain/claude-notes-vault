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
