---
thread_name: "askcruz-cold-email-mailbox-infra"
user: "Harsimran"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

th# Thread: askcruz-cold-email-mailbox-infra

## User (turn 1)
i want to buy 50 emails for bulk cold emailing , my budget is 50 dollar and i have 50 different domains

## Assistant (turn 1)
Quick reality check before anything else: $50 doesn't cover 50 professionally-provisioned mailboxes anywhere in the current market. The cheapest verified option for exactly 50 mailboxes is $69/month, not $50. At $50 you'd realistically get about 36 mailboxes at the best rate available, not 50.

Bigger issue worth flagging first: your own strategy says EOXS grows through inbound only, and AskCruz is the one meant to push outbound toward $1M ARR. Which product is this cold email infrastructure for? If it's EOXS, this directly contradicts your stated inbound-only approach. If it's AskCruz, cold outbound is a reasonable lever for the ARR target and this is worth doing properly.

One process note, per your own instruction to flag skill mismatches rather than guess: you told me to check raj-eoxs-vault and sales-strategist skill files before acting on a new thread. Neither exists in this environment — only threads-ov and eoxs-data-general are installed. eoxs-data-general covers internal EOXS data (emails, calls, wiki, tickets, CRM) and doesn't apply here since this is external vendor research, not a data lookup. So nothing here matches your setup cleanly.

Here's where the market actually sits for ~50 mailboxes, since you already own the 50 domains (which matters — one of these lets you use your own domains for free instead of paying for provisioning):

[Comparison card rendered — "Realistic mailbox-provider pricing for 50 domains against a $50 budget"]

| Provider | Price | Mailboxes for that price | Per-mailbox cost | Bring your own domain | Warmup | Infrastructure |
|---|---|---|---|---|---|---|
| Winnr (Startup plan) | $69/mo | 50 | $1.38 | Free | $0.60/mailbox/mo add-on | Custom SMTP, shared IP |
| Mailforge | $100-150/mo (raw) | 50 | $2-3 | Not confirmed free | Add-on (~$200/mo total w/ warmup) | Shared-IP SMTP |
| InboxKit (Agency plan) | $164/mo | 30 base + 20 extra | ~$3.25 avg | Not confirmed free | Included | Managed SMTP + monitoring |

Before I recommend one and finalize a plan, I need three things clarified:

[ask_user_input_v0 card rendered with three questions]
1. Which product is this cold email push for? (EOXS / AskCruz / Both / Something else)
2. Is $50 a monthly recurring budget or a one-time spend? (Monthly recurring / One-time only / Flexible starting point)
3. Do you already have a sending platform to plug mailboxes into (Smartlead, Instantly, lemlist, Apollo)? (Yes, already have one / No, need that too / Not sure yet)

## User (turn 2 — answers to clarifying questions)
Q: Which product is this cold email push for?
A: AskCruz

Q: Is $50 a monthly recurring budget or a one-time spend?
A: Monthly recurring

Q: Do you already have a sending platform to plug mailboxes into (Smartlead, Instantly, lemlist, Apollo)?
A: I will connect with my claude

## Assistant (turn 2)
AskCruz makes sense — cold outbound is a legitimate lever toward the $1M ARR target, unlike EOXS which you've committed to inbound-only.

On the numbers: at $50/month recurring, you can't get 50 mailboxes properly warmed — that math doesn't work anywhere in the market. Here's what actually fits:

Winnr Startup (BYOD your 50 domains for free):
- Mailboxes: $1.38 each
- Warmup: $0.60 each (do not skip this — fresh domains without warmup land in spam within days and get burned fast)
- Combined: $1.98/mailbox/month

$50 / $1.98 ≈ 25 mailboxes fully set up and warmed, for about $49.50/month.

That's less than your 50 domains, but it's not actually a bad place to start — 25 SMTP mailboxes at the recommended ~15 sends/day cap each gives you 375 emails/day, which is plenty for an early AskCruz outbound test. Run 25 domains now, keep the other 25 in reserve, and add them once this batch proves out (or once ARR growth justifies the extra ~$50/month).

If you'd rather use all 50 domains from day one: bump the budget to about $99/month ($69 mailboxes + $30 warmup for 50). Against a $1M ARR target, that $49/month difference is not the constraint that matters — reply rate and deliverability are. I'd lean toward doing 25 properly rather than 50 half-warmed, if forced to pick.

One more thing: the save above shows this vault resolves you as "harsimran," not Rajat. Worth checking if that's the intended account for AskCruz outbound work, or if there's a connector mismatch.

On sending: whatever you route this through — your Claude/Gmail setup or something else — it needs to respect the per-mailbox daily send cap and the warmup ramp schedule. That's not optional at this volume; exceeding it is the single fastest way to get a fresh domain flagged. If "connect with my claude" means manual or semi-automated sending through the Gmail connector, that works for testing on a handful of mailboxes, but it has no automatic safety net (no auto-pause on bounce spikes, no enforced daily caps) once you're running 25+ mailboxes at once — worth knowing that gap exists before you're mid-campaign.

## User (turn 3)
just tell me from where we should buy these emails

## Assistant (turn 3)
Winnr (winnr.app), Startup plan.

Reasons: cheapest verified per-mailbox rate ($1.38), it's the only one of the three that lets you bring your own domains for free (you already own the 50, so this matters directly), and it's SMTP with a documented API if you want to automate later.

What to actually buy at $50/month recurring: 25 mailboxes with warmup included, not 50. That's $49.50/month (25 × $1.98, where $1.98 = $1.38 mailbox + $0.60 warmup). Don't buy the mailbox without the warmup add-on — an unwarmed mailbox on a fresh domain gets flagged fast and you'll have wasted the spend.

If you want all 50 domains live instead of 25, the real number is about $99/month, not $50.
