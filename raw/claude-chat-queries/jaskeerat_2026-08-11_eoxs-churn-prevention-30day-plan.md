---
thread_name: "eoxs-churn-prevention-30day-plan"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# EOXS Churn Prevention: 30-Day Intervention Plan

## Executive Prioritization (Next 30 Days)

### Priority Ranking: URGENT → HIGH → MEDIUM

| Priority | Client | Risk % | Days Since Last Major Update | Key Contact | Decision Urgency | Recommended Action |
|----------|--------|--------|------------------------------|-------------|------------------|-------------------|
| **🔴 URGENT #1** | **Discount Pipe & Steel** | 70% | ~20 days (Aug 2026 billing dispute) | Austin Rayzor (CEO/Owner) | **Decision imminent** — contract at 14-month mark; renewal signals needed by Q4 2026 | **Executive intervention call + task audit** |
| **🔴 URGENT #2** | **PPC Metals** | 65% | ~30 days (July 2026 ongoing ops) | Eddie Poindexter (Owner) | **Still actively escalating** — 9 months post-live; if issues don't resolve by Oct, renewal at risk | **Stability sprint + performance demo** |
| **🔴 HIGH #3** | **Sabre Alloys** | 55% | ~10 days (latest IRIS QA status) | Michael Mercadante (Champion) | **AI expansion pending** — IRIS feature critical to renewal decision; stalled 88 days risks deal momentum | **AI sprint + bug closure** |

---

## PRIORITY #1: Discount Pipe & Steel (70% Risk) — START IMMEDIATELY

### Why #1 (Not #2 or #3)?

1. **Highest concrete risk signals:**
   - 207 open implementation tasks (no other client has >30)
   - Pattern of tickets closed without root-cause (suggests systemic dysfunction)
   - Most recent action: **Billing dispute (Aug 6, 2026)** — trust erosion active NOW
   - Third-party consultants engaged (Tina Valdez, Jamie Vernon from Alt Digital) — clear signal of shopping for alternatives

2. **Timeline urgency:**
   - **Contract: April 2025 → June 2028 (3 years)**
   - **Renewal decision window: Q4 2026–Q1 2027** (6–9 months away)
   - **If no turnaround by November 2026**, renewal strategy shifts to exit planning

3. **Highest organizational friction:**
   - Zana Williams (operations) frustrated by recurring issues
   - Austin Rayzor (CEO) involved in multiple dispute resolutions
   - Amy Rayzor (co-owner, marketing) also engaged — whole leadership team is paying attention

4. **Relationship risk:**
   - Not in full crisis like PPC was, but in **slow-motion decay phase**
   - Third-party consultant engagement is a churn precursor (client building exit plan)
   - One more billing dispute or major bug could trigger active exit conversations

### 30-Day Concrete Plan for Discount Pipe & Steel

#### Week 1: Executive Intervention & Triage (Aug 12–18, 2026)

**Monday, Aug 12 — Rajat + Ron J Call with Austin Rayzor (60 min)**
- **Objective:** Reset relationship; show EOXS is serious about stabilization
- **Talking points:**
  1. Acknowledge billing dispute (Aug 6) — clarify: Bank Reconciliation Module was [yes/no] in scope; commit to clear contractual clarity
  2. "207 open tasks" is misleading framing — actually ~30 critical, ~177 are routine product adds/config — but we own the communication failure
  3. Present **"Discount Pipe Recovery Sprint"** (see below) with clear milestones
  4. Explain **packing list bug fix** (platform-wide issue; benefits DPS + Sabre; in dev now)
  5. Introduce **dedicated stability liaison** (Ron J explicitly assigned to daily standup through Oct 31)
- **Success metric:** Austin agrees to pause alt-vendor conversations; commits to Dec 15 checkpoint call
- **Escalation path:** If Austin declines, Rajat sends written commitment + 48-hour response SLA for critical issues

