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
