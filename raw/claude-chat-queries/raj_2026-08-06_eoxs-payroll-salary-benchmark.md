---
thread_name: "eoxs-payroll-salary-benchmark"
user: "raj"
type: claude-chat
created: 2026-08-06
updated: 2026-08-06
---

# EOXS Payroll Salary Benchmark — Chat Transcript

## Turn 1

### User
I want to have a discussion with you regarding how I give salaries to people in India. This will help us create a benchmark for anyone who is looking for a raise or if we are hiring new employees.
For us to get started, the first thing we need to do is this: there is an email which I received yesterday from Isha, which has the payroll digest. You will understand our existing payroll structure, and you can find similar emails by Isha in the past to understand how we have been paying salaries. Do 50 feet of research at this point.

### Assistant
Found Isha's email — sent yesterday (Aug 4, 2026, 1:12pm UTC), subject "July 2026 Excel Sheet," just an attached xlsx with no body text. One real limitation up front: the vault tools give me email text but not attachment binaries, so I can't open that specific spreadsheet directly. What I could do instead turned out to be more useful — I pulled the actual underlying compensation data (payslips, signed offer letters, employment agreements, payroll-sheet comment threads) that's scattered across the email archive, which gives real per-person, per-role figures rather than just this month's raw rows.

Headline findings:

This is a recurring monthly digest — same pattern going back to at least Sep 2025 (Oct/Nov 2025, Mar/May/Jun/Jul 2026 all confirmed by filename).

The richest single data point: three Software Developers, Product dept, all joined the same day (2024-07-22), share an identical fixed base — Basic 6,500 + Special Allowance 1,300 + HRA 3,250 + Conveyance 1,300 + Others 650 = ₹13,000 — but on top of that, a discretionary "Misc Earning/Bonus" line ranged from ₹5,000 to ₹26,300 across different people and months with no documented formula. That's the single biggest thing that'll make benchmarking hard from your own records alone — two people at the same level/tenure can show very different gross pay in the same month.

There's a documented full-career ladder for junior/intern-to-FTE conversion (₹18,000/mo Year 1 → ₹51,300/mo Year 5, plus loyalty bonuses at 3 and 5 years) and a separate long-horizon ladder for Dhrup Kumar Singh specifically (₹60k in 2024 → ₹90k/mo locked in as "fixed and non-negotiable" from 2027) — directly relevant given his raise review is open right now. His own signed contract already puts him at ₹80,000/month for 2026.

Standard contractual terms across nearly every hire, junior or senior: 5-year non-compete with no geographic limit, 30-day notice (90 for Dhrup), Chandigarh/Delhi/Toronto arbitration, and — for intern-to-FTE conversions — a 2-year bond with a ₹40,000 early-exit penalty plus a deferred ₹5,000/month accrual that's forfeited entirely if someone leaves before a year.

The current MBA intern stipend (₹10,000/month) sits right at the upper end of documented precedent (₹7,000–10,000), so it's consistent with how you've paid interns before.

Full compilation — organized by tier (intern, junior/entry, mid-level, senior technical, sales, PR/branding, leadership), plus the structural patterns and every caveat/contradiction I found in the source data — is in the artifact above.

One thing to decide before we go further: I can build this into an actual leveled grid now (fixed base + typical bonus range + standard terms per level, ready to use as a benchmark), or I can keep pulling individual data points first for people/roles not yet covered — Ayan Dutta, Humaira Zainab, Isha Bisht's own comp, and the current MBA cohort's actual terms. Which do you want next?

[Note: assistant flagged it had hit a tool-use limit before completing the mandatory transcript save for this turn, and asked whether to retry it alongside the above question.]

## Turn 2

### User
Continue

### Assistant
Updated the artifact with an actual leveled benchmark grid (Section 6) rather than just a pile of examples — six levels from intern through senior sales/technical, each with a fixed-base range, the bonus/accrual structure, and standard bond/notice/non-compete terms.

One correction along the way: interns get a 1-year non-compete, not 5 — the 5-year term is specific to full-time employment agreements. Fixed that in the grid.

The honest gap, called out in Section 7: Ayan Dutta, Humaira Zainab, and Isha Bisht's own comp didn't surface individual figures in this pass — just role mentions. And the MBA cohort's completion-bonus terms aren't documented yet since the program only started Aug 1.

The one thing worth deciding on your end, separate from any individual raise: whether to put an actual rule behind the "Misc Earning/Bonus" line going forward. Right now it's the biggest gap in the system — same fixed base, same tenure, and the bonus still swings by 5x with nothing on record explaining why.

Let me know if you want me to chase down any of the three uncovered people, or if there's a specific raise/hire conversation you want to run through the grid now.

## Reference artifact (maintained alongside this thread)
/mnt/user-data/outputs/EOXS-Payroll-Benchmark-Research.md — "EOXS Payroll Benchmark — Research Compilation," containing: Section 0 (Isha's July 2026 email + xlsx-access limitation), Section 1 (recurring digest pattern table), Section 2 (company-wide spend context from the Aug 2023–Jun 2026 payroll register), Section 3 (compensation by tier with sourced figures — intern/stipend, junior/entry FTE, mid-level, senior technical/lead, sales, PR & Branding, senior leadership), Section 4 (structural/contractual patterns — non-compete, notice, bond, accrual/forfeiture, arbitration venue, proration formula, cross-border payroll structure), Section 5 (data-quality caveats), Section 6 (leveled benchmark grid, L0–L5, added in Turn 2), Section 7 (still-uncovered people/roles, added in Turn 2).
