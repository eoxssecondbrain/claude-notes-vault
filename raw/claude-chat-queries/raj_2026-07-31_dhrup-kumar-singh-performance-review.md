---
thread_name: "dhrup-kumar-singh-performance-review"
user: "raj"
type: claude-chat
created: 2026-07-31
updated: 2026-07-31
---

User: make me a preformance review for dhrup.

Assistant: [Read threads-ov and raj-eoxs-vault skills per user preference. Asked rigor-level and purpose clarifying questions via ask_user_input_v0 tool.]
Questions asked:
1. What rigor level for Dhrup's performance review? Options: 5ft deep - quick pass from available records / 10ft deep - verified against underlying records / 50ft deep - full investigation incl. adjacent risks/blind spots
2. What's this review for? Options: Comp/raise decision / General check-in / record / Role or scope change / Other (I'll specify)

User answers:
Q: What rigor level for Dhrup's performance review?
A: 50ft deep - full investigation incl. adjacent risks/blind spots

Q: What's this review for?
A: Role or scope change

Assistant: [Queried OV2 get_index, OV2 get_wiki_page "Dhrup Kumar Singh", OV2 get_wiki_page "HR Weekly Team Reports — Overview", OV2 get_wiki_page "Dhrup Kumar" (weekly time tracking), EOXS Teams Live queries for project_task assigned to user_id 33 (Dhrup Kumar Singh), task stage breakdown, stalled task list with days-in-stage, monthly "Paid" task completion counts, and planned/effective hours sums, plus OV2 search_emails "Dhrup" on raj_gmail.]

Final response delivered:

Performance review — Dhrup Kumar Singh, Lead Developer. 50ft deep, built for a role/scope change decision.

## 1. Current role & standing

Lead Developer, EOXS engineering. Owns the approval chain: developer self-test → Dhrup code review/QA → Ron J functional approval → production. Reports structure below him includes a "production team" layer under Nizamuddin, headcount otherwise undocumented.

Compensation: INR 80,000/month (2026), rising to a fixed INR 90,000/month 2027–2034 under a signed 10-year agreement — unusually long-horizon for an India-based dev hire, with a 5-year non-compete (no geographic limit) and arbitration in Chandigarh/Delhi/Toronto. This is a retention-heavy contract, not a standard at-will arrangement — worth knowing before any scope conversation, since the downside of a bad scope call is harder to unwind than with most hires.

## 2. What he's actually built (real strength)

He authored all three of EOXS's core engineering SOPs on 2026-06-30 in one push: GitLab branching/deployment, code review & QA, and development standards. These are the governing documents for how the entire dev org ships code. That's a genuine architectural contribution, not busywork — someone has to own "what does good look like here," and he did.

He's also been doing real hands-on infra/dev work since at least 2024 (server config, access rights, client troubleshooting) — the SOP authorship isn't a first flash of competence, it's a senior operator finally formalizing what he'd already been doing.

## 3. Live task load (EOXS Teams DB, pulled just now)

44 active tasks assigned to him. 27 are in "Paid" (closed/billed). Throughput on closed tasks by month: Feb 5, Mar 4, Apr 0, May 1, Jun 9, Jul 8 — a real dip in Apr/May, recovering sharply in Jun/Jul (which lines up with the DPS ultimatum period below).

15 non-closed tasks, several stalled well past normal cycle time:

| Task | Stage | Days open | Days stuck in current stage |
|---|---|---|---|
| Receiving through MTR | Scoping | 335 | 335 |
| Delivered Qty Not Updating (Multi Control Tags) | QA Passed | 204 | 101 |
| Log Deletion of Processes on SO | On Live | 198 | 86 |
| DPS Code Videos | Task Pool | 196 | 25 |
| PPC Code Videos | Task Pool | 196 | 25 |
| Review Integrations, DPS | Tabled | 178 | 106 |
| Install Theme in System | Tabled | 157 | 76 |
| Missing Negative Entries, Inventory Valuation | On Sandbox/QA | 129 | 14 |
| CODE 101 Module Transition Loading Screen | QA Failed | 80 | 53 |
| Unable to Confirm Packing List | Assigned | 78 | 38 |

A task sitting in "Scoping" for 335 days with no deadline set is not an edge case — it's the same pattern Rajat called out company-wide today (2026-07-31): tasks sitting past 90 days, one over 300 days with no response to nudges. That memo, sent to Dhrup's own team, effectively describes Dhrup's own task list. That's not circumstantial — it's the exact evidence.

Note: planned_hours/effective_hours are 0 across his entire task list. Timesheet/effort tracking isn't actually being used at the task level, so none of this can currently be cross-checked against time invested — a real blind spot if you're trying to judge efficiency, not just output.

## 4. The pattern that should worry you most

Three separate threads converge on the same theme — commitments made, then silence:

- DPS packing-list bug (2026-07-08): Rajat gave a 2-day, full-ownership ultimatum after "three builds failed QA three times" and 100+ tickets from one client. The actual fix shipped a week later, not two days — whether that's Dhrup missing his own deadline or Rajat's timeline not surviving real QA isn't fully established, but the pattern of slipped commitments is now twice-documented.
- June SOP assignment: Dhrup was assigned a solo "Server Infrastructure & Upgrade SOP" and a joint "Data Migration & Cleanse SOP," due June 29. Neither is confirmed delivered — Ron's status updates never mention Dhrup's pieces. He did deliver three other SOPs four days later, so it's plausible those substituted, but nobody's confirmed it either way.
- Team-growth request (2026-07-25, escalated 2026-07-31 — today): Rajat asked Dhrup directly for headcount under his production layer and a six-month growth plan. Six days later, no reply. Rajat's follow-up was a single "??". Still unanswered as of this pass.

Separately, the HR weekly-report data (Cattr-tracked) shows a declining productivity metric across five weeks: 42.7% → 40.3% → 31.0% → 28.3% → 27.2%, with 87% late logins in the June monthly summary — despite hours worked meeting or exceeding expected hours most weeks. Take Cattr's productivity score with a grain of salt (it's an automated proxy, not a judgment call), but the trend direction combined with the unanswered-request pattern and the stalled task list is three independent signals pointing the same way, not one noisy metric.

## 5. Read on this, for a scope-change decision specifically

You asked for role/scope change as the purpose. The evidence complicates a scope expansion right now, specifically because the thing you're deciding — does he lead a bigger team — is the exact thing he's currently not responding to when asked directly. If he can't close the loop on "how many people report to you and what's your 6-month plan" after a direct ask and a follow-up, handing him more organizational scope compounds the risk rather than testing it.

On the flip side: the SOP-authorship work is real senior-level output, done unprompted-relative-to-any-crisis, and it's exactly the kind of work that scales — it doesn't need him personally in the loop once it exists. If the "scope change" under consideration is more architectural/technical authority (more say over standards, code review gate, technical direction) rather than more people-management, the case is much stronger than if it's "give him a bigger team."

Before deciding, I'd want a direct answer from him on the team-growth email — not another Claude-side data pull — since that's the single cleanest signal of whether he can operate at a bigger scope. I'd also want to know whether the 300+-day Scoping task and the two 196-day-stalled video tasks are genuinely his to unstick or if they're blocked upstream (client, QA capacity, Ron's approval queue) — the data here shows where things sit, not whose bottleneck it is.

Sources: OV2 wiki page Dhrup Kumar Singh (updated 2026-07-31 material), HR Weekly Team Reports — Dhrup Kumar page, EOXS Teams Live project_task (live query, 2026-07-31).
