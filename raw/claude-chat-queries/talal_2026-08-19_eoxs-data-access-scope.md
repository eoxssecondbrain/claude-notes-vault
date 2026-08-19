---
thread_name: "eoxs-data-access-scope"
user: "talal"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

User: Ok what are threshould access areas that i should or should not touch

Assistant: Access on these connectors is scoped like this (from the eoxs-data-general skill, both connectors are read-only, no write path exists anywhere):

Clearance level: this connection has tier2_confidential and tier2. It does not have tier1 (Raj's own personal data). That's a hard boundary, not something to route around.

Always stripped, regardless of tier:
- Every monetary figure — payroll, salary, bonus, invoice totals, deal size, discounts, vendor payments, investor amounts. Shows as [restricted: amount].
- Employee activity/performance/productivity monitoring data (e.g. Cattr) — the whole mention is stripped, not just a number.

Everything else in tier2_confidential (legal/compliance, investor relations, vendor contract terms, financial-statement discussion) is fully visible in text.

Not found is final and ambiguous by design — it means the record genuinely doesn't exist, or it exists but is above clearance (tier1). Same tool response either way, so I can't tell you which, and I won't guess.

eoxs-teams (raw SQL against EOXS Team Live Odoo) is not tier-filtered — it's direct database access, current by definition, and the only source for tickets, invoices, and CRM/pipeline data.

No write capability exists on either connector — nothing here creates, updates, or deletes anything.

If you meant something else by "threshold access areas" — e.g. which production servers/systems you can change freely vs. which need approval — that's a different question (covered by your own change-control rule that EOXS production systems are never touched without approval) and I'd need you to confirm that's what you're asking before I answer it as such.
