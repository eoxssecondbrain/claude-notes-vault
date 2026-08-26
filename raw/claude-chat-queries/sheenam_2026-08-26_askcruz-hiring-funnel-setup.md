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