**Wednesday, Aug 14 — Ron J + Hashir Saleem + Humaira Zainab: Task Triage Meeting (90 min)**
- **Objective:** Sort 207 tasks into **CRITICAL → HIGH → ROUTINE**
- **Deliverable:** Spreadsheet with:
  - **CRITICAL (resolve by Sept 30):** Packing list confirmation failures, "done quantity" discrepancies, recurring quote-stage bugs, stock transfer errors
  - **HIGH (resolve by Oct 31):** Salesperson field bugs, invoice status display, reporting field availability
  - **ROUTINE (resolve by Nov 30 or defer):** Product adds, warehouse locations, cosmetic UX fixes
- **Output:** Email to Austin with **"3-month roadmap"** showing 40+ tasks closing by Oct 31
- **Ownership:** Ron assigned as DPS "recovery lead"; Hashir owns CRITICAL bugs; Humaira owns HIGH priority

**Friday, Aug 16 — Billing Clarity Call: Rajat + Austin + Amy Rayzor (30 min)**
- **Objective:** Clarify Bank Reconciliation Module scope (avoid repeat disputes)
- **Deliverable:** Written statement emailed Aug 17:
  - List all included modules (base ERP contract)
  - List all à la carte add-ons (with pricing [restricted])
  - Bank Reconciliation Module: Was it in-scope for DPS? [Clarify]
  - If NOT in-scope: Offer [restricted] credit for Aug billing; reset expectations going forward
  - If IN-SCOPE: Apologize for communication gap; provide training/docs; resolve Aug dispute
- **Success metric:** Written clarity + Austin's sign-off before Aug 18

#### Week 2–3: Stabilization Sprint (Aug 19–Sept 1)

**Monday, Aug 19 — Discount Pipe "Recovery Sprint" Kickoff**
- **Team:** Hashir (lead), Ron J (account mgmt), Humaira (QA), Dhrup (backend if needed), Sheenam (product comms)
- **Sprint Goal:** Close 15 CRITICAL tasks + reproduce/fix packing list bug (platform issue)
- **Daily standup:** 10 AM ET, 30 min, async Slack updates if needed
- **Blockers:** Ron J escalates within 4 hours to Rajat if any task is stuck >24 hours
- **Public communication:** Weekly update email to Austin (Tuesday, 9 AM) showing closed tickets + blockers

**Key Bugs to Close by Aug 31:**
1. **Packing list confirmation failures** (T07103 + related) — spans DPS + Sabre; Hashir leads fix
2. **Stock transfer "done quantity" discrepancy** (recurring) — Humaira roots cause; Dhrup codes fix
3. **Quote stuck at quote stage** (recurring bug on J & I Mfg SO) — Humaira traces; fix by Aug 25
4. **Invoice status showing "Not Paid" post-invoicing** (bug) — Hashir roots cause; fix by Aug 28

**Supporting Infrastructure:**
- **Sandbox environment:** Dedicated DPS sandbox for testing packing list fixes (Aug 19)
- **User acceptance testing:** Zana Williams + Amy Rayzor invited to test fixes before prod rollout (Aug 30)
- **Rollout plan:** Production deployment + training call scheduled for Sept 3 (after labor day)

#### Week 4: Checkpoint & Forward Plan (Sept 2–8)

**Wednesday, Sept 4 — DPS Stabilization Checkpoint Call: Rajat + Austin + Zana + Amy (60 min)**
- **Deliverables to discuss:**
  1. ✅ Packing list fix deployed + tested (Aug 31)
  2. ✅ Quote-stage bug resolved (Aug 25)
  3. ✅ Invoice status fixed (Aug 28)
  4. ✅ Stock transfer reconciliation workaround deployed (pending permanent fix Oct 15)
  5. ✅ Billing clarity documented (Bank Rec module scope resolved)
  6. ✅ Task tracking updated: 40 CRITICAL/HIGH closed by Sept 4
- **Forward plan:** Present Q4 roadmap
  - **Sept–Oct:** Close remaining HIGH tasks (20–25)
  - **Nov 1:** "Discount Pipe Stabilization Complete" milestone
  - **Nov 15:** Feature roadmap for 2027 (upsell opportunity: AI features, advanced reporting)
