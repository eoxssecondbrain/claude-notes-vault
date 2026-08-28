---
thread_name: "gmail-spam-detection-scheduled-run-2026-08-28"
user: "raj"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

# Scheduled Email Spam Detection Run — 2026-08-28

**Trigger:** Scheduled task "Scheduled Email Spam Detection (v3)" fired automatically (unattended).

## Actions taken

**Step 0 (repair pass):** Searched `label:AI-SPAM -in:spam` (including trash) — 0 orphaned threads found. No repair needed.

**Step 1 (run sizing):** AI-Reviewed and AI-SPAM labels already existed and had prior usage (AI-Reviewed had 1856 threads before this run), so this was treated as a normal run: `in:inbox -label:AI-SPAM -label:AI-Reviewed`, paginated in batches of ~20-50.

**Backlog discovery:** The `resultCountEstimate` field returned a static "201" on every page, but the actual backlog was much larger — pagination continued processing threads dating back to mid-June 2025 before the run was wrapped up. This indicates prior runs left a substantial unprocessed backlog beyond what the estimate suggested.

## Classification summary (this run only)

- Threads reviewed and labeled NOT_SPAM (AI-Reviewed): 377
- Threads classified SPAM/SUSPICIOUS, labeled AI-SPAM + AI-SPAM/Advertising or AI-SPAM/Fraud, and moved to Spam folder: 44
- Total processed this run: 421 threads
- Orphans found/fixed in repair pass: 0

### Spam/Advertising sub-label (most)
Cold B2B sales pitches (dev/freelance services, staffing/recruiting, M&A/investment banking cold outreach, insurance, accounting services, ISO certification mass blasts, cleaning services), generic event/community marketing blasts (Eventbrite, Luma, spiritual/wellness event invites) unrelated to EOXS business, and one "$500 giveaway" style marketing email.

### Spam/Fraud sub-label
- "Funding Saints" fake pre-approved $440,100 business credit line email (classic loan-approval scam pattern).
- "Global Business Leaders" magazine pay-to-be-featured solicitation ($1150 ask) — vanity press scam pattern.

### Preserved as NOT_SPAM (per skip rules)
All eoxs.com/eoxsteam.com correspondence, internal task-bot notifications (info.eoxs@gmail.com, info.*@gmail.com pattern), client/vendor business threads (Sabre Alloys, 3GM Steel, Discount Pipe & Steel, PPC Metals, Titanium Industries, Eastern States Steel, Gerdau/Hansen Solutions, Greer Steel, Conklin Steel), invoices/receipts/payment notices (Contabo, Google Workspace, Stripe, Square, SHEIN, Interac e-Transfers from known contact PRATA INC., Expedia, Atlassian), investor relations (Mucker Capital, Base10, Volition Capital, JMI Equity, Telescope Partners), tax/accounting correspondence (Liberty CPA — established relationship), calendar declines, security alerts, and EOXS's own outbound sales/prospecting emails.

## Verification
- Confirmed via `list_labels` before/after: AI-Reviewed threads 1856 → 2233 (+377); SPAM folder threads 903 → 947 (+44); INBOX threads 21046 → 21002 (-44). Counts reconcile exactly with the classification tally above.
- Re-ran the orphan-repair search after finishing — 0 orphans, confirming every AI-SPAM label was paired with a successful move to Spam.

## Outcome / notification
Sent a push notification to the user: backlog is much larger than the task's assumed ~201-email scope; 421 threads reviewed this run (44 moved to Spam); a large remaining backlog will continue to be processed on future scheduled firings of this same task (already-labeled threads are automatically excluded from future runs, so no duplicate work).

## Follow-up for next run
Next firing will pick up wherever `in:inbox -label:AI-SPAM -label:AI-Reviewed` still returns results — no manual intervention needed. Consider whether the task's per-run scope should be bounded (e.g., a max thread cap per firing) if clearing the full historical backlog in very large batches is not desired.
