---
thread_name: "cattr-data-access-question"
user: "ron"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

Formula correction round 2: Ron clarified the real mechanic — 40 hrs/week is the standard employee baseline (protected, never costs extra to fall below); the 20 hours above that (60 total) are "founder" hours tied to the 5yr goal. weekly_target (goal/260) is the value of those 20 hours, so hourly_rate = weekly_target/20 (not /60). Then Ron added a cap: a week can never lose more than the full weekly_target even if hours worked are well under 40 (Sheenam's case) — because the employee baseline isn't itself at risk. Confirmed: surplus above 60 hours is uncapped on the upside at the same /20 rate.

Final formula: extra_hours_worked = max(hours_worked-40, 0). If extra<20: shortfall=20-extra (capped at 20) -> delta = -(shortfall/20)*weekly_target. If extra>20: surplus=extra-20 (uncapped) -> delta = +(surplus/20)*weekly_target.

Recalculated week 1 (Aug 24-30): Ron 42h worked, 2h of 20 founder hours covered, delta -$34,615.38, balance $9,965,384.62. Sheenam 35.6h worked (under 40h baseline, extra=0), shortfall capped at 20, delta -$19,230.77 (exactly her full weekly_target, not more), balance $4,980,769.23.

Actions taken: 
1. Old Drive tracker file (id 1S6L9uxPyeCle10fOAVmzssHuvXFVTNxU) could not be trashed (permission denied by classifier) so renamed to "SUPERSEDED - Ownership Pace Tracker (wrong formula, do not use)".
2. New Drive tracker file created (id 1y7xtoTZxHUvs7aHuQA0Xleb0O4GzqIJp), title "Ownership Pace Tracker", with corrected formula description and week 1 figures.
3. Scheduled task trig_01EMxMYQ4iRXV9iiGZB9RV4p renamed "Mission Freedom Weekly Report" and prompt fully rewritten with the 40/20 split formula, the cap rule, pointer to the new tracker file id, and instructions to supersede-and-recreate the Drive file each run (since Drive content can't be overwritten in place, only trashed+recreated or renamed if trash is blocked).
4. Sent third email ("Mission Freedom — Week of Aug 24-30, 2026 (corrected)", Gmail id 1a05fbeb52f0f838) to rajat@eoxs.com, sheenam@eoxsteam.com, ronn@eoxs.com with the corrected numbers, explicitly stated as replacing the two earlier wrong emails.

Known constraint for future runs: Google Drive connector here has no "update file content" tool, only create/trash/rename/copy/share — the automation prompt documents the trash-or-rename-then-recreate workaround.
