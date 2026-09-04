---
thread_name: "eoxs-time-off-extract"
user: "isha"
type: claude-chat
created: 2026-09-04
updated: 2026-09-04
---

User: Sep 2026 leave data

Assistant: [Re-queried EOXS Team Live (Odoo) live rather than reusing cached extraction, to account for any approval changes since last pull. SQL: SELECT e.name AS employee_name, lt.name AS leave_type, l.date_from, l.date_to, l.number_of_days, l.state FROM hr_leave l JOIN hr_employee e ON e.id = l.employee_id JOIN hr_leave_type lt ON lt.id = l.holiday_status_id WHERE l.date_from >= '2026-09-01' AND l.date_from < '2026-10-01' ORDER BY e.name, l.date_from — returned 2 rows, matching the cached data. Confirmed live matches cache.]

Live data confirmed. Only 2 leave records logged for September 2026 so far (makes sense — today is Sep 4).

| Employee Name | Leave Type | Leave Start Date | Leave End Date | Number of Days | Status |
|---|---|---|---|---|---|
| Aryan Bakshi | Sick Leave | 09/01/2026 | 09/01/2026 | 1 | Approved |
| Nidhi Rana | Sick Leave | 09/04/2026 | 09/04/2026 | 1 | Refused |

Note Nidhi Rana's entry was refused, not approved — flagging in case you were expecting it to count as taken leave.
