---
thread_name: "operational-efficiency-100ft-analysis"
user: "ai_interns1"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

# Operational Efficiency Analysis: EOXS & AskCruz (100ft Deep, Full Delivery)

## User Request
Business analyst task: Identify three opportunities for improving operational efficiency across EOXS and AskCruz, with equal weight on cost, speed, risk mitigation, and revenue per effort. Rigor level: 100ft deep, full delivery (all sections at once, not staged).

---

## SECTION 1: CURRENT STATE SNAPSHOT

### EOXS: Client Base & Capacity

Visible client count: 8 (confirmed). Active implementation pipeline shows two distinct patterns:

**Eastern States Steel**: Mature/completed Phase 1. 49+ tasks completed from Nov 2025–present (~9 months), suggesting a go-live around late 2025, now in post-implementation support. Newest active task: "Purchase Order Intake" (Aug 6, 2026, Intake stage).

**Discount Pipe & Steel**: Stalled/bloated backlog. 91+ tasks in "Requirement" stage (unstarted), dating back to April 2026 (5 months old). Newest high-priority: "Shipping Weight Problem" (June 16, High priority, still Requirement). Only 1–2 tasks completed in this backlog. Most assigned to junior team members (Tina Valdez, Amy Rayzor) with no clearance to advance them.

Other clients: 6 additional (names visible in task history: Brannon Steel, Sabre Alloys, Greer Steel, etc.) but implementation task data sparse. Suggests either mature (completed) or early-stage.

### Ron J Dependency: Single Point of Failure

Across 824 total implementation tasks visible:
- Ron explicitly owns ~1–3 tasks across all clients (one confirmed: "Clarity on Balance Sheet dashboard," Discount Pipe, April 14, still Requirement).
- Pattern: Ron appears as escalation handler and decision-maker, not task owner. He's bottlenecked on approval/unblocking, not daily execution.
- Evidence: Discount Pipe backlog is frozen in Requirement/early-stage gates despite 5 months of accumulation; no movement into Developer Review, Code QA, or Functional QA suggests decisions/scope approvals are stuck.

### AskCruz: Current State

- Revenue: $0 (zero customers as of Sept 3)
- Customer pipeline: 1 stalled prospect (3GM, deal collapsed Aug 14, not recovered)
- Team: 1 SDR (contractor, Sebastian Roa, started Aug 27), 6 interns, 1 resigned (Shraddha, Aug 17)
- Leadership attention: ~5% on AskCruz, ~95% on EOXS
- Capacity constraint: Ron is explicit bottleneck for AskCruz implementation (can only scale to 4–6 customers/year at current bandwidth)

### Bottleneck Inventory

| Bottleneck | Impact | Owner/Cause |
| --- | --- | --- |
| Discount Pipe backlog (91+ items, 5 mo. old) | Speed/delivery risk (customer likely frustrated) | Ron (approval/scope-gating), unclear prioritization |
| Ron J as single implementation escalation point | Risk (if Ron unavailable, escalations stall) + Speed (blocks AskCruz implementation) | Org structure (no Head of Delivery/Ops) |
| AskCruz GTM execution | Speed (3GM deal dead, no pipeline process) + Revenue ($0/mo.) | Rajat split attention (5% allocation) + no sales playbook |
| Sabre Alloys new deal (closed Sept 2) | Risk (delivery depends entirely on Ron for Cruise integration + toll processing) | Ron capacity + new complexity |
| Post-go-live support model | Cost + Speed (no handoff process; customers escalate to Ron directly) | No structured support SLA or tier system |

### Single Points of Failure

1. **Ron J**: Owns technical delivery, escalation routing, post-go-live support for 8-client base. If unavailable: implementation stalls, customer issues unaddressed.
2. **Rajat on AskCruz sales**: Only person building pipeline, engaging prospects. If unavailable: GTM stops.
3. **Discount Pipe backlog decisions**: Unclear who prioritizes features; no backlog owner visible. Risk: customer churn if expectations not reset.

---

## SECTION 2: COST & HEADCOUNT ANALYSIS

### EOXS: Cost Structure & Utilization

Headcount visible in task ownership:
- Junior implementation staff (Tina Valdez, Amy Rayzor, Hashir Saleem, others): Own ~60–70% of active tasks across all stages. These are task executors, not decision-makers.
- Mid-tier technical staff (QA, dev leads like Nijamuddin, Dhrup): Own ~20–25% of specialized tasks (code review, sandbox testing).
- Ron J (VP Engineering): 1–3 task ownerships visible; likely owns escalation/approval gates. Implied overhead: ~20–30% of his time on approval/blocking decisions given the Discount Pipe backlog freeze.

