---
thread_name: "scheduled-email-spam-detection"
user: "raj"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

## Scheduled Email Spam Detection (v4) — Run: 2026-08-31

**User (scheduled task prompt):** Scheduled Email Spam Detection (v4) — automated Gmail spam/phishing triage task. Full spec: call list_labels, determine first-run vs normal-run, search_threads for unprocessed mail, classify each as SPAM/SUSPICIOUS/NOT_SPAM per detailed rules (phishing indicators, investor-outreach carve-out, EOXS-domain skip list, expired-OTP rule, etc.), apply AI-SPAM/AI-Reviewed labels, move confirmed spam to Gmail Spam, and report counts.

**Assistant actions and findings:**

1. Called `list_labels`. Found AI-Reviewed (Label_37) already applied to 22,515 threads / 42,920 messages, and AI-SPAM (Label_33) + all 4 sub-labels already exist (0 threads each). Since AI-Reviewed has clearly been applied before, this was determined to be a **normal run**, not a first run.

2. Ran `search_threads` with query `-in:sent -in:chats -label:Label_33 -label:Label_37`, pageSize 50, and paginated through 6 pages (300 threads total, resultCountEstimate stayed at "201" throughout — an inaccurate/stale estimate).

3. Discovered the search tool's documented quirk (message-level matching within threads) was causing heavy false-positive resurfacing: the vast majority of returned threads had ALL their messages already carrying Label_37 (already fully reviewed in prior runs), yet still matched the `-label:Label_37` exclusion query. To avoid double-processing per instruction #8 ("do not process the same email twice"), applied a defensive check: only threads with at least one message NOT already carrying Label_37/Label_33 were treated as genuinely new and processed; fully-already-labeled threads were skipped even though the search returned them.

4. Verified this approach was correct by also testing the query with label display-names instead of IDs (`-label:AI-SPAM -label:AI-Reviewed`), which returned resultCountEstimate 1206 (essentially unfiltered — confirming label-name negation doesn't work reliably here, and the ID-based query + per-thread verification is the right approach).

5. Out of 300 threads reviewed across 6 pages, found exactly **4 threads with genuinely new/unlabeled content**:
   - `1a04a3ec8cbce169` — Zoho Calendar "Invitation ... accepted by sheenam@eoxsteam.com" (internal calendar notification) → NOT_SPAM
   - `1a0593818a1cfcd7` — info.eoxs@gmail.com internal EOXS system task notification → NOT_SPAM
   - `1a0570892464fc5f` — new message in existing Zoom/Fireflies notetaker-joined thread → NOT_SPAM
   - `1a04cb877a6ff758` — new message (Raj's "Approved 45k." reply) in existing internal incentive-claim thread (ayan@eoxsteam.com / isha@eoxsteam.com) → NOT_SPAM

   All 4 were internal/automated business notifications with no phishing, prize, OTP, or investor-outreach indicators. Applied `label_thread` with AI-Reviewed (Label_37) to all 4.

6. Special check performed: one older already-processed thread (`1a0408c5905aa7d6`, FasterCapital "Insights & Next Steps" follow-up) looked like it could be unsolicited Investor-Outreach spam, but a check of `in:sent to:fastercapital.com` showed Rajat had proactively emailed contact@fastercapital.com back in 2023 ("Investment Opportunity") — an existing relationship, so the 2a investor-outreach carve-out would not have applied even if this were being freshly classified. This thread was already fully labeled from a prior run, so it was not reprocessed, but the relationship check confirms the earlier classification logic was sound. Also spot-checked: Banneker Partners and Level Equity cold investor-outreach emails found in the result set were already labeled AI-Reviewed (NOT_SPAM) from a prior run — not reprocessed, per no-double-processing rule.

**Final counts for this run:**
- Checked (genuinely new/unprocessed): 4
- SPAM: 0
- SUSPICIOUS: 0
- NOT_SPAM: 4
- Moved to Gmail Spam: 0
- Sub-label breakdown: AI-SPAM/Advertising: 0, AI-SPAM/Expired-OTP: 0, AI-SPAM/Fraud: 0, AI-SPAM/Investor-Outreach: 0

**Outcome:** Clean run, no spam/phishing found, nothing moved to Spam. No push notification sent to the user (per operating instructions: an all-clear/no-op result doesn't warrant interrupting them). Flagged to self for a future run: the Gmail search's `-label:` exclusion is unreliable/stale (resurfaces already-labeled threads), so this defensive per-thread label check should continue to be used every run to avoid double-processing or mis-classifying already-reviewed mail.
