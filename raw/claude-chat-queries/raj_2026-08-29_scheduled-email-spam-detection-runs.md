---
thread_name: "scheduled-email-spam-detection-runs"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-30
---

# Scheduled Email Spam Detection Run — 2026-08-30

**Trigger:** Automated scheduled task "Scheduled Email Spam Detection (v3)".

**Step 0 (repair pass):** Searched `label:AI-SPAM -in:spam` (includeTrash true) — 0 orphaned threads found. Healthy.

**Step 1 (run type):** AI-Reviewed label already had ~34,481 messages applied (not first run). Ran normal-run query `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, paginated through 6 pages (300 threads total) covering inbox backlog from 2019 (this mailbox — rajat@prata.ca — has a large multi-year unprocessed backlog; Gmail's resultCountEstimate stayed stuck at "201" throughout, which is a stale/inaccurate API estimate, not the real remaining count).

**Results across 300 threads processed:**
- NOT_SPAM (labeled AI-Reviewed): 267 — mostly calendar invites, Authentisign e-signature notices, Buildinglink building notices, Uber/Air Canada/OpenTable/U-Haul/Amazon receipts, business correspondence (Buddy app, Farjess Steel, Social Tutors, app-dev vendor threads), security/password-changed notices, Google Docs/Sheets share invites, and personal correspondence.
- SPAM/SUSPICIOUS (labeled AI-SPAM + sub-label, then moved to Spam folder): 33 total
  - AI-SPAM/Advertising: 30 (cold sales pitches — LinkedIn InMail lead-gen/executive-program pitches, contact-form SEO/conversion spam, VC/agency/conference bulk newsletters — NFX, STRV, Cooley LLP, SVYP, Wave Financial, Freshdesk re-engagement, Lifograph, Buzz Theory Media, YEDI, RCLUB, Uber discount promos, Fuckup Nights, MPC Berlin, SAP Sapphire, kcwisdom Pitch Global, Eventbrite re-engagement blast, "Fwd: guest banner" backlink spam, "1-Day Sale" speed-reading course, "thejellysocial" newsletter, Sputnik/Gust-style bulk pitches, etc.)
  - AI-SPAM/Fraud: 1 (a "9% for US Investors" contact-form investment-scam pitch, classic guaranteed-return fraud pattern)
  - AI-SPAM/Expired-OTP: 2 (a PayPal password-reset verification code and a Myphoner email-confirmation link, both from 2019, long past the 24h usability window)

**Judgment calls applied consistently:**
- Calendar invites/updates, security/password-changed notices, payment/invoice/receipt mail, and Buildinglink building-management notices → always NOT_SPAM per the skill's exclusion list.
- Newsletters/updates tied to the user's own account or tool the user actively uses (Myphoner, GitLab, YouTube Creator, NFX Signal stats, TDSB school newsletter) → NOT_SPAM (relationship/account mail, not cold marketing).
- Unsolicited third-party bulk marketing, cold B2B sales pitches (incl. LinkedIn InMail), conference/event promo blasts, and SEO/backlink contact-form spam → SPAM/Advertising.
- Outbound sales/prospecting sent BY Rajat's own ventures (Buddy app model casting, Farjess Steel outreach to a prospect) to third parties → NOT_SPAM (treated as the user's own outbound activity, same logic as the EOXS exclusion rule).

**Outcome / next steps:** Notified user via push: 300 processed, 33 moved to spam (incl. 1 fraud pitch), large historical backlog remains and will continue to be worked through on future scheduled firings (already-labeled threads are excluded from future runs, so progress is cumulative and non-repeating).