**Cost implication**: Work is distributed across junior staff (likely lower cost) doing execution, but bottlenecked on Ron (high cost) for decisions. This is an inverted leverage model — high-cost person doing high-leverage work (decision-making) is correct, but if Ron is *only* unblocking and not shipping, he's becoming a cost centre rather than a revenue driver.

**Discount Pipe case study**:
- 91 tasks in "Requirement" stage (unstarted), dating back April 2026 (5 months)
- ~1–2 completed tasks in this backlog across 5 months (completion rate: ~0.3 tasks/month)
- Most assigned to Tina Valdez, Amy Rayzor (junior staff)
- No forward movement suggests decisions stuck at Ron level (scope approval, prioritization, release gating)

**Opportunity cost**: If Ron is spending ~5–10 hours/week on Discount Pipe backlog triage that never ships, he's losing 5–10 hours of high-value work (AskCruz delivery, architecture, Sabre Alloys integration). Over 6 months, that's 120–240 hours of blocked leverage.

### AskCruz: Cost Structure

- 1 SDR (Sebastian Roa, contractor at SRV Consulting, started Aug 27): Likely $3–5k/month all-in contractor cost
- 6 interns + 1 resigned: Likely $0–2k/month total (unpaid or minimal stipend)
- Ron J (split allocation, ~10% on AskCruz): Estimated ~$2.5–4k/month allocated
- Rajat (5% on AskCruz): Founder time, representing opportunity cost of ~$833/month in lost personal productivity (understates true opportunity cost of split focus)

**AskCruz customer acquisition cost (implied)**:
- 1 prospect (3GM) after 4 weeks (Sebastian + Rajat 5% + interns) = ~$8–12k cost to date, $0 revenue
- Cost per pipeline opportunity: $8–12k
- Cost per customer: undefined (0 customers)
- Expected CAC at $115–160k ARR (8 months remaining): $40–60k per customer if 2–3 customers close; $80–120k per customer if only 1 closes

**Post-go-live support model cost leak**:

EOXS has no documented support SLA or tiering. Pattern: customers escalate directly to Ron (implied by his role as "escalation handler"). This means:
- Ron handling Tier 1 (customer calls) + Tier 2 (technical troubleshooting) + Tier 3 (architecture decisions)
- Junior staff cannot resolve issues independently without Ron approval
- Result: High-cost person doing low-value work (first-call troubleshooting)

**Cost impact**: If Ron spends 2–3 hours/week on post-go-live customer escalations across 8 clients, that's ~100–150 hours/year on support. At $150+/hour (estimated loaded cost), that's $15–22k/year in misdirected high-cost labor that should be tiered to junior staff.

---

## SECTION 3: SPEED & EXECUTION BOTTLENECKS

### Implementation Cycle Time

Eastern States Steel timeline:
- 49+ completed tasks from Nov 2025–present (~9 months)
- Task creation dates span Nov 2025 → Aug 2026, suggesting ongoing Phase 1 + Phase 2
- Completion rate: ~5.4 tasks/month sustained, but backlog distribution suggests front-loaded (many Nov-Dec, fewer Aug) — pattern of ramping down post-launch

**Inference**: Single-client cycle time ~8–10 months from kickoff to stable operation. At 8 clients, with staggered onboarding, the implementation queue is perpetually full.

### Discount Pipe Backlog Stall

- 91 tasks in "Requirement" stage (5 months stalled)
- Tasks created April–June 2026 with ZERO forward movement into Dev, QA, or complete
- Newer tasks (June, August) also stuck at Requirement
- Only 2 completed tasks in entire backlog

**Root cause**: Scope approval bottleneck. "Requirement" stage is where feature requests sit awaiting prioritization and Ron's sign-off before dev can begin. The stall suggests Ron has not prioritized/approved any of these 91 items in 5 months. Discount Pipe is in feature-freeze de facto.

**Speed impact**: If Discount Pipe items take 1–2 weeks each to resolve once approved, the 91-item backlog represents 3–6 months of delivery *after* approval. If approval is stuck, the customer sees zero forward momentum for 5 months. Churn risk is high.

