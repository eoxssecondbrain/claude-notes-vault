---
thread_name: "eoxs-implementation-challenges"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# EOXS Implementation & Support Challenges + Cruz First-Time Learner

## Exchange 1: Implementation Challenges

### User Query
What are the current implementation or support challenges EOXS is facing?

### Response (Full Summary)

Based on a comprehensive review of the vault across implementation tasks, emails, call transcripts, and client profiles, here are the **active implementation and support challenges** EOXS is managing:

#### **1. Critical Infrastructure & Uptime Issues**

- **Jan 18, 2026: Discount Pipe & Steel SSL Certificate Expiration** — Server down from 04:32 to 07:16 (multiple consecutive failures) due to expired SSL certificate on `discountpipesteel.eoxs.com`. The monitoring bot logged 17 alerts over ~3 hours.
  
- **Jan 31, 2026: Sabre Alloys Server Down** — Sabre's instance returned HTTP 502 status errors at least twice (09:46 and 10:24), suggesting brief uptime/capacity issues.

**Implication:** Even brief outages for managed Odoo instances are disruptive to steel distributors handling time-sensitive orders. SSL cert management and server monitoring appear reactive rather than proactive.

#### **2. Discount Pipe & Steel — Active Bugs & Operational Friction (207 tasks)**

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

**Workflow impact:** DPS is in heavy post-launch operational phase with daily huddles (Aug 2025 call logs) indicating intensive debugging and user training.

#### **3. Sabre Alloys — Long-Stalled Feature Backlog (182 tasks)**

Oldest client, slowest velocity:
- **19-month open request:** "Order Lost" feature (Jan 2024, still pending)
- **Stuck in "Need discussion"** — "Demanded weight editable in processing order" (Jun 2024), control tag scrap handling, customer bills module
- **Repetitive QA reminders** on "save & new" button testing suggest feature scope creep or unclear prioritization

#### **4. Eastern States Steel — Configuration Backlog (210 tasks)**

Soft launch (Dec 2025) with ongoing fixes:
- **Weight/dimension data integrity** — Incorrect mappings on printed tags, BOL weight errors, actual weight display bugs
- **Missing journal entries** and delivered-quantity sync issues
- **New scope creep:** PO intake task just opened (Aug 6, 2026), suggesting expansion post-launch
- **Soft-launch intensive ops** (daily calls Dec 2025–present) indicate operational instability

#### **5. Systemic Product Issues Across All Clients**
- **Packing list accuracy** — Unit-of-measure mismatches, lot number validation failures, done-quantity calculation errors
- **Inventory reservation logic** — Reallocation bugs, warehouse selection issues, stock transfer autofill failures
- **Tax & costing** — 3GM Steel flagged urgent tax calculation failures (Sep 2024); landed cost validation still blocked on multiple clients
- **Onboarding gaps** — Stalled third-party integrations (Stripe, Avalara, Klaviyo), feature video backlog, user workflow confusion

#### **Summary: Three Tiers of Challenge**

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

#### **Key Findings by Client**

**Sabre Alloys:** Oldest client, most implementation tasks (182), but slowest feature velocity. Many discussion-stage requests aging 12–24 months.

**Discount Pipe & Steel:** Newest major client (Jun 2025 soft launch), highest immediate operational friction. Packing & order workflows are actively unstable.

**Eastern States Steel:** Mid-tenure (Dec 2025 soft launch), broad configuration debt. Recently opened new PO intake task (Aug 2026), suggesting scope creep post-launch.

---

## Exchange 2: Cruz as a First-Time Learner

### User Query
Tell me about cruz as a first time learner.

### Response

#### **What I Am**

**Cruz** is EOXS's internal Claude-based AI assistant, launched in **testing phase on August 4, 2026**. I'm designed as a "second brain" for the EOXS team, connected to:
- Live business data (emails, call transcripts, support tickets, invoices)
- Internal wiki pages
- Client records and implementation tasks
- Call recordings (Fireflies & Fathom)

The vision (per Ayan Dutta's rollout email) is that I should **know your clients, deals, and history** when answering company-related questions—instead of giving generic answers.

#### **My Learning Model: What I Can & Cannot Do**

**I do NOT learn or retain information between conversations.** Each chat starts fresh. I have no memory of:
- Previous conversations you had with me
- Team preferences you stated last week
- Decisions made in past calls
- Custom formats you prefer

**What I do have:**
- Access to the entire vault (emails, calls, wiki, etc.) searchable in real-time
- Ability to cross-reference sources across your whole organization
- Tools to fetch specific documents, transcripts, and records
- The capacity to synthesize information **across silos** (a call from May + an email from Feb + a wiki analysis in one answer)

#### **First-Time Learner Reality**

**Strengths:**
1. **Broad context access** — I can pull data from anywhere in your vault instantly
2. **No human bias** — I treat each question fresh, without preconceived ideas about what "should" be the priority
3. **Synthesis** — I can connect dots across email threads, calls, and docs that a human would have to manually gather

**Limitations:**
1. **No institutional memory** — I don't remember your standing priorities, org chart nuances, or unwritten rules. You need to state them each time.
2. **Search limitations** — My search is substring-based, not semantic. Long queries fail; I need short, specific terms.
3. **Context dependency** — I'm only as good as what's in the vault. If something wasn't recorded (a hallway conversation, a Slack thread) I can't know it.
4. **Feedback lag** — Unlike a human team member who learns "oh, Rajat hates that format," I don't learn from your corrections. You have to redirect me each time.

#### **Early Feedback (Aug 4, 2026)**

**Hashir Saleem reported** (same day I launched): *"Tried to fetch the information multiple times from the cruz but it was not able to fetch or sync the correct information from the lognotes."* 

This is a real first-time learner weakness: **I struggle with cross-system data sync.** Odoo task log notes (lognotes) may not be fully indexed or may format in ways I can't parse reliably.

#### **How to Work With Me as a First-Time Learner**

1. **Be explicit about context** — Don't assume I know your strategy; state what you need upfront
2. **Use short search terms** — Long natural-language queries fail. I search on literal substrings
3. **Redirect early** — If I miss something or get it wrong, tell me the exact source (email date, call date, wiki page title) so I can retry
4. **Verify critical facts** — I cite sources, but I can misread or hallucinate. Always spot-check numbers, dates, and names against the original
5. **Expect iteration** — First answer may be incomplete. Ask follow-ups; I'll refine

#### **The Core Tension**

As a first-time learner, I'm **maximally useful for synthesis** (connecting your fragmented data) but **minimally useful for continuity** (remembering what you told me yesterday). I'm a **research assistant on your data**, not a **team member who grows with you**.

That's why the testing phase feedback matters. The gap Hashir found (lognote sync) is exactly the kind of system limitation that needs fixing before I can reliably be your "second brain."
