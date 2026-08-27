---
thread_name: "priyanshu_sinha_report"
user: "nidhi"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

**User:** Hey can you report on Priyanshu Sinha

**Assistant:** I see that a tool call was declined when I attempted to search your employee directory for Priyanshu Sinha. 

To pull together a report on Priyanshu Sinha, I would need to search across emails, calls, and potentially employee records. Could you confirm whether you'd like me to proceed with searching emails and calls for any mentions of or correspondence with this person?

Alternatively, if you have specific information you'd like me to look up — such as a client profile, implementation task involvement, or a particular time period — let me know and I can search more narrowly.

**User:** can you give me any info on brannon steel

**Assistant:** **Brannon Steel** — Active client on MTR AI implementation.

| | |
|---|---|
| **Domain** | brannonsteel.com |
| **Key Contacts** | David Brannon, Kevin Brannon (K.R.), Manish Trivedi, Ranim Fallaha |
| **Primary Project** | MTR AI implementation (ongoing since Jan 2026) |
| **Status** | Weekly implementation huddles; most recent call Aug 25, 2026 |

**Engagement:**
- 29 recorded calls (mostly weekly huddles since March)
- 42 email threads spanning Nov 2025–present
- 0 active implementation tasks (no open dev work currently logged)

**Key Issues & Analysis:**
- MTR Inventory Module escalation vs. ticket status conflict (flagged in wiki analysis)
- Algoma Join Report review and pre-purchase MTR spec verification work (proposed)
- Samples tracking referenced in task threads

**Wiki Coverage:**
9 live pages including entity record, CRM details, call logs, and technical analyses. No pages pending promotion.

Would you like details on a specific call, email thread, or the inventory module escalation?

**User:** what these mcp's can give data on?

**Assistant:** Your connected MCPs provide data across three main systems:

## **EOXS Data (Synthesized Second Brain)**
*Connectors: Eoxs-data-general, RAJ (full), Raj Vault, HR., Intern, Internal Team*

**Emails & Calls**
- Full-text search across all email accounts (live + deep history)
- Call transcripts (Fireflies & Fathom, live ingestion)
- Thread reconstruction, attachment extraction

**Clients & Contacts**
- Client profiles, slug lookup
- Contact registry (name, email per client)
- Live + pending-promotion wiki pages cross-linked by client

**Implementation Work**
- Odoo implementation tasks (onboarding, dev work)
- Task stage, owner, priority, descriptions, chatter history
- Distinct from support tickets (those are elsewhere)

**Employee Directory**
- Active/inactive headcount
- Role, department, manager, employment type
- Full change history per employee
- Write capability: create, update, deactivate, reactivate

**Internal Reference Docs**
- Curated assets (SOPs, company overview, salary register, ICP, product specs)
- Wiki pages (synthesized entities, analyses, trends)

---

## **EOXS Teams Live Odoo (Operational)**
*Raw SQL connectors — current by definition, no curation*

**Billing & Revenue**
- Support tickets
- Invoices & sales orders
- CRM, pipeline, prospect data

---

## **askcruz Odoo (Project Management)**
*teams-askcruz connector — raw SQL + write capability*

**Task Management**
- Create, update, move tasks between stages
- Add notes to task chatter
- Read task schema via SQL

---

## **Threads OV (Conversation Archive)**
*Internal record-keeping for Claude chats in this workspace*

**Transcript Archival**
- Save & retrieve conversations
- Search across chat history
- Synthesis & cross-reference to OV2 wiki

---

**Key limits:** eoxs-db has no CRM/tickets/invoices (moved to eoxs-teams in Aug 2026). Both email/call and wiki data are live or recently ingested. Employee directory writes require explicit confirmation.

What data are you looking to pull?

**User:** can these mcp's give me data on any employee

**Assistant:** Yes — the EOXS Data connectors have a dedicated **employee directory** on eoxs-db that covers any employee in the system.

**Search capabilities:**

- **By name** — fuzzy match (e.g. "Priyanshu" or "Sinha")
- **By role, department, manager, email** — substring or exact match
- **By status** — `active` (default), `inactive`, or `all` (including departed employees)

**Data returned:**
- Full name, official email, role title, department
- Manager, employment type, date of joining
- Change history — every prior update to that record

**Access & limits:**

- Tiered by connector URL — your clearance determines which records are visible
- A "not found" result means the record doesn't exist **or** is above your access level (the system returns the same response either way)
- No way to know which is which without explicit promotion of access tier

**Writing:**

- Create, update, deactivate, reactivate employees
- Requires explicit confirmation first (no speculative writes)
- Changes are logged with full audit trail

**Earlier:** When you first asked about Priyanshu Sinha, a tool call to search the employee directory was declined. That could mean:
1. The tool access was declined by policy
2. The record is tier-restricted above your current clearance
3. The person is not in the employee directory

Would you like me to try searching the employee directory again, or search for Priyanshu Sinha across emails/calls instead?
