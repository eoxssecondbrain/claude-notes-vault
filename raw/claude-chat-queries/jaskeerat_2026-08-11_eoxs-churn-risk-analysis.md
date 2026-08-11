---
thread_name: "eoxs-churn-risk-analysis"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# EOXS Client Churn Risk Assessment

## Executive Summary

**High-Risk Clients (Active monitoring needed):**
1. **PPC Metals** — Turbulent post-launch (Dec 2025–Feb 2026); accounting misconfigurations; performance issues; relationship strain
2. **Discount Pipe & Steel** — 207 open implementation tasks; post-go-live instability; billing disputes; recurring bugs unresolved
3. **Sabre Alloys** — High satisfaction on roadmap expansion, but critical production bugs unresolved for 6+ months

**Medium-Risk Clients:**
4. **Eastern States Steel** — Strategic shifts (Long Products winding down); CFO resistance to multi-year implementation costs; contract may not renew at 3-year term
5. **3GM Steel** — Longest-running client showing fatigue; recurring inventory/data-integrity issues since 2022

**Lower-Risk Clients:**
6. **RW Conklin Steel** — Smooth post-launch; strong executive alignment; too small to generate major issues
7. **Greer/Ohio Strip Steel** — CRM-only deal; stable post-launch; low complexity
8. **Brannon Steel** — New AI-only product; too early to assess

---

## Detailed Client Risk Assessment

### 🔴 HIGH RISK: PPC Metals (Acquired Sept 2025, Went Live Oct 2025)

**Timeline of Dysfunction:**
- **Oct 2025:** Go-live completed
- **Nov–Dec 2025:** Dense backlog of issues emerged simultaneously across accounting, inventory, workflows, email config
- **Dec 2025–Feb 2026:** "Most turbulent post-launch window" — relationship under strain

**Critical Issues:**

| Issue | Impact | Status |
|-------|--------|--------|
| **Bank journal misconfiguration** | Payments routed to legacy account (101401) instead of Truist (111200); P&L confusion for 3+ months | Partially corrected; confusion persisted through Feb 2026 |
| **Accounting/COGS complexity** | Crystal McDaniel (Accounting Manager) repeatedly requesting formatting, account repositioning, clarification | Unresolved as of batch end (June 2026) |
| **Group/check payment reconciliation bug** | Persistent problem preventing accurate payment tracking | Unresolved |
| **Inventory workflow complexity** | Tag-based inventory system required dimension formatting/item ID conventions not standard in EOXS | Backlog ongoing |
| **Performance degradation** | System felt "slower in process" than previous solution; processing slowdown (April–June 2026) | Quick fix for April; structural issue identified; workaround in QA only |
| **Automation failures** | James Baker (Inside Sales) escalated scope confusion around SmartQuote AI; feature gaps vs. prior system | Unresolved |

**Client Sentiment:**
- **Eddie Poindexter** (executive contact): Made clear system still felt "slower" than replaced system — signal of buyer's remorse
- **James Baker:** Escalated concerns about scope confusion and automation gaps
- **Crystal McDaniel:** High-frequency requests for corrections, indicating ongoing operational friction

**Churn Risk: 65%** — Post-launch instability, relationship strain, performance concerns, and comparison to prior system (unfavorably) are classic pre-churn signals. Without rapid stabilization, renewal decision at contract end will be negative.

**Mitigation Needed:**
- Dedicated stability sprint (accounting, inventory, performance)
- Executive check-in with Eddie to address "slower than prior system" perception
- Clear roadmap for SmartQuote AI scope clarification

---

### 🔴 HIGH RISK: Discount Pipe & Steel (Acquired April 2025, Went Live June 2025)

**Scale of Open Work:**
- **207 open implementation tasks** (highest of any client)
- **495 total support tickets** across platform
- **Multiple waves of issues** from July 2025 onward

**Critical Issues Documented:**

| Issue | Frequency | Severity | Status |
|-------|-----------|----------|--------|
| **Packing list confirmation failures** | Recurring throughout post-launch | Critical — blocks order fulfillment | Spans Sabre & DPS; root cause unconfirmed |
| **Stock transfer "done quantity" discrepancies** | Recurring; client own phrasing: "this issue...again" (Aug 2026) | High — inventory accuracy | Resolved same-day but no root-cause note; pattern unclear |
| **Billing disputes** | Bank Reconciliation Module billing dispute (Aug 2026) | Medium — trust erosion | Client disputed whether module was included |
| **Duplicate tag numbers** | Bug: System created duplicate tag IDs | High — inventory corruption | Assigned to Humaira Zainab |
| **Salesperson field changing unexpectedly** | Quote → SO → Invoice workflow bug | Medium | Partially resolved (May 2026) |
| **Receiving/packing error prevention** | Part 1 & Part 2 in development for months | Medium | Still in Requirement/Decision stages as of June 2026 |

