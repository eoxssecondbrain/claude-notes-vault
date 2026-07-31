---
thread_name: "sales-numbers-3yr-analysis"
user: "raj"
type: claude-chat
created: 2026-07-31
updated: 2026-07-31
---

User: do an analysis on my sales numbers. for the last 3 years.

Assistant: [called ask_user_input_v0 with two clarifying questions]
Q1: What should 'sales numbers' mean here — invoiced/collected revenue, new deals closed, or both? Options: Invoiced/collected revenue | New deals/clients closed | Both revenue and deal count
Q2: How deep should this analysis go? Options: 5ft — Quick: fastest read from invoice summaries | 10ft — Verified: cross-checked against raw invoices/CRM records | 50ft — Deep: verified + trend drivers, risks, blind spots

User: Q: What should 'sales numbers' mean here — invoiced/collected revenue, new deals closed, or both?
A: Both revenue and deal count

Q: How deep should this analysis go?
A: 50ft — Deep: verified + trend drivers, risks, blind spots

Assistant: Trailing-12-month invoiced revenue is $391,288 across 71 invoices — call that today's number. Here's the full breakdown.

## Revenue by year (invoiced, USD, excl. tax)

| Year | Invoices | Revenue | YoY |
|---|---|---|---|
| 2023 | 6 | $80,511 | — |
| 2024 | 24 | $265,640 | +230% |
| 2025 | 61 | $374,750 | +41% |
| 2026 YTD (Jan–Jul) | 49 | $267,926 gross / $240,702 net of $27,224 in credit notes | on pace to roughly flat-to-down vs 2025 if the pace holds |

2026 monthly revenue is choppy: Jan $74.5K (Brannon onboarding invoices hit all at once), Feb $20K, Mar $45K, Apr $7.3K, May $54K, Jun $37.7K, Jul $29K. No clean upward trend within the year — it's lumpy, driven by whichever client gets invoiced that month, not a steady subscription ramp.

Trailing 12 months (Aug 2025–Jul 2026): $391,288. Against the $1M ARR goal, that's ~39%, and it's not accelerating — TTM is barely above calendar-2025's $374,750.

## Deal count — verified against invoices, not CRM

I checked crm_lead's "won" stage first, per the sales-strategist playbook, but it's unusable: it shows only 1 won deal in 2024, 3 in 2025, 1 in 2026 YTD — nowhere near what the invoice ledger shows. This matches the existing note that CRM stage data isn't reliable. So the numbers below are built from first-invoice date per client, which is ground truth (revenue-backed).

| Year | New paying clients (first invoice) | Who |
|---|---|---|
| 2023 | 1 | Morgan Hauser Steel (churned after 1 invoice) |
| 2024 | 2 | Sabre Alloys, Greer Steel |
| 2025 | 6 | R W Conklin, Bri-Steel, Hansen Metallurgical, Discount Pipe & Steel, Eastern Steel Sales, PPC Speciality Metals |
| 2026 YTD | 1 | Brannon Steel |

2025 was the real logo-acquisition year, not 2026. 2026 has added exactly one new logo in seven months against six the year before — new-client velocity has slowed sharply even though total revenue held up, because existing accounts (Sabre, 3GM, Discount, Eastern) kept ordering.

Note: your memory has "six clients closed to date" — that's stale. The ledger shows 15 distinct companies invoiced since 2020, 8 of them active in 2026.

## Concentration and dormancy risk

- Sabre Alloys and 3GM Steel are the only two clients with revenue in every one of the last 3 years. Sabre alone is $375K lifetime, the single largest account.
- R W Conklin Steel and Bri-Steel Manufacturing — both 2025 logos — haven't invoiced since March/July 2025. That's 12+ months dormant. Worth confirming whether they're churned, paused, or just under-billed, because right now they're silently not counted as losses anywhere.

## Collections — this is the flag worth your attention

2023–2025: 100% of posted invoices paid, zero residual. Clean collection history.

2026: $90,063 outstanding across 13 unpaid invoices. Almost all of it is one client:

Brannon Steel has never paid a single invoice — all 8 invoices since Jan 7, 2026 are unpaid, $55,239 outstanding, oldest now ~7 months overdue. That's 100% of Brannon's booked 2026 revenue sitting as uncollected AR, not cash. The wiki shows active engagement (UAT calls through June, real usage) so this doesn't look like a dead account — more likely a billing/reconciliation gap (there's a note from Manish Trivedi in April asking about confirmation on the March invoice). But as booked, $52,860 of 2026's reported revenue is receivable, not collected — your real cash-basis 2026 number is closer to $215K than $268K.

The rest of the $90K (3GM, Sabre, Greer, Eastern, PPC — one invoice each, all due late July) is just normal end-of-month AR, not a concern yet.

## Bottom line against the $1M ARR filter

TTM revenue $391K is ~39% of the 12-month goal, growth has stalled since 2025, new-logo velocity dropped from 6/year to 1 in the current year, and a fifth of 2026's revenue is uncollected from one client. The lever that actually moved the needle historically was net-new logos (2025), not expansion of existing accounts — and that lever is close to idle right now.

Sources: EOXS Teams Live (account_move, crm_lead, crm_stage), OV2 wiki (Brannon Steel entity and related pages) for the AR context check.