- **Relationship reset:** Ask Austin: "What would success look like for your team by Dec 31?" — re-engage on business outcomes
- **Success metric:** Austin commits to Q1 2027 renewal conversation (formal commitment)

**Friday, Sept 6 — Post-Sprint Retrospective: Ron J + Hashir + Humaira**
- **Questions:**
  1. Why did packing list take this long to fix? (Architecture issue? Resource gap?)
  2. Why were 207 tasks lingering without closure? (Communication, scope creep, or prioritization?)
  3. What do we change to prevent this with next client?
- **Output:** Brief memo to Rajat (1 page) on process improvements for future accounts

---

### Success Metrics for DPS (30 Days)

| Metric | Target | Indicator of Success |
|--------|--------|----------------------|
| CRITICAL tasks closed | 15 of 15 | Packing list, quote status, invoice display all working |
| Weekly email updates | 4 consecutive | Austin reads them (opens + engagement) |
| Billing dispute resolved | Written clarity | Austin no longer disputing module scope |
| Renewal signal | Explicit commitment | Austin commits to Q1 2027 renewal conversation (not exit) |
| Third-party consultant engagement | Tapers | No new meetings scheduled with Alt Digital after Sept 1 |
| Zana's satisfaction | Documented | Positive feedback in Sept 4 call |

---

## PRIORITY #2: PPC Metals (65% Risk) — START WEEK 2

### Why #2 (Not #1)?

1. **Less imminent than DPS:**
   - Contract: Oct 2025 go-live → Oct 2028 (still 2+ years out)
   - Renewal decision window: 12–18 months away
   - Crisis window (Dec 2025–Feb 2026) **already passed** — we're in recovery phase, not acute crisis

2. **BUT still critical:**
   - Eddie Poindexter still escalating routine bugs (July 2026) — engagement hasn't cooled, trust isn't restored
   - "Slower than prior system" is a killer signal — performance perception matters more than actuality
   - 9 months post-live with ongoing accounting COGS issues = confidence problem
   - **If PPC becomes vocal about churn risk, it signals to other clients**

3. **Opportunity:**
   - James Baker + Crystal McDaniel are now operational power users — they can advocate for system IF we fix performance + accounting
   - Relationship is strained but not broken

### 30-Day Concrete Plan for PPC Metals

#### Week 1–2: Root-Cause Analysis (Aug 12–25, 2026)