**Client Operational Impact:**
- **Zana Williams** (key contact) flagged recurring issues repeatedly, signaling frustration
- **Austin Rayzor** (contract signatory) involved in multiple dispute resolution threads
- **Alt Digital AI consultants** (Tina Valdez, Jamie Vernon) engaged as third-party support, suggesting DPS lacks confidence in EOXS alone

**Post-Launch Stability:**
- First 3 months (July–Sept 2025): 165 tickets, all marked "Paid" (closed), but 94% unassigned — suggests tickets were closed without proper resolution
- Batch 2 (Oct–Dec 2025): Continued pattern; tickets closed but issues resurface
- Batch 3 (Jan–Mar 2026): High volume continues; new patterns emerge (quote status bugs, warehouse location issues)

**Churn Risk: 70%** — The highest number of open tasks, recurring unresolved bugs (especially packing list), billing disputes, and pattern of tickets closed without proper root-cause analysis suggest a client losing confidence. The engagement of third-party consultants indicates they're seeking alternatives.

**Mitigation Needed:**
- **Root-cause analysis on packing list bug** (spans Sabre too; fix benefits both)
- **Task completion audit:** Why are 207 tasks still open? Resource constraint or scope inflation?
- **Billing clarity:** Clarify what's included in base contract vs. add-ons; regain trust
- **Executive reset:** Austin & Zana need a "state of union" call with Raj on Q4 roadmap

---

### 🔴 HIGH RISK: Sabre Alloys (Migrated 2024, Soft Launch April 2024, Live June 2024)

**Paradox:** Highest engagement and expansion ambitions, BUT critical production bugs unresolved for 6+ months.

**Critical Unresolved Issues:**

| Ticket | Issue | Days Idle (as of Aug 2026) | Impact |
|--------|-------|--------------------------|--------|
| **T06021** | Control Tag unit-value revert | **78+ days** (ignoring daily SupportAI escalations) | Data corruption risk; affects processing cost accuracy |
| **T05973** | Processing module issue | **199 days idle** | No human reply of any kind since creation |
| **T06181** | Related to T05973 | **100+ days idle** | No human reply since June 8, 2026 |
| **T07029** | IRIS QA (Claude AI agent) | **88 days idle** | Key expansion feature stalled in review |
| **T05944** | Long-open issue | **200+ days idle** | Complete abandonment signal |

**Processing/Warehouse Production Bugs:**
- **Packing list confirmation failures:** "Cannot confirm packing list" chronic bug — blocks order fulfillment; same bug reported in Sabre and Discount Pipe & Steel (suggests platform-wide defect)
- **Processing-order confirmation/timeout failures:** T07095, T07105, T07110, T07052, T07124, T07176, T07242, T07249, T07253 (cluster of 9+ related tickets)
- **Inch UOM value bug (T05162):** 9+ months unresolved; 78 SupportAI escalations ignored
- **"Control tag already linked to this transfer" error:** Recurring confirmation-error cluster; blocks operations

**Operational Friction:**
- **Excel-export server errors:** Juan Deshon unable to export Income Statement (July 31, 2026); new error hits same day
- **Sandbox access issues:** Juan unable to log into sandbox as of July 31, 2026 — testing/validation blocked
- **Group Payment feature:** Port from PPC Metals (T07155/T06669) suggests feature development driving client frustration

**Client Expansion Ambitions (Positive Signal):**
- **Claude AI agent (IRIS):** Jun 2026, Michael Mercadante pitched ERP-AI for decision support; Raj's reaction: "Gold fucking mine" — expansion opportunity
- **User growth:** 12 → 28 users (post-launch expansion)
- **High engagement:** 1,186 emails, 81 calls, 182 implementation tasks

