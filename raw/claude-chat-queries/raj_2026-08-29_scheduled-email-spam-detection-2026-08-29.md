---
thread_name: "scheduled-email-spam-detection-2026-08-29"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

## Scheduled Email Spam Detection (v3) — Run 2026-08-29

**Task**: Automated Gmail spam/phishing detection scheduled task (system prompt, not a user message).

**Step 0 — Repair pass**: Searched `label:AI-SPAM -in:spam` (includeTrash: true) — 0 orphaned threads found. Healthy.

**Step 1 — Run size determination**: AI-Reviewed label already had thousands of applied messages (not a first run). Ran normal-run query `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, paginating through backlog.

**Processing**: Reviewed 500 inbox threads across 10 pages (backlog dated back to Aug–Sep 2023, apparently never fully processed before). For each: read sender/subject/snippet, checked skip-list overrides (eoxs.com/eoxsteam.com domain, security notices, payment/invoice mail, calendar mail, auto-replies, offer letters, outbound EOXS sales), then classified SPAM / SUSPICIOUS / NOT_SPAM.

**Results**:
- Checked: 500
- Moved to Spam/Advertising: 57 (recurring cold-outreach senders: distributionstrategy.com, hustlefund.vc, revgenius.com, invera.com competitor-ERP ads, conventioneers.us, various SDR/growth-hacking/backlink/SEO/HR-outsourcing pitches, Marriott Bonvoy promo, a bar Halloween promo, etc.)
- Moved to Spam/Fraud: 1 (ERC "Employee Retention Credit" refund-claim solicitation from a personal Gmail address — known tax-scam pattern)
- Marked AI-Reviewed (NOT_SPAM): 442
- Orphans repaired: 0

**Notes / judgment calls flagged to Raj**: Kept as NOT_SPAM (not moved): steel-industry newsletters he appears subscribed to (Kallanish Steel, Steel Market Update/SMU, CRU/marketing@crugroup.com content), MSCI trade-association training emails, AngelList conference invite, personalized VC/investor outreach and replies (even when unsolicited, since personalized rather than bulk), LinkedIn/Zoom/Gust/OpenAI account notifications, community/social lists (Founder Poker Toronto, HVE amenity/dance/swim classes), and a distinction was drawn between distributionstrategy.com's bulk "content@" newsletter (spammed) vs. personal replies from its co-founder Ian Heller (kept, since personal correspondence).

**Notification sent**: Pushed a summary to Raj via PushNotification, since moving mail to Spam is a real, semi-destructive action (Gmail auto-purges Spam after ~30 days) and this was a large first-time backlog sweep.

**Remaining work**: Backlog is larger than what was processed this run (estimate stayed around ~200+ unprocessed for several pages, suggesting Gmail's estimate is imprecise and/or the backlog spans further back than Aug 2023). Processed threads are now labeled (AI-SPAM or AI-Reviewed) so future scheduled runs will pick up where this one left off without reprocessing.