### AskCruz GTM Bottleneck

- 3GM deal: Proposal rejected Aug 14 (5 critical errors: pricing, math, template bugs). Rajat promised rebuild Aug 14. As of Sept 3: 20+ days of zero follow-up.
- Pipeline: 1 stalled prospect, zero pipeline process, zero playbook
- Sebastian (SDR) started Aug 27 → 9 days of ramp as of Sept 5. No pipeline visibility yet.
- Founder attention: 5% on AskCruz (~2 hours/week). 3GM recovery requires ~10–20 hours (re-engagement, new proposal, negotiation). At current allocation, that's 5–10 weeks of founder time.

**Speed impact**: AskCruz is in execution stall. Zero revenue, dead deal, no playbook, SDR still ramping. Time-to-first-customer is now target 6–12 weeks (mid-Oct to Jan 2027 at best), vs. 8–12 weeks if 3GM recovery succeeds.

### Rework Loops (Cost + Speed)

Discount Pipe backlog reveals patterns:
- "Packing Error Prevention: Part 1", "Part 2", "Part 3" (3 sequential tasks)
- "Bug - Tag X Has Wrong Y", "Bug - Duplicate Tag Numbers", "Bug - System Created Duplicate Tag Numbers" (multiple attempts at same issue)
- "Sticker Descriptions - Bug", "Invoice Status - Bug", "Payment Status Behavior - Bug" (same component, multiple reported issues)

Pattern: Customer reports a feature gap or bug. Dev builds a fix. Customer tests, finds it incomplete or introduces new issues. Dev re-builds (Part 2). This repeats. Implied rework overhead: 20–30% of delivered features going back into revision.

**Speed cost**: If a single feature takes 2 weeks to build initially, and 30% enter rework, the effective cycle time is 2.6 weeks per feature. Across 824 tasks, if even 100 tasks hit rework, that's an extra 4–6 weeks of delay.

---

## SECTION 4: RISK & RESILIENCE

### Ron J: Single Point of Failure Map

Visible dependencies:
1. **Escalation routing**: Discount Pipe backlog (91 items) blocked waiting for Ron's scope approval
2. **Post-go-live support**: Implied all customer escalations → Ron
3. **Technical architecture decisions**: "Clarity on Balance Sheet dashboard" (Discount Pipe, Requirement, assigned Ron) suggests design calls funnel through him
4. **AskCruz delivery**: New deals (Sabre Alloys, 3GM if recovered) depend on Ron for implementation (Cruise integration, toll processing custom work)

**Failure scenario**: Ron unavailable for 2 weeks (illness, family, burnout, departure). Immediate impact:
- Discount Pipe escalations pile up unresolved → customer frustration
- 3GM recovery stalls (no technical feedback on revised proposal)
- Sabre Alloys delivery blocked (Ron owns Cruise integration)
- EOXS post-go-live support issues accumulate

**Resilience gap**: No documented handoff process, no backup owner, no escalation override. Two-week outage would create 4–6 weeks of downstream rework/recovery.

### Customer Concentration Risk (EOXS)

8 clients visible. Distribution unknown, but pattern suggests:
- Sabre Alloys: New deal (Sept 2), high complexity (Cruise integration + toll processing), 47% discount on recurring = lower margin
- Eastern States Steel: Mature (Phase 1 complete), now in post-go-live support
- Discount Pipe Steel: Stalled (5 months, 91-item backlog) — churn risk *high*
- Other 4 clients: Unknown status (no recent tasks visible)

**Churn risk**: If Discount Pipe churns (customer abandons due to unresponsive backlog), that's 12.5% revenue loss (1 of 8). If two small clients churn, that's 25% loss. EOXS is stable *only* if every existing customer stays — no land-and-expand, no margin improvement visible.

### Delivery Risk (AskCruz)

- 1 prospect (3GM): Trust damaged (5 errors in proposal, 20+ days no follow-up)
- PMF unproven: Zero paid revenue after months of effort
- Sabre Alloys trial: "Claude access provisioned Sept 1" but no formal agreement, no revenue
- Expected ARR by Aug 2027: $115–160k (50% miss on $250–500k target)

**Failure modes**:
1. 3GM deal dies → lose flagship prospect, narrative breaks (PMF claim is false)
2. Sabre Alloys trial ends without conversion → $60–80k ARR opportunity vanishes
3. New outbound (3 customers) targets miss → ARR lands at $0–50k
4. Founder goes full-time on AskCruz → EOXS destabilizes (Ron solo on 8 clients + AskCruz delivery)

