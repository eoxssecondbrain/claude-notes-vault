---
thread_name: "dhrup-raise-review"
user: "raj"
type: claude-chat
created: 2026-08-01
updated: 2026-08-01
---

User: Can you review with Dhrup’s performance. He came to me for a raaise. Give me a 50 feet deep analysis and in a easy digestible format.

Assistant: Verdict upfront: the data doesn't clearly support a raise right now, and there's one live, unresolved signal from your own outreach to him that should be resolved before that conversation, not after.

## Dhrup Kumar Singh — Performance Review (50ft deep)

### 1. Compensation reality check — this matters most

He's on a signed, decade-long salary ladder (Senior Product Developer, EOXS dba Prata Inc, signed 2024):

| Year | Base salary |
|---|---|
| 2024 | INR 60,000/mo |
| 2025 | INR 75,000/mo |
| 2026 | INR 80,000/mo (current) |
| 2027–2034 | INR 90,000/mo — contract states "fixed and non-negotiable" |

Plus: annual incentive bonus INR 90,000/yr (2026–2033), a INR 480,000 five-year bonus (2029), INR 900,000 ten-year bonus (2034). There's also a still-running INR 5,000/mo deduction repaying a INR 110,000 advance through ~early 2027, and a 5-year post-termination non-compete.

This is the most heavily structured individual comp package in the vault. Before you even weigh performance, ask him directly what he's asking for — an off-ladder raise now, or accelerating the 2027 jump (90K) to 2026? The contract calls the ladder "non-negotiable," which was presumably his own leverage point when he signed it, not yours. If you renegotiate this once, it's not "non-negotiable" for anyone else either.

Source: signed employment agreement, `raw/emails/raj_gmail/attachments/192ba175cddf2cf2/updated-employement-agreement-dhrup-kumar-singh.pdf`.

### 2. Hard performance signals — mixed, trending negative on the metric you'd actually cite

Cattr weekly/monthly tracking (his own logged data):

| Period | Worked vs Expected | Productivity % | Note |
|---|---|---|---|
| May 25–31 | 32.9h / 34.0h | 42.7% | |
| Jun 15–21 | 36.6h / 34.0h | 40.3% | |
| Jun 22–28 | 41.0h / 42.5h | 31.0% | |
| Jun 29–Jul 5 | 52.5h / 51.0h | 28.3% | |
| Jul 6–12 | 42.0h / 38.3h | 27.2% | |
| June (monthly) | 169h / 187h (-18h) | 35.9% avg | 87% login late, 1 leave day |

Productivity % is declining week over week even as logged hours hold roughly steady or rise. 87% late logins in June is a real flag, not noise. This is the exact kind of data you just told his whole team (today, July 31) would be weighed in raise conversations — so if you grant a raise now without addressing it, that message loses credibility with everyone else who saw it.

### 3. The open incident that should sit in front of any raise conversation

July 8, 2026 you personally sent Dhrup an ultimatum ("URGENT: DPS Packing List Bug — Your Full Ownership Required"): bug open ~1 year, 100+ tickets from one client, three failed QA builds in the prior month, client had frozen new spend over it, 2-day resolution demand, explicit warning of "a serious conversation about what is going wrong on your end."

Resolution actually landed ~July 15 — a week later, not two days. Whether that's Dhrup missing his deadline or your 2-day framing not surviving real QA process is genuinely unclear from the record — worth asking him directly, not assuming either way.

More live and more relevant: on July 25 you asked him directly for a 6-month team growth plan and a status update on "the speed issue." No reply. You followed up with a bare "??" on July 31 — today. As of this writing that's still unanswered. That's not a historical data point, that's an open loop with him right now, and it's a bigger performance signal than anything from June — he's not responding to a direct, unambiguous ask from you.

I'd resolve that before discussing money. A raise conversation that starts before he's answered your last two messages sends the wrong signal about what gets rewarded here.

### 4. What's genuinely strong

- Authored all three of EOXS's core engineering SOPs in one day (GitLab branching, code review/QA, dev standards) — real, foundational IP, not busywork.
- He's the sole code-review/QA gate before anything reaches Ron J for approval — structurally load-bearing role.
- Trusted with an HR retention call (intern conversion) in 2025 — atypical for a pure IC.
- Long tenure relative to most of the dev team (since 2022 as a Pragtech contractor, direct EOXS employee since ~2024), survived an early rocky patch (unpaid Pragtech salary, phone dispute) without it recurring.

### 5. Bottom line

The case for "yes" is his SOP ownership and structural centrality. The case for "not yet" is: he's already on a rich, signed comp ladder that he agreed was non-negotiable; his own logged productivity is declining; and he's currently non-responsive to two direct asks from you, one sent today. Given you just told his team PM-tracker discipline and responsiveness will factor into raise decisions, granting one now — before he's even answered you — undercuts that standard on day one.

Suggested sequencing: get him to close the loop on your July 25/31 emails first, ask him plainly what he's actually requesting (off-ladder increase vs. contract acceleration), and use the productivity trend as a direct talking point rather than a silent factor.

Sources: Dhrup Kumar Singh entity page; Dhrup Kumar — Weekly Time Tracking (HR analysis branch); signed employment agreement PDF; `2026-07-08` DPS ultimatum thread; `2026-07-25`/`2026-07-31` team-growth request thread; `2026-07-31` company-wide PM-standard email.
