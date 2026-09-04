---
thread_name: "gmail-spam-sweep-2026-08-28"
user: "raj"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

# Scheduled Email Spam Detection Run — 2026-08-28

**Prompt (scheduled task, v3 spec):** Run the AI-SPAM detection sweep on rajat@eoxs.com's Gmail: repair pass for orphaned AI-SPAM threads not yet moved to Spam, then classify unprocessed inbox threads as SPAM/SUSPICIOUS/NOT_SPAM, labeling and moving spam atomically, labeling NOT_SPAM as AI-Reviewed.

## Actions taken

**Step 0 (repair pass):** Searched `label:AI-SPAM -in:spam` (includeTrash) — 0 orphaned threads found. Healthy.

**Step 1 (normal run):** Searched `in:inbox -label:AI-SPAM -label:AI-Reviewed`, paginated 13 pages of 50 (650 threads checked). For each: read sender/subject/snippet, checked skip-list exceptions (eoxs.com/eoxsteam.com domain, security notices, payment/invoice/receipt mail, calendar mail, auto-replies, EOXS's own outbound sales campaigns identifiable by cc/bcc to rajat@eoxs.com and EOXS/ERP pitch content), then classified.

Notable pattern: large volume of EOXS's own outbound cold-email sales campaign using persona gmail accounts (emma.eoxs, victoria.eoxs, sophia.eoxs, natalie.eoxs, christine.eoxs, kathy.eoxs, gabriel.eoxs, walter.eoxs, megan.eoxs, pamela.eoxs) all cc'd/bcc'd to rajat@eoxs.com pitching AI tools to steel industry prospects — classified NOT_SPAM per the outbound-sales skip-list exception.

**34 threads labeled AI-SPAM and moved to Spam** (atomic label+move per thread, no orphan risk):
- 26 × AI-SPAM/Advertising (cold sales pitches: SEO/guest-post link spam x4 from 2 senders, AI-tool demo pitches, data-broker/contact-list sales, staffing/intern-pool pitch, cloud-cost cold pitch, chargeback-protection pitch, competitive-intel pitch, Google Maps engagement bait, generic "let's reconnect" cold follow-ups, etc.)
- 6 × AI-SPAM/Fraud (suspicious templated "someone wants to know about your organization — download inquiry" lures from unrelated business domains x2, a "we want to buy your company" cold offer from a .shop domain, a foreign "trading company" catalog request scam pattern, an "Associates Press" feature-story impersonation scam, an unsolicited "$2-15M family office capital injection" investment scam)
- 2 × AI-SPAM/Expired-OTP (Western Union and a bank transaction-verification OTP, both >7 months old)

**616 threads labeled AI-Reviewed** (NOT_SPAM) — legitimate EOXS business mail: client correspondence (Sabre Alloys, PPC Metals, 3GM Steel, Greer Steel, Eastern States Steel, Brannon Steel, etc.), invoices, payroll, HR/resignation letters, investor/PE outreach, EOXS's own outbound sales, travel confirmations, personal mail, bank/security notices, and vendor payment notices.

## Notable finding flagged to user (not spam, but a security anomaly)
Four legitimate Google "Gmail Forwarding confirmation" emails for lookalike accounts: rajjainpellex@gmail.com, rajjainpapnox@gmail.com, rajjainglazix@gmail.com, rajjainbuildix@gmail.com — all requesting to forward mail, all landing in rajat@eoxs.com's inbox on 2025-10-03. Classified NOT_SPAM (genuine Google system mail, not phishing itself), but the pattern of multiple similarly-named lookalike accounts is unusual and was surfaced to the user via push notification for manual review.

## Status
Backlog was very large (Gmail's resultCountEstimate stayed pinned at "201" throughout, an API estimate cap, not the true remaining count). 650 threads were processed this run; more unprocessed backlog likely remains and will be picked up automatically on the next scheduled run (the exclusion filter `-label:AI-SPAM -label:AI-Reviewed` skips everything already processed, including this run's work).

Sent a push notification to the user summarizing the run and flagging the forwarding-confirmation anomaly for review.
