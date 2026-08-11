---
thread_name: "eoxs-revenue-analysis"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# EOXS Revenue & Client Distribution Analysis

## Question
What is EOXS's current revenue, and how is it distributed across the 8 clients?

## Findings

### Limitation
**Most specific pricing and contract values in the vault are [restricted] and not accessible.** This is a deliberate information-governance choice. The analysis below is built from what can be extracted from unredacted sections.

### Revenue Model
EOXS operates on a **per-seat monthly SaaS subscription model** with:
- Implementation fees (one-time)
- Monthly recurring revenue (MRR) based on user count and selected modules
- Standard 3-year contracts (with some exceptions)
- 4% max annual renewal increase cap (per contract language)

### Known Clients & Status (8 total)

| Client | Acquisition | Status | User Count | Modules | Notes |
|--------|-------------|--------|------------|---------|-------|
| **Sabre Alloys** | Migrated from Steel Plus | Live | Grew from 12 → 28 | Full (Inventory, Processing, Accounting, CRM, Sales) | First/largest client; highest email volume (1,186 threads) |
| **3GM Steel** | Early adopter | Live | Not disclosed | Full ERP | Longest-running client (implementation 2022); 827 emails |
| **Discount Pipe & Steel** | Won April 2025 | Live (June 2025) | 6-7 documented | Full ERP | 207 implementation tasks; highest complexity in post-launch |
| **PPC Metals** | Won Sept 2025 | Live (Oct 2025) | Not disclosed | Full ERP | Go-live intensive (Oct 2025); 29 calls in launch period |
| **Eastern States Steel** | Won May 2025 | Live (June 2025) | 6-7 users | **Sales + CRM only** (no Inventory/Processing/Accounting) | Lightest deal; 1-year contract (vs. standard 3-year); **lowest MRR** |
| **Ohio Strip Steel** (formerly Greer) | Won July 2024 | Live | 8-12 users (with discounts) | CRM (primary) + others | Sales-led champion; CRM-only deal showing modularity |
| **RW Conklin Steel** | Won Nov 2024 | Live (March 2025) | 4 users | Full ERP | Smaller deal (~[restricted]); daily support model |
| **Brannon Steel** | Won Jan 2026 | Active | Not disclosed | **MTR AI only** (NOT full ERP) | Newest; AI-only product, not traditional ERP |

### Revenue Distribution (Observed Patterns)

**Pricing Tiers (all [restricted], but relative hierarchy visible):**
- **Smallest:** Eastern States Steel (1-year, sales-only) — **lowest MRR**
- **Small:** RW Conklin Steel (4 users) 
- **Mid-Market:** 3GM Steel, Discount Pipe & Steel, PPC Metals (6-8+ users, full modules)
- **Largest:** Sabre Alloys (28 users, full modules, custom features, AI agent expansion)

### Key Insight: Sabre Alloys as Revenue Anchor
- **Grew from 12 to 28 users** — internal expansion post-launch
- **Highest activity:** 1,186 emails, 81 calls, 182 implementation tasks
- **AI product expansion:** Jun 2026 requested Claude-powered ERP agent (generating ~[restricted] monthly in API costs alone; decision pending between Claude vs. open-source)
- **Deep customization:** Control tags, processing module overhauls, landed cost, inventory aging — continuous high-touch development

### Billing & Collections Issues Noted
- **March 2026 overbilling error at PPC Metals:** Invoice INV/2026/0127 billed [restricted] instead of correct [restricted] (corrected by June)
- **User license adjustments:** [restricted] credit issued to Discount Pipe & Steel (June 2026) for archived user
- **License model friction:** Users must be archived to stop billing — operational burden on clients

### Contract Structure
- **Standard:** 3-year, 4% max annual increase, full ERP modules (~[restricted] per user/month range, estimated from peer SaaS norms)
- **Exceptions:**
  - Eastern States: 1-year term (lighter deal negotiation)
  - Brannon: AI-only, not ERP (different pricing tier entirely)
  - Discount Pipe: 25% sign-by-deadline discount applied

### Total Addressable Market (per ICP)
- **Target:** Steel distributors & service centers, 10–200 employees, North America
- **Current penetration:** 8 live clients across small-to-mid-market
- **Expansion signals:** Ryan Capinski (Eastern States President) transitioning into EOXS referral/sales role (June 2026 onward)

---

## What's Missing
1. **Total ARR / MRR:** Not calculable from vault without unredacted contract values
2. **Per-client revenue breakdown:** All monetary figures are [restricted]
3. **Customer acquisition cost (CAC) and lifetime value (LTV):** Not available
4. **Churn/renewal history:** No explicit renewal or cancellation data visible
5. **Implementation services revenue:** Implementation fees documented as [restricted]
6. **AI Worker / IRIS premium pricing:** Strategy exists but pricing tier unclear

---

## Recommendations for Leadership
1. **Request CFO summary:** Current ARR, MRR, and per-client contribution needed for board/investor reporting
2. **Monitor Sabre Alloys AI expansion:** The Claude-based agent is a key upsell opportunity; cost/benefit decision imminent
3. **Watch Discount Pipe & Steel post-launch stability:** Highest number of open tasks (207); billing disputes noted; operational risk
4. **Leverage Eastern States referral potential:** Ryan Capinski is actively exploring referral opportunities (mentioned June 2026); track pipeline impact
5. **Clarify Brannon Steel strategy:** AI-only deal represents new product category; pricing and expansion roadmap unclear

---

## Sources
- Client profiles (get_client_profile calls)
- Ideal Customer Profile wiki page
- Eastern States Steel — Sales & Proposal (contract terms, user counts)
- Sabre Alloys — Claude AI Agent Request (June–Aug 2026)
- Internal email archives (invoice references, billing disputes)
- Call transcripts (implementation intensity, client feedback)
