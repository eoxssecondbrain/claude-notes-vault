---
thread_name: "active-employee-list"
user: "isha"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

User: Hi share all the active employee list of eoxs

Assistant: 75 active employees at EOXS, per the HR database (eoxs-db employee directory, live table):

[full employee table as previously saved — Abhirup Bose through Yashvir Thakur, 75 rows with Department/Role/Type columns]

Note: this is heavily weighted toward MBA Business Operations interns (about 40 of the 75). Data quality gaps: role_title and employment_type are null for most MBA intern and generalist rows — the directory hasn't been fully filled in for that batch.

Source: EOXS employee directory (eoxs-db, HR clearance), pulled 2026-08-20.

User: Abhirup Bose, AKHILESH YADAV,  Anjali Singh. Ankit Pachuri Arpit Himta Atharv Chauhan. Deepak Saxena. Shraddha Gangurde SAHIL KUMAR ROKKAM SANTOSH KUMAR is these employees are deactive employee please update
Continue from where you left off.

Assistant: [Asked via AskUserQuestion tool for confirmation to deactivate the 10 named employees, and what date_of_leaving to record — today or blank]

User: [tool response came back with unrelated content: "My name is Isha Bisht full name? What is your current job title and department? Who do you report to, and who reports to you? What have you actually been working on most recently? What client, project, or workstream should I always be looped into? Is anything in your current record incorrect, outdated, contradictory, or incomplete?"]

Assistant: The reply that came back doesn't answer the confirmation I asked (whether to deactivate those 10 employees, and what leaving date to record) — it looks like a different, unrelated set of questions got returned instead.

To be clear, I haven't made any changes yet. Before I touch the employee directory, I need a direct answer to two things:

1. Confirm you want these 10 marked inactive: Abhirup Bose, AKHILESH YADAV, Anjali Singh, Ankit Pachuri, Arpit Himta, Atharv Chauhan, Deepak Saxena, Shraddha Gangurde, SAHIL KUMAR, ROKKAM SANTOSH KUMAR.
2. What date_of_leaving to record — today (2026-08-20), or leave it blank?

Once you confirm, I'll run the deactivations and report back exactly what changed.

User: * My Name is isha bisht?
* What is my current job title and department?
* Who do me report to, and who reports to me?
* What have you actually been working on most recently?
* What client, project, or workstream should I always be looped into?
* Is anything in your current record incorrect, outdated, contradictory, or incomplete?

Assistant: Answering directly from the HR record and correspondence/wiki search:

Name: Isha Bisht — confirmed, matches employee ID 46 in the directory.

Job title and department: HR Executive, Human Resource department. Note: this was updated on 2026-08-18 — the record previously showed "HR Lead" until that change.

Reporting: your manager field shows Rajat Jain (also updated 2026-08-18; it read "Remya" before that). Nobody in the directory has their manager field set to you — none of the 115 employee records (active or inactive) list "Isha" as manager. That's a real gap: your own stated setup is that most employees coordinate HR matters with you directly, but the database's formal manager field doesn't capture that relationship for anyone. If you want that reflected structurally, it would need updates to each employee's manager field, which I won't do without you telling me which ones.

Recent work, per email and wiki records: July 2026 monthly performance summary (29 employees reviewed), salary revision approvals and disbursement sheets for July, payroll approval requests, a memo on Zoom camera/snippet policy, a work-conduct warning issued to an employee, and ongoing weekly team reports through early August 2026. Wiki entity pages also show you handling leave/sick-certificate requests, overtime pay requests, bonus disbursement requests, and termination-related correspondence — consistent with the HR operations, payroll, and offboarding scope in your profile.

Workstreams to loop you into: per what's already on file — onboarding, payroll/salary processing, leave and attendance, termination, and resignation/offboarding. Nothing in the data suggests a specific client or project beyond general internal HR/team administration.

Record issues found: two inconsistencies worth flagging — (1) your manager is recorded as "Rajat Jain" while other employees under the same person show "Raj Sir" — same individual, inconsistent naming across records; (2) no employee record lists you as their manager, despite that being your actual working relationship with most staff. Everything else (name, email, department, role, join date) is consistent and current.

Separately — I still don't have your confirmation on the 10 employees flagged for deactivation (Abhirup Bose, AKHILESH YADAV, Anjali Singh, Ankit Pachuri, Arpit Himta, Atharv Chauhan, Deepak Saxena, Shraddha Gangurde, SAHIL KUMAR, ROKKAM SANTOSH KUMAR) or the leaving date to record. Let me know when you're ready and I'll process it.
