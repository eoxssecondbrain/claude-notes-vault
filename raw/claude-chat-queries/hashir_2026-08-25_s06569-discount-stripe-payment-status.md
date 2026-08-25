---
thread_name: "s06569-discount-stripe-payment-status"
user: "hashir"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

User: Can you provide me more information on S06569 ON DISCOUNT LIVE  and tell me about there stripe payment information that whether the payment has been made with this sales order or not what is status and the history for the paYMENT on this one.

Assistant: Now I have the full picture. Summary:

**Sales Order S06569 — Discount (Discount Pipe & Steel, Odoo 13)**

| Field | Value |
|---|---|
| Customer | Divine Lighting |
| State | Confirmed (sale) |
| Order date | Aug 24, 2026 |
| Amount total | $6,541.56 (no tax) |
| Invoice status | No invoice generated yet |

**Payment status: NOT paid.**

There is one Stripe payment attempt tied to this order, not a completed payment:

| Field | Value |
|---|---|
| Reference | S06569-1-1-1 |
| Amount | $6,541.56 (matches full order) |
| Stripe payment intent | pi_3U7zXXKla669mNZE0XZwEivT |
| Transaction state | draft |
| Processed | No |
| Created | Aug 24, 2026, 15:11:58 |
| Last updated | Aug 24, 2026, 15:11:58 (never changed) |

Payment history: only this single record exists — no retries, no state transitions after creation, no acquirer reference back from Stripe, no entries in stripe_payment_details or stripe_payment_operation for this order. That means the payment intent was created (checkout initiated) but Stripe never confirmed/captured it — the customer likely didn't complete checkout, or the webhook confirming success never landed.

No invoice (account_move) exists yet for this order either, consistent with invoice_status = "no".

Source: DPS LIVE (Discount Odoo, live). Not found in eoxs-db (correspondence) — didn't check emails/calls since the structured payment record already answers this fully; can search correspondence for Divine Lighting if you want context on why checkout wasn't completed.

User: We need to see why this payment is not processed because for other sale orders the stripe payment is working fine.

Assistant: This is a diagnostic/comparative analysis task, not a simple lookup — pick a rigor level before I dig in:

- **5ft (Quick):** Pull a handful of successfully-processed Stripe transactions from the same DB and compare their state/timestamps/pattern against S06569's record to spot the obvious difference.
- **10ft (Verified):** Same as above, but verify against actual account_move/payment records tied to those successful orders (not just payment_transaction summary fields) to confirm they truly completed, and cross-check timing patterns.
- **50ft (Deep):** Full investigation — compare against multiple successful orders, check for patterns (specific customer, specific time window, acquirer config changes, webhook delivery gaps), check correspondence (emails/calls) with Divine Lighting for any hints (failed card, abandoned checkout), and flag anything structurally different about this transaction.

Which level?

User: 50ft

Assistant: Here's the finding:

**This is not a system malfunction — it's a normal abandoned/incomplete checkout, not a broken Stripe integration.**

What actually differs between S06569 and a working payment:

| | S06569 (stuck) | S06600 (normal, same day) |
|---|---|---|
| Transaction state | draft | done |
| `date` (payment confirmed) | null | 2026-08-24 16:35:59 |
| `acquirer_reference` (Stripe charge ID) | null | ch_3U80ptKla669... |
| `is_processed` | false | true |
| `write_date` vs `create_date` | identical — never updated | +1 min — updated on confirmation |

A "draft" `payment_transaction` record is created the moment the Stripe checkout **form loads** — before the customer submits payment. It only advances to `done` when Stripe fires a `payment_intent.succeeded` webhook back to Odoo. For S06569, that second half never happened: no webhook event, no charge ID, no 3DS confirmation data, `write_date` frozen at the exact moment of creation.

Ruled out as causes:
- **Webhook config isn't broken system-wide** — the webhook endpoint (`/payment_status`) is registered and correctly subscribed to `payment_intent.succeeded` and related events, and it clearly worked for other orders that same day and hour.
- **Not a Divine Lighting-specific config issue** — this is their only transaction on record, so there's no prior successful payment to compare against, but nothing else on their record looks broken.
- **Not actually anomalous system-wide** — draft/abandoned transactions are routine: August has 21 done vs 11 draft (~31% never complete), consistent with prior months (Jan–Jul range roughly 10–30% draft rate). "Other orders work fine" is true, but a chunk of orders every month also never complete online payment — this one just happens to be one of them.
- **No error state** — it didn't fail (state=error would mean Stripe rejected it); it simply never got resubmitted/confirmed.

Most likely explanation: the customer opened the payment form and then either abandoned it, paid via another method (check/wire) which is why the sale order still shows confirmed (`state=sale`) despite no payment, or hit a client-side issue (browser closed, 3DS step not completed) before Stripe ever confirmed the charge. No email/call correspondence in EOXS's own records mentions this order or a broader Stripe outage on Discount's side.

One caveat: I can't see Stripe's own dashboard/logs from here — only what Odoo recorded. If you want to fully rule out webhook delivery failure (as opposed to customer non-completion), that requires checking Stripe's event log for `pi_3U7zXXKla669mNZE0XZwEivT` directly, which isn't accessible from this connector.
