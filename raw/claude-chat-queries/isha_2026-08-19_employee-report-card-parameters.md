---
thread_name: "employee-report-card-parameters"
user: "isha"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

**Human:** it was by mistake 60% productivity and 40% hours take it 50-50%  for scoring

**Assistant:** Confirming the interpretation, since "50-50" could mean two different things in that spec: within the CATTR base score, productivity and hours adherence are each 50% (not 60/40) — but log notes still work as the capped ±15-point adjustment on top, not a full 50% weight against CATTR. That's a different thing than "CATTR 50 / log notes 50" at the top level, which is how your original message read before this correction. If that's right, here's the corrected method:

Base score = (Productivity % × 0.5) + (Hours adherence % × 0.5), 0-100.
Adjustment = -15 to +15 from log notes, quoted reason required, 0 if notes don't bear on the numbers.
Final = base + adjustment, clamped 0-100, mapped to band (85-100 Strong / 70-84 Solid / 55-69 Needs attention / <55 At risk).

If you actually meant CATTR and log notes should be true 50/50 overall (log notes worth up to 50 points, not capped at 15), say so — that needs a different formula, not a small tweak.

Send an employee's Cattr figures and log notes for a period whenever you want me to run it.
