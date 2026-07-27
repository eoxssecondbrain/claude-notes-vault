---
thread_name: "ayan-weekly-performance-eoxs-teams"
user: "raj"
type: claude-chat
created: 2026-07-27
updated: 2026-07-27
---

**User:** what is the weekly performance in eoxs team for ayan

**Assistant:** Queried EOXS Teams Live (Odoo 13) for Ayan Dutta (hr_employee id 275, res_users id 314).

Findings for this week (Jul 20-27, 2026):
- Task activity (project_task): 3 new tasks created 7/27 in "Tools" stage (Support Automation, Brannon MTR AI, Poder - OV2), all 0 progress. 1 older task ("Assigned to test Test - Dev Task") moved to "Paid" stage same day. No other tasks touched this week.
- effective_hours / total_hours_spent = 0.0 across every task assigned to Ayan (hours not being logged at all).
- hr_attendance: zero check-in/check-out records for Ayan this week.
- No timesheet entries.

Conclusion given to user: no real performance signal exists in the system currently - no hours logged, no progress %, no completion tracking, just task titles moving through kanban stages. Asked user to clarify what "weekly performance" should mean (tasks completed vs assigned, new intern KPI system not yet built, etc.), and flagged that the broader data hygiene issue (zero hours logged org-wide, not just Ayan) is itself the real finding.

**User:** what about isha

**Assistant:** Found multiple partial name matches for "isha" in hr_employee (Disha Acharia, Tisha Dhiman, Disha Jain, Aisha Fatima, Risha Sarmah, Madalisha Tomar, Isha Bisht). Proceeded with exact first-name match Isha Bisht (hr_employee id 91, res_users id 141), flagged the other partial matches in case wrong person.

Findings:
- project_task: zero tasks assigned to Isha Bisht (user_id 141), as owner or as multi-assignee - not just this week, none at all in this DB.
- hr_attendance: zero check-in/check-out records this week.

Conclusion given to user: no task or activity trail for Isha Bisht at all in EOXS Teams Live - either she's not being assigned work through this Odoo instance or nothing's logged. Suggested checking Gmail/Fireflies via the vault (OV2) if user wants to know what she's actually doing, since this Odoo tenant shows nothing.
