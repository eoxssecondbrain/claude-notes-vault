---
thread_name: "employee-report-card-parameters"
user: "isha"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

**Human:** This is final ; Final = (CATTR base × 0.5) + (log-notes score × 0.5)

**Assistant:** Locked. Full method now confirmed:

Base score = (Productivity % × 0.5) + (Hours adherence % × 0.5)
Log-notes score = Completeness (0-25) + Specificity (0-25) + Corroboration with Cattr (0-25) + Blockers/escalation (0-25), each requiring a quoted phrase to justify points
Final = (Base × 0.5) + (Log-notes score × 0.5), clamped 0-100
Bands: 85-100 Strong / 70-84 Solid / 55-69 Needs attention / <55 At risk

This is the operating method going forward for individual employee scoring.

Two things still open before this runs on anything real: I have no working access to Cattr and no confirmed source for log notes (the earlier "team.eoxs" question was never resolved — is that eoxs-db's implementation tasks, or somewhere else). For a one-off test I can work from whatever you paste me directly — one employee's Cattr figures (productivity %, hours worked vs expected) plus their log notes for a period — and score it by hand against this method. Send that whenever you're ready.
