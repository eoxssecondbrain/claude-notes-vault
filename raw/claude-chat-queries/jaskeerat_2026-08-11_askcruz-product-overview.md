---
thread_name: "askcruz-product-overview"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# Ask Cruz Product Overview

## Question
What is Ask Cruz, what are the core features, and who is the target audience?

## Answer

**Ask Cruz** (also called "Cruz") is EOXS's **Claude-based AI agent product** designed to be a centralized company intelligence layer for ERP-connected organizations. It first appeared in customer conversations around June–August 2026.

### Core Features

Ask Cruz is positioned as a **tiered product with three layers**:

**Layer 1: ERP-Only Chatbot** (Free/no incremental cost)
- Direct access to live ERP data, no need to extract reports manually
- Responds to natural-language queries about company data: revenue, margins, KPIs, inventory, accounts receivable aging, dormant accounts, etc.
- Example: "Show me revenue, gross profit, and margin percentage for this month, quarter, and year-to-date"
- Real-time data pull (no batching delay); takes 30–40 seconds per query
- Accessible via chat interface (appears to be Claude-based)

**Layer 2: Company "Second Brain"** (Requires 2–3 weeks implementation)
- Integrates ERP data with email (Outlook) data across the entire organization
- Each user gets an AI account with role-based access control (e.g., salespeople cannot see other salespeople's data unless the CEO grants it)
- Surfaces relationship history, deal history, customer intelligence
- Enables personalized insights: each salesperson's own dormant accounts, revenue, and performance against targets
- Saves and learns from all interactions; every thread persists in the database
- Machine-learning component: feeds back context corrections so "it understands" future queries better
- Automated reporting: can schedule periodic emails (e.g., daily/weekly sales summaries to each rep)

**Layer 3: Advanced Automations** (Deployment-dependent)
- Proactive role-based alerts (e.g., "Your sales team is having trouble finding new prospects; here are the three pain points they've surfaced")
- Role-specific AI agents (e.g., an "AI Sales Director" that monitors all opportunities daily to ensure nothing falls through the cracks)
- Example pricing mentioned: replaced a $180k/year sales director hire with a $40k/year AI agent

### Key Differentiators vs. Generic Claude
- **Persistent thread history**: Every conversation is saved in a database, allowing a CEO to ask "What has my sales team been talking about over the last three months?" and get a synthesis
- **Real-time company data context**: Claude doesn't know your live ERP data; Ask Cruz feeds it continuously
- **Multi-user coordination**: 15+ employees can share one company AI while maintaining access controls, vs. everyone using separate ChatGPT accounts in silos
- **Knowledge preservation**: When an employee leaves, the new hire can be given the account and asked to create a 30-day onboarding plan based on prior conversations
- **Secure**: Data is not sent to OpenAI; only structured query results are fed to the LLM

### Target Audience

Positioned for **mid-market manufacturing and distribution companies** (specifically steel/metals sector visible in demos):
- Companies with 15–50+ employee sales/operations teams using shared ERP data
- Founders and senior leaders overwhelmed by data fragmentation and manual reporting
- Organizations where **opportunities are falling through the cracks** due to volume and coordination gaps
- Companies with **multiple users already using ChatGPT individually** for work, looking to centralize and govern it

Early pilots/proposed customers (as of Aug 2026):
- **Sabre Alloys** — requested "decision support built on their own data" (not a simple report writer), described by Rajat as "Gold fucking mine" (strong product-market fit signal)
- **3GM Steel** — multi-layer proposal under discussion; trial period offered
- **Ohio Strip Steel** — intro call held Aug 10, 2026
- **A Houston trading company** — already deployed an "AI Sales Director" variant ($40k/year contract)

### Pricing Model (Observed)
- **Layer 1 (ERP chatbot)**: Free or minimal cost (live data pull has no incremental AI spend)
- **Layer 2 (Second Brain with email integration)**: Custom implementation pricing; ~2–3 weeks delivery
- **Layer 3 (AI agents/automations)**: $40k–$180k replacement scenarios mentioned, but pricing not standardized

### Internal Status (as of Aug 2026)
- Built and actively demoing by Rajat Jain
- Claude API cost concerns were flagged internally (tokenization overhead; ~[restricted] for a single 21k-token session); team was evaluating open-source alternatives but continued with Claude
- Marketed as addressing a core pain point: "data sits in silos. Everyone has their own ChatGPT accounts. Nobody knows what anyone else is using it for."
