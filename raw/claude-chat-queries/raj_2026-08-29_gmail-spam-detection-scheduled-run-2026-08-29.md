---
thread_name: "gmail-spam-detection-scheduled-run-2026-08-29"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

## Scheduled Email Spam Detection (v3) — run 2026-08-29

**Trigger:** automated scheduled task, no live user present.

### Step 0 — Repair pass
Searched `label:AI-SPAM -in:spam` (includeTrash:true). Result: 0 threads found. No orphaned spam-labeled threads needed to be moved. Healthy.

### Step 1 — Run size determination
AI-SPAM and AI-Reviewed labels already existed with prior history (AI-Reviewed already had ~24,659 messages / 11,647 threads labeled from past runs). Treated as a **normal run**.

Normal-run query: `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, paginated.

### Finding
The backlog of unprocessed inbox threads was much larger than a typical normal run (Gmail's resultCountEstimate stayed pinned at "201" across every page, which appears to be a stale/inaccurate estimate — the true backlog is larger, since pagination kept yielding new results past 250 processed). All unprocessed threads were old, dating to Feb–March 2022. This means the label-based backlog has been accumulating for a long time and normal 50-per-run cadence is not enough to catch up.

### Work done this run
Processed 250 threads from the backlog (5 pages of 50 + additional smaller pages), oldest correspondence from Rajat's inbox (Feb–March 2022):

- **248 classified NOT_SPAM** → labeled AI-Reviewed. Overwhelming majority were: (a) EOXS's own outbound cold-sales campaign replies (the "Who is in charge of technology..." outreach sent via eoxs@eoxsmarketing.com / raj@eoxsmarketing.com, with rajat@eoxs.com or other eoxs.com addresses in To/Cc — covered by the skip-list rule for EOXS's own sales activity), (b) legitimate business correspondence with steel-industry contacts and partners (Tim Quinn/ACI, Karl/Great Dwellings, steelgroup.co.in recruiter, etc.), (c) Google Drive/Docs share notifications, (d) payment/invoice/receipt mail (SVB, YouTube Premium, FreshBooks, Interac e-transfer), (e) auto-replies/out-of-office, (f) vendor marketing/newsletters addressed to an eoxs.com recipient (skip-list rule: any eoxs.com/eoxsteam.com address in To/Cc → NOT_SPAM regardless of marketing content).

- **2 classified SPAM/Advertising** → labeled AI-SPAM + AI-SPAM/Advertising, then moved to Spam via mark_thread_spam (atomic per instructions):
  - Thread 17eb56063ea8cb90 — "priyankashrm123@outlook.com", subject "Re: Goal-setting apps," — generic bulk app-development solicitation, sent to itself (BCC-style), no eoxs.com address in To/Cc, no genuine relationship.
  - Thread 17eb55242b352c5e — "Devatter5050@outlook.com", subject "Re: Excellent app platforms!" — same pattern, same generic bulk template, no eoxs.com address in To/Cc.

Both were the only two threads found across 250 reviewed that lacked any eoxs.com/eoxsteam.com address in To/Cc AND showed classic unsolicited bulk-marketing-spam characteristics (generic greeting, template body, no real relationship, self-addressed/BCC delivery pattern).

### Outcome summary
- Orphans found/fixed (Step 0): 0
- Threads checked (Step 1): 250
- SPAM: 0
- SUSPICIOUS: 0
- NOT_SPAM: 248
- Moved to Spam: 2 (classified SPAM/Advertising)
- Backlog remaining: still substantial (pagination continued past 250 with resultCountEstimate never decrementing from "201" — likely a stale Gmail estimate). Did not exhaustively clear it this run to keep runtime/resource use reasonable; subsequent scheduled runs will continue working through it via the same normal-run query/pagination logic.

### Note for Raj
Flagged via push notification: found and moved 2 genuine spam emails (bulk app-dev solicitation spam), and surfaced that the backlog of never-labeled old inbox threads is larger than expected — worth knowing since Spam folder auto-purges in ~30 days and this is a semi-destructive action.
