---
thread_name: "eoxs-30day-action-plan"
user: "ai_interns1"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

# EOXS Strategic Opportunities: 30-Day Action Plan

## Context
User: Rajat Jain (CEO EOXS, transitioning full-time to AskCruz)
Date: September 3, 2026
Request: "Check latest information and tell me what we should do next" (follow-up to 50ft deep analysis)

---

## Session Summary

### Prior 50ft Deep Analysis Delivered
Five high-impact opportunities identified:
1. AI Workers as standalone SaaS (Epicor/SAP customers)
2. Predictive churn monitoring + expansion revenue
3. Productized integrations (Stripe, Aircall, TaxCloud, etc.)
4. Anonymized steel industry intelligence platform
5. Sales acceleration toolkit (CRM + coaching)

**Total TAM: $1.7M-$4.3M incremental ARR**

Recommendation: Tier 1 (start now) = Opportunities 2 & 3. Tier 2 (Q4) = Opportunities 1 & 5. Tier 3 (defer) = Opportunity 4.

---

### Current Business Reality (as of Sept 3)
- 8 clients, 824 active implementation tasks
- 9 unpaid invoices totaling $27,822 outstanding
- Discount Pipe & Steel: $7,879 overdue (94 days), 60+ open tasks, 5+ high-priority bugs
- Sabre Alloys: $9,380 invoice 30 days old
- Hansen: $1,200 invoice 94 days overdue
- 84 implementation tasks unowned in Requirement stage
- Ron J is single point of failure for all escalations/technical decisions
- Payment status bug making invoice collection worse (customers show "Not Paid" even when paid)

---

## 30-Day Action Plan: This Week & Next

### WEEK 1 (Sept 4-6): Immediate Decisions & Hiring

**Action 1: Hire Interim Customer Success Lead (By Friday)**
- Role: 90-day contract, $50-60k annualized (pro-rated)
- Profile: SaaS/account management background, data-comfortable, scrappy ops
- Posting: LinkedIn, Angel List, Slack startup communities
- Why: Opportunity 2 (churn monitoring + expansion) requires this person. Can't execute without it.
- Time required: 6 hours (write posting, screen, interview this week)
- Owner: Rajat

**Action 2: Direct Call to Discount Pipe & Steel (By Thursday EOD)**
- What to ask: "Are invoices actually paid? Which tasks are blocking you most? What would make you recommend us to peers?"
- Goal: Distinguish between accounting friction (broken payment tracking) vs. customer unhappiness (task delays).
- Outcome: Clarify real vs. perceived problem. Commit to specific fix.
- Time: 45 min total (15 min prep, 30 min call)
- Owner: Rajat

**Action 3: Audit Integration Task Backlog (By Sunday)**
- Filter implementation tasks for: Stripe, Aircall, TaxCloud, QuickBooks, Klaviyo, Email, Bank Transaction, Website Forms
- For each: note client count, status (not started / partial / complete), estimated complexity
- Create ranking: (Client Count × Margin Potential) / Estimated Effort
- Outcome: Top 3 tier-1 integrations identified (likely Stripe, Aircall, TaxCloud)
- Time: 2 hours
- Owner: Rajat or junior analyst

---

### WEEK 2 (Sept 9-13): Validation Sprints & Specs

**Action 4: Churn Scoring Pilot Launch (Mon-Fri)**
- Monday: CS lead onboarded on customer contracts, task status, invoice aging
- Tue-Wed: CS lead builds churn risk score for 8 customers (framework: open tasks + invoice days overdue + feature adoption + support velocity)
- Thu-Fri: CS lead calls top 2 at-risk customers (Discount Pipe, Sabre Alloys). Capture feedback (what would retain them?)
- Measure: Churn score spreadsheet completed. 2 customer calls logged with 1-2 page summaries.
- Owner: CS lead (primary), Rajat (1 hr/week check-in)

**Action 5: Spec Out Stripe Integration & Get Ron's Approval (Mon-Wed)**
- Monday: Rajat writes 1-page Stripe MVP spec (scope, timeline, success criteria, pricing)
  - Scope: payment capture, webhooks, basic reconciliation
  - Timeline: 2 weeks build + 1 week QA
  - Pricing: $8k Discount Pipe (pilot), $3k per additional customer
  - Success metric: quote-to-payment cycle time reduction
- Tuesday: 30-min call with Ron. Get sign-off on: feasibility, timeline, who owns build
- Wednesday: Assigned engineer does 1-hour technical audit (integration blockers?)
- Measure: Signed spec + engineer audit completed
- Owner: Rajat (spec) + Ron (approval) + engineer (audit)

**Action 6: Outreach to Epicor Partners (Thu-Fri)**
- Thursday: Identify 3-5 mid-tier Epicor partners in steel/distribution (LinkedIn search)
- Friday: Send short emails (~150 words): "We've built SmartQuote AI (98% quote accuracy, cuts cycle from 30 to 3 days), works with any ERP including Epicor. Interested in white-label or referral partnership?"
- Measure: 3 emails sent, track responses
- Owner: Rajat (2 hours)
- Outcome: Early signal on partner interest (likely 0-1 responses this week; follow up in 2 weeks)

---

### WEEKS 3-4 (Sept 16-27): Parallel Validation Streams

