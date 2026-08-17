---
thread_name: "askcru-ae-hiring-india"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

# AskCru AE Hiring — India (thread: askcru-ae-hiring-india)

## Phase 1: Hiring rubric setup
User: Considering hiring an AE in India for AskCru; ~300 LinkedIn applicants. Wants to build screening criteria before evaluating resumes. Hard red flag: high iteration (e.g. six jobs in seven years, one-year stints then moving on). Disqualify brand-chasers (big logo names, no substance). Assess resumes for right skills. Then check (last, in this order): US selling experience, SMB experience.

Assistant: Offered 5ft/10ft/50ft rigor options. User selected 50ft deep (full investigation, verify claims, explore adjacent risks, cite sourcing).

Assistant built AE hiring rubric:
- Must-have: full-cycle quota-carrying closing experience (not just SDR/BDR pipeline gen), US-market selling experience, SMB/mid-market motion matching actual deal size, quantified track record.
- Hard red flags: high iteration (6+ jobs/7 yrs, or 10-14 month stints unexplained), brand-chasing without substance (logo-heavy, numbers-empty resumes).
- Screening sequence (matching user's stated order): tenure/iteration → brand-chasing → skills/experience match → US selling/SMB experience.
- Confirmed via eoxs-db that "AskCru" ties to EOXS's Enterprise AE function selling ERP software to steel distributors in the American market (2021 internal email); flagged as assumption, user did not correct, workflow continued.

## Phase 2: Candidate-by-candidate evaluation (23 resumes)
User uploaded 23 resumes sequentially ("check this" / "check" / similar), each evaluated against the rubric: rating out of 10, qualify/borderline/disqualify verdict, exact tenure math against Aug 17, 2026, quantified achievement evidence, brand-chasing assessment, AE-vs-SDR role distinction, US market / SMB experience check. Running leaderboard maintained and restated after each candidate.

Candidates evaluated in order: 1. Rajan Rastogi, 2. Ipsita Sukanya, 3. Shaun Sylvester, 4. Pravin Sigtia, 5. Shreyash Patil, 6. Shiv Sharma, 7. Aswan Basha I, 8. Rohit Rana, 9. Ridaiy Ajrawat, 10. Arnold Stanley Dias, 11. Shruti Sharma, 12. Ranjeet Kour, 13. Kamal Kumar Pandey, 14. Prerna Paswan (flagged: duplicated bullet text reused verbatim across job entries — resume integrity issue), 15. Mohammed Abuzar Bangar (flagged: employment dates predate stated graduation year + suspiciously uniform precise metrics on every bullet — fabrication risk, recommended active verification not face-value scoring), 16. Amit B Udagatti, 17. Himanshu Motwani, 18. Rimpa Sen, 19. Shasti Mani, 20. Anshuman Saini, 21. Ajinkya Ambulkar, 22. Fazil Khan, 23. Narendra Bhoi.

(Note: mid-conversation compaction occurred; this save reconstructs from the retained summary rather than verbatim per-candidate text. Full original ratings/reasoning for each candidate are in this thread's message history prior to compaction.)

Assistant caught its own lapse early on (missed save_chat_transcript calls for several turns) and self-corrected with a catch-up save, then called save_chat_transcript after every subsequent turn without exception.

## Phase 3: Interview guide request
User: "I'm an HR Executive and I'll be conducting interviews for the Account Executive (AE) role. Since you already have the job-post details, prepare a concise but comprehensive interview question set based specifically on the role. Include the most important HR, sales, AE-specific, client-handling, objection-handling, situational, and behavioral questions. For each key question, tell me what I should look for in the candidate's answer and any red flags. Also include a simple scoring/evaluation framework so I can assess whether to shortlist the candidate."

Assistant: Built a docx (AE_Interview_Guide_AskCru.docx) via the docx skill/npm library — initially a full ~30-question, 8-category (A-H) bank with scoring table and shortlist decision guide, grounded in the rubric and screening learnings from Phase 2. Generated successfully but not yet verified/sent.

User (mid-turn interrupt): "give 8-10 questions"

Assistant: Trimmed the guide to the 9 highest-signal questions spanning all requested categories:
1. [HR/Tenure] Career timeline walkthrough incl. gaps — direct iteration/job-hopping check.
2. [Sales Fundamentals] Full sales-cycle ownership question (AE vs SDR/BDR distinction).
3. [Sales Fundamentals] Quota/attainment math.
4. [US Market] Specific US-buyer deal description.
5. [SMB Fit] Deal size/buyer title vs. AskCru's actual $15-50K/30-100 employee ICP.
6. [Client Handling] Unhappy client after sale.
7. [Objection Handling roleplay] Price objection ("30% higher than competitor").
8. [Behavioral] Missed quota / toughest loss, STAR-style.
9. [Closing/Motivation] Why this role + 90-day success plan.

Kept "Look for" (green) / "Red flags" (red) guidance per question, weighted scoring table (Sales fundamentals 25%, US market 20%, SMB fit 15%, Client handling 10%, Objection handling 10%, Behavioral/tenure 15%, Motivation 5%), and shortlist decision guide (80-100 strong shortlist / 60-79 borderline / <60 do not shortlist, plus automatic disqualifiers list).

Rebuilt via /home/claude/ae_interview/build.js, regenerated AE_Interview_Guide_AskCru.docx (US Letter, docx-js), verified by converting to PDF (soffice.py) and rendering to JPEG (pdftoppm) then visually inspecting all 3 pages — rendered cleanly, no formatting issues. Delivered to user via SendUserFile (file_uuid 5d56d02f-0adb-4ba3-835d-3c4c5290be57).
