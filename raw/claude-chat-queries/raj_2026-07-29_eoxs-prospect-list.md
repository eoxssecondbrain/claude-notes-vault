---
thread_name: "eoxs-prospect-list"
user: "raj"
type: claude-chat
created: 2026-07-29
updated: 2026-07-29
---

User: prospect list of eoxs

Assistant: 252 total opportunities in the CRM (EOXS Teams Live, live query, not OV2's deprecated prospect tools). Breaking down by stage:

**Closed — not live prospects**
- WON (clients): 7 — 3GM Steel, Sabre Alloys, Discount Pipe & Steel, RW Conklin Steel, David Brannon, PPC Speciality Metals, plus Monarch's earlier WON entries don't appear here (Monarch shows as Unsure/Parked, worth checking separately)
- LOST: ~34
- Disqualified: ~15

**Live pipeline (the actual "prospect list")** — roughly 196 open opportunities, by stage:

| Stage | Count (approx) |
|---|---|
| Leads | ~55 |
| Unsure | ~40 |
| Intent | ~35 |
| Actions Pending | ~20 |
| Parked Accounts | ~20 |
| Discovery Call (Done) | ~12 |
| Client Proposal | ~7 |
| Rescheduled | 1 |

Notable open ones with real expected_revenue attached (most records show $0 expected_revenue, meaning it's not filled in — not a reliable pipeline-value indicator):
- Titanium Industries Inc — $61,632, Actions Pending, Scott Begin
- North Shore Steel — $328,800, Intent, Ron
- Three D Metals Canada — $277,107, Parked, Raj
- Superior Steel Supply — $119,017, Parked, Lew Dennen
- Coilplus — $308,400, Intent, RJ
- Farmers Copper — $73,152, Intent, RJ
- Varsteel/Varsteel Company — $484,400 / $207,600, Parked/Intent, RJ/Lew
- Worthington Industries — $4,154,400, Leads, Raj (very old, 2022, likely stale)
- Excelsior Metals — $394,320, Disqualified (dead)

Raj — this full 252-row list has a data-quality problem: 60-70% of open opportunities have $0 expected_revenue filled in and haven't had a stage update since 2025 or earlier despite "active=true" — that's not a real pipeline, that's a stale CRM. If you want, I can pull the ones stalled >90 days for cleanup, or filter to just this year's genuinely active motion.

Want the full 196-row list as a file (CSV/xlsx) instead of a truncated table, or a filtered cut (e.g. only 2026 activity, or only >$0 expected revenue)?
