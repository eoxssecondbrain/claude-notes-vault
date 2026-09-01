---
thread_name: "askcruz-board-management-logic"
user: "ayan"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

USER:
in board structure it is mentioned arcs crews, it is AskCruz, fix it. Also we should have guidance on how to properly communicate with log notes, tagging relevant people, how assigning works,

How to put daily snippets.

A guidance for everyone to follow

ASSISTANT:
Updated AskCruz_Team_SOP.docx (regenerated from the same build script, re-verified by rendering to PDF/images):

- Fixed "ARCS Crews (AskCruz)" to just "AskCruz" everywhere it appeared (Purpose section and Board Structure list).
- Added section 5, "How Assigning Works": owner assigns, multi-assignee tasks (builder + QA reviewer both stay tagged), tasks needing external input belong in Requirements/Need Discussion not silent in Assigned, say when your part is done and tag the owner, say why if you can't start yet.
- Added section 8, "How to Write a Good Log Note": say what you did and what needs to happen next, tag (@mention) whoever needs to act, be specific with a good vs bad example, log actual QA pass/fail results not just "done," name specifically what a blocker is waiting on ("waiting on Talal for SSH access" vs "stuck"), note explicitly if a Recurring Task wasn't touched and why.
- Expanded section 9, "Daily Snippets": post to your own task every working day, keep it short but specific enough for the team lead and automated digest to tell real work happened, note absences instead of skipping silently, post it yourself (team lead can't post on your behalf), plus the existing team-lead-standing and flag rule.
- Renumbered all subsequent sections (What Gets Flagged now 10, Automated Monitoring 11, Daily Routine 12, Questions 13) and fixed the internal cross-reference to the log-note cadence section (now correctly points to section 7).

Delivered as an updated 3-page Word document via present_files.
