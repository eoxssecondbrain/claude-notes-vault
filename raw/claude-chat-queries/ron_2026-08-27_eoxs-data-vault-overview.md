---
thread_name: "eoxs-data-vault-overview"
user: "ron"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

**User:** Go through the vault and tell me what is EOXS data general.

**Assistant:** eoxs-db (the connector this vault runs through) is EOXS's synthesized "second brain" — one system covering:

- 34,864 email threads, 2,280 Fireflies calls, 136 Fathom calls — correspondence and meeting history
- 1,886 wiki pages, split: 722 entity, 635 analysis, 308 source, 164 concept, 34 prospect, 23 overview
- 828 implementation tasks (onboarding/dev work, not support tickets)
- 8 clients with cross-linked profiles (contacts, tasks, emails, calls, wiki)
- Employee directory (read + write)

Not in eoxs-db: support tickets, invoices/sales orders, CRM/pipeline/prospect deal data — those live in eoxs-teams (live Odoo). The askcruz project itself is separate again, in teams-askcruz.

Counts above are visible in this session — reflect this connection's clearance, not necessarily the full database.

**User:** Is it the DB that is called this or the tool or the connector or something else?

**Assistant:** Neither, exactly — there's no single object in the skill file called "EOXS data general." Two separate things could account for the phrase:

1. "EOXS Data" is the skill's own title (`# EOXS Data — Session Skill`) — a heading for the whole three-connector setup, not a DB, tool, or connector name itself.

2. "general" shows up separately as a tier label: eoxs-db rows carry `tier1` (Raj's personal), `tier2_confidential` (salary/payroll, investor relations, financials, legal), or `tier2` — which the skill doc glosses as "general." That's an access classification on individual rows, not a system name.

So if you meant "what's the general-tier data" — that's a clearance level (tier2) within eoxs-db, not a separate database. I answered your first question as if you meant "give me a general overview of the eoxs-db connector," which is a different thing. Which did you actually mean — the tier2/general clearance level, or the overview?

**User:** Is there something called 'EOXS data general'?

**Assistant:** No. Nothing in the skill file, the connector list, or the tool names is called "EOXS data general." The closest matches are the skill's heading "EOXS Data" (a session skill covering three connectors) and the tier label "general" (tier2) — but "EOXS data general" as a single named thing doesn't exist.

**User:** Can you tell me what is EOXS Data?

**Assistant:** EOXS Data is the name of the session skill covering the full set of EOXS data connectors — not a database, tool, or connector itself, but the guide that governs how to use three separate systems:

| Connector | What it is | Shape |
|---|---|---|
| eoxs-db | The curated "second brain" — emails, calls, implementation tasks, synthesized wiki, internal docs, employee directory | 27 tools (20 read-only + 7 employee-directory) |
| eoxs-teams | EOXS Team Live Odoo — the only source for support tickets, invoices/sales orders, CRM/pipeline/prospects | Raw SQL, read-only (4 tools) |
| teams-askcruz | The askcruz Odoo project | Raw SQL + 4 write tools (8 total) |

Key rules from that skill: default to eoxs-db first since it's synthesized and answers most things in 1-2 calls; eoxs-db rows carry access tiers (tier1, tier2_confidential, tier2/general); eoxs-teams and teams-askcruz are live and untiered; support tickets, invoices, and CRM data moved out of eoxs-db entirely in August 2026 and now live only in eoxs-teams.

**User:** Then could EOXS Data General could be acces right. Which has a special instructions to it.

**Assistant:** Yes — that's the accurate reading. "General" is tier2, one of three access-clearance levels stamped on eoxs-db rows:

- tier1 — Raj's personal
- tier2_confidential — salary/payroll, investor relations, financial statements, vendor pricing, legal
- tier2 (general) — everything else

The special instructions attached aren't unique to "general" specifically — they're the tiering rules that apply across all three levels (§2 of the skill):

- Filtering is server-side and invisible to me; there's no tool to check which clearance a given connection has
- get_index() counts reflect that connection's clearance, not a global total — I say "visible in this session," never "the database contains"
- A "not found" result is final and ambiguous by design — it means the record doesn't exist, or it exists above the connection's clearance. Same text either way. I report it as not found, never speculate that something restricted might exist
- I don't explain or apologize for tiering, and if asked directly whether data is hidden, I can say access levels exist without confirming or denying specifics
- The connector URL itself is the authorization — I never refuse a question based on topic alone (this covers sensitive areas like Raj's finances, salary, payroll, investor relations); I search first, then answer from what comes back

So "EOXS Data General" = tier2 clearance, and the special instructions are those tiering rules, not a separate distinct ruleset carved out just for "general."

**User:** Is tier 1 Raj OV Vault?

**Assistant:** No — those are two different things.

- tier1 is a row-level tag inside eoxs-db meaning "Raj's personal" data — one of three classification labels (tier1, tier2_confidential, tier2/general) stamped on individual records.
- OV2 (aliased "raj-wiki-vault" in the threads-ov skill description) is the connector itself — the tool prefix you see as `OV2:get_index`, `OV2:get_client_profile`, etc. It's the same thing as "eoxs-db" in the raj-eoxs-vault skill's terminology.

So OV2/raj-wiki-vault is the whole system; tier1 is just one of three access tags on records within it — not a separate vault.
