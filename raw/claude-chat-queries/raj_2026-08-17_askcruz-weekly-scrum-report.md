---
thread_name: "askcruz-weekly-scrum-report"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

[SCHEDULED TASK - AUTOMATED FIRING OF A CONFIGURED PROMPT]

USER (scheduled task prompt):
1. Locate the askcruz project management connector (teams-askcruz / "Ask cruz"). If you cannot find or reach it, stop and report that as the finding — do not substitute a different connector.
2. Call get_business_schema (or list_tables + describe_table) on it first to confirm current field names for: task stage, assignee, priority, log notes/chatter, and stage-change timestamps. Do not assume a prior schema.
3. This connector holds multiple project boards (rows in project_project), not just one. Query project_project first and list every board with its active flag. Pull task data from ALL boards where active = true. Exclude inactive/archived/placeholder boards (anything like "Test", "Test1", "Start here to discover Odoo", "Daily Snippets", or similar non-working boards — check the active flag and board name, don't guess). State the full list of active boards included in the run at the top of the output.
4. Pull, for the 7-day window ending today, across ALL active boards combined:
   a. Total tasks currently on each active board, and a combined total across all of them.
   b. Total tasks in a "Completed" (or equivalent) stage per board and combined, and how many of those were completed within this window.
   c. Every task with one or more stage changes in this window — which board, old stage, new stage, who moved it, and when.
   d. Every task with at least one log note (chatter message, not a stage-change system log) dated within this window — which board, and who posted it. Log notes vs. system stage-change logs must be distinguished at the data level (not by keyword-guessing) — confirm how the schema marks this before counting.
   e. Every open task assigned to someone that got zero log notes and zero stage changes across the entire window, on any active board — this is the gap list, the most important number here. Tag each with its board.
5. For each team member with tasks assigned anywhere across the active boards, compute ONE combined score out of 10 for the week (not one score per board) — aggregate their tasks across all boards they appear on:
   - Acknowledgment (0-2): share of their open tasks (across all boards) with at least one log note sometime in the window that was authored by the assignee themselves — not a note from anyone else (e.g. a manager chasing them on the task does not count as the assignee acknowledging it; call this out explicitly if raw any-author note counts would tell a materially different story). 100%=2, ≥50%=1, <50%=0.
   - Movement (0-3): stage-advances across the week, weighted 1.5x for high priority, 1x normal, 0.5x low. Calibrate the full-marks bar to roughly 5x the old daily bar as a starting point (i.e. ~15 weighted moves = 3 pts) — this is a placeholder until real data sets the actual baseline.
   - Completions (0-2): 1 pt per task completed in the window, capped at 2. A task that moved into Completed and then back out again within the window does not count as a completion (only count it if it ends the window in a Completed stage AND has a move-into-Completed event in the window).
   - Engagement depth (0-2): based on log note specificity across the week (mentions blockers, next steps, or concrete detail vs generic one-word notes). Flag this component explicitly as a low-confidence proxy in the output.
   - Scope engagement (0-1): 1 pt if they touched at least one high-priority/flagged task during the window, on any board.
6. Output format, in this order:
   - Boards included: list of active boards pulled from, with a one-line note on any boards excluded and why.
   - Board summary: total tasks per board and combined, total completed (all-time and this week) per board and combined, tasks moved this week, tasks with any log note this week vs. tasks acknowledged by their own assignee this week (both numbers, since they can diverge materially), combined gap list (untouched tasks + assignee + board, with days-since-last-activity for each).
   - Per-person weekly report card, aggregated across all boards: name, combined score /10, one-line breakdown of the five components, gap-list count if nonzero, which board(s) their tasks are on.
   - Flag anything anomalous: a person with zero activity all week, a task open >7 days with no log note at any point, a completed task that never got acknowledged before closing, non-human/bot accounts holding real tasks, or any board-attribution ambiguity (e.g. someone with tasks on multiple boards whose combined score masks a board-specific problem).
7. Keep it brief and scannable — this is a weekly read, lead with the numbers, no long preamble.
8. Email Delivery:
   - Once the report is generated, use the email tool to send the complete output.
   - To: rajat@eoxs.com
   - Subject: Weekly AskCruz Board Scrum Report - [Today's Date]
   - Body: Paste the full scannable output from Step 6.

ASSISTANT:
Located the teams-askcruz connector (Ask_cruz MCP tools). Called get_business_schema and list_tables to confirm schema — this is an Odoo 13 instance (HR + Project + Training focused, no sale/purchase/account apps). Confirmed field names: project_task.stage_id (task stage, FK to project_task_type), project_task.user_id (assignee), project_task.priority / priority_level (priority — priority='1' is the Odoo star, priority_level='P1' is a custom high-priority flag; no explicit Low tier exists in this schema), and for log notes vs system logs: mail_message.message_type='comment' = human-typed chatter, vs message_type='notification' with mail_tracking_value.field='stage_id' (subtype "Stage Changed") = system-logged stage moves. A third bucket (subtype "Note" + message_type "notification", empty body) is Odoo auto-logging simple field changes like "Assigned To ->" — excluded as noise from both notes and stage-move counts. date_last_stage_update / mail_message.create_date give stage-change timestamps.

Queried project_project: 9 boards total. Active=true: 50 MBA Inters Cohert (id 3), Customer 1 - EOXS (id 4), AskCruz (id 6), Idea Board (id 7), Hiring Funnels (id 9). Active=false (excluded): Daily Snippets, Start here to discover Odoo, Test, Test1.

Pulled task data, stage-change history, and log notes across all 5 active boards for the 7-day window 2026-08-11 to 2026-08-17, computed board summaries, the combined gap list (37 untouched open tasks), and per-person combined weekly scores per the rubric, then sent the full report by email.

Report emailed to rajat@eoxs.com, subject "Weekly AskCruz Board Scrum Report - 2026-08-17":

WEEKLY ASKCRUZ BOARD SCRUM REPORT
Window: 2026-08-11 to 2026-08-17 (7 days ending today, 2026-08-17)
Connector: teams-askcruz (live Odoo, current by definition)

BOARDS INCLUDED
Active boards pulled: 50 MBA Inters Cohert (id 3), Customer 1 - EOXS (id 4), AskCruz (id 6), Idea Board (id 7), Hiring Funnels (id 9).
Excluded (inactive, not pulled): Daily Snippets, Start here to discover Odoo, Test, Test1 — all active=false in project_project.

METHOD NOTES (read before the numbers)
- "Completed" stage per board: 50 MBA -> Paid, Customer 1-EOXS -> Complete, AskCruz -> Completed, Idea Board -> Completed. Hiring Funnels has NO completed-equivalent stage defined at all (only one stage, "Task") — its completion numbers are N/A, not zero. Flag this to whoever owns that board.
- Log note vs system log: distinguished at the data level via mail_message.message_type. 'comment' = human-typed chatter. 'notification' with subtype "Stage Changed" = system-logged stage moves. A third bucket, subtype "Note" + message_type "notification", is Odoo auto-logging simple field changes (e.g. "Assigned To ->") with empty bodies — excluded from both notes and stage-move counts as noise.
- "High priority/flagged" = priority_level = 'P1' OR the Odoo star priority = '1'. There is no explicit Low tier in this schema, so Movement weighting only distinguishes High (1.5x) vs Normal (1x) — no 0.5x events existed this week.
- Movement is attributed to the task's CURRENT assignee, not whoever physically dragged the card (a manager or teammate often moves someone else's task). Flagged inline wherever that matters.
- Acknowledgment scope = self-authored note in the window on tasks currently OPEN. Engagement-depth scope = self-authored notes on ANY of their tasks (open or completed) in the window. This is a low-confidence proxy per your instructions — treat directionally, not as ground truth.

BOARD SUMMARY
Board                    Total  Completed(all-time)  Completed(this wk)  Moved(events/tasks)  Any-note tasks  Self-ack'd tasks
50 MBA Inters Cohert       20        0 / 20                0              10 / 5                  5               2
Customer 1 - EOXS          50       34 / 50               19              35 / 29                27               4
AskCruz                    41       10 / 41                4               9 / 8                  21              11
Idea Board                  8        0 / 8                 0               0 / 0                   0               0
Hiring Funnels               4       N/A (no stage)        N/A            11 / 1                   2               0
COMBINED                  123       44 / 119*             23              65 / 43                 55              17

*119 = total tasks on the 4 boards that have a defined Completed stage (excludes Hiring Funnels' 4 tasks).

Any-note vs self-ack'd diverges hard on every board with volume: Customer 1-EOXS had 27 tasks touched by a note this week but only 4 where the assignee wrote it themselves — the other 23 are QA/manager notes landing on someone else's task. Same pattern on AskCruz (21 vs 11) at smaller scale. Read the "self-ack'd" column, not "any-note," if you want to know who is actually reporting on their own work.

Hiring Funnels: 11 stage-change events but only 1 distinct task moved (task 142, "0 to 1 SDR") — it ping-ponged between Task List / Claimed / In Progress six times this week, driven by four different people (Kashish Chauhan, Ankita Sharma, Karun Verma, Rajat Jain). Reads as uncoordinated card-dragging, not real progress — worth a direct look.

COMBINED GAP LIST — open, assigned, ZERO log notes AND ZERO stage changes all week (37 tasks)
Ayan Dutta — Idea Board (7 tasks, 12.1d untouched): CRM AI/Agent Architecture, Obsidian Vault/OV2, Ideas/Vision, EOXS Product/ERP Features, General/Team Coordination, Infrastructure/Integrations (all 12.1d), scalable customer info system (3.3d). This is effectively the entire Idea Board — dormant.
Ayan Dutta — AskCruz (5 tasks): Front End Function to upload/update data (12.2d), Integrate All Ask Cruz Email Data (12.1d), Project Manager Skill (10.4d), QA on AskCruz iOS app (10.1d), Deploying iOS cruz app (5.2d).
Ayan Dutta — Customer 1-EOXS (3 tasks): Front End Refinements (7.1d), Project Board Management (3.3d), Access Rights QA (11.1d).
MCP Write Tool (bot account) — AskCruz: Calendar (11.2d), R&D Voice Call-In feasibility — flagged P1 (10.9d, untouched all week despite being marked high priority).
MCP Write Tool (bot account) — 50 MBA: R&D Ambient Voice Device sample build (7.2d).
MBA Cohert 1 (shared cohort login) — 50 MBA: Website Design-Landing Page (12.3d), Google Reviews (10.1d), Linkedin Post Everyday (10.2d), Claude Features (0.7d, just created).
MBA Cohert 1 — Hiring Funnels: Onboarding SOP (0.6d, just created).
Cohert 1 Dev Team (shared login) — Idea Board: Mobile App - iOS & Android (12.2d).
Nidhi Rana — AskCruz: Email integration Automation (5.2d).
Yashvir Singh Thakur — AskCruz: Alternative to ZoomInfo (3.3d).
Sheenam — AskCruz: Optimize 35 MBAs LinkedIn (4.9d).
Rajat Jain — AskCruz: Linkedin HR Tool (0.8d, just created).
Ron — AskCruz: Have another company configure AskCruz (0.3d, just created).
Muskan Sharma — Hiring Funnels: SDR - Toronto (0.7d, just created).
Rajat Jain — 50 MBA: 6 "Video Evaluation" tasks + 1 Linkedin Engagement task, all 0.2-0.3d old (created today — noise, not neglect).
Vanshi B — 50 MBA: Linkedin Engagement (0.2d, just created).

Real staleness (>7 days, not just-created) accounts for 21 of the 37 — concentrated almost entirely on Ayan Dutta's Idea Board backlog and a handful of stale AskCruz/50-MBA tasks sitting with Ayan and the MCP Write Tool bot account.

PER-PERSON WEEKLY REPORT CARD (combined across all boards they appear on)
Name                     Score/10  Ack(0-2)  Move(0-3)  Complete(0-2)  Depth(0-2)  Scope(0-1)  Gap-list  Boards
Ayan Dutta                 6.0        0          3            2            0           1          15      Customer1-EOXS, AskCruz, Idea Board, Hiring Funnels
Sheenam                    4.6        1         0.6           2            1           0           1      AskCruz
Yashvir Singh Thakur       4.0        0          3            0            1           0           1      50 MBA, AskCruz, Hiring Funnels
Ron                        4.0        0          1            2            1           0           1      AskCruz
Nidhi Rana                 2.6        0         0.6           1            0           1           1      Customer1-EOXS, AskCruz
Priyanshu Sinha            2.2        0*         0.2          1            1           0           0      Customer1-EOXS
Jaskeerat Singh            2.0        0          1            1            0           0           0      Customer1-EOXS
MBA Cohert 1 (shared)      0.4        0         0.4           0            0           0           5      50 MBA, Hiring Funnels
Rajat Jain                 0.0        0          0            0            0           0           7**    50 MBA, AskCruz
Cohert 1 Dev Team (shared) 0.0        0          0            0            0           0           1      Idea Board
MCP Write Tool (bot)       0.0        0          0            0            0           0           3      50 MBA, AskCruz
Muskan Sharma               0.0       0          0            0            0           0           1      Hiring Funnels
Vanshi B                    0.0       0          0            0            0           0           1      50 MBA

*Priyanshu Sinha has 0 open tasks right now (his one task closed this week) — Ack is scored 0 for lack of an open-task base, not an actual failure; treat as N/A.
**Rajat Jain's 7 gap-list tasks were all created same-day today — this is a timing artifact, not neglect. Excluding it, his board is clean.

ANOMALIES / THINGS TO LOOK AT DIRECTLY
1. Acknowledgment gap, systemic on Ayan Dutta: he completed 16 tasks this week but only self-authored a note on 2 of them (task 40, task 82) before/at closing. The other 14 closed tasks (122, 159, 134, 127, 123, 153, 145, 126, 128, 163, 161, 97, 98, 191) have zero explanation from him in the chatter — all the substantive write-ups on those came from Nidhi Rana and Priyanshu Sinha auditing/QA-ing his work after the fact, not from Ayan reporting his own progress.
2. Nidhi Rana's real-world activity this week is invisible in her own score: she wrote 10+ long, detailed QA/audit notes this week (schema audits, migration reviews, staging-server checks) — every one of them on Ayan Dutta's tasks, not her own. Her combined score (2.6/10) reflects her own 1-task board, not the substantial audit work she's actually doing. Worth tracking her contribution separately if this pattern continues.
3. Jaskeerat Singh shows the same shape at smaller scale — his 4 chatter notes this week (frontend feature-test results, HR access QA) are all posted on Ayan's tasks, none on his own 4 open tasks.
4. Non-human/shared accounts holding real, active tasks: "MCP Write Tool" (a bot/API account) holds 3 open tasks across 2 boards, including one P1-flagged task ("R&D: AskCruz Voice Call-In") that's sat untouched for 11 days. "MBA Cohert 1" and "Cohert 1 Dev Team" are shared/group logins, not individuals — any score attributed to them is really an unassigned-to-a-person bucket and should probably be reassigned to real owners.
5. Idea Board is functionally dead: 7 of 8 tasks belong to Ayan Dutta, all in stage "Idea," zero moves and zero notes all week (one task 12+ days untouched). If this board still matters, it needs an owner decision, not another week of silence.
6. Hiring Funnels task 142 ("0 to 1 SDR") thrashed across 4 different people's hands this week (6 stage changes) with no net progress — looks like a coordination problem, not individual underperformance.
7. Board-attribution masking: Ayan Dutta's 6.0/10 combined score is carried almost entirely by his Customer 1-EOXS work (16 completions there this week alone, plus most of the movement weight). His Idea Board and half his AskCruz load are completely dormant — the combined number hides a real board-specific problem.
8. No completed task this week shows signs of being "acknowledged before closing" for most of Ayan's 14 unexplained completions above — same finding as #1, restated because it's the biggest single data point this week.

Sources: teams-askcruz (live Odoo SQL) — project_project, project_task, project_task_type, mail_message, mail_tracking_value, res_users, res_partner. All figures current as of 2026-08-17 ~21:30 (server time).