### Knowledge Risk

Visible gaps:
- No documented GTM playbook (AskCruz)
- No documented support SLA or escalation process (EOXS)
- No documented implementation methodology or backlog prioritization (EOXS)
- Ron is the only person who can approve Discount Pipe features (no decision framework visible)

**Runbook risk**: If Ron leaves or is unavailable, EOXS operations become opaque. Junior staff cannot make decisions without Ron's verbal okay.

### Cash/Runway Risk

- EOXS: Stable revenue (8 clients, inbound-only growth). Sufficient to pay team + ops.
- AskCruz: Burning cash ($8–12k spent to date, $0 revenue). Runway depends on Rajat's personal funds or EOXS profits. No clarity on funding model.

**If AskCruz fails** (likely scenario given 50% miss probability): Rajat has invested 4+ months of founder time + ~$50–100k in direct costs. If no customers close by March 2027, the bet is abandoned, but the time/money is sunk. Opportunity cost: no new EOXS features, no founder focus on improving EOXS margins.

---

## SECTION 5: REVENUE PER EFFORT

### EOXS: Revenue Per Implementation Hour

- 8 clients, 824 implementation tasks, ~9-month average cycle
- Assume 50% of tasks = implementation (the other 50% = QA, support, rework)
- Rough estimate: 412 "actual work" tasks × 8 hours/task = ~3,300 hours implementation per complete client
- Average implementation timeline: 8–10 months per client
- Team size on implementation: ~8–10 staff

**Revenue visibility problem**: Client-by-client revenue data redacted. But pattern suggests:
- Recurring revenue model (not transactional), likely $5–20k/month per client
- Average client value: ~$60–100k ARR (estimated from Sabre Alloys trial scope + Discount Pipe feature requests suggesting mid-market)
- 8 clients × $80k ARR = ~$640k ARR

**Revenue per hour**: $640k ÷ 3,300 hours = ~$194/hour

**But rework overhead**: If 30% of tasks re-enter the backlog, effective hours = 3,300 × 1.3 = 4,290 hours, so revenue/hour drops to ~$149/hour.

**And Discount Pipe margin loss**: 47% discount on Sabre Alloys + stalled Discount Pipe backlog likely means EOXS is *not* optimizing for high-margin work. True revenue per hour may be 20–30% lower, so ~$105–120/hour.

**Leverage problem**: Implementation-heavy model (high hours-to-revenue ratio) means scaling requires proportional headcount. EOXS is not leveraged — it's a services business with services economics.

### AskCruz: Revenue Per Effort (Pre-revenue, Brutal)

- Team: 1 SDR + 6 interns + Ron 10% + Rajat 5% = ~2.5 FTE equivalent
- Cost to date: ~$50–100k (estimated)
- Revenue to date: $0
- Revenue per FTE: $0 ÷ 2.5 = $0

**If Sabre Alloys converts** ($60–80k ARR, Jan 2027):
- Cost to Jan: ~$150k ($50k initial + 6 months of $15–20k/month team cost)
- Revenue per FTE: $80k ÷ 2.5 = $32k/FTE (vs. EOXS at ~$80–100k/FTE)

**AskCruz is currently a capital-loss business.**

**Break-even analysis** ($250k ARR target by Aug 2027):
- Cost to target: ~$250k (9 months × $25–30k/month team cost) + customer acquisition (assumed 15–20% of revenue = $37–50k)
- Total cost: ~$290k
- Revenue at Aug 2027: $250k
- Net: -$40k (year one loss)

**AskCruz must hit $400k+ ARR by year-two to justify the founder time and capital burn.**

---

## SECTION 6: TOP 3 EFFICIENCY OPPORTUNITIES

Ranked by impact on four dimensions: cost saved + speed gained + risk reduced + revenue per effort improved.

### Opportunity 1: Ron J Dependency Mitigation — Hire Head of Delivery/Ops (Oct 2026)

**What to do**: Hire a Head of Implementation/Delivery/Operations by Oct 1, 2026. Role owns:
- Post-go-live customer support (escalation routing, SLA enforcement)
- Implementation backlog prioritization and approval
- Handoff process from implementation to support
- Redundancy for Ron (backup on critical decisions)

