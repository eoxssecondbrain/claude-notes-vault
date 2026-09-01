---
thread_name: "askcruz-board-management-logic"
user: "ayan"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

USER:
this is a meeting transcirpt in which i am talking about how i manage out Askcruz project board, how each tasks are moved into different stages and how it is maintained by me. Go through this call, and you also have access to Askcruz MCP to look at the board. Get yourself upto speed so we can have an informed discussion.

[Attached document: "Impromptu Zoom Meeting - August 29" — full transcript between Ayan Dutta and Kriti Jain covering AskCruz project board management: stage flow, ownership rules, QA policy, judgment criteria, and action items.]

ASSISTANT:
I went through the call and pulled the live board (Ask-Cruz/askcruz Odoo). Here's where things stand.

Logic from the call, distilled:

Stage flow: Intake (unassigned, new) → Requirements (blocked on someone outside the team) / Need Discussion (blocked on an internal brainstorm) → Assigned → In Dev → QA → Complete. Tabled sits parallel — parked work, owner's call. Recurring/Continuous tasks don't move stages at all; they're tracked by whether a daily log note gets posted.

Ownership rule: only the owner moves a stage — one exception: the assignee can move Assigned → In Dev themselves. Only the owner can move a task to Complete (Jaskirath owns his sub-team's tasks even though he's a developer, so his team can't close their own work, he can).

Judgment: no formal scoring system — Ayan reviews every task personally against the scope in the task description. Proxy signals discussed for automating this later: missing log note in In Dev/QA on any given day = flag; missing log note in Assigned every other day = flag; a non-owner moving a stage = flag; a task sitting in Assigned for an extended period with no explanatory log note = flag. Talal is explicitly carved out of Ayan's team's reflection since he's not actually on the team.

QA rule: whoever built it can't QA it. Kriti's resolution: assigned_to may show both people (builder + QA'er), ownership/credit for the build stays with whoever's log note shows they did the work.

Daily Snippets: Ayan's team runs it with the team lead owning the report and the individual assigned — lead gets credit/penalty for their reports' log-note discipline. Kriti flagged this diverges from the company standard (assignee = owner = whoever's log note it is) and is letting it stand for now, but wants consistency.

Seven action items came out of it: email team on the stage-change/ownership policy, email team on the QA cross-check policy, replicate the EOXS board structure onto 3GM, stand up a 3GM Support board, stand up a Bannon board, clean up/ignore stale access-related tasks for Jaskirath's team, and send Kriti the current org chart.

What the live board actually shows right now (Sept 1):

AskCruz (their own internal board) — 60 active tasks, but only using 5 stages: Intake, Assigned, QA, Completed, Tabled. No tasks currently sitting in Requirements, Need Discussion, In Dev, or Recurring — either genuinely empty or those stages aren't even attached to this project.

Customer 1 - EOXS — matches the full description exactly: all 9 stages present (Intake, Recurring Tasks, Requirements, Assigned, In Dev, QA, Complete, Need discussion, Tabled), 65 of 90 tasks sitting in Complete.

Customer 2 - 3GM — partially replicated. Has Intake, Recurring Task, Assigned, In-Dev, QA, Complete, Tabled — still missing Requirements and Need discussion. So the "replicate EOXS structure" action item looks incomplete as of today.

Bannon board and 3GM Support board — neither exists yet in the project list. Both action items appear not started.

AI interns — only 4 tasks total (3 Complete, 1 In Dev), light usage. Idea Board — 10 sitting in Idea, 1 moved past it, consistent with Ayan's comment that it's a backlog, not actively worked.

Caveat: this was a fast reconnaissance pass — aggregate counts and stage presence, not a log-note compliance audit or a check of unauthorized stage moves. If you want either of those (e.g. "who's been sitting in Assigned without a log note" or "any non-owner stage moves in the last week"), that's a real query I can run — say the word and I'll pick it up at whatever depth you want (quick count vs. verified against actual chatter history).

What do you want to dig into first?
