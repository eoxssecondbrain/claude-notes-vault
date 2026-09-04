---
thread_name: "askcruz-implementation-onboarding-screening-questions"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

User:
You are helping us screen candidates for a specific job role. I will share the Job Description (JD) below.
Based on the JD, create a list of 10 thoughtful, role-specific questions that we can use for a 2-minute candidate video assessment.
Requirements:
- Do not include basic or repetitive questions such as "Tell me about yourself," "Introduce yourself," "Why should we hire you?", or "What are your strengths and weaknesses?"
- Avoid generic, textbook, or easily memorized questions.
- Questions should be directly relevant to the responsibilities, skills, and expectations mentioned in the JD.
- Prefer scenario-based, situational, and practical questions that reveal how the candidate thinks and approaches real-world situations.
- Questions should help us understand the candidate's problem-solving, decision-making, communication, critical thinking, creativity, and practical understanding of the role.
- Make the questions challenging enough to differentiate strong candidates from average candidates.
- Keep each question clear and concise so it can be answered meaningfully within a 2-minute video.
- Avoid questions that require company-specific knowledge the candidate could not reasonably have before joining.
- Make all 10 questions distinct and relevant to the specific role.
- We will select 3–4 questions ourselves from the list and send those questions to the candidate. Do not ask the candidate to choose.
Job Description:
US Shift
Work from Home
Mandate: owns the full path from signed contract to a client actively running AskCruz day to day — configuration, data ingestion (ERP, email, call transcripts), OV setup, user training, and adoption. This person is the difference between a signed deal and a renewed/expanded one, which is the actual leverage point given AskCruz's current revenue is expansion-motion off existing steel clients, not new logos.
Core responsibilities:

* Run onboarding for raw material distributors (15-50 employees) — steel, fastener, plastics, lumber verticals
* Map the client's existing workflow (quoting, inventory, order desk) into AskCruz's Company Brain / IRIS layer
* Own data ingestion setup: ERP connection, email/call transcript pipelines, wiki seeding
* Train end users (often non-technical, floor/counter staff to ops managers) to actual daily usage, not just a demo
* Be the first escalation point for implementation-stage issues before they become support tickets
* Report adoption metrics back to you — this role should tell you if a client is going to churn before they tell you

Hard requirements (disqualifiers if missing):

* Has personally implemented software (ERP, CRM, or similar) into a mid-size company before — not just sold it, not just supported it
* Comfortable being hands-on technical (SQL, API/webhook concepts, basic data mapping) without being an engineer
* Can run a room of skeptical, non-technical operators and get them to change how they work
* No job-hopping pattern (same bar you're applying to AE/SDR — stability signal matters more here since this person becomes the face of AskCruz post-sale)

Nice to have, not required:

* Industrial/distribution domain exposure (steel, metals, building materials)
* Has worked at an early-stage SaaS company (small team, high ownership, no hand-holding)
* Open question I'd flag: this JD assumes one person can own both the technical setup and the change-management/training side. At more mature software companies these are usually two different people (implementation engineer vs. customer success/onboarding). Bundling them into one hire is fine at your current stage but caps how many clients one person can carry in parallel — worth deciding now whether this is a scaling role or a stopgap.

Assistant:
This doesn't match eoxs-data-general (no EOXS/AskCruz data being queried) or threads-ov's content purpose (nothing to synthesize or cross-link) — flagging per your standing instruction, then proceeding since it's a standalone content task that doesn't need either tool.

10 questions for the Implementation & Onboarding Manager role:

1. A client's counter staff run quoting from memory, not the ERP. You have three weeks before go-live to map that workflow into the Company Brain. What do you prioritize first, and what do you deliberately leave for after go-live?

2. You walk into a training session with counter and floor staff who've used the same system for 15 years and see this as pointless extra work. What's the first thing you say, and what do you avoid saying?

3. A client's ERP export is missing fields your data ingestion needs, and their IT contact takes two days to respond to anything. Go-live is in a week. What's your move?

4. Six weeks post-launch, login counts look fine but actual daily usage is flat. What specific signals would tell you this is normal ramp-up versus a client quietly heading toward churn?

5. Where's your personal line between "I'll write this SQL query or map this webhook myself" and "this needs an engineer"? Give a concrete example on each side of that line.

6. Two clients need you the same week: one has a broken data pipeline, the other has a training session already booked with a room full of skeptical users. Walk through how you decide what gets your Monday morning.

7. An ops manager tells you their process is too unique to fit into a standard structure and pushes back on changing it. How do you respond in that meeting?

8. You take over a client where onboarding notes are thin and the client is already annoyed at the pace. Before your first call with them, what three things do you check?

9. Besides login frequency, name one adoption metric you'd track that would actually tell you a team changed how they work, not just that they opened the software.

10. Think back to a software implementation you've personally run before AskCruz. What's one mistake from that process you'd deliberately not repeat here, and why?

Coverage check: workflow mapping/prioritization, change management with resistant users, technical troubleshooting under time pressure, churn detection, technical hands-on ceiling, multi-client prioritization, handling pushback, diligence on a messy handoff, adoption-metric thinking, and self-critical reflection on real prior implementation work. None are answerable from a script, and #5 and #10 directly test the two hard disqualifiers (hands-on technical, personally implemented before).
