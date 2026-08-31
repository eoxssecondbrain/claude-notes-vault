---
thread_name: "linkedin-818-candidates-export"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

User: i'm given a task to copy and paste resume of total 818 top fit candidates for operation manager job post on google sheet along with name, gmail, contact and screening questions. tell me a way to do it quickly

Assistant: [Noted that this request doesn't clearly match any configured skill — not eoxs-data-general (EOXS emails/calls/wiki/CRM data), not sales-strategist (not a sales task), and no "Muskan-eoxs-vault" skill found enabled in the account. Flagged this per instruction rather than guessing, then asked two clarifying questions via AskUserQuestion:
Q1 "Where do the 818 candidates (resume, name, gmail, contact, screening answers) currently sit?" — options: ATS/recruiting software, Job board dashboard, Google Forms responses, Gmail/manual applications.
Q2 "Can you pull data out of that source as a file, or only view it through the browser?" — options: Yes I can export CSV/Excel, No browser view only, Not sure.]

User: [answered Q1: "linkedin"] [answered Q2: "Not sure"]

Assistant: This isn't covered by any of your configured skills (not EOXS data, not sales), and there's no "Muskan-eoxs-vault" skill currently active in your account — noting that per your instruction rather than guessing at what it might say.

Checked: LinkedIn's free job-posting applicant view has no native bulk export — no "download all applicants" button that gives you resume plus screening answers in one file. The fact that a whole market of third-party Chrome extensions exists just to fill that gap (ApplicantSync, LinkedIn Candidates Exporter, etc.) is itself the confirmation — they wouldn't exist if LinkedIn shipped this natively. So there are three real paths, not one.

1. If EOXS has a paid LinkedIn Recruiter seat (different product from the free job-posting tool), Recruiter has an official "Export profiles" feature — check with whoever manages that seat. It's the only fully sanctioned bulk path. I couldn't confirm whether its export includes full resume text and screening-question answers specifically (LinkedIn's own help page blocked automated access when I tried to verify) — test it on 5 candidates before trusting it for all 818.

2. If you're on the free job-posting applicant manager (more likely, given the question), a Chrome extension like ApplicantSync reads the applicant list inside your own logged-in session and exports name, email, phone, resume PDF, and screening answers to CSV — free tier, doesn't ask for your LinkedIn credentials. This is the genuinely fast option: minutes instead of days. Two things to check before running it on all 818 at once: it operates in a gray area under LinkedIn's user agreement, which restricts automated data collection, and pulling 818 profiles in one go is exactly the volume that can trip LinkedIn's bot detection and get the company account restricted. Test on 20-30 first, and check the extension's privacy policy for where that batch of candidate contact info gets processed before running the full set through it.

3. I wouldn't drive a browser to click through all 818 profiles myself either — automated clicking through that many LinkedIn pages in one session is more likely to trigger bot detection than a passive extension is, and a flagged company LinkedIn account is a worse outcome than slow data entry.

If neither export path works out, the fallback is manual but parallelized: split the 818 across two or three people, one tab on the applicant, one on the Sheet, a fixed column order, no formatting decisions mid-entry. At roughly 90 seconds a candidate that's about 20 hours of work split three ways — still a lot of time.

One thing worth pushing back on before anyone spends a day on this: 818 is a very large "top fit" shortlist for one Operations Manager hire. Is that the number that passed an initial screen, with interviews still to come, or is a sheet of 818 people actually meant to go into the interview pipeline? If it's the former, tightening the filter further before doing any bulk data entry is probably higher leverage than transcribing 818 records just to filter them again inside the Sheet.

Sources:
- Export profiles in Recruiter | Recruiter Help - LinkedIn (https://www.linkedin.com/help/recruiter/answer/a412149/exporting-profiles-in-recruiter?lang=en)
- Export LinkedIn Job Applicants to Excel — Free Step-by-Step (2026) (https://www.applicantsync.com/articles/how-to-export-linkedin-job-applicants-to-excel)
- ApplicantSync — Export LinkedIn Job Applicants to CSV & Excel + Resumes (https://www.applicantsync.com/why/export-linkedin-job-applicants)

User: yes they passed initial screen with interviews still to come

Assistant: [Asked three clarifying questions via AskUserQuestion:
Q1 "Does EOXS have a paid LinkedIn Recruiter seat for this job post, or is it the free job-posting tool?" — options: Free job posting tool, Paid Recruiter seat, Not sure.
Q2 "Want me to build the starter sheet template now (columns: name, gmail, contact, resume link, screening Q&A)?" — options: Yes build it now, No I'll set it up myself.
Q3 "If I build the template, what level of polish?" — options: Sketch, Draft, Painting.]

User: [answered Q1: "Not sure"] [answered Q2: "No, I'll set it up myself"] [answered Q3: "No preference"]

Assistant: To check Recruiter access: log into LinkedIn and look at the top-left account switcher — if "Recruiter" shows up as an option alongside the regular account, EOXS has a seat. If all you see is the normal Jobs dashboard (Jobs > Manage job postings > Applicants tab), you're on the free tool. That check takes two minutes and decides the whole method, so worth doing before picking a path.

Given "not sure," and that a single job post is more likely on the free tool: default to ApplicantSync. Install the free Chrome extension, open the applicants tab for the Operations Manager post, run it on a batch of 20-30 first to confirm it's actually pulling gmail, contact, and screening answers correctly before running the rest. If it turns out EOXS does have Recruiter, use its official Export profiles feature instead — no ToS risk — but still test on a small batch since I couldn't confirm from LinkedIn's own docs whether that export includes resume text and screening answers.

Since you're building the sheet yourself, the columns you need from either method: name, gmail, contact, resume (link or file), and one column per screening question.
