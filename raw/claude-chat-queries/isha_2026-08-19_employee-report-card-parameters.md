---
thread_name: "employee-report-card-parameters"
user: "isha"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

**Human:** yes cattr and log note should be equal weighatge 50-50

**Assistant:** Locking that in, but flagging it plainly first: full 50/50 weight is the exact risk the original team-wide analysis called out as the single biggest hole in this whole exercise — "you're rewarding whoever writes the longest snippet." My earlier recommendation was to keep log notes as context that adjusts the score, not a co-equal input, specifically to avoid that. Giving it 50% doesn't just partially reopen that risk, it fully reopens it: someone with mediocre Cattr numbers and well-written notes can now outscore someone with strong Cattr numbers and terse notes. If that trade-off is deliberate, fine — but it should be a decision made knowingly, not a default.

Given that, converting free-text notes into a 0-100 subscore without fabricating a number needs its own rubric, or "log notes score" is undefined and I'd be inventing exactly the kind of number the RULES section says not to invent. Proposed rubric, each component requiring a quoted phrase to justify the points awarded or deducted:

Completeness (0-25) — is there a note for every day/period the employee logged hours for. Unexplained gaps get penalized here, not guessed at.
Specificity (0-25) — do notes name concrete tasks/deliverables, not generic filler like "worked on tasks." Vague notes score low, not a default mid-range.
Corroboration with Cattr (0-25) — do the notes' claims line up with or plausibly explain the Cattr numbers (e.g. a claimed client call during a Cattr idle window). Contradictions score low.
Blockers/escalation (0-25) — were delays or blockers flagged when they happened, rather than surfacing only in this review.

No notes at all → 0 for this half, stated explicitly as a data gap, not smoothed into a mid-range guess.

Final = (CATTR base × 0.5) + (log-notes score × 0.5), banded same as before.

Confirm this rubric (or adjust it) before I treat it as final — then send an employee's data and I'll run it.
