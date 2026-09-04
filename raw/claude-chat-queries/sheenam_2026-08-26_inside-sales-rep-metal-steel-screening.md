---
thread_name: "inside-sales-rep-metal-steel-screening"
user: "sheenam"
type: claude-chat
created: 2026-08-26
updated: 2026-08-26
---

Human: One thread per job post. First message in each thread is the job post itself (or a link/paste of it).
Role
Screening assistant for EOXS and AskCruz hiring. Sheenam is the first-round interviewer for every open post — my job is to rank and flag candidates before that round, not to make the hiring decision.
Step 1 — On the first message in a thread
Read the job post and extract, before doing anything else:
Role title, seniority level
Must-have requirements (disqualifying if missing)
Nice-to-have requirements
Any explicit candidate profile described in the post (background, industry, tools)
State this extraction back in a short list so Sheenam can correct it before screening starts. Don't screen anyone until this is confirmed for that thread.
Step 2 — Common bar (applies to every role, on top of role-specific requirements)
Culture/values fit — evidence of ownership, initiative, low ego, honest communication in past roles
Communication and remote-work self-management — clarity in writing, evidence of working async/independently, not just "remote experience" as a label
Startup pace / ambiguity tolerance — evidence of operating without heavy process, wearing multiple hats, comfort with undefined scope
These are working definitions — adjust per thread if a role needs something more specific added.
Step 3 — Screening each candidate
Applicant data will vary: pasted text, PDF resumes, or LinkedIn export/CSV. Read whatever form it comes in before scoring.
For every candidate, check must-haves first.
If any must-have is missing: flag it explicitly at the top as "Disqualifier: [what's missing]" before anything else. Still give a score, but the tier is capped at No Fit regardless of other strengths.
If no disqualifiers: proceed to scoring.
Score 1-10 against fit (role requirements + common bar combined, weighted toward the specific role's must-haves). Tier: 8-10 Strong Fit / 5-7 Maybe / 1-4 No Fit. Reasoning: one short paragraph — what supports the score, what's missing or risky, one line on common-bar signals specifically.
Step 4 — Output format
Single candidate: Name — Score — Tier Disqualifier (if any) Reasoning (short paragraph)
Batch of candidates: return a ranked table, highest score first. Columns: Name | Score | Tier | Disqualifier (Y/N + what) | Key strength/gap
Don't draft interview questions, rejection messages, or anything beyond the score/rank unless asked — that's a separate step Sheenam runs manually after this screen.
Ground rules
Never invent a candidate's experience or qualifications not in the material given.
Separate fact (what's on the resume/profile) from inference (what you're reading into it) — label inference as inference.
If the job post's must-haves are ambiguous or contradictory, ask rather than guessing a threshold.
Keep responses scannable — table for batches, short block for single candidates, no filler.

Let us start with this job posting - Inside Sales Representative Metal/Steel
About the job
Company Description - EOXS combines advanced AI and machine learning with deep expertise in the metal industry to help Metal Service Centers automate and grow their businesses. By digitizing and optimizing core processes, EOXS enables customers to achieve up to 50% revenue growth in the first year without increasing staff headcount. The company focuses on practical, scalable solutions that streamline operations, improve decision-making, and enhance customer experiences. Team members work with innovative technologies and real-world industrial challenges, contributing directly to measurable business impact.
Role Description - This is a full-time, remote Inside Sales Representative role. The Inside Sales Representative will engage with prospective and existing customers via phone, email, and virtual meetings to understand their needs and present EOXS solutions. Day-to-day responsibilities include qualifying leads, nurturing prospects through the sales cycle, preparing and delivering product demonstrations, and maintaining accurate records in the CRM system. The role also involves collaborating with account management and customer success teams to ensure a smooth onboarding experience and high customer satisfaction. The successful candidate will consistently follow up on opportunities, meet or exceed sales targets, and provide feedback to help refine EOXS products and sales processes.
Qualifications

* Demonstrated Inside Sales experience, with the ability to manage the full sales cycle and close deals
* Strong Customer Service and Customer Satisfaction focus, with excellent relationship-building skills
* Proven Lead Generation skills, including prospecting, qualifying, and nurturing potential customers
* Account Management abilities to support ongoing client relationships and identify upsell or cross-sell opportunities
* Clear and professional verbal and written communication skills
* Comfort working in a remote environment with effective time management and self-motivation
* Familiarity with CRM tools and basic sales analytics
* Experience in B2B technology, SaaS, or industrial sectors (metal or manufacturing) is a plus
* Relevant education or training in business, sales, or a related field preferred

Assistant: Extraction from the job post — confirm before I screen anyone:

Role title / seniority: Inside Sales Representative — Metal/Steel industry vertical. No seniority tier stated (not "Senior," "Junior," or "SDR"); reads as an individual-contributor, full-cycle closer role, not entry-level based on "full sales cycle and close deals."

Must-have requirements (disqualifying if missing):
- Demonstrated inside sales experience with full sales cycle ownership (prospect through close)
- Strong customer service / customer satisfaction track record with relationship-building
- Proven lead generation (prospecting, qualifying, nurturing)
- Account management experience (ongoing client relationships, upsell/cross-sell)
- Clear, professional verbal and written communication
- Demonstrated ability to self-manage in a remote setting (time management, self-motivation — not just "worked remotely")
- Familiarity with CRM tools and basic sales analytics

Nice-to-have requirements:
- B2B tech, SaaS, or industrial sector experience (metal/manufacturing specifically called out)
- Relevant education/training in business, sales, or related field

Explicit candidate profile described in post: No explicit industry-background mandate — metal/manufacturing/industrial B2B experience is flagged as "a plus," not required. So a strong SaaS/B2B inside sales candidate without metal industry exposure is not disqualified on that basis alone.

Note on ambiguity: the post doesn't specify years of experience or deal size/ACV — I'll treat "demonstrated full-cycle inside sales" as the bar rather than inferring a number. Flag if this matters for your threshold.

Confirm this list (or correct it) and I'll start screening candidates for this thread.
