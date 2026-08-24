---
thread_name: "linkedin-applicant-export"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-24
updated: 2026-08-24
---

User: [uploaded screenshot of LinkedIn "Hiring Pro" applicant list showing 146 applicants, columns Name/Title/Company/Location/Qualifications/Resume/Move to/Shortlist] i want to download all the details of all apllicants from linkedin guide me how to download it

Assistant: This doesn't match eoxs-data-general or threads-ov (both are EOXS internal data/transcript tools) — it's a LinkedIn product question, so noting that per your preference before proceeding.

What you're looking at is LinkedIn's basic "Hiring Pro" applicant manager (not full LinkedIn Recruiter). It has no native bulk export button — no "select all → download CSV." Your options:

1. Manual, per-applicant (what LinkedIn actually supports): click each applicant, use the Resume icon to download their PDF one at a time, and read name/title/company/location/qualifications off the list view. With 146 applicants that's 146 clicks — slow but it's the only fully compliant path with no ATS or paid seat involved.

2. Upgrade to LinkedIn Recruiter and use Recruiter System Connect (RSC) to sync applicants into a connected ATS automatically, or use Recruiter's own "Export profiles" feature for candidates added to a project — this is capped per export and doesn't include full resume text, just profile fields. Requires a Recruiter seat, which Hiring Pro alone doesn't give you.

3. Third-party Chrome extensions (ApplicantSync, LinkedIn Candidates Exporter, etc.) that scrape the applicant list into CSV/Excel including resume links. These work, but they're unofficial — bulk scraping like this sits against LinkedIn's User Agreement, and using one risks the account/job posting getting flagged. Worth knowing before you install one, not something I'd quietly hand you a workaround for.

If you want, I can drive this through your Chrome browser and click through the 146 applicants to download resumes and pull the list-view data (name, title, company, qualifications match) into a spreadheet for you — that's just automating the same manual clicks in option 1, nothing scraped. Say the word and I'll start.

Sources:
- [Export profiles in Recruiter | Recruiter Help](https://www.linkedin.com/help/recruiter/answer/a412149)
- [Export candidates to your ATS with RSC | Recruiter Help](https://www.linkedin.com/help/recruiter/answer/a414459)
- [Export LinkedIn Job Applicants to CSV or Excel | ApplicantSync](https://www.applicantsync.com/why/export-linkedin-job-applicants)