**Why it matters**:
1. **Risk**: Eliminates single point of failure. If Ron is unavailable, operations continue.
2. **Speed**: Unblocks Discount Pipe backlog. New leader can clear the approval queue in 2–3 weeks, ship stalled features.
3. **Cost**: Frees Ron for high-leverage work (AskCruz delivery, Sabre Alloys integration). Redirects junior staff to ship, not wait for approval. Estimated $30–50k annual payroll savings (Ron's time redirected to revenue-generating work, junior staff velocity increases).
4. **Revenue per effort**: Improves implementation cycle time from 8–10 months to 6–8 months per customer. At 8 clients, this means faster onboarding, faster to revenue, lower rework overhead.

**Impact quantified**:
- Discount Pipe backlog: Clear 91-item queue in 8–12 weeks (assuming 10 items/week cleared post-approval). Recover $50–100k at-risk revenue (prevent churn).
- AskCruz: Ron freed ~10 hours/week → available for Sabre Alloys delivery + new customer implementations. Unblocks scaling from 4–6 customers/year to 8–12.
- EOXS stability: Redundancy built; customer satisfaction improves (faster support response).

**Tradeoff**: Short-term cost ($40–60k salary), long-term savings (Ron productivity + junior staff utilization + churn prevention).

**90-day execution**:
- Oct 1–15: Write job description, recruit (contractor or FTE)
- Oct 15–Nov 15: Onboarding, knowledge transfer from Ron
- Nov 15+: New leader owns backlog triage, support SLA, escalation routing

---

### Opportunity 2: Discount Pipe Backlog Strategic Reset — 1-Week Executive Intervention (Sept 2026)

**What to do**: Rajat + Ron + Discount Pipe customer (Michael/ops lead) spend 1 week (20–30 hours total, 4–6 hours/day) triaging the 91-item backlog. Outcome: prioritized list (Top 10 ship in Q4, rest deferred to Q1 or won't-fix).

**Why it matters**:
1. **Speed**: Customer sees forward momentum immediately. Clear roadmap reduces frustration.
2. **Risk**: Prevents churn (5-month stall = customer contemplating exit). One churn = 12.5% EOXS revenue loss.
3. **Cost**: 1 week of exec time (estimated $5–10k cost) vs. $50–100k+ churn loss. ROI: 5–10×.
4. **Revenue per effort**: Focuses team on high-value items only. 91 → 10 items means 80% of low-priority work gets deprioritized, freeing Ron + team for AskCruz + EOXS growth.

**Impact quantified**:
- Churn prevention: $50–100k at-risk revenue protected (Discount Pipe is stable, customer confidence restored)
- Velocity improvement: Ship 10 prioritized features in 8 weeks (1 feature/week) vs. 0 in 20 weeks (status quo stall)
- Morale: Junior staff see their work ship (vs. languishing in Requirement forever). Team engagement improves.

**Tradeoff**: 1 week of founder + Ron + customer time upfront. Fast payback.

**90-day execution**:
- Sept 5–8: Triage call with Discount Pipe, list top 10 priority features
- Sept 9–12: Ron scope-approves top 10, dev team starts
- Oct 1+: Bi-weekly shipping cadence (1–2 features/week), customer sees momentum

---

### Opportunity 3: AskCruz GTM Focused Execution Model — Rajat 100% Sales + Fractional CMO/GTM Lead (Sept 2026)

**What to do**:
1. Move Rajat to 100% sales/GTM allocation on AskCruz (exit the 5% split-brain state)
2. Hire fractional CMO/GTM advisor (contract, 10–15 hours/week, Sept–Dec 2026) to build:
   - Sales playbook (pitch, objection handling, deal structure)
   - Marketing messaging + positioning
   - Sales metrics dashboard (pipeline, conversion rates, CAC)
3. 3GM recovery sprint: Rajat + CMO spend 10–15 hours in Sept to rebuild trust + new proposal + close attempt
4. Sabre Alloys closing: Hand off implementation to new Head of Delivery (see Opportunity 1), Rajat focuses on deal close + contract negotiation

**Why it matters**:
1. **Speed**: Founder attention moves from 5% to 100% on AskCruz. 3GM recovery attempt starts immediately (vs. 20+ days of stall). Sabre Alloys deal closes by Oct 1 (vs. "mid-implementation" indefinitely).
2. **Revenue**: Probability of hitting $250k ARR target increases from ~50% to ~70–75%. Most likely outcome improves from $115–160k to $180–250k.
3. **Risk**: De-risks AskCruz bet. Playbook + metrics mean subsequent customers are repeatable (vs. ad-hoc sales process). PMF validation happens by Feb 2027 (clear signal of win or pivot).
4. **Cost**: Fractional hire (~$8–12k for 4 months) + Rajat opportunity cost (EOXS growth projects deferred, but EOXS is stable/inbound-only anyway). Net cost: ~$10k.

**Impact quantified**:
- 3GM recovery: 30–40% probability of close by Oct (vs. 10% at current 20-day stall). If closes: +$30–42k ARR, +confidence for investor/board narrative.
- Sabre Alloys: Closes by Oct 1 → +$60–80k ARR (vs. stalled indefinitely)
- New pipeline: Sebastian (SDR) ramps faster with playbook (vs. shooting in dark). 2–3 new prospects by Jan 2027 (vs. 0–1 today).
- Most likely AskCruz ARR by Aug 2027: $200–280k (vs. $115–160k baseline)

**Tradeoff**: EOXS loses founder focus (but EOXS is stable/self-operating + Ron handles delivery). Short-term hit to EOXS improvement projects; long-term bet on AskCruz winning.

**90-day execution**:
- Sept 1–5: Recruit fractional CMO, kick off 3GM recovery sprint
- Sept 5–20: Rajat + CMO rebuild 3GM proposal, close attempt
- Sept 20–Oct 20: Sabre Alloys deal close (Rajat + Ron on technical), Sebastian on pipeline generation
- Oct 20+: Playbook locked, metrics dashboard live, GTM repeatable

---

## SUMMARY: EXECUTION ROADMAP (NEXT 90 DAYS)

**Week of Sept 5:**
- Decision on Opportunity 3: Is Rajat committed to 100% AskCruz GTM for 4 months? If yes, move forward with fractional CMO hire. If no, defer to Opportunity 2 + 1.
- Start Discount Pipe triage (Opportunity 2): Rajat + Ron + customer, 4–6 hours/day for 1 week. Output: prioritized list of 10 items to ship in Q4.
- 3GM recovery sprint (if Opportunity 3 approved): Rajat + CMO brainstorm revised proposal, contact Michael by Sept 10.

**Week of Sept 15:**
- Discount Pipe triage complete. Top 10 items approved, dev team starts shipping. Weekly cadence: 1–2 features/week.
- Sabre Alloys: Rajat + Ron finalize technical specs for Cruise integration + toll processing. Legal review starts.
- Fractional CMO (if hired): onboarding, playbook kickoff.

**Week of Oct 1:**
- Head of Delivery/Ops hired (Opportunity 1). Knowledge transfer from Ron starts.
- Sabre Alloys deal signed (target close). Implementation handed off to Head of Delivery (Ron freed).
- Discount Pipe: 4–6 features shipped. Customer confidence recovering.
- 3GM: Decision point (close or dead).

**Week of Oct 15 – Nov 15:**
- Head of Delivery owns backlog prioritization, support SLA, escalation routing. Discount Pipe backlog continues shipping (1–2/week).
- Ron: 100% on AskCruz + Sabre Alloys technical delivery (Cruise integration, toll processing setup).
- Rajat: 100% on AskCruz GTM (if committed) + Sabre Alloys post-close relationship.

**By Dec 1:**
- Discount Pipe backlog reduced from 91 → 50+ items (40 shipped or deprioritized). Customer relationship stable.
- Sabre Alloys live (or near-live). $60–80k ARR incoming.
- AskCruz playbook documented. 2–3 new prospects in pipeline (from Sebastian + Rajat outreach). PMF signal emerging.
- Ron capacity: Available for new feature work (EOXS modernization, AskCruz scaling beyond Sabre Alloys + recovered 3GM).
- EOXS implementation cycles: Trending toward 6–8 months (from 8–10).

---

## CRITICAL DECISIONS REQUIRED (FROM RAJAT)

1. **Commitment to Opportunity 3?** Is Rajat willing to go 100% on AskCruz GTM for Sept–Dec 2026, deferring EOXS growth projects? (EOXS is stable; this is a tradeoff, not a risk.)
2. **Discount Pipe customer relationship?** Is the customer salvageable? (Assess morale/trust before the triage week.)
3. **Head of Delivery hiring?** Internal candidate or external hire? Contract or FTE?
