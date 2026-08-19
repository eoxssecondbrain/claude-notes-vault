---
thread_name: "employee-report-card-parameters"
user: "isha"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

**Human:** Do it for Isha Bisht

**Assistant:** [Queried eoxs-teams (Eoxs_team connector) for hr_employee/res_users to find Isha Bisht's partner_id, then joined mail_message on author_id for 2026-08-10 to 2026-08-17. 75 rows returned; filtered to message_type='comment' (actual authored log notes vs system notifications) on model='project.task' — 11 comments across 4 tasks: "Need to share weekly invoice details with Raj sir", "Report Google Reviews", "Review Onboarding/Offboarding Process", "Revoke All Access – Anvitha", "Revoke All Access – Ankit Pachuri". Also confirmed her 0.5-day leave via hr.leave message "Your Casual Leave planned on 2026-08-10 12:00:00 has been accepted".]

Ran it. Data pulled: CATTR figures from the weekly report email (Isha Bisht — 35.4h worked, 33.8h expected, 56.5% productivity, 0.5 days leave). Log notes: 11 comments she authored on project.task in eoxs-teams (mail_message, model='project.task') between 2026-08-10 and 2026-08-16, across 4 tasks.

CATTR base score
Productivity 56.5% × 0.5 = 28.25
Hours adherence: 35.4h / 33.8h = 104.7% × 0.5 = 52.35 — assumption flagged: I did not cap this at 100% for hours over the expected amount, since the team's own notes said extra hours should be rewarded. If you want it capped instead, base drops to 78.25 instead of 80.6.
Base score = 80.6

Log-notes score
Completeness 20/25 — comments logged on every working day except the half-day she was on leave (leave record confirms "Your Casual Leave planned on 2026-08-10 12:00:00 has been accepted").
Specificity 18/25 — several concrete and traceable, e.g. "Pending Payment Invoices: Discount Pipe & Steel, Sabre Alloys, Greer Steel Company" and "Received Anvitha Shetty's signed resignation letter and completed the required exit formalities for her." A few are low-content: "ok", "attached here."
Corroboration with Cattr 10/25 — no note explains the gap between 35.4h logged and only 56.5% productivity; nothing contradicts it either, it's just unaddressed.
Blockers/escalation 10/25 — no blockers or delays flagged anywhere this week.
Log-notes score = 58

Final = (80.6 × 0.5) + (58 × 0.5) = 69.3 → Needs attention (0.7 points under the Solid cutoff)

Summary: Isha Bisht scores 69.3, Needs attention. The CATTR half is strong — 56.5% productivity and 104.7% hours adherence (35.4h against a 33.8h expectation) — but the log-notes half pulls the result down: notes are mostly specific and cover every working day, yet none explain why measured productivity is only ~56% despite the high hours logged, and no blockers were flagged all week. This is a single week with no prior period to compare, so whether the productivity number is a one-off or a pattern can't be said yet — that needs next week's data, not a guess now. One structural flag: "log notes" here means Odoo project-task comments, and her role (HR) routes a lot of real work through leave approvals, offboarding, and direct messages rather than task updates — the same designation-based scoring gap the original team session raised and never resolved.

Let me know if the uncapped hours-adherence assumption stands, and which employee's next.
