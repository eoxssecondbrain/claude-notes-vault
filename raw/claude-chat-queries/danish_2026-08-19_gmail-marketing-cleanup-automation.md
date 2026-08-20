---
thread_name: "gmail-marketing-cleanup-automation"
user: "danish"
type: claude-chat
created: 2026-08-19
updated: 2026-08-20
---

# Gmail Marketing Cleanup Automation — Run Log

## Task
Scheduled, unattended run: find marketing/promotional email in inbox since last run, apply label "Marketing Review" (Label_12), archive out of inbox (remove INBOX). Skip transactional/important (OTPs, statements, receipts, order confirmations, payment confirmations). Account: iraqidanish@gmail.com. Cap: 300 threads/run.

## Run (2026-08-20)
Query: `in:inbox (category:promotions OR unsubscribe)` — ~201 estimate, scanned 6 pages (300 threads, hit run cap).

Inbox is heavily transactional (HDFC/Axis/YES bank alerts & statements, CDSL/demat, mutual fund TER notices, Paytm payment-received, Delhivery shipment tracking, CIBIL alerts, CKYC updates, credit-card application status). These were all SKIPPED as transactional.

Labeled + archived (~47 threads) — marketing/promotional only, examples:
- Job spam: Indeed, Shine, Cutshort welcome, LinkedIn job digest, WorkIndia leads
- Newsletters: Substack (Business Analytics, House of the Dragon), Quora digest, Reddit subreddit digests
- Retail/promo: Amazon Music offer, PlayStation, YouTube promos, Nykaa, Playasia cashback, FirstCry(no—order was transactional), CoinDCX, Snapchat nudges, NotebookLM feature announce
- Service promos: Google Business Profile prompts, Delhivery experience survey, Xbox Research Panel survey, CDSL easi onboarding, HDFC "2nd card + Amazon voucher" offer

Skipped as borderline-transactional: Reddit direct reply notifications, ZoomInfo welcome/list-ready, Google account/security notices, CIBIL report-change alerts, bank minimum-balance notices, credit-card application-status emails.

## Notes
- Gmail MCP threw frequent transient "service unavailable"/connection-timeout errors; all retried once and succeeded per run rules. No persisted failures.
- Batch size normal (~47), no escalation needed.
