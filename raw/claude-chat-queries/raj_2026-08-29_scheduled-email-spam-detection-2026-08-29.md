---
thread_name: "scheduled-email-spam-detection-2026-08-29"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

# Scheduled Email Spam Detection (v3) — Run 2026-08-29

**Trigger:** Automated scheduled task firing (no live user present).

**Task:** Run the configured spam-detection routine against Gmail: repair pass for orphaned AI-SPAM threads, then classify unprocessed inbox threads as SPAM/SUSPICIOUS/NOT_SPAM, label and move spam to the Spam folder.

## Actions taken
- Step 0 (repair pass): searched `label:AI-SPAM -in:spam` (incl. trash) — 0 orphans found.
- Labels confirmed to already exist: AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-Reviewed. No creation needed.
- Not a first run (AI-Reviewed already had 14,415 messages / 7,054 threads applied historically), so used normal-run query `in:inbox -label:AI-SPAM -label:AI-Reviewed`, paginating 50 at a time.
- Discovered the backlog is very large (estimate stayed ~201-402 across pages, historical mail back to 2023). Processed 10 pages = 500 threads this run.
- For each thread: read sender/subject/snippet, applied skip-list rules (eoxs.com/eoxsteam.com senders or recipients, security alerts, calendar mail, invoices/receipts, auto-replies/OOO, outbound EOXS sales, offer letters), then classified.
- Results: 429 threads labeled AI-Reviewed (NOT_SPAM). 71 threads labeled AI-SPAM + sub-label and moved to Spam via mark_thread_spam (atomic per thread, label then immediate move): 67 AI-SPAM/Advertising (cold sales/marketing blasts — e.g. distributionstrategy.com, invera.com, CIENCE, chatvic.ai, practicalfounders.com, various cold outreach), 3 AI-SPAM/Fraud (ERC tax-credit scam, two nonsensical/pretext spam emails), 1 AI-SPAM/Expired-OTP (password reset link >24h old).
- Verified post-run: re-ran the orphan-repair search — 0 orphans, confirming every label+move pair completed cleanly.
- Backlog NOT exhausted — many more unprocessed inbox threads remain (Gmail's resultCountEstimate stayed pinned near 201 through multiple pages, which is a known Gmail API estimate quirk, not a reliable countdown). Next scheduled run will continue automatically since processed threads are excluded from the search.
- Sent a proactive push notification to the user flagging: large historical backlog discovered, 71 emails moved to Spam this run (semi-destructive, auto-purges ~30 days), more backlog remains for future runs.

## Notes / judgment calls
- Treated industry-specific trade content (steelmarketupdate.com, MSCI, CRU) and VC/startup-ecosystem newsletters (YC, Array VC, Sierra Ventures, Hustle Fund) as legitimate business content, not spam, even though marketing-toned.
- Treated generic SaaS vendor marketing (Stripe, Zoom, Grammarly, Carta) and unrelated cold B2B outreach/newsletters as AI-SPAM/Advertising.
- No emails were trashed or archived — only labeled and moved to Spam per the task's permitted actions.