**Stream A: Churn Mitigation (CS Lead + Rajat + Ron)**
- CS lead continues customer advisory calls with other clients (not just top 2 at-risk)
- Discount Pipe intervention: Ron fixes payment status bug (4 hours) + publicly commits to Aircall integration timeline (Q4)
- Schedule executive business review with Discount Pipe (late Sept): Rajat + Ron present retention plan + roadmap
- Measure: Retention commitments made. Discount Pipe confidence restored (track via NPS / direct feedback)

**Stream B: Integration Pilot Execution (Ron + Engineer)**
- If Stripe spec approved: engineer starts 2-week build sprint (target completion: Oct 1)
  - Weekly standup with Ron (1 hour/week oversight, not execution)
  - Build, QA, pilot setup with Discount Pipe (early adopter)
- If Stripe blocked: pivot to TaxCloud or Aircall, restart spec
- Measure: Stripe integration builds (or clear reason it doesn't)

**Stream C: Sales Toolkit Minimum Spec (Rajat)**
- Draft 1-pager: "Sales Accelerator for Steel, MVP"
  - Features: email threading + Aircall sync + 3 sales coaching videos (mined from call transcripts)
  - Price: $2,500/month
  - Target segment: sales directors/inside sales teams (not ops)
- Identify 2 potential pilots (ideally non-current-ERP customers to test land-and-expand)
- Measure: 1-page spec + 2 candidate customers identified

**Stream D: Hiring & Budget Planning (Rajat)**
- Decide: do you hire 1) delivery manager for integrations, or 2) delegate to mid-level engineer?
- Decide: do you hire VP of Product for sales toolkit + AI workers, or use contractor/advisor model?
- Draft Q4 budget: assume $50-75k for staff/contractors through Dec 31
- Measure: hiring decisions made, budget approved

---

## By October 1: Go/No-Go Decisions

### Decision 1: Churn Mitigation (Opportunity 2)
- Did Discount Pipe stay + commit to expansion? (payment bug fix + Aircall timeline)
- If yes: scale retention playbook to other at-risk customers (Sabre, Hansen)
- If no: customer was churning regardless; focus energy elsewhere

### Decision 2: Stripe Integration (Opportunity 3)
- Did 2-week build complete on time?
- If yes: sell Stripe integration to Discount Pipe + Sabre Alloys ($8k + $3k) by Oct 15
- If no: why? (Ron unavailable? technical blockers? engineer skill gap?) Pivot or hire

### Decision 3: Sales Toolkit MVP (Opportunity 5)
- Did pilot customers bite on $2.5k/month pricing?
- If yes: scale toolkit with full coaching content + launch
- If no: shelve until Q4 or redesign positioning

### Decision 4: Epicor Partnerships (Opportunity 1)
- Any partner responses to outreach?
- If yes: schedule depth calls, explore co-selling
- If no: follow up once in Oct or defer to later

---

## Staffing Reality Check

**What you need (not 5 new hires, just 1 new role):**
- 1 CS lead (hire this week): $50-60k annualized, owns churn + expansion + customer advisory
- 1 mid-level engineer (hire Q4 if Opportunity 3 successful): owns integrations, reports to delivery manager (not Ron)
- 0 new hires Q3 beyond CS lead
- Ron becomes "strategy + escalation + unblocking" resource, not day-to-day execution
- You (Rajat) focus on decision-making + strategy for EOXS while going full-time on AskCruz

**Budget assumption:** $50-75k for CS lead + contractors/tools through Dec 31

---

## Why This Sequence Matters

1. **Churn prevention** (Opportunity 2) is #1 urgency + lowest risk. $7.8k overdue from largest customer is a siren. Fix now.
2. **Integrations** (Opportunity 3) proves "productized services" model scales. Early revenue validates thesis.
3. **AI workers** (Opportunity 1) + **Sales toolkit** (Opportunity 5) can wait until Oct when you have proof points from Opportunities 2 & 3.
4. **Intelligence platform** (Opportunity 4) deferred to 2027 due to legal/privacy complexity.

---

## Daily Decision Points (This Week)

| Date | Decision | Owner |
|---|---|---|
| Monday Sept 9 | Does CS lead start on time? | Rajat |
| Tuesday Sept 10 | What does Discount Pipe say about payment + task delays? | Rajat (after call) |
| Wednesday Sept 11 | Does Ron approve Stripe spec + assign engineer? | Ron |
| Friday Sept 13 | Does CS lead have preliminary churn score? | CS lead |

**By Friday Sept 13, you'll know if Opportunities 2 & 3 are real or need pivot.**

---

## Success Metrics (30 Days)

- **Churn**: Discount Pipe commits to staying + defines expansion buy-in (Aircall integration commitment)
- **Integrations**: Stripe spec approved, engineer audit complete, 2-week build kicks off Oct 1
- **Sales Toolkit**: 1-pager drafted, 2 pilots identified, initial pricing tested
- **Partnerships**: At least 1 Epicor partner responds to outreach (even if "not interested now")
- **Hiring**: CS lead onboarded and producing insights by Sept 15

---

## TL;DR: Do This Week

1. **Monday**: Post CS lead job, start recruiting
2. **Tuesday-Thursday**: Interview/hire CS lead
3. **Thursday**: Call Discount Pipe directly (Rajat)
4. **Sunday**: Audit integration backlog, identify top 3
5. **Tuesday Sept 10**: CS lead starts
6. **Wed Sept 11**: Stripe spec presented to Ron
7. **Fri Sept 13**: CS lead churn score ready

**One month from now (Oct 3), you'll have real signals on which opportunities are worth scaling vs. which to shelve.**
