---
thread_name: "scheduled-spam-detection-2026-08-29"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

## Scheduled Email Spam Detection Run — 2026-08-29

**User (system, automated firing):** Scheduled Email Spam Detection (v3) — repair orphaned AI-SPAM threads not yet moved to Spam, then classify unprocessed inbox threads as SPAM/SUSPICIOUS/NOT_SPAM per the configured rules, label and move confirmed spam, label the rest AI-Reviewed, report counts.

**Assistant actions taken:**
1. Confirmed labels exist (AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-Reviewed — ids Label_33–37).
2. Step 0 repair pass: searched `label:AI-SPAM -in:spam` (includeTrash) — 0 orphaned threads found. Healthy.
3. Normal run (not first run — AI-Reviewed already had ~4936 messages historically): searched `in:inbox -label:AI-SPAM -label:AI-Reviewed`, paginated 50 at a time, processed 7 pages = 350 threads (covering inbox mail from roughly late Aug 2025 back through mid-April 2025).
4. For each thread: read sender/subject/snippet, applied the skip list (eoxs.com/eoxsteam.com domains, security notices, payment/invoice/receipt mail, calendar mail, auto-replies, offer letters/onboarding, EOXS's own outbound sales, codes <24h old), then classified.
5. Confirmed SPAM/SUSPICIOUS threads (37 total): labeled AI-SPAM + sub-label, then immediately called mark_thread_spam (atomic per thread, no batching).
   - 32 × AI-SPAM/Advertising: unsolicited cold sales/lead-gen/agency pitches, guest-post/SEO link spam (repeat sender mizrahilawpc.com), competitor ERP marketing (invera.com), webinar/podcast/database-sales spam, a fake-reviews-service pitch, a Beehiiv mass newsletter, a real-estate listing blast, etc.
   - 4 × AI-SPAM/Fraud: two unsolicited "ERC/pandemic relief credit" tax-scam emails from a "nassaustreet...co" domain family, one "35% returns" investment webinar scam (dubai-lifestylechoice.com), one fake "RE:" investment cold-pitch from an unclear domain (evlvhld.com) using false familiarity framing.
   - 1 × AI-SPAM/Expired-OTP: a Healthians OTP code from May 2025 (over a year old, well past the 24h cutoff).
6. 313 threads classified NOT_SPAM and labeled AI-Reviewed only (no move) — mostly real client/business correspondence (Sabre Alloys, 3GM Steel, Eastern States Steel, Discount Pipe & Steel, Greer Steel, Gerdau/Hansen Solutions, Conklin Steel, etc.), internal EOXS operations (info.eoxs@gmail.com task bot, invoices, leave requests), Contabo/Google/Zoom/Upwork vendor notices, and Rajat's personal wellness-community mail (Othership, Luma events, Eventbrite, Acuity) which come from established paid/registered relationships rather than cold spam.
7. Judgment calls flagged for Raj: recurring industry/vendor newsletters with a plausible existing relationship (Steel Market Update, Distribution Strategy Group's "AI News & Gurus", Contabo's own promo emails, Zoom product-update mail) were kept NOT_SPAM rather than Advertising, since AI-SPAM/Advertising has never been applied before this run (0 messages historically) and moving established-vendor mail to Spam (30-day auto-purge) is a real, semi-destructive action or Raj's judgment. Two cold "Founder Poker" event-invite duplicates and two cold podcast/workshop pitches were the closer calls, resolved as Advertising given no established relationship and templated cold-outreach language.

**Result:** 0 orphans (Step 0), 350 threads checked, 37 SPAM/SUSPICIOUS (32 Advertising, 4 Fraud, 1 Expired-OTP) all moved to Spam, 313 NOT_SPAM marked AI-Reviewed. ~150+ older inbox threads remain unprocessed and will be picked up automatically by the next scheduled firing (the exclusion filter permanently skips anything already labeled, so nothing is lost by stopping here). Notified Raj by push given the fraud attempts found and the backlog size.
