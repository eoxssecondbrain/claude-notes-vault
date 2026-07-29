---
thread_name: "eoxs-business-health-view-5ft"
user: "raj"
type: claude-chat
created: 2026-07-29
updated: 2026-07-29
---

User: what are your view on eoxs, 5 ft

Assistant: [called ask_user_input_v0 with question "What angle do you want my view on EOXS from?" options: "Overall business health/trajectory (pipeline, revenue, clients)", "Progress toward the $1M ARR goal specifically", "Operational risks (billing, infra, team)", "Something else — I'll clarify in chat"]

User: [selected] Overall business health/trajectory (pipeline, revenue, clients)

Assistant: **Revenue base — thin and concentrated**
Active clients (from OV2): Sabre Alloys (~$10,970 MRR, HIGH risk), 3GM Steel ($4,759, LOW risk), Discount Pipe & Steel ($3,120, HIGH risk), PPC Metals (~$2,750, HIGH risk), Eastern States Steel (~$2,340, MEDIUM risk), Ohio Strip/Greer ($1,713), Brannon Steel (~$927 USD), RW Conklin ($450). That's roughly **$27K/month** across 8 clients — annualized ~$324K. Against the $1M ARR/12mo goal, that's under a third, and three of your five biggest accounts are flagged HIGH risk in your own vault.

**HIGH risk isn't noise — it's structural**
- Sabre: legal settlement, chronic performance issues, this is your biggest account
- DPS: legal letter from client, 4 outages, Austin escalating
- PPC: "processing performance structural" — code revert pending, churn risk explicitly noted HIGH

You're carrying real churn exposure on ~60% of MRR concentrated in three accounts.

**Pipeline — 1,952 leads sitting in one stage**
The live CRM shows one stage (id 13) holding 1,952 of ~2,400 active leads — almost certainly a dead/unqualified bucket (consistent with your memory note that ~1,124 of these are junk 2022 bulk-imported contacts never archived). Real distributed pipeline across other stages is a few hundred leads at most. This matches what's already in memory: ~4% real-signal hit rate on a 260-opportunity sweep.

**Bottom line**
- Revenue: concentrated, not growing fast enough to hit $1M ARR organically off ERP alone
- Retention: three of eight paying clients are actively at risk — losing any one is a bigger hit to ARR than most new deals would add
- Pipeline: mostly junk; the CRM inflates apparent activity
- Growth bet: it's rational that you're leaning into Krinox/GFC — the ERP book alone doesn't get you to $1M ARR on its own trajectory, and it's more fragile than the client count suggests

Want me to go 10ft on any one piece — e.g. verify the actual current MRR against real invoices rather than the wiki snapshot, or pull true CRM pipeline value excluding the junk stage?