**The Risk:**
Sabre is EOXS's anchor client and revenue engine, actively expanding. BUT the combination of:
1. **Critical bugs blocking daily operations** (packing list, processing orders, Inch UOM)
2. **Abandoned tickets with 100–200+ days idle time**
3. **SupportAI bot escalations ignored** (78 on T06021 alone)
4. **Sandbox/testing infrastructure issues** (Juan can't access to validate fixes)

…suggests internal EOXS dysfunction, NOT product maturity. If Sabre's trust erodes — especially when they're betting on IRIS AI expansion — churn risk becomes **existential**.

**Churn Risk: 55%** — Paradoxically lower than PPC or DPS because Sabre is actively expanding and deeply integrated. BUT if critical bugs persist through Q4 2026 and AI expansion stalls, this could flip to 80%+ fast.

**Mitigation Needed:**
- **Immediate:** Assign a dedicated senior developer (Dhrup?) to close T06021, T05973, T06181 by Sept 15
- **IRIS Expansion:** Get Claude AI agent to production by Oct 2026; don't let expansion features stall
- **Sandbox Access:** Fix Juan's access immediately; unblock validation workflows
- **Packing List Bug:** This is platform-critical (affects Sabre, DPS, others) — make it P0

---

### 🟡 MEDIUM RISK: Eastern States Steel (Acquired May 2025, Went Live June 2025)

**Strategic Disruption:**
- **Long Products Division winding down by year-end 2025** (announced May 2026 by Ryan Capinski)
- **Implementation cost pushback:** Ryan had to defend multi-year costs to Board; Raj waived cage-workflow fee + partnership discount to retain
- **CFO resistance:** Described costs to implementation as unfavorable compared to alternative (Enmark)

**Contract Structure Weakness:**
- **1-year term** (vs. standard 3-year) — easier exit window
- **"Sales + CRM only"** model — doesn't leverage full ERP platform; lower stickiness
- **Lowest MRR tier** in ICP — economically less valuable

**Positive Signals:**
- **Ryan Capinski transitioning to EOXS referral/sales role** (June 2026) — suggests personal buy-in
- **Active engagement:** Multiple team members (Ryan, Rose Torres, Tom Meyer, Vince Pappas) submitting product requests, accounting reconciliation
- **Steady-state operations:** No critical bugs; post-launch relatively smooth

**The Risk:**
- 1-year contract expires **~June 2026–2027** depending on exact terms
- Strategic shifts (Long Products wind-down) reduce operational value of ERP
- Board-level cost concerns suggest renewal negotiation will be difficult
- Referral potential (Ryan's new role) could be offset by his own potential departure if EOXS doesn't grow

**Churn Risk: 40%** — Medium. Not in crisis, but contract expiration approaching with organizational changes. Renewal depends on referral success and cost-value realignment.

**Mitigation Needed:**
- **Path to 3-year renewal:** Tie Ryan's referral incentives to their renewal
- **Cost-value demo:** Show ROI from Sales+CRM module (pipeline conversion, sales velocity)
- **Referral tracking:** Quantify pipeline from Ryan's efforts; tie to pricing

---

### 🟡 MEDIUM RISK: 3GM Steel (Acquired 2022, Live ~2022–2023)

**Longevity Concern:**
- **Longest-running client** (2022 onward) — but longest-running clients often show fatigue
- **Minimal contact volume** in recent period (12 calls total in profile; most 2022–2024)

**Recurring Issue Pattern:**
- **Coil data-integrity bug:** "Individual coil lot records would zero out all values (weight, footage, cost)" — threading through performance episodes since 2023–2024
- **Performance episode 1 & 2:** Persistent load-time issues on processing screens
- **Server upgrade decision stalled:** Proposed server upgrade (Nov 2024) with three tiers; no selection made before year-end

**Organizational Changes:**
- **Restructuring (Jan 2023):** General Manager Travis Lane not replaced; instead restructured to COO Brittany Meece + CFO Stefan Brown (new structure less familiar with EOXS)
- **2024 onwards:** Minimal escalation contacts; suggests either stable usage or reduced engagement

**Silent Risk:**
- If 3GM is generating <5% of total platform errors but seeing recurring coil-data issues since 2022, either:
  1. EOXS hasn't prioritized the fix (they're a smaller account)
  2. 3GM isn't complaining loudly (quiet exit prep)

**Churn Risk: 35%** — Lower than PPC/DPS, but fatigue + organizational changes + 4 years in place suggest potential multi-year renewal decision at contract reset.

**Mitigation Needed:**
- **Proactive health check:** When was last meaningful executive call? (Likely >6 months)
- **Coil data-integrity fix:** Closes a 4-year-old wound
- **Server upgrade decision:** Move decision forward; costs money but shows investment

---

### 🟢 LOWER RISK: RW Conklin Steel (Acquired Nov 2024, Went Live March 2025)

**Positive Indicators:**
- **Smooth post-launch:** Entered 2026 with positive momentum
- **Daily executive engagement:** Ron J ran daily calls with Pete Conklin post-go-live
- **Smallest account (4 users):** Lower operational friction; easier to manage
- **Full ERP implementation:** Not a limited deal; shows product confidence

**Risk Factors:**
- **Too new to assess long-term fit** (only 5 months live as of Aug 2026)
- **Highly dependent on Ron J:** If Ron becomes unavailable, relationship at risk

**Churn Risk: 15%** — Too early to assess; currently stable. Monitor for any drop-off in engagement post-honeymoon period.

---

### 🟢 LOWER RISK: Greer/Ohio Strip Steel (Acquired July 2024, Live ~2025)

**Positive Indicators:**
- **CRM-primary deal:** Sales & relationship management; lower dependency on full ERP complexity
- **Post-launch stability:** No critical issues documented
- **Discount-aware buyer:** Negotiated 30% discount; price-sensitive but committed

**Churn Risk: 20%** — Stable; price-sensitive but no operational red flags.

---

### ⚪ TOO NEW TO ASSESS: Brannon Steel (Acquired Jan 2026)

- **AI-only product:** MTR (Material Test Report) AI, not traditional ERP
- **Only 6 months in:** Insufficient post-launch data
- **Separate product category:** Pricing/success metrics differ from ERP

**Churn Risk: 25%** — Monitor for adoption metrics; AI-only products have different failure modes (integration complexity, ROI clarity).

---

## Historical Reference: Morgan-Hauser Steel (Churned Feb 2024)

**Why it matters:** EOXS has one confirmed churn case in the vault — Morgan-Hauser Steel, which failed during implementation and churned Feb 2024.

**Failure Pattern:**
- Ron J assigned to work directly with Alicia Núñez on data-entry backlog (Jan 2024)
- Backlog never fully cleared
- Account churned (Feb 2024)

**Lesson:** Data-entry and backlog management are early-warning signals. Discount Pipe (207 open tasks) mirrors this pattern.

---

## Portfolio Risk Summary

| Client | Risk Level | Key Risk | Renewal Timing | Priority Action |
|--------|-----------|----------|-----------------|-----------------|
| **PPC Metals** | 🔴 65% | Post-launch instability, performance, buyer's remorse | Oct 2028 (3-yr est.) | Stability sprint; executive reset |
| **Discount Pipe & Steel** | 🔴 70% | 207 open tasks; recurring bugs; billing disputes; third-party consultants | June 2028 (3-yr) | Root-cause analysis; task audit; billing clarity |
| **Sabre Alloys** | 🔴 55% | Critical bugs idle 6+ months; AI expansion stalled; sandbox access blocked | June 2027 (3-yr) | Bug sprint; IRIS to production; clear roadmap |
| **Eastern States Steel** | 🟡 40% | 1-yr contract; cost concerns; org changes; low stickiness (Sales+CRM only) | ~June 2026–2027 | Referral incentive; cost-value demo; renewal negotiation |
| **3GM Steel** | 🟡 35% | 4-year fatigue; recurring data-integrity issues; minimal recent engagement | ~2026–2027 (est.) | Executive health check; fix coil-data bug |
| **RW Conklin Steel** | 🟢 15% | Too new; Ron J dependency | March 2028 (3-yr) | Continue strong engagement; validate adoption |
| **Greer Steel** | 🟢 20% | Price-sensitive; CRM-only | ~2026–2027 (est.) | Stable; monitor for upsell opportunity |
| **Brannon Steel** | ⚪ 25% | Too new; AI-only product (different metrics) | Jan 2029 (3-yr est.) | Monitor adoption; integration clarity |

---

## Top 3 Retention Priorities (Next 90 Days)

### 1. PPC Metals Stability Sprint
**Deliverable:** Clear bank journal routing, resolve accounting COGS discrepancy, performance stabilization (background-processing live)
**Owner:** Dhrup Kumar Singh (Lead Dev) + Ron J (Account)
**Timeline:** Sept 15, 2026

### 2. Discount Pipe & Steel Task Audit
**Deliverable:** Closure plan for 207 open tasks; root-cause analysis on packing list bug (platform-wide issue)
**Owner:** Project Manager + Hashir Saleem (Lead Dev)
**Timeline:** Sept 30, 2026

### 3. Sabre Alloys Bug Sprint + IRIS Launch
**Deliverable:** T06021, T05973, T06181 closed; IRIS Claude agent in production; Juan's sandbox access restored
**Owner:** Dhrup Kumar Singh (Lead Dev) + Sheenam Rawat (Product)
**Timeline:** Oct 31, 2026

---

## Conclusion

**Portfolio Retention Risk: ~45% Average**

Two clients (PPC, DPS) are in active danger and need immediate intervention. Sabre, while expanding, has underlying trust issues that could accelerate if not addressed. Eastern States and 3GM will face renewal decisions within 12 months.

**Upside:** Sabre's AI expansion (IRIS) and Ryan Capinski's referral role suggest growth potential that could offset churn risk if execution improves.

**Downside:** If PPC or DPS churn (especially Discount Pipe at 207 open tasks), churn becomes a public signal and other clients may reconsider.

**Recommendation:** Treat PPC + DPS as emergency accounts through Q4 2026. Success stabilizes the portfolio; failure accelerates other renewals.
