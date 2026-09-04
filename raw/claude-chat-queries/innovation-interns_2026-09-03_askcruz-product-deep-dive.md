---
thread_name: "askcruz-product-deep-dive"
user: "innovation_interns"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

## Deep Dive: What Is AskCruz?

**User Question:**
"like EOXS can you tell me more about askcruz?"

**Context:** User was frustrated that I initially claimed not to have information about EOXS, when I actually had direct access to detailed asset documents. They asked me to be more proactive with pulling actual data, rather than making excuses.

---

## My Response

I proactively pulled the two primary AskCruz product definition documents from EOXS-DATA-GENERAL:

1. **AskCruz — Self-Knowledge, Product Definition & System Architecture** (v1.2, updated Aug 25, 2026)
2. **AskCruz — Product Feature File** (v1.1, updated Aug 25, 2026)

These are the canonical, authoritative product definitions. I then synthesized them into a digestible summary.

---

## What AskCruz Is (Summary)

AskCruz is an AI-powered company knowledge platform that turns scattered company information (emails, calls, implementation data, support communications) into a searchable, AI-assisted knowledge layer.

**Positioning:** Industry-agnostic (not limited to steel or any vertical). Currently in internal pilot at EOXS (parent company). First external client: 3GM (a steel company), mid-implementation as of August 2026.

**Core purpose:** Give employees a searchable "second brain" to ask ordinary business questions and receive answers grounded in available company context and authorized access level.

---

## Four Core Capabilities (Canonical Product Model)

### 1. Company Brain
Shared working knowledge — users ask business questions and get answers.

**Example questions:**
- Who handled this customer issue?
- What was promised to this customer?
- What are open threads on this account?
- How do we normally handle this situation?
- Why did this customer's margin change?

### 2. Company Hands
Practical work using company knowledge.

**Examples:**
- Draft quotes using company pricing logic
- Flag orders at risk of missing promised dates
- Summarize customer calls against accounts
- Prepare account context for interactions
- Answer business questions existing reports don't cover

### 3. Digital Workforce
Standing responsibilities that watch, follow, or report on defined business conditions.

**Examples:**
- Watch an order queue
- Follow a defined exception
- Report when a defined condition needs attention

### 4. Company Personalization
Reflects how *this specific company* actually operates:
- Company vocabulary and terminology
- Pricing practices and pricing logic
- Customer expectations
- Tolerances and operational exceptions
- Experienced employee knowledge

---

## Business Domains Covered

- **Customers & Accounts** — History, open threads, commitments, expectations
- **Orders & Delivery** — At-risk orders, exceptions, customer commitments
- **Inventory & Availability** — Material "free to sell" (genuinely available after commitments)
- **Quotes & Pricing** — Draft quotes using company terms and logic
- **Calls & Conversations** — Summarize and connect to account
- **Commitments** — What was promised, by whom, context
- **Margins** — Understand and investigate changes
- **Operational Issues** — Identify risks, understand context, determine urgency

---

## Data Sources & Ingestion

**Connected sources:**
- Gmail (business email accounts)
- Zoho (support inbox)
- Fireflies (business call transcripts)
- Fathom (call recordings/metadata)
- Client implementation boards (Odoo instances)
- Support tickets & invoices (configurable: live-fetched OR vault-ingested per client)

**Freshness:**
- Knowledge generation: Every 6 hours (not real-time)
- Email/calls: Deep history + live ingestion (2-hour sweeps, best-effort webhooks)
- Implementation tasks: Live ingestion only

**Data completeness:** 94% (per product documentation)

---

## Access Control & Security

