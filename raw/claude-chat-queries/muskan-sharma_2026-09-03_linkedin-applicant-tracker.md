---
thread_name: "linkedin-applicant-tracker"
user: "muskan-sharma"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# Linkedin Applicant Tracker

## Turn 1

**User:**
I'm given a task to add resume and screening questions of the applicants applied for the job on linkedin on google sheet and  also add name, gmail and contact if i copy paste resume can you help with it

**Assistant:**
This doesn't clearly match eoxs-data-general (that's scoped to EOXS business/CRM/client data) or sales-strategist (not a sales task) — treating it as a standalone HR data-entry task, flagging that per your instruction rather than guessing.

Second thing: I don't have a live Google Sheets connector active right now, so "add it to Google Sheet" could mean a few different things depending on your actual setup. Need to pin that down plus the row structure before I start pulling fields out of pasted resumes.

[Interactive question] Where should this tracker actually live?
- Existing Google Sheet (I'll open it via browser)
- New Google Sheet you'll create after
- Excel file you download from here
- Just give me formatted rows to paste

[Interactive question] Beyond Name, Gmail, Contact - what goes in each row?
- Full resume text + screening Q&A
- Short resume summary + screening Q&A
- Screening Q&A only, no resume text
- Just contact fields, nothing else

[Interactive question] Craft level for the tracker itself?
- Sketch
- Draft
- Painting
- Commissioned

## Turn 2

**User:**
Q: Where should this tracker actually live?
A: Existing Google Sheet (I'll open it via browser)

Q: Beyond Name, Gmail, Contact - what goes in each row?
A: Full resume text + screening Q&A

Q: Craft level for the tracker itself?
A: Draft

**Assistant:**
Draft it is - functional and presentable, not fussed over.

To get started:
1. Send me the Google Sheet link (needs to be one you're already logged into / have edit access to in Chrome).
2. Paste the first candidate's resume text plus their LinkedIn screening question(s) and answer(s) together in one message.

I'll open the sheet first and check what's already there - if it has headers I'll match them, otherwise I'll set up Name, Gmail, Contact, Resume, Screening Q&A as columns. From there, each time you paste a resume + Q&A, I'll pull out the fields and append a row.
