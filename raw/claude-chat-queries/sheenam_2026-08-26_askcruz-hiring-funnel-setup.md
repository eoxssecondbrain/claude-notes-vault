---
thread_name: "askcruz-hiring-funnel-setup"
user: "sheenam"
type: claude-chat
created: 2026-08-26
updated: 2026-08-28
---

User selected rigor level: 10ft deep - verified claims.

Assistant verified via web search (LinkedIn Recruiter Help docs + third-party blog) that LinkedIn's applicant "top fit/maybe/not a fit" categorization is actually a binary match/no-match against recruiter-authored screening questions, based on self-reported candidate answers — LinkedIn explicitly does not prevent unqualified applicants from applying; the filter quality depends entirely on question wording.

Feedback given on Sheenam's described process (LinkedIn screening questions -> manual resume copy into Google Sheet for "top fit"/"maybe" -> feed to Claude with JD + general qualities for scoring -> LinkedIn outreach to shortlisted -> 15-20 min first-round call conducted by Sheenam -> her fit decision):

Sound parts: pre-filtering via LinkedIn screening questions before Claude; feeding both "top fit" and "maybe" tiers into Claude rather than trusting LinkedIn's tier as final (correct, since LinkedIn's match is only against her screening questions, not the full JD); keeping the interview decision with her.

Two gaps flagged:
1. "Not a fit" bucket is a dead end with no audit — since LinkedIn's match is self-reported/unverified, badly worded screening questions could silently exclude qualified candidates and nobody ever reviews that bucket. Suggested periodic spot-check of 5-10 "not a fit" resumes per post.
2. Manual resume copy-paste into Google Sheets is the actual scaling bottleneck / least structured step, more so than the scoring logic — relevant because she wants this process eventually handed off to someone else.

One gap specific to her "trainable process" goal: no mechanism to log when Claude's score and her actual post-interview decision diverge, so there's no way to calibrate the rubric over time or tell a future person running this when to trust vs override Claude. Suggested adding an outcome-tracking column (Claude score -> her final call decision) per candidate.

Ended by asking whether to add the "not a fit" spot-check step and outcome-tracking column into the Project instructions now, or wait until after her first batch.
