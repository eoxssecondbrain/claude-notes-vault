---
thread_name: "askcruz-how-companies-use"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# How AskCruz Is Used by Companies - Real Examples

## Summary

This conversation explored how companies like Sabre Alloys actually use the AskCruz AI agent to solve real business problems. The primary evidence comes from Michael Mercadante (CEO, Sabre Alloys) who outlined 20 high-priority use cases in a detailed email to Rajat Jain (June 16, 2026).

## Key Use Cases by Category

### 1. **Cash & Accounts Receivable (AR)** 
Critical questions the AI helps answer:
- Which invoices are overdue?
- Which customers owe the most money?
- Which customers should be reviewed for credit hold?
- Which customers are profitable but slow to pay?
- What cash is expected in the next 7, 14, 30, and 60 days?

**Business value**: Identify cash traps and collection priorities instantly, not through manual reports.

### 2. **Open Orders & Shipment Risk**
The AI identifies what profitable work is blocked:
- Which open orders are late?
- Which orders can ship today?
- What's blocking shipment, and who owns the next action?
- How much gross profit is sitting in orders ready to ship but haven't shipped?

**Business value**: Every day an order sits unshipped = money stuck in operations. AI shows what to prioritize immediately.

### 3. **Inventory Management**
One of Sabre's biggest pain points. AskCruz answers:
- What inventory hasn't moved in 90, 180, 365, or 730 days?
- Which inventory items have the most dollars tied up with no demand?
- Which items are overstocked/understocked?
- What stock is available to sell today after allocations?

**Business value**: Steel is capital-intensive. Dead stock = cash bleed. AI exposes hidden inventory costs.

### 4. **Quotes & Sales Activity**
Separating productive sales activity from noise:
- Which open quotes need follow-up?
- Which quotes can be filled from current inventory?
- Which quotes are below target margin?
- What's the quote-to-order conversion rate by salesperson?
- Which accounts should sales call today based on inventory availability?

**Business value**: Sales teams focus on winnable deals with margin, not chasing low-probability quotes.

### 5. **Margin & Pricing**
Identifies where margin is leaking:
- Which orders were below target margin?
- Which customers discount too much?
- Which orders sold material below replacement cost?
- Which customers should get price increases?

**Business value**: Finds the $ $10K-$50K margin leaks that compound fast in a steel business.

### 6. **Purchasing & Vendor Management**
Reduce unnecessary buying and identify vendor risk:
- Which POs are late?
- Which vendors are causing shipment delays?
- Are we buying material we already have in inventory?
- What material should we reorder now vs. avoid?

**Business value**: Avoid double-buying and obsolescence. Identify vendor risks before they cost customers.

### 7. **Customer Profitability & Behavior**
Who's actually good for the business:
- Who are the most profitable customers by gross profit dollars?
- Who is least profitable after freight, disputes, and slow payment?
- Which customers have stopped buying?
- Which customers require too much service relative to profit?

**Business value**: Revenue ≠ profit. AI shows which customers are actually worth the effort.

### 8. **Certs, Documentation & Quality Blockers**
Material can look available but be unshippable:
- Which open orders are missing certs or MTRs?
- Which shipments are blocked by documentation?
- Which vendors have recurring quality issues?

**Business value**: Prevents expensive last-minute order holds.

### 9. **Daily Management Briefing** (The #1 Use Case)
The single most valuable prompt Michael requested:

> "Give me today's management briefing: cash risks, late orders, overdue AR, margin exceptions, inventory issues, vendor problems, and anything that changed materially since yesterday."

**Business value**: CEO gets 1-page intelligence each morning instead of slogging through 5 different reports. Drives decision-making in real time.

---

## Why This Matters for Sabre (and Any Steel Company)

Michael's email explicitly stated: 

> "The core objective is simple: we want Claude to help Sabre **see what deserves attention now, why it matters, and what action should be taken.**"

This is not a chatbot. It's **decision support powered by actual ERP data.**

---

## Implementation Status

- **June 16, 2026**: Michael submitted the detailed 20-question request
- **Aug 7-10, 2026**: Rajat scheduled a demo call with Michael (Monday 1 PM CT)
- **Aug 10, 2026**: Call took place; Rajat confirmed "we have something ready to show you"

No public confirmation yet of go-live, but the infrastructure was in place for a working demo.

---

## The Difference from "Generic AI"

Michael was explicit about what he **didn't** want:

> "We are not looking for a generic chatbot or a simple report writer."

What he wanted:
1. **Accurate answers tied to actual ERP records** (not guesses)
2. **Company definitions** (e.g., "available inventory" = on-hand minus allocated/reserved, not just ERP number)
3. **Traceability** (answer should drill back to source records)
4. **Speed** (replace a 30-minute manual report with a 30-second question)

This is the threshold AskCruz was built to cross.