**Monday, Aug 12 — PPC Performance Task Force Kickoff (Dhrup + Hashir + Yash M**
- **Objective:** Identify why system "feels slower" + fix architecture issue
- **Scope:**
  1. **Performance profiling:** Measure processing module load times vs. benchmark (what was prior system?)
  2. **Background processing workaround:** Currently in QA (April–June issue) — move to production by Aug 25
  3. **Database query optimization:** EOXS may have n+1 query issues or missing indexes on tag-based inventory
- **Success metric:** Performance regression fully resolved by Aug 31; demo to Eddie shows measurable improvement

**Wednesday, Aug 14 — Accounting COGS Deep Dive: Rajat + Yash M + Pam Poindexter (controller)**
- **Objective:** Clarify the Nov 2025 bank journal reclassification issue + COGS confusion
- **Agenda:**
  1. Walk through the Nov reclassification journal (101401 → 111200) — did it actually clear the issue?
  2. Review latest P&L statement: Are COGS figures now correct?
  3. Identify if issue is data (wrong balances) or UI (confusion about account structure)
  4. **Action:** If data issue, provide one-time corrective entry + training; if UI issue, create P&L format guide
- **Deliverable:** Written "PPC COGS Reconciliation" doc signed off by Pam by Aug 16
- **Success metric:** Pam confirms "P&L numbers now match bank statements"

#### Week 2–3: Executive Reset (Aug 19–31)

**Monday, Aug 19 — Rajat + Eddie Poindexter Call (60 min)**
- **Objective:** Address "slower than prior system" perception directly
- **Talking points:**
  1. Acknowledge: EOXS had performance issues (April–June); we own that
  2. Background processing fix deployed (Aug 25) — measurable improvement
  3. Request: "Let's measure it together" — Eddie runs same workflow as before, we show timing side-by-side
  4. Address accounting COGS: "Pam confirmed P&L is now correct as of Aug 20"
  5. Broader point: "9 months in, you've surfaced real issues; we've fixed most of them. Let's reset expectations on what Q4 looks like"
- **Ask:** Can we do a "system health check call" weekly through Oct 31 with James + Crystal + Eddie to track improvements?
- **Success metric:** Eddie agrees to weekly check-ins; commits to "give us 60 days to prove performance is fixed"

**Wednesday, Aug 21 — James Baker + Crystal McDaniel One-on-Ones (30 min each)**
- **Purpose:** Understand operational friction from day-to-day user perspective
- **James Baker (Inside Sales):** "What automation gaps still exist vs. your prior system?"
  - SmartQuote AI scope confusion (from Feb escalation) — is this still an issue?
  - Any quotes taking longer than expected?
  - **Commitment:** By Sept 15, we'll clarify SmartQuote scope (is it available? When production-ready?)
- **Crystal McDaniel (Accounting):** "Are COGS/P&L numbers now matching bank statements?"
  - What other accounting friction remains?
  - Any check-printing or payment-receipt issues?
  - **Commitment:** By Sept 1, we'll validate her P&L against bank statements together

#### Week 3–4: Stabilization & Momentum (Sept 2–8)

**Monday, Sept 2 — Performance Demo Call: Eddie + Rajat + Yash M (45 min)**
- **Demo:** Run same sales order → processing → invoice workflow vs. old system (side-by-side timing)
  - Old system: X seconds (benchmark they remember)
  - New system (with Aug 25 fix): X - Y seconds (improvement)
- **Live data:** Use actual PPC sales order from July to show it's not synthetic
- **Result:** "EOXS is now measurably faster than your prior system for these core workflows"
- **Ask:** Eddie's feedback — does this match his perception now?

**Wednesday, Sept 4 — PPC Metals Quarterly Business Review Call: Rajat + Eddie + James + Crystal + Pam (60 min)**
- **Agenda:**
  1. ✅ Performance improvements validated
  2. ✅ COGS/P&L reconciliation complete
  3. ✅ Accounting workflow clarity documented
  4. Q4 roadmap: What features/fixes do you want us to prioritize?
     - SmartQuote AI finalization (James's ask)
     - Tax configuration/Avalara integration (ongoing)
     - Advanced reporting for Pam
  5. 2027 renewal: "Let's plan a formal renewal conversation for Dec/Jan — here's what success looks like for you by then"
- **Success metric:** Eddie's tone shifts from critical to collaborative; asks about new features (signal of forward-thinking, not exit planning)

#### Week 4: Relationship Locks (Sept 8–15)

**Friday, Sept 8 — Weekly Check-In #1: Ron J + James Baker + Crystal + Eddie (if available)**
- Purpose: Establish cadence; show EOXS is committed to ongoing partnership
- Format: 30 min, async Slack if needed, structured agenda (performance check, issues, wins)
- **Success metric:** Eddie attends or delegates to James/Crystal (shows trust)

---

### Success Metrics for PPC (30 Days)

| Metric | Target | Indicator of Success |
|--------|--------|----------------------|
| Performance improvement | Measurable | Demo shows EOXS faster than prior system on core workflows |
| COGS reconciliation | Confirmed | Pam signs off: "P&L now matches bank statements" |
| Weekly check-ins established | 4+ scheduled | Eddie/James/Crystal actively participating |
| SmartQuote scope clarity | Documented | James has clear answer: available Y/N, timeline X |
| Relationship sentiment | Shifted | Eddie asks about 2027 roadmap (not exit options) |
| Renewal signal | Explicit | Eddie commits to Dec/Jan renewal conversation |

---

## PRIORITY #3: Sabre Alloys (55% Risk) — START WEEK 3

### Why #3 (Not #1)?

1. **Lower urgency (but not low-risk):**
   - Contract: June 2024 live → June 2027 (2+ years out)
   - Renewal decision window: 12–18 months away
   - Sabre is still actively expanding (28 users, IRIS AI expansion)

2. **BUT paradoxical risk:**
   - **Critical bugs idle for 6+ months** (T06021, T05973, T06181) = platform stability concern
   - **IRIS AI expansion stalled 88 days** = growth initiative at risk
   - **If expansion stalls**, Sabre's "growth trajectory" becomes a "growth disappointment" → churn accelerates
   - **SupportAI bot ignored** on key tickets = internal process breakdown

3. **Strategic opportunity:**
   - Michael Mercadante (champion) is betting on IRIS AI for business value
   - If we deliver IRIS + close critical bugs by Oct 31, Sabre becomes a **success case + expansion reference**
   - This is about winning them over more decisively for 2027 renewal

### 30-Day Concrete Plan for Sabre Alloys

#### Week 1: Triage & Executive Alignment (Aug 12–18)

**Monday, Aug 12 — Sabre Critical Bug Sprint Kickoff (Dhrup + Hashir + Aryan Bakshi)**
- **Priority order:**
  1. **T06021 (Control Tag unit-value revert):** 78+ idle days; CRITICAL path to processing
  2. **T07029 (IRIS QA):** 88 idle days; AI feature stuck
  3. **T05973 + T06181 (Related processing issues):** 100–200+ days; unblock other features
- **Goal:** Get T06021 to "QA Passed" by Aug 25; T07029 to Staging by Aug 28
- **Success metric:** Sabre can test packing list fix + IRIS in sandbox by Sept 1

**Wednesday, Aug 14 — Michael Mercadante + Rajat Call (60 min)**
- **Objective:** Confirm IRIS AI expectations + delivery timeline
- **Talking points:**
  1. "We know you've been waiting on IRIS QA (88 days) — we own that delay"
  2. IRIS feature set: Clarify what's in scope (decision support queries? Margin analysis? Forecasting?)
  3. Claude API cost model: "We're evaluating cost-effective ways to deliver AI; options are X/Y/Z"
  4. Delivery target: "IRIS to staging by Aug 28; production by Oct 15" (realistic?)
  5. **Broader point:** "IRIS is a strategic expansion for us too; let's align on what success looks like for your team"
- **Ask:** Can Michael lead a Sabre "IRIS pilot user group" starting Sept 1? (Engagement + advocacy)
- **Success metric:** Michael's excitement returns; he volunteers to be pilot tester

**Friday, Aug 16 — Sandbox Access Troubleshooting: Ron J + Juan Deshon (30 min)**
- **Problem:** Juan can't access sandbox (July 31, 2026) — blocks his ability to test Income Statement reports
- **Solution:** Reset his account; provide sandbox credentials; confirm he can log in by EOD Aug 16
- **Downstream:** Juan can now test Income Statement export (T07513) + Inventory Aging Report (T07056) starting Aug 19
- **Success metric:** Juan confirms "I can now test in sandbox"

#### Week 2–3: Execution Sprint (Aug 19–Sept 1)

**Monday, Aug 19 — Sabre IRIS Delivery Sprint Kickoff**
- **Team:** Dhrup (lead), Sheenam (product), Aryan Bakshi (QA)
- **Sprint goal:** IRIS to staging by Aug 28; documentation ready by Sept 1
- **Daily standup:** 2 PM ET, 15 min (covers Dhrup + Sheenam updates)
- **Blockers:** Dhrup escalates to Rajat within 4 hours if stuck >24 hours
- **Sabre communication:** Weekly update email to Michael (Tues) on feature progress

**Key Deliverables by Sept 1:**
1. ✅ **IRIS Claude integration:** Feature in staging environment; Michael can demo queries
2. ✅ **Control Tag unit-value fix (T06021):** Deployed to production; tested with Juan
3. ✅ **Packing list confirmation fix:** Staging ready; Sabre QA team invited to test (Aug 30)
4. ✅ **Income Statement export:** Working in sandbox; Juan validates by Aug 28
5. ✅ **IRIS documentation:** "Getting Started with IRIS" guide (2 pages, plain English)

**Supporting Infrastructure:**
- **Sabre pilot user group:** Michael + Juan + Ernie Valdez (operations) invited to Sept 5 kickoff meeting
- **Weekly IRIS updates:** Bi-weekly calls (Michael + Sheenam) to track feedback → product roadmap
- **Test environment:** Dedicated "Sabre-IRIS-Pilot" sandbox with sample data (manufacturing scenarios)

#### Week 4: Checkpoint & Relationship Reset (Sept 2–8)

**Wednesday, Sept 4 — Sabre IRIS Pilot Kickoff: Michael + Rajat + Sheenam + Dhrup (60 min)**
- **Demo:** Live IRIS queries running against Sabre's production-like data
  - Example 1: "Show me margin by customer (YTD)"
  - Example 2: "Forecast Q4 revenue based on open orders"
  - Example 3: "Flag any processing orders with negative contribution"
- **Feedback loop:** Michael's team tries 3–5 custom queries; notes pain points
- **Roadmap:** "Bi-weekly updates; production launch targeting Oct 15"
- **Success metric:** Michael's enthusiasm restored; commits to pilot participation through Oct 31

**Thursday, Sept 5 — Sabre Packing List Fix Verification: Juan + Ernie + Ron J (45 min)**
- **Objective:** Verify packing list confirmation fix works end-to-end
- **Test scenario:** Create sample processing order → confirm packing list → invoice
- **Success:** "Packing list confirms without timeout; order proceeds to invoice"
- **If issues remain:** Root-cause immediately; fix by Sept 8

**Friday, Sept 6 — Critical Bug Resolution Summary: Ron J + Rajat**
- **Recap for Michael (email by Sept 7):**
  ```
  🎯 Sabre Critical Bug Status (30-Day Sprint)
  ✅ T06021 (Control Tag unit-value) — Resolved Aug 22; in production
  ✅ T07029 (IRIS QA) — Staging Aug 28; pilot starts Sept 5
  ✅ T05973 + T06181 (Processing) — Resolved Aug 25; production tested
  ✅ T07513 (Income Statement export) — Working; Juan validated
  ✅ Packing list confirmation — Production fix deployed Sept 3
  
  🚀 Next: IRIS production launch Oct 15
  📅 Sabre Pilot User Group: Bi-weekly updates starting Sept 5
  ```
- **Success metric:** Michael forwards email to his team; shows confidence restored

---

### Success Metrics for Sabre (30 Days)

| Metric | Target | Indicator of Success |
|--------|--------|----------------------|
| IRIS to staging | Aug 28 | Michael can demo live queries |
| Critical bugs closed | 4 of 4 | T06021, T07029, T05973, T06181 resolved + tested |
| Sandbox access restored | Aug 16 | Juan confirms he can log in + test |
| Pilot user group formed | 3+ participants | Michael, Juan, Ernie committed to Sept 5 kickoff |
| Michael's sentiment | Shifted | Asks about 2027 IRIS roadmap (not frustrations) |
| Renewal signal | Implicit | Active participation in IRIS pilot (shows forward momentum) |

---

## Summary: 30-Day Intervention Timeline

### Week 1 (Aug 12–18)
- **DPS:** Rajat-Austin call + billing clarity + task triage
- **PPC:** Performance task force + COGS analysis + Eddie call prep
- **Sabre:** Bug triage + Michael call + sandbox access fix

### Week 2 (Aug 19–25)
- **DPS:** Recovery sprint begins; 5 CRITICAL bugs targeted
- **PPC:** Eddie call (Aug 19) + performance profiling continues
- **Sabre:** IRIS sprint begins; Dhrup leads feature to staging

### Week 3 (Aug 26–Sept 1)
- **DPS:** Close packing list + quote-stage bugs; prep sandbox testing
- **PPC:** Performance demo preparation; James/Crystal check-ins
- **Sabre:** IRIS staging complete; packing list fix deployed

### Week 4 (Sept 2–8)
- **DPS:** Checkpoint call (Sept 4); present Q4 roadmap; lock renewal conversation
- **PPC:** Performance demo (Sept 2); QBR (Sept 4); establish weekly cadence
- **Sabre:** IRIS pilot launch (Sept 5); packing list verification (Sept 5); bug summary email (Sept 6)

---

## Success Criteria (All Three Clients, Day 30)

| Client | Day 30 Outcome | Churn Risk Shift |
|--------|----------------|------------------|
| **Discount Pipe & Steel** | 15 CRITICAL tasks closed; billing dispute resolved; Austin commits to Q1 2027 renewal | 70% → 45% |
| **PPC Metals** | Performance fix deployed & demoed; COGS reconciliation confirmed; Eddie agrees to weekly check-ins | 65% → 40% |
| **Sabre Alloys** | IRIS to staging; 4 critical bugs closed; Michael leads pilot user group | 55% → 35% |

**Portfolio outcome:** Churn risk reduced from ~45% to ~40% (modest but solid progress). All three accounts show forward momentum instead of decay.

---

## Resource Requirements (30 Days)

| Resource | Allocation | Assigned To |
|----------|-----------|------------|
| **Rajat Jain** | 3 executive calls (DPS, PPC, Sabre); 1 performance demo | Prioritize over other sales activities |
| **Ron J** | 30% allocation (DPS sprint lead, PPC relationship mgmt, Sabre verification) | Dedicated to these three accounts |
| **Dhrup Kumar Singh** | 40% (IRIS sprint, performance fixes, bug closures) | Lead dev on all three |
| **Hashir Saleem** | 25% (DPS packing list, PPC COGS, Sabre critical bugs) | Coordinated with Dhrup |
| **Humaira Zainab** | 20% (DPS HIGH-priority tasks, Sabre QA) | Support role |
| **Sheenam Rawat** | 15% (IRIS product management, client communications) | Part-time |

**Total: ~1.5 FTE of dev + support time for 30 days.** If EOXS doesn't have spare capacity, defer other work or bring in contractors.

---

## Risk Mitigation: What If We Miss a Deadline?

| If This Happens | Mitigation |
|-----------------|-----------|
| DPS packing list not fixed by Aug 31 | Offer interim workaround + promise Sept 7 prod deployment; maintain Aug 19-31 momentum |
| PPC performance demo fails (still slow) | Honest assessment: "Issue is architectural; permanent fix by Oct 15"; offer manual optimization in meantime |
| IRIS staging delayed past Aug 28 | Update Michael by Aug 25 with new target (Sept 5?); show staging progress to maintain momentum |
| Sabre sandbox still broken on Aug 16 | Escalate to infrastructure team; offer temporary SSH access to database for Juan's queries (workaround) |
| Any client misses weekly update email | Send 48-hour apology + detailed status; recommit to schedule for following week |

---

## Decision Point: Go/No-Go (Aug 12)

**If Rajat commits to this 30-day plan by EOD Aug 12:**
- ✅ Book all executive calls (Rajat's calendar, non-negotiable)
- ✅ Assign Ron J, Dhrup, Hashir full-time
- ✅ Cancel or defer non-critical work
- ✅ Daily 2 PM sync (Rajat + Dhrup + Ron J) to track blockers

**If Rajat cannot commit full resources:**
- ⚠️ Prioritize DPS #1 only (highest risk signal + newest dispute)
- Defer PPC to Week 3
- Defer Sabre to Week 4
- Accept higher churn risk for PPC/Sabre while betting on DPS stabilization

**Recommended:** Full go. 30 days of focused effort now prevents 6–12 months of churn conversations later.
