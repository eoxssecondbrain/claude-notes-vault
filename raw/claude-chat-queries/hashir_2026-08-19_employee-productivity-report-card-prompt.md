---
thread_name: "employee-productivity-report-card-prompt"
user: "hashir"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

User: I need you to provide me a prompt which needs to be provided to claude based on two parameters which would be used for creating Employee productivity report card automation , those two parameters are cattr productivity and working hours and the second one could be based on the log notes ...

Assistant: [called ask_user_input_v0 with three questions]
Q: How should the two inputs combine into the report card?
Options: Single weighted score (CATTR % + hours blended with log notes context) / Separate scores per input, no blending / Qualitative narrative only, no numeric score

Q: Output format needed?
Options: Structured JSON (for pipeline/automation) / Formatted text/markdown report (human-readable) / Both JSON and readable summary

Q: Where will this prompt run?
Options: Direct Claude API call inside an automation (n8n/Zapier/script) / Claude Project custom instructions, run manually per employee / Not sure yet / just want a general-purpose version

User answers:
Q: How should the two inputs combine into the report card?
A: Single weighted score (CATTR % + hours blended with log notes context)

Q: Output format needed?
A: Both JSON and readable summary

Q: Where will this prompt run?
A: Not sure yet / just want a general-purpose version

Assistant: Two blending questions to settle before I write this: what "log notes" actually contain (task descriptions, self-reported blockers, manager comments?) and whether these report cards score individuals or teams. I'll build a general-purpose version with those as configurable inputs rather than guessing — you can tighten it once you point this at a real pipeline.

[created file /mnt/user-data/outputs/employee-productivity-report-prompt.md with the following content, then presented it via present_files]

# Employee Productivity Report Card — Claude Prompt

Two inputs, one blended score, dual output (JSON + readable summary).
Copy the block below as the system prompt. Fill `{{CATTR_DATA}}` and `{{LOG_NOTES}}` per employee per run.

---

## SYSTEM PROMPT

```
You are an employee productivity report card generator. You receive two inputs
for one employee, for one reporting period, and produce a single blended
assessment.

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

OUTPUT — return both blocks, in this order:

1. A fenced JSON block:
{
  "employee": "<name or ID from input>",
  "period": "<reporting period from input>",
  "cattr_productivity_pct": <number or null>,
  "hours_logged": <number or null>,
  "hours_expected": <number or null>,
  "base_score": <number>,
  "qualitative_adjustment": <number>,
  "final_score": <number>,
  "band": "<Strong|Solid|Needs attention|At risk>",
  "adjustment_reason": "<quoted note phrase, or null if adjustment is 0>",
  "data_gaps": ["<any missing/unreliable input>", ...]
}

2. A short readable summary (4-6 sentences, plain text) covering: the final
   score and band, what drove it, any data gaps, and one flag if the trend
   looks concerning (repeated low weeks, contradicting notes, etc.) — omit
   the flag line if nothing stands out.

INPUTS FOR THIS RUN:

CATTR DATA:
{{CATTR_DATA}}

LOG NOTES:
{{LOG_NOTES}}
```

---

## Notes on the parts I assumed

- **Weighting (60/40, ±15 cap):** arbitrary starting point. If your CATTR export has a category breakdown or idle-time detail you want weighted separately, that changes the base-score formula — tell me and I'll adjust it.
- **Log notes source:** written to accept anything (manager comments, self-reported, task tool exports). If they're one specific format (e.g. a fixed template with blocker/task/hours fields), the prompt can parse them more precisely instead of treating them as free text.
- **Scope:** built for one employee per run, since that's the safer default for a report-card automation. If you need team/roll-up aggregation, that's a second prompt layered on top of these JSON outputs, not the same prompt.
- **Deployment:** this is model-agnostic text — drop it into an API call, an n8n/Zapier prompt node, or a Claude Project system prompt as-is once you land on where it runs.
