---
thread_name: "askcruz-customers-pipeline"
user: "raj"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

# AskCruz Customers & Pipeline

**User:** Can you tell me about how many customers AskCruz has and which prospects are in the pipeline?

**Assistant:** Based on the AskCruz CRM (Ask Cruz Odoo, `crm_lead`) and known deal context:

Customers (paying)

Only 2 confirmed signed AskCruz customers: Sabre Alloys and 3GM Steel. The CRM itself doesn't reflect this cleanly — 3GM Steel shows as "Won" stage there, but Sabre Alloys still sits in the raw "Leads" stage despite being a paying account, which is the CRM-unreliability issue already flagged.

Pipeline (22 total lead/opportunity records in CRM)

| Stage | Count | Notable names |
|---|---|---|
| Won | 1 | 3GM Steel |
| Proposal | 1 | Michael Mercadante (91.67% probability — this is the Sabre Alloys expansion/proposal contact) |
| Follow-up Action | 1 | Lawerence 3D Metals (marked closed 8/27) |
| Leads (untouched, $0 revenue logged) | 19 | Hascall Steel, Esserman Steel, Ratner Steel Supply, Alliance Metal Products, Cowtown Express, Denton J. Nordhues (Leeco Steel), North American Steel Alliance, Maverick Steel, Curtis Steel, Hephaistos Building Supplies, Modern Metals Magazine, FerroSource, Bossard (Smart Quote AI), Ava Hascall, Juan's network, Aviva-Pacesetter, Greer Steel, Eastern State Steel, Sabre Alloys (duplicate lead entry) |

Gap: Collier Metals and IMS Metals/Ram Shenoy — two of the more advanced deals you've been working (IMS has a formal $48K + $3.5K/month proposal out) — don't appear in this CRM at all. That's the same board-reliability problem: real deal activity is happening in email/calls, not getting logged here.

Bottom line: 2 paying customers, ~$7K MRR confirmed. Active proposal-stage or later-stage deals outside what's captured in CRM: Collier Metals, IMS Metals, Sabre Alloys expansion (Michael Mercadante), 3GM Steel expansion (Travis Lane). Everything else in the CRM (19 records) is cold/untouched.

Source: Ask Cruz Odoo CRM (teams-askcruz, live query, Aug 28 2026) cross-referenced with known deal context; no eoxs-db wiki hits came back for AskCruz-specific pipeline pages, so this leans on the live CRM plus what's already tracked.
