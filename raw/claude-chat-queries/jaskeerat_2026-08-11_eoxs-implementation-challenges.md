---
thread_name: "eoxs-implementation-challenges"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# EOXS Implementation & Support Challenges

## User Query
What are the current implementation or support challenges EOXS is facing?

## Response

Based on a comprehensive review of the vault across implementation tasks, emails, call transcripts, and client profiles, here are the **active implementation and support challenges** EOXS is managing:

---

## **1. Infrastructure & Uptime Issues**

**Severity: Critical**

- **Jan 18, 2026: Discount Pipe & Steel SSL Certificate Expiration** — Server down from 04:32 to 07:16 (multiple consecutive failures) due to expired SSL certificate on `discountpipesteel.eoxs.com`. The monitoring bot logged 17 alerts over ~3 hours.
  
- **Jan 31, 2026: Sabre Alloys Server Down** — Sabre's instance returned HTTP 502 status errors at least twice (09:46 and 10:24), suggesting brief uptime/capacity issues.

**Implication:** Even brief outages for managed Odoo instances are disruptive to steel distributors handling time-sensitive orders. SSL cert management and server monitoring appear reactive rather than proactive.

---

## **2. Discount Pipe & Steel — Active Bugs & Operational Friction (207 tasks)**

**Status: Ongoing implementation burden**

Recent high-priority items in active work:

- **Packing List Confirmation Failures** (Jun–Jul 2026)
  - Tasks: "Unable to Confirm Packing List," "No. of Pcs discrepancy (packing list)," "Recurring 'Done Quantity' Discrepancy on Stock Transfers"
  - Impact: Blocks order fulfillment workflow; affects physical warehouse ops.
  
- **Sales Order Line & Inventory Issues**
  - "Sales Order Status Not Updating" (Code QA, Jul 6)
  - Shipping weight calculation bugs, tag data quality issues.
  
- **Control Tag & Inventory Reservation Bugs**
  - Duplicate tag generation, wrong footage on tags, quote-to-SO field retention issues.
  - Multiple months of remediation work across May–Jul 2026.

- **Quote & Order Creation Gaps**
  - Quote price defaults incorrectly; customer contact updates require delete/re-add; salesperson field changes between quote and SO.

- **Reporting & Data Visibility** — Feature backlog on custom reports, all fields/measures not exposed.

**Workflow impact:** DPS is in heavy post-launch operational phase with daily huddles (Aug 2025 call logs) suggesting intensive debugging and user training.

---

## **3. Eastern States Steel — Configuration Backlog (210 tasks)**

**Status: Soft launch stabilization**

- **Weight & Dimension Data Integrity** (ongoing)
  - Incorrect width mapping on printed tags, BOL weight column errors, incorrect actual weight display.
  - Three separate tasks on weight field mapping alone.

- **Control Tag Alignment** — Packing list sync, weight display in delivered quantities, landed cost blocking.

- **Order & Financial Workflow** — Missing journal entries, reservation field updates, delivered quantity not updating on sales orders.

- **UI Customization Debt** — Hide unused menu items, filter delivery address dropdowns, manual CRM add option, prospect contact visibility filtering.

- **New Requirement:** Purchase order intake task just opened (Aug 6, 2026), suggesting post-launch expansion scope.

**Pattern:** ESS is 5–6 months into soft launch (late Dec 2025 calls) with ongoing configuration requests and bug fixes piling up.

---

## **4. Sabre Alloys — Long Open Task Backlog (182 tasks)**

**Status: Mature but stalled features**

- **"Demanded Weight Editable in Processing Order"** — Marked "Need discussion" since Jun 2026. No forward movement visible.

- **Control Tag Automation & Scrap Handling** — Multiple completed control-tag fixes (Apr–Jun 2024), but newer requests like "Control tag for Scrap" stuck in "Need discussion."

- **Financial Reporting** — "Bills" task in "Need discussion" since May 31, 2024. Customer AR/AP reconciliation and payment terms have had sporadic work.

- **Feature Requests Aging Without Resolution**
  - "Order Lost" feature open since Jan 2024 (19+ months).
  - Various UX improvements (save & new button QA, header tab reorganization) repeatedly flagged in task deadline reminders but showing slow closure.

**Pattern:** Sabre is the largest/longest client but feature velocity appears constrained; many requests linger in discussion/need-decision states.

---

## **5. Systemic Product & Data Quality Issues**

**Spanning multiple clients:**

- **Packing List Accuracy** — Unit-of-measure mismatches (SO/PO), control tag unavailability on packing list, lot number validation, done-quantity calculation errors.

- **Inventory Reservation Logic** — Reservation reallocation, warehouse selection, delivered-quantity sync, stock transfer field bugs.

- **Tax & Costing Calculations**
  - 3GM Steel has urgent tax calculation issues impacting financial reporting (Sep 2024).
  - Landed cost validation still appears in multiple client backlogs (Sabre, DPS).

- **UI/UX Friction** — Quote/SO field retention, salesperson assignment changes, customer statement formatting, contact deduplication.

---

## **6. Post-Launch Onboarding & Training Gaps**

**Identified across clients:**

- **Feature/Training Video Backlog** (Discount Pipe, open since Jan–Feb 2026).
- **Stalled Third-Party Integrations** — Stripe payment issues, Avalara/TaxCloud bugs, Klaviyo integration requirement not yet built.
- **Airflow & Workflow Documentation** — Repeated QA testing reminders suggest user confusion on intended workflows (e.g., "What does Put In Pack button do?").

---

## **Summary: Three Tiers of Challenge**

| Tier | Issue | Clients | Impact |
|------|-------|---------|--------|
| **Critical** | Server uptime, SSL cert expiration | Sabre, DPS | Order/cash flow interruption |
| **High** | Packing/inventory/reservation bugs | DPS, ESS, Sabre | Fulfillment delays, data integrity |
| **Medium** | Feature requests, UI polish, reporting | All | User friction, delayed expansion |

**Root patterns:**
1. **Reactive ops over proactive:** Infrastructure issues are caught by alerts, not prevented.
2. **Feature bloat:** 600+ open tasks across clients; prioritization unclear.
3. **Post-launch debt:** All three major clients (Sabre, DPS, ESS) have soft launches followed by long backlogs of bug fixes and feature requests.
4. **Cross-cutting data problems:** Weight, UOM, reservation, and tag data integrity issues repeat across clients, suggesting product design debt.

---

## Key Findings by Client

**Sabre Alloys:** Oldest client, most implementation tasks (182), but slowest feature velocity. Many discussion-stage requests aging 12–24 months.

**Discount Pipe & Steel:** Newest major client (Jun 2025 soft launch), highest immediate operational friction. Packing & order workflows are actively unstable.

**Eastern States Steel:** Mid-tenure (Dec 2025 soft launch), broad configuration debt. Recently opened new PO intake task (Aug 2026), suggesting scope creep post-launch.
