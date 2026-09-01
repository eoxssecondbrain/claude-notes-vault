---
thread_name: "hiring-process-help-scope"
user: "muskan-sharma"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

USER: how can you help in hiring process

ASSISTANT: I looked for a skill file matching this before answering, per your setup rules: threads-ov is loaded, but I couldn't locate a "raj-eoxs-vault" skill or file anywhere in my available skills, tools, or memory — it doesn't appear to exist under that name right now. Separately, this query doesn't clearly match any configured skill: sales-strategist is scoped to sales/GTM/deal work, not hiring, and no HR-specific skill has been set up yet in your preferences list. Flagging both rather than guessing, per your instructions.

To be useful rather than generic, I want to narrow down what you actually need help with in hiring.

[AskUserQuestion] "What part of the hiring process do you want help with right now?" (multiSelect)
Options: Drafting materials (Job descriptions, outreach/rejection emails, interview questions, offer letters) | Screening candidates (Reviewing resumes/applications against criteria, shortlisting, scoring) | Process & tracking (Pipeline tracking, scheduling, status updates, checklists for a role you're hiring) | Just an overview (General sense of what I can realistically do here before you commit to a task)

USER ANSWER: Screening candidates, Process & tracking, Drafting materials

ASSISTANT: Here's what's actually useful across those three areas, and where the limits are.

Screening candidates: paste or attach resumes/applications and a role's criteria, and I can score and rank them, flag gaps against requirements, and pull structured summaries (skills, years of experience, education, notice period) into a comparison sheet. What I can't do: pull candidates automatically from an ATS or job board — no recruiting/HR data connector is set up in this session. The EOXS connectors available here (EOXS_data_general, Team_EOXS_live) cover clients, calls, emails, wiki, and implementation tasks — not candidate or HR data. If EOXS uses an ATS (Greenhouse, Lever, etc.), I can check the MCP connector registry and suggest a connection if you want that wired in.

Process and tracking: I can build a pipeline tracker (spreadsheet or a live artifact) with stages, statuses, and next actions per candidate, set up a role-specific hiring checklist, and set scheduled reminders for follow-ups (e.g., "check on outstanding offers every Monday"). I can't see or write to a calendar or ATS directly unless one is connected.

Drafting materials: job descriptions, screening/interview questions, interview scorecards, outreach and rejection emails, and offer letter drafts — all doable, and I'll ask for craft level (sketch/draft/painting/commissioned) before producing any of these since they're deliverables, per your preference.

Given you picked all three, tell me which specific thing to start on — e.g., a role you're actively hiring for, or a batch of resumes to screen — and I'll go from there.

USER: we have 2 minutes video of candidates who have applied for software implementation consultant, can you help me shortlist the candidates through it

ASSISTANT: Before I start, a technical note: I don't have native video playback. To actually evaluate the candidates I'd extract audio and transcribe it (and pull a few frames if visual presentation matters), then assess content — this depends on where the files are and what's installed, which I'll confirm once I know the files' location.

A few things I need first.

[AskUserQuestion]
Q1 "Where are the candidate videos?" -> Uploaded to this chat / On my computer / Cloud link / Not yet decided
Q2 "What should the shortlist weigh most?" (multiSelect) -> Content of answers / Communication & clarity / Match to a JD/must-haves / Holistic impression
Q3 "How deep should this evaluation go?" -> 5ft Quick / 10ft Verified / 50ft Deep / 100ft Staged
Q4 "What craft level for the shortlist deliverable?" -> Sketch / Draft / Painting / Commissioned

USER ANSWERS: Video location = Uploaded to this chat; Criteria = Content of answers, Communication & clarity; Rigor level = 50ft - Deep; Craft level = Sketch

[ASSISTANT internal check: checked uploads directory in the workspace — no video files present yet; checked for ffmpeg (found, available) and a local transcription tool (none installed yet, would need to install one such as faster-whisper once files arrive)]

ASSISTANT: I don't see any video files in this conversation yet — please attach the candidate videos (or a zip of them) here.

Once they're in, here's the plan given your picks (content of answers + communication/clarity, 50ft deep, sketch-level output): I'll extract audio from each video with ffmpeg, transcribe it locally, and evaluate each transcript for technical/domain understanding relevant to a software implementation consultant role plus how clearly and confidently they communicate — then flag risks or gaps per candidate (per the 50ft rubric) and hand you a ranked sketch list.

One thing worth deciding now: do you have a job description or must-have list for this role? Even a short one would sharpen "content of answers" scoring — otherwise I'll judge against a general software implementation consultant profile (technical aptitude, client-facing communication, process/change-management sense), which is a reasonable but generic bar.
