---
thread_name: "gmail-spam-detection-2026-08-29"
user: "raj"
type: claude-chat
created: 2026-08-29
updated: 2026-08-29
---

# Scheduled Email Spam Detection (v3)

At each scheduled run, call `list_labels` first to get label IDs; create any missing label with `create_label` (AI-SPAM, AI-SPAM/Advertising, AI-SPAM/Expired-OTP, AI-SPAM/Fraud, AI-Reviewed).

**Step 0 — Repair pass (run this FIRST, every single firing, before anything else):**
Search `label:AI-SPAM -in:spam` (pass `includeTrash: true`) to find any thread that was already labeled as spam/suspicious by a past run but never actually got moved into the Spam folder. Call `mark_thread_spam` on every thread this search returns, paginating with pageToken until it returns none. Record how many orphans were found and fixed; report this count at the end of the run.

**Determining run size (Step 1):**
- FIRST RUN: process at most the 100 most recent inbox emails.
- Otherwise (a normal run): search `in:inbox -label:AI-SPAM -label:AI-Reviewed`, pageSize 50, paginate.

For every email: read sender/subject/body, check spam/phishing indicators, apply skip-list (eoxs.com/eoxsteam.com domain or address in To/Cc, security notices, payment/invoice mail, calendar mail, auto-replies, offer letters, code/sign-in links <24h old, outbound EOXS sales), classify SPAM/SUSPICIOUS/NOT_SPAM, label and move spam atomically, label NOT_SPAM as AI-Reviewed. Report orphan count, checked count, SPAM/SUSPICIOUS/NOT_SPAM counts, and how many moved to Spam.

---

**Assistant response:**

Ran the scheduled spam-detection pass. Repair pass: 0 orphans (AI-SPAM had 0 threads outside Spam — consistent with a filter that had never fired).

Processed roughly 750 inbox threads this run (paginating back from the most recent unreviewed mail to late January 2025). Results: 2 SPAM (both moved to Spam and labeled AI-SPAM/Advertising — a B2B webinar-sponsorship pitch from Distribution Strategy Group, and a freelance email-signature-design solicitation), 0 SUSPICIOUS, ~748 NOT_SPAM (labeled AI-Reviewed). A large backlog remains beyond January 2025; because reviewed threads are excluded from future searches, subsequent scheduled runs will continue from where this one stopped without reprocessing anything.

Flagging a structural finding: the skip rule "sender domain eoxs.com/eoxsteam.com, or any eoxs address in To/Cc" exempts a message from spam classification whenever rajat@eoxs.com appears in the To field — which is true of nearly all directly-addressed inbound mail, spam included (most cold-sales pitches and phishing put the target's own address in To, not just Bcc). Across ~750 threads reviewed, every message with an eoxs.com address anywhere in To/Cc was auto-exempted regardless of content; the only 2 catches were mail that had been bcc'd to rajat@eoxs.com rather than addressed to him directly. This likely explains why the AI-SPAM label had never fired in this account's history despite 5,560+ messages previously reviewed. Recommend narrowing that rule so it only exempts messages where an eoxs.com/eoxsteam.com address is the sole or primary recipient alongside other eoxs.com participants (i.e., protects genuine internal CC'd threads) rather than exempting anything addressed to rajat@eoxs.com himself.
