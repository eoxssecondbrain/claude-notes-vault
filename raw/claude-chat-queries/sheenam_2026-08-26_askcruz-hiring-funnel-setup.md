---
thread_name: "askcruz-hiring-funnel-setup"
user: "sheenam"
type: claude-chat
created: 2026-08-26
updated: 2026-08-26
---

**User:** I am going to lead the hiring funnel for AskCruz now. I want to ensure that each hiring process starts with me as the first round of interviewer. I want to setup a systematic process which I can implement for all posts and can later train someone to execute it. To start with, I will give you all the open job posts that we have on LinkedIn. I want you to understand each job post, its requirements, the candidates that we are looking for and then help me screen the applicants. I want to create a project in claude calling 'Hiring' and under that project create chat threads for each job post and keep the conversation for separate job posts in separate chats. I want this project to have standardized instructions which it follows for each chat thread so I dont have to explain the criteria for hiring in every chat. ask me questions to understand the requirements and based on my answers create custom instructions for this project

**Assistant:** This doesn't touch EOXS data (eoxs-db / eoxs-teams / askcruz-odoo) — raj-eoxs-vault doesn't apply here. It's a project-setup task, so no data connector is in play.

One thing to flag before we start: I can't create a Project or chat threads inside claude.ai myself — that's a UI action only you can do. What I can do is write the exact custom-instructions text for the Project (so you paste it once and it applies to every thread), plus a standard screening template for you to reuse per job post.

To write instructions that actually work without you re-explaining criteria every time, I need clarity on a few things first.

[Tool call: ask_user_input_v0 — three questions: (1) what Claude should actually do with each applicant, (2) how applicant data will be provided, (3) what common bar applies to every AskCruz hire regardless of role]

**User (answers):**
Q: For each applicant, what should I actually produce in the chat?
A: Score/rank against the JD only

Q: How will you give me applicant data?
A: Mix, varies by job post

Q: Is there a common bar that applies to every AskCruz hire regardless of role (on top of role-specific requirements)? (Select all that apply)
A: Yes — culture/values fit, Yes — communication + remote-work self-management, Yes — startup pace / ambiguity tolerance

**Assistant:** [Tool call: ask_user_input_v0 — three follow-up questions: (1) how should the score/rank be expressed, (2) should disqualifiers be flagged separately, (3) how will candidates usually be fed in]

**User (answers):**
Q: How should the score/rank be expressed?
A: Numeric score + tier + reasoning

Q: Should I flag automatic disqualifiers (missing a must-have requirement) separately from the overall score?
A: Yes, call these out explicitly before scoring

Q: How will you usually feed me candidates?
A: Both, depends on the day

**Assistant:** Enough to build this now — one assumption I'm making: numeric scale is 1-10 with tier bands (8-10 Strong Fit, 5-7 Maybe, 1-4 No Fit). Edit if you want different cutoffs.

[Created file /mnt/user-data/outputs/hiring-project-instructions.md with the following content:]

# Hiring Project — Custom Instructions

Paste this whole thing into the Project's "custom instructions" field. One thread per job post. First message in each thread is the job post itself (or a link/paste of it).

## Role
Screening assistant for AskCruz hiring. Sheenam is the first-round interviewer for every open post — my job is to rank and flag candidates before that round, not to make the hiring decision.

## Step 1 — On the first message in a thread
Read the job post and extract, before doing anything else:
- Role title, seniority level
- Must-have requirements (disqualifying if missing)
- Nice-to-have requirements
- Any explicit candidate profile described in the post (background, industry, tools)

State this extraction back in a short list so Sheenam can correct it before screening starts. Don't screen anyone until this is confirmed for that thread.

## Step 2 — Common bar (applies to every AskCruz role, on top of role-specific requirements)
- Culture/values fit — evidence of ownership, initiative, low ego, honest communication in past roles
- Communication and remote-work self-management — clarity in writing, evidence of working async/independently, not just "remote experience" as a label
- Startup pace / ambiguity tolerance — evidence of operating without heavy process, wearing multiple hats, comfort with undefined scope

These are working definitions — adjust per thread if a role needs something more specific added.

## Step 3 — Screening each candidate
Applicant data will vary: pasted text, PDF resumes, or LinkedIn export/CSV. Read whatever form it comes in before scoring.

For every candidate, check must-haves first.
- If any must-have is missing: flag it explicitly at the top as "Disqualifier: [what's missing]" before anything else. Still give a score, but the tier is capped at No Fit regardless of other strengths.
- If no disqualifiers: proceed to scoring.

Score 1-10 against fit (role requirements + common bar combined, weighted toward the specific role's must-haves).
Tier: 8-10 Strong Fit / 5-7 Maybe / 1-4 No Fit.
Reasoning: one short paragraph — what supports the score, what's missing or risky, one line on common-bar signals specifically.

## Step 4 — Output format
Single candidate:
Name — Score — Tier
Disqualifier (if any)
Reasoning (short paragraph)

Batch of candidates: return a ranked table, highest score first.
Columns: Name | Score | Tier | Disqualifier (Y/N + what) | Key strength/gap

Don't draft interview questions, rejection messages, or anything beyond the score/rank unless asked — that's a separate step Sheenam runs manually after this screen.

## Ground rules
- Never invent a candidate's experience or qualifications not in the material given.
- Separate fact (what's on the resume/profile) from inference (what you're reading into it) — label inference as inference.
- If the job post's must-haves are ambiguous or contradictory, ask rather than guessing a threshold.
- Keep responses scannable — table for batches, short block for single candidates, no filler.

[File presented to user via present_files.]

Setup: create the Project named "Hiring" in claude.ai, paste this file's content into its custom instructions field, then create one chat thread per job post inside it. First message in each thread should be the job post itself — the instructions have Claude extract and confirm requirements before screening starts.

Two things worth deciding now rather than mid-screening:

1. Score 1-10 for a candidate missing a must-have — right now they still get a score but are capped at No Fit tier. If you'd rather they get no score at all, say so and I'll change it.
2. The common-bar definitions (culture fit, remote self-management, ambiguity tolerance) are my working defaults, not yours — if AskCruz has a sharper version of these (specific behaviors you've seen fail before), that's worth swapping in now rather than discovering it three threads in.
