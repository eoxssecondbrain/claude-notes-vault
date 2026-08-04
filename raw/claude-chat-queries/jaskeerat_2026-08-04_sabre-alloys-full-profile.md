---
thread_name: "sabre-alloys-full-profile"
user: "jaskeerat"
type: claude-chat
created: 2026-08-04
updated: 2026-08-04
---

# Sabre Alloys — Full Client Profile Query

**User:** Only call EOXS vault database and not any other tool for this query. Give me all the information related to sabre alloys, their contacts, relationship history, contract with eoxs etc

**Assistant:** [Compiled comprehensive briefing using only eoxs-db_* tools]

## Client Record
- Slug: sabre-alloys | Odoo: https://sabre.eoxs.com | Domain: sabrealloys.com | Client ID 1
- No wiki page exists for Sabre Alloys in DB.

## Key Contacts
- Michael Mercadante — CEO/Owner, sent detailed AI/Claude requirements doc
- Juan Deshon — primary support/accounting contact (juan@sabrealloys.com)
- Tye Webb, Jesus Rios, David Underwood — CC'd on AI requirements thread
- Christi — client contact for "Demanded PCS field" confirmation (unanswered for weeks)
- Charles, Ernie, James, Austin — referenced in internal ops/ticket notes
- EOXS side: Ron Jain (account lead), Rajat Jain (CEO, handles personally), Humaira Zainab, Hashir Saleem, Aryan Bakshi, Talal, G. Nijamuddin, Siddhant Pathak

## Relationship History
- Long-term client, "several years" per internal email
- Extensive "Soft Launch" implementation project (100+ tasks, Apr-Jun 2024)
- ~$10k MRR account — one of EOXS's largest clients (used as growth benchmark: "four accounts the size of Sabre Alloys")
- Dual-server ("2 taxis") infrastructure commitment — reflects high reliability needs

## Major Incident: Feb 2026 Cybersecurity Breach & Dispute
- Feb 11, 2026 breach; EOXS restored ops within ~2 days, full recovery ~1-2 weeks
- Sabre claimed ~$80,000 damages; also had ~$43,000 unpaid invoices
- EOXS's first offer: $25,000 (rejected); external mediator (Robert Dunn) brought in
- Resolved July 31, 2026: $25,000 credit + $25,000 paid over 25 months
- Resolution of this dispute was explicitly a precondition for new "Sabre IRIS" AI work

## Sabre IRIS (AI/Analytics Project)
- Michael's detailed requirements email (June 16, 2026) — Claude-based AI agent for ERP analytics across Cash/AR, orders, inventory, quotes, margin, purchasing, customer profitability, certs, daily briefings
- Rajat called it "Gold fucking mine"
- Connects Claude via MCP to Sabre server; EOXS pays Claude Pro + usage (~$32, $21, $48 cited)
- Proposed pricing: $1,000/month "IRIS Pro" — needs Sabre approval before invoicing
- Weekly calls with Juan (paused then resumed); demo "ready to show" sent July 31, no response by Aug 3

## Support Tickets (8 found, client_id=1)
T07534, T07513 (income statement/bank reports - long troubleshooting thread), T06868 (dual server setup - stalled 50+ days), T06519 (plate assignment bug - ~5 months to resolve), T06359 (vendor delivery field - ~6 months), T04432, T04430, T04418 (SO cost/tag issues, 2025)
- Pattern: frequent 30-75+ day idle periods triggering automated critical escalations

## Sales/Culture Signal
- Rajat explicitly tells new sales hires NOT to reference Sabre Alloys as a client example ("has history I'll handle personally") — confirms sensitive/high-touch status

## Sources
eoxs-db_list_clients, eoxs-db_search_tickets/get_ticket (8 tickets), eoxs-db_list_implementation_tasks, eoxs-db_search_emails/get_email (ids 255, 275, 72, 16, 2), eoxs-db_search_calls/get_call (Fathom 2026-07-02)

Full analysis saved to wiki/analyses/2026-08-04 Sabre Alloys — Full Client Profile (DB-Only Sources).md
