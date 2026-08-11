---
thread_name: "prospect-pipeline-summary"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# Prospect Pipeline Analysis & Re-engagement Strategy — Complete

## Part 1: Current Pipeline Summary

[Earlier sections included...]

---

## Part 4: What is IRIS?

### Quick Definition
**IRIS is EOXS's AI-powered natural-language business intelligence (BI) layer.** It allows users to ask questions in plain English and automatically generates cross-module reports from live data.

**Example:** A commercial user asks "Show me which customers have ordered less than expected this quarter" → IRIS queries the Sales, CRM, Inventory, and Accounting modules simultaneously and generates a ranked report with customer names, order history, and risk flags.

---

### IRIS in the Product Architecture

EOXS sells **two distinct product tracks**:

1. **ERP Modules** (5 core: Books, CRM, People, Shop, Report Builder)
2. **AI Workers Suite** (15+ standalone AI co-pilots, including IRIS)

**Key distinction:** IRIS is NOT a replacement for the CRM module. Rather:
- The **CRM module** stores prospect/customer records, manages pipeline stages, and tracks activities
- **IRIS** is a reporting/intelligence layer that sits *on top* of all modules (CRM, Sales, Inventory, Accounting) to surface insights and patterns users couldn't easily find manually

---

### What IRIS Does (From Vault Records)

**Core Capability:** Natural-language BI across all EOXS modules
- Users type a question in plain English
- IRIS parses the question, identifies relevant data sources, and generates a live report
- No SQL, no manual report-building — conversational interface

**Specific Applications Documented:**

1. **Customer At-Risk Detection** — IRIS identifies which customers are ordering less frequently or smaller volumes than historical patterns (RevTrack AI monitors continuously; IRIS surfaces the report)

2. **Upsell Opportunity Flagging** — Analyzes customer purchasing patterns to recommend additional products/services

3. **Financial Reconciliation** — IRIS was used in June 2026 to reconcile Sabre Alloys' balance sheet across the Accounting module by cross-checking system data with actual transactions

4. **Stuck Order Diagnosis** — Sabre Alloys' team used IRIS to identify 519 POs stuck in "Waiting Bill" status (e.g., 339 tied to a specific vendor "Drop")

5. **Days-Since-Last-Contact Tracking** — Works with CRM's "Days Feature" to auto-flag neglected prospects (45 days) and existing customers (180 days)

---

### IRIS vs. the CRM Module: Why Both Are Needed

| Aspect | CRM Module | IRIS |
|--------|-----------|------|
| **Purpose** | Store records, manage pipeline, track activities | Answer questions, surface insights from stored data |
| **Interface** | Forms, Kanban board, activity log | Natural-language chat/query |
| **Use Case** | "Add this prospect to pipeline Stage 2" | "Show me which Stage 2 prospects haven't responded in 30+ days" |
| **Data Scope** | Focused on CRM data | Cross-module (CRM + Sales + Inventory + Accounting + Finance) |

**Example scenario:**
- Sales rep adds prospect to CRM, fills in contact info, logs a call (CRM module)
- Sales manager asks IRIS: "Which prospects did we call in June but haven't qualified yet?" (IRIS layer)
- IRIS queries CRM activity logs + Sales module + qualification data → generates ranked list

---

### Why IRIS Mattered for Ace Steel Re-engagement

Ace's **2024 gap:** They evaluated EOXS ERP (for transactions/operations) but needed **CRM + commercial intelligence** to identify prospects, manage the pre-sales pipeline, and surface account insights.

EOXS in 2024: Had CRM module, but **no IRIS** (no BI layer to surface patterns/risks).

**IRIS launch (2024–2026 timeline, active as of June 2026):**
- Adds the **"structured intelligence dataset of the steel industry"** Raj mentioned to Bruce
- Companies can now search EOXS's industry database (companies, buyers, contacts, market data, AI profiles) via natural language
- Queries like "Show me all steel distributors in Texas with 50+ employees that purchased coils last year" → instant answers

**Why this reopens Ace:** Ace can now use EOXS CRM + IRIS to manage pre-transaction prospecting/intelligence *alongside* Invera's transaction/operations strength — complementary, not competitive.

---

### Current IRIS Status (as of Aug 2026)

- **Active product:** QA in progress (June 2026 Balance Sheet reconciliation documented)
- **Re-engagement outreach:** Bruce Margolin (Ace Steel) received IRIS demo videos June 8, 2026
- **Pricing:** Appears to have a "IRIS Pro" tier mentioned in product pricing discussions (exact cost [restricted])
- **Rollout:** Limited to existing clients + strategic re-engagements (Ace, Sabre Alloys testing)
- **Deployment status:** In staging/testing phase; not yet fully production-released across all clients

---

### Sources

- **EOXS Company Overview:** "Suite of five core ERP modules (Books, CRM, People, Shop, Report Builder) and a separate AI Co-Pilot suite of 12+ standalone AI Workers"
- **EOXS ERP Product Features Overview:** "IRIS provides natural-language business intelligence across all modules — users type a question and IRIS generates the report"
- **IRIS QA — Accounting Module Balance Sheet Reconciliation (Jun 2026):** Evidence of IRIS being used in QA/testing for financial reconciliation (Chandvi Gupta, June 4, 2026)
- **Eastern States Steel — Post-Launch Operations:** "IRIS product is active in this period; US Steel demo connected to live database showing IRIS expansion"
- **Sabre Alloys — Support Tickets:** IRIS used to identify 519 stuck POs in "Waiting Bill" status; formal closure July 6, 2026
- **June 8, 2026 Email to Bruce Margolin:** Raj pitches IRIS as "structured intelligence dataset of the steel industry" that solves pre-transaction prospecting gap

---

## Summary: IRIS in Context of Ace Steel Prospect Re-engagement

**IRIS is the product innovation that makes Ace a viable prospect again.**

- **2024 Problem:** EOXS had ERP (transactions) but no BI/intelligence layer → Ace picked Invera
- **2026 Solution:** IRIS adds the commercial intelligence + CRM pre-transaction capability → Ace can now use both
- **Pitch to Bruce:** "Invera handles post-order operations. IRIS handles pre-order intelligence and prospecting. Together, your commercial team gets a 360° view."

**Next Step:** On your July call with Bruce, ask if Ace's commercial teams are still looking for that pre-transaction intelligence capability they wanted in 2024. If yes, IRIS is the answer. If no (they solved it another way), pivot to understanding what has changed at Ace in 2 years.
