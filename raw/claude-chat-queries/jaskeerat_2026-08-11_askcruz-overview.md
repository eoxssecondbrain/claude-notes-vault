---
thread_name: "askcruz-overview"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# AskCruz Overview

## User Request
User asked for:
- How AskCruz works
- Business problems it solves
- Key benefits

## Response

### **How AskCruz Works**

**AskCruz** (also called "Cruz") is EOXS's Claude-based AI agent product that gives steel and metals distributors a conversational interface to query and analyze their ERP data in real time.

#### **Technical Architecture**

Three-layer product design (currently evaluating layer implementations):

1. **Layer 1: ERP-Only Chatbot** (deployed, no additional cost)
   - Pulls live data from the EOXS ERP system
   - Allows natural-language questions about inventory, sales orders, customers, pricing, et cetera
   - Answers without needing email or document context
   - Built on Claude API integration

2. **Layer 2: "Second Brain" (under evaluation)**
   - Expands context beyond ERP data to include company email
   - Allows the agent to answer questions about customer discussions, deal status, strategic context
   - Significantly increases Claude API token usage and cost

3. **Layer 3: Full Collaborative Knowledge Base** (proposed open-source alternative being evaluated)
   - Per-user access controls with secret tokens and tiered file-hash permissions
   - Admin portal with full cross-user thread visibility
   - Custom tool editor for job-specific agents
   - Shared/collaborative chat threads
   - Built-in calendar integrations and automations
   - PDF export capabilities

#### **Current Cost Pressure**

- Claude API integration currently costs ~[restricted] per month
- Single 21,000-token conversation session hit [restricted] cost
- Problem: integration has no native thread context — every prompt resends full conversation history, inflating token counts
- Mitigation attempted: summary-based approach proposed by Ayan, but still costs more than ideal
- Team evaluating whether to move to open-source AI UI to manage costs

---

### **Business Problems It Solves**

AskCruz addresses **two major pain points** for steel and metals distributors:

1. **Decision Support Without Manual Report Writing**
   - Eliminates need for analysts to pull custom reports for operational questions
   - Enables executives to ask ad-hoc questions about inventory levels, customer history, pricing trends, etc., without IT/analyst delays
   - "Configured, trained, or taught to answer real operating questions" — not a generic chatbot, but decision support built on actual company data

2. **Cross-Functional Knowledge Access**
   - Layers 2–3 (once deployed) bridge the gap between ERP data and email/document context
   - Allows sales, operations, finance to understand deal context (customer emails, strategic conversations) alongside transactional data
   - Reduces institutional knowledge silos where information lives in email or tribal knowledge

---

### **Key Benefits**

#### **For Clients (Steel Distributors)**

1. **Speed of Decision-Making**
   - Real-time answers to operational questions (e.g., "Which customers bought coil over 50 tons in Q3?" or "What was our margin on this order?")
   - No wait for analysts or report-generation cycles

2. **Reduced Manual Work**
   - Less time spent pulling reports, running VLookups, or hunting through email for deal context
   - Frees operations/finance teams for higher-value work

3. **Competitive Advantage in Pricing & Sales**
   - SmartQuote AI (companion product) can generate competitive quotes in seconds using the agent's data access
   - Sales teams have instant context on customer history, prior pricing, inventory availability

#### **For EOXS (as a Product & Revenue Driver)**

1. **Product Differentiation**
   - Positions EOXS as AI-native, not just an ERP vendor
   - AI Workers suite is marketed as ERP-agnostic — compatible with Invera, Stratix, SAP, Epicor, other platforms
   - Means EOXS can *win new customers who are NOT buying the ERP* (Brannon Steel, for example, bought MTR AI standalone, not full EOXS ERP)

2. **Strong Product-Market Fit Signal**
   - Sabre Alloys (existing customer) emailed directly: "We want to move quickly on getting this configured" — Rajat's internal reaction: "Gold fucking mine"
   - Indicates expansion revenue opportunity (upsell to existing clients)

3. **Viral Sales Potential**
   - Ryan Capinski (Eastern States Steel, EOXS customer for 1 year) referred Collier Metals (Atlanta, family-owned, expected to triple revenue this year) after being impressed by AskCruz capabilities
   - Joe Brom (Ohio Strip Steel EVP) had an "Ask Cruz" intro call with Rajat on Aug 10, 2026 — product awareness spreading

4. **Subscription Revenue Model**
   - AI Workers are positioned as per-seat or per-agent, separate from ERP modules
   - Opens recurring revenue stream beyond core ERP implementation

---

### **Current Status (As of August 2026)**

- **Sabre Alloys**: June 2026 request; internal cost evaluation underway; Rajat considering whether to keep Claude API or move to open-source UI
- **Ohio Strip Steel**: Intro demo call completed Aug 10, 2026 (Rajat screen-shared Cruz walkthrough with Joe Brom)
- **Collier Metals**: Prospect referral from Eastern States Steel; "prime candidate" for EOXS/IRIS per Ryan Capinski
- **3GM Steel**: Three-layer design documented in a call log, suggesting internal brainstorming on feature scope
- **Agent Naming**: Completed naming exercise in May 2026 (Sheenam Rawat led; chose "Cruz" from options like Planets, Gemstones, Animals themes)
- **Development Team**: Multiple engineers assigned to Claude API training (Syed Gufran Hussain, Ankit Pachauri, Jaskeerat Singh, others)

---

## Sources

- **Sabre Alloys — Claude AI Agent Request & Internal Cost Evaluation (Jun–Aug 2026)** — Sabre's request (June 16), internal cost/architecture analysis (July 31)
- **Ohio Strip Steel — "Ask Cruz" AI-Agent Intro Call (Aug 10, 2026)** — Rajat demo to Joe Brom, confirms product name and scope
- **Ryan Capinski → Tripp Collier (Collier Metals) Referral Call (Jul–Aug 2026)** — Product expansion/viral sales signal
- **3GM Steel — Fireflies Call Log** — Three-layer product architecture details
- **EOXS Company Overview** — AI Workers suite positioning (12+ standalone agents, ERP-agnostic)
- **Internal Email Archive — Product and Operations (batch 18, 2026-04-30 to 2026-06-26)** — Agent naming exercise, Claude API training assignments
