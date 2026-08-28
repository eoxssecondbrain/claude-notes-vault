---
thread_name: "sabre-alloys-toll-processing-laser-entity"
user: "raj"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: Tye from Sabre Alloys called me today and he said that they are starting a new company where they are buying a Laser Machine and they will be doing toll processing for other customers. This is a comparatively smaller business which he wants us to set up separately and still have access to all the users. And he was saying that he doesn't want to pay another $10,000 a month to setting up this because this is a much smaller business and it won't make sense for them however, point to note is that they will be doing processing in this business so they know that they need our system and they can't now have a separate system for it.   he even said he will bring dave. 

I was thinking of creating a new instance, just simply copy pasting savers code to that new instance and setting it up and creating all the new IDs for everyone in their team, or just create a new company in Sabre instance itself.

Assistant: Quick flag before I dig in: you're already halfway to solving Tye's pricing objection with an architecture decision, before he's even formally asked for a discount. "They know they need our system and can't have a separate system" is your leverage — it's not a reason to make the setup easier or cheaper for them preemptively. Keep those two decisions (technical architecture vs. commercial terms) separate or you'll give away margin for free.

On the two options you named: a full new instance with copy-pasted code is the wrong default — it doubles your hosting/maintenance burden and undercuts the "one platform" story you're selling. A new company within the existing Sabre Odoo instance (multi-company) is the standard way to handle "same users, separate books/entity" — but I don't know yet if that's actually sufficient for what they need (separate data isolation for a toll-processing customer base that isn't Sabre's own customers, separate invoicing, etc.), and I don't have Sabre's current contract terms, seat count, or what that $10K/month figure actually represents.

Before I go further — pick a depth:

5ft — quick take using what's in the CRM/contract summary as-is
10ft — verified against actual Sabre contract/invoice records and prior similar setups (if any)
50ft — full investigation: pricing precedent across other multi-entity clients, technical implications of shared users across companies, and a recommended negotiating position with Tye

Which one, and do you know yet whether this new entity will have its own EIN/legal structure, or is it just a new business line under Sabre proper?

User: 50 - even spend some time in understanding where our present relationship stands based on our email exchange and firefly calls with Tye and Dave.

Assistant: Where things actually stand, and what I'd do — in order.

1. Relationship reality check (not just the friendly banter)

The Aug 13 call with Tye and Michael was warm on the surface — jokes, "we're together 30 years," genuine rapport. But underneath that:

- Feb 2026 server outage took the whole Sabre instance down, lost ~3 weeks of transaction data, triggered a formal settlement (June 2026) that included a $51,276.98 hard-cash-loss claim (SO18263) and a $1,000/month settlement credit still running on invoices as of the latest data pulled.
- Documentary evidence since found (Sabre's own processing order + the customer's pre-crash email) actually undermines Tye's account of that SO18263 dispute — meaning if it resurfaces, EOXS is holding the stronger position, not Sabre. Don't reopen it, but know it's live ammunition if things get adversarial.
- Right now, this week: a daily inventory valuation report failed again yesterday (Aug 27–28) with $19K–$269K in flagged variances, plus four separate "Blanking Processing Order Error" tickets and a "Cannot Confirm PL" error, all in August. GP calculation has been a manual workaround since September 2025 — over a year.
- Most relevant to this specific ask: Tye already had a documented dispute with EOXS about Toll Processing — his explicit rule that a standalone toll-processing line should never post to inventory. The wiki record flags that fix as unverified — support may have manually removed the bad tags rather than fixing it at the system level. You're about to build a whole external-facing business on top of the exact feature that's already had a design dispute and an unconfirmed fix.

Bottom line: the relationship is intact, but you're pitching a platform expansion into a stretch of genuinely rocky reliability, on the one feature that already has an open question mark.

2. Who's "Dave"

Almost certainly David Underwood — Sabre's investor/advisor, not staff. He was central to the Feb 2026 outage response and is on record with the sharpest reporting-reliability criticism EOXS has gotten from this account. Tye looping him in means this isn't going to a operations gut-check, it's going to the person who audits your numbers hardest. Same discipline you'd want anywhere else applies double here — don't let a soft user-count or a rounded pricing figure go out. That's exactly the kind of thing Underwood catches.

3. Where "$10,000/month" actually comes from

Not made up. Current Sabre billing: $425/user/month × 27–28 users + $1,200/month server fee ≈ $12,675/month gross, net ≈ $11,675 after the settlement credit. Tye is pricing the new business the way he already knows EOXS charges, because that's his lived experience. His objection is rational, not a lowball — he's assuming a second instance replicates Sabre's own cost structure. That also confirms this has nothing to do with the AskCruz/Company Brain proposal you pitched Aug 13 ($34K setup + $4K/month for 15 users) — that's a separate product line and separate ask. Don't let those two get conflated in the room.

4. The actual architecture call

Multi-company within the existing Sabre Odoo instance is correct — not a new instance, not copy-pasted code. Reasons:
- The 27–28 users are already licensed and paying $425/user/month. A new instance means re-licensing them, which is exactly the cost Tye is objecting to and has no technical justification — same people, same logins.
- A second instance means a second server, second maintenance surface, second everything to keep in sync — direct tax on your own margin and support load, for a business a fraction of Sabre's size.
- I checked for internal precedent: EOXS has never actually built a multi-company setup before. One prospect (Triple-S Steel, 2023) raised it and never converted. So this is real, first-time engineering work — not a config toggle.

What the build actually requires: a new company record with its own chart of accounts and invoicing, inventory/data segregation so toll customers' material doesn't mix with Sabre's own book, and — critically — extending the Toll Processing SO-line logic (the thing already in dispute) to handle third-party-owned material at production scale, not just Sabre's internal test case. Laser cutting itself is already a supported processing type in the EOXS feature set, so that part isn't new.

5. Commercial structure I'd bring to Tye

Don't discount to solve his objection and don't hand him a duplicate subscription either — both are wrong. Structure it as: no new monthly user-license fees, since no new seats are being added. A scoped one-time implementation fee for the multi-company build (real work — I'd price it closer to a mid-size onboarding, not free), and a modest incremental monthly fee tied to the new company's server/support overhead — not a second $10–12K/month subscription. That answers his stated objection with facts about what he's actually paying for, rather than a concession. It also happens to be true, which matters with Underwood in the room.

One open question I don't have an answer to yet: is this a genuinely separate legal entity (own EIN) or a DBA/division under Sabre? That changes whether this is a clean Odoo "company" record or something that also needs its own tax/reporting boundary. Worth asking before you quote anything.

I'd also fix or get firm confirmation on the Toll Processing posting bug and the current valuation-report failures before this goes live for a new revenue line — selling expansion on top of an admitted open defect, to the account's harshest critic, is the wrong sequencing.