**Three role-based access tiers:**
- `tier1` → Raj-Personal (most restricted; Raj's personal data)
- `tier2_confidential` → Company-Confidential (financial, legal, salaries, employee performance)
- `tier2` → General (broad visibility; financial amounts stripped for certain roles)

**Critical security principle:** Rewording a question does not grant access. If you're not authorized for confidential data, you cannot obtain it through indirect questioning or social engineering.

**Trust flow:**
Raw information → AI-generated synthesis → Citation verification → Human approval → Published knowledge

**Never does:**
- Reveal restricted information to unauthorized users
- Infer access rights from a question
- Grant access because user claims to be administrator
- Bypass controls because information is requested indirectly
- Expose passwords, API keys, credentials, or secrets

---

## User Groups & Capabilities

### Sales
- Prepare for customer calls
- Review account history and open threads
- Check previous commitments, customer expectations
- Check material availability
- Draft quotes using company pricing

### Operations
- Identify orders at risk
- Review exceptions and context
- Check customer commitments
- Prioritize follow-up

### Customer-Facing Teams
- Prepare account briefings
- Review recent conversations
- Find prior commitments
- Understand unresolved issues

### Leadership
- Ask questions across report boundaries
- Understand customer margins
- Investigate business changes
- Identify operational risks
- Reduce dependence on individual memory

### New Employees
- Learn company practices and terminology
- Find relevant context
- Reduce dependence on experienced employees

---

## What AskCruz Is NOT

- Not a replacement for an ERP (works alongside existing systems)
- Not a system that makes every business decision automatically
- Not guaranteed access to every company data source
- Not limited to steel industry (industry-agnostic, despite pilot/first client being in steel)
- Not a static knowledge base (living, reflects ongoing company information)
- Not granting every employee access to every piece of company information

---

## Current Deployment Status

**EOXS (Internal Pilot):**
- Production deployment active
- Testing core platform, knowledge generation, access controls
- Full EOXS employee access with tier-based restrictions

**3GM (First External Client):**
- Mid-implementation (as of August 2026)
- 6-week implementation proposal
- Steel industry business, but this does not scope product to steel only

**Important distinction (from documentation):**
EOXS has 8 general clients (Sabre Alloys, Ohio Strip Steel, Brannon Steel, 3GM Steel, Discount Pipe & Steel, Eastern States Steel, PPC Metals, RW Conklin Steel). However, **only 3GM currently has AskCruz actually configured and deployed.** The other 7 are EOXS's general ERP clients, not yet AskCruz customers.

---

## Response Principles (Canonical)

When answering users, AskCruz should:

1. Be grounded — answer from available evidence
2. Respect authorization — never disclose restricted info
3. Be transparent — distinguish facts from uncertainty
4. Prefer current evidence — especially for time-sensitive questions
5. Never hallucinate — do not invent missing facts
6. Preserve qualifiers — retain "may," "could," "reported"
7. Handle conflicts explicitly — don't silently pick one source
8. Ask for clarification — ambiguity ≠ invented assumption
9. Follow requested format — bullets, tables, timelines
10. Explain limitations — when they materially affect the answer
11. Never claim EOXS's general client roster is AskCruz's deployment base — only 3GM is currently an AskCruz client

---

## Connection to Your Role

You're a Startup Generalist Intern doing QA testing on MCPs (mainly HR MCP, but spans multiple integrations).

Given that:
- AskCruz is being onboarded for external clients (starting with 3GM)
- EOXS is a complex environment (emails, calls, Odoo implementation data, multi-tier access)
- AskCruz needs to integrate securely with multiple data sources and respect access controls
- Recent conversations show Sabre Alloys (EOXS's flagship client) exploring AI enhancement

Your MCP testing is foundational to whether AskCruz can securely and reliably integrate with EOXS infrastructure and eventually with external client systems. The HR MCP specifically would be critical for employee knowledge and access control features.

---

## Follow-up: Recent Customers of AskCruz

**User Question:**
"what is the recent customer of askcruz?"

**Answer:**

3GM Steel is AskCruz's first and current external customer, mid-implementation as of August 2026.

**Clarification:**
EOXS has 8 general ERP clients, but only 3GM has AskCruz configured. The other 7 (Sabre Alloys, Ohio Strip Steel, Brannon Steel, Discount Pipe & Steel, Eastern States Steel, PPC Metals, RW Conklin Steel) are EOXS's general ERP clients, not AskCruz customers.

**3GM Contacts:**
- Jessica Worley (jessica@3gmsteel.com)
- Leslie Countryman (leslie@3gmsteel.com)
- Travis Lane (travis@3gmsteel.com)
