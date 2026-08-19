---
thread_name: "employee-report-card-parameters"
user: "isha"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

**Human:** You are an employee productivity report card generator. You receive two inputs
for one employee, for one reporting period, and produce a single blended
assessment.
Take both parameters equally 50-50 for sscoring 


INPUT 1 — CATTR DATA (quantitative)
- Productivity % (active time / tracked time, or CATTR's own productivity metric)
- Working hours logged vs. expected/scheduled hours
- Any CATTR-flagged idle time, app/category breakdown if provided

INPUT 2 — LOG NOTES (qualitative)
- Free-text notes: task descriptions, blockers, manager comments, self-reported
  context (e.g. "spent 2hrs on client call, not reflected in CATTR")
- Treat this as context that can explain or adjust the raw numbers, not as a
  separate score to average in blindly.

SCORING METHOD
1. Compute a base score (0-100) from CATTR data:
   - Productivity % contributes 60% of the base score
   - Hours adherence (logged vs expected) contributes 40% of the base score
   - If either figure is missing, state that explicitly and score only on
     what's available — do not invent a number.
2. Apply a qualitative adjustment (-15 to +15) based on log notes:
   - Positive: legitimate reasons for low tracked time (client calls, offline
     work, meetings) that CATTR wouldn't capture
   - Negative: notes indicating disengagement, repeated unexplained gaps, or
     contradicting the CATTR data
   - No notes, or notes with no bearing on the numbers → adjustment = 0
   - Never let the adjustment flip a clearly poor CATTR result into a "good"
     final score without a specific, quoted reason from the notes.
3. Final score = base score + adjustment, clamped to 0-100.
4. Map final score to a band:
   - 85-100: Strong
   - 70-84: Solid
   - 55-69: Needs attention
   - Below 55: At risk

RULES
- Never fabricate a number, quote, or reason not present in the inputs.
- If CATTR data is missing, incomplete, or contradictory, say so — do not
  smooth it over.
- Quote the specific log note phrase that drove any adjustment; an adjustment
  without a quoted reason is not allowed.
- Do not speculate about intent, mental state, or reasons beyond what the
  notes state.
- Keep the readable summary to 4-6 sentences. No filler, no praise padding.


2. A short readable summary (4-6 sentences, plain text) covering: the final
   score and band, what drove it, any data gaps, and one flag if the trend
   looks concerning (repeated low weeks, contradicting notes, etc.) — omit
   the flag line if nothing stands out.

**Assistant:** Before I treat this as the operating spec, two contradictions worth resolving.

You say "take both parameters equally 50-50 for scoring" at the top, but the SCORING METHOD below doesn't do that: the base score is 100% CATTR (60% productivity + 40% hours adherence), and log notes only ever apply a capped ±15-point adjustment on top. On a 0-100 scale, that means log notes can move the result by at most 15 points — roughly 15% of the outcome, not 50%. These are two different formulas. Which governs: a genuine 50/50 blend (which would need its own log-notes-to-score conversion, not an adjustment), or the capped-adjustment model you spelled out in SCORING METHOD — in which case the "50-50" framing at the top should be dropped since that's not what the method does?

Second, the message jumps straight to "2. A short readable summary..." with no "1." above it. Looks like the first output item (presumably the numeric score/band/breakdown) didn't make it into what you pasted — was there more before this?

Separately: no employee's actual Cattr figures or log notes are attached here, so there's nothing to run yet — this only defines the method. Once the weighting question is settled, send me one employee's data for a period and I'll produce the blended assessment against it.
