---
thread_name: "weekly-askcruz-scrum-report"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

## User (scheduled task, automated firing)

1. Locate the askcruz project management connector (teams-askcruz / "Ask cruz"). If you cannot find or reach it, stop and report that as the finding — do not substitute a different board.
2. Call get_business_schema (or list_tables + describe_table) on it first to confirm current field names for: task stage, assignee, priority, log notes/chatter, and stage-change timestamps. Do not assume a prior schema.
3. Pull, for the 7-day window ending today:
   a. Total tasks currently on the board.
   b. Total tasks in a "Completed" (or equivalent) stage, and how many of those were completed within this window.
   c. Every task with one or more stage changes in this window — old stage, new stage, who moved it, and when.
   d. Every task with at least one log note (chatter message, not a stage-change system log) dated within this window, and who posted it.
   e. Every open task assigned to someone that got zero log notes and zero stage changes across the entire window — this is the gap list, the most important number here.
4. For each team member with tasks assigned on the board, compute a score out of 10 for the week:
   - Acknowledgment (0-2): share of their open tasks with at least one log note sometime in the window. 100%=2, ≥50%=1, <50%=0.
   - Movement (0-3): stage-advances across the week, weighted 1.5x for high priority, 1x normal, 0.5x low. Calibrate the full-marks bar to roughly 5x the old daily bar as a starting point (i.e. ~15 weighted moves = 3 pts) — this is a placeholder until real data sets the actual baseline.
   - Completions (0-2): 1 pt per task completed in the window, capped at 2.
   - Engagement depth (0-2): based on log note specificity across the week (mentions blockers, next steps, or concrete detail vs generic one-word notes). Flag this component explicitly as a low-confidence proxy in the output.
   - Scope engagement (0-1): 1 pt if they touched at least one high-priority/flagged task during the window.
5. Output format, in this order:
   - Board summary: total tasks, total completed (all-time and this week), tasks moved this week, tasks acknowledged this week, gap list (untouched tasks + assignee, with days-since-last-activity for each).
   - Per-person weekly report card: name, score /10, one-line breakdown of the five components, gap-list count if nonzero.
   - Flag anything anomalous: a person with zero activity all week, a task open >7 days with no log note at any point, or a completed task that never got acknowledged before closing.
6. Keep it brief and scannable — this is a weekly read, lead with the numbers, no long preamble.
7.  Email Delivery:
   - Once the report is generated, use the email tool to send the complete output.
   - To: rajat@eoxs.com
   - Subject: Weekly AskCruz Board Scrum Report - [Today's Date]
   - Body: Paste the full scannable output from Step 5.

## Assistant

Ran the weekly AskCruz scrum report and emailed it to rajat@eoxs.com. Summary of what I found:

**Scope call:** The teams-askcruz Odoo instance actually hosts 6 active project boards (AskCruz, 50 MBA Interns Cohort, Customer 1-EOXS, Idea Board, Hiring Funnels, +1 more). Since the task said "the board" without specifying which, I scoped to the project literally named "AskCruz" (project_id 6) as the clearest match. Flag me if you want it widened to all boards or a different one — I proceeded rather than blocking since this is an unattended run.

**Board summary (window: Aug 11–17, 2026):**
- Total tasks: 39 active
- Completed: 9 all-time, 3 this week (tasks 154, 137, 131)
- Stage changes this week: 7
- Tasks acknowledged (≥1 note) this week: 20 of 39 (51%)
- Gap list: 11 tasks with zero notes + zero stage changes all week — 9 on real people, 2 on a "MCP Write Tool" bot account

**Report card (out of 10):** Sheenam 5.6, Ron 3, Ayan Dutta 1.4, Rajat Jain 0, Nidhi Rana 0, Yashvir Singh Thakur 0.

**Anomalies worth your attention:**
1. Ron's Ack score reads 100% but he authored zero comments this week — every note on his tasks was Ayan Dutta chasing him for status. The metric doesn't check authorship, so that score overstates his real engagement.
2. Task 137 ("Ask Cruz LinkedIn Page") was created and marked Completed same-day with zero log notes ever — closed with no documented work.
3. Four of Ayan Dutta's tasks have sat untouched 9–11 days with zero notes ever (Integrate Email Data into Vault, Front End Function, Project Manager Skill, QA on AskCruz iOS app).
4. The board's one high-priority/flagged task ("R&D: AskCruz Voice Call-In") is assigned to the non-human "MCP Write Tool" account and has had zero engagement in 10 days — looks like a data/assignment issue.
5. Isha is actively working this board (2 moves, 5 notes, moved 2 of Sheenam's tasks to Completed) but has no tasks formally assigned to her here — informal cross-coverage worth tracking explicitly.

Full report with per-task gap list and per-person breakdowns is in the email sent to rajat@eoxs.com.
