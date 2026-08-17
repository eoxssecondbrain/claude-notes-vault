---
thread_name: "founder-payout-tracker-automation"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

User: @"/root/.claude/uploads/787bb454-72d9-5e21-bef2-f59701b29ee1/328c81d7-founderpayoutcoworktask.md" [uploaded file: founderpayoutcoworktask.md]

Go through this

[Uploaded file content — Founder Payout Tracker Cowork Task Spec — full text:]
# Founder Payout Tracker — Cowork Task Spec

## Purpose
Track Ron's and Sheenam's weekly founder-hours commitment against their agreed payout ceilings, and send a daily status email to Raj, Ron, and Sheenam showing both running totals.

Founder agreement (per Raj):
- First rights order: Sheenam first $5,000,000, then Ron next $10,000,000, then Raj.
- Base salary covers 40 hrs/week (zero founder credit).
- The payout is priced against an additional 20 hrs/week founder commitment (60 hrs/week total).
- 5-year term = 260 weeks. Each person's total commitment is split evenly across all 260 weeks — that week's allowance.
- A week worked at the full 60 hrs earns that week's full allowance. Fewer hours earns a proportional share; the unearned portion is lost permanently, not averaged out or recoverable later.

## File
`founder_payout_tracker.xlsx` — four tabs: `Legend`, `Config`, `Ron Tracker`, `Sheenam Tracker`.

## Structure (for reference — do not rebuild, use the existing file)

### Config tab
| Row | Field | Ron (col B) | Sheenam (col C) |
|---|---|---|---|
| Term start date | editable | editable |
| Base hours/week | 40 | 40 |
| Founder premium target/week | 20 | 20 |
| Total commitment ($) | 10,000,000 | 5,000,000 |
| Term length (weeks) | 260 | 260 |
| Weekly allowance (auto) | =Total/260 → $38,461.54 | =Total/260 → $19,230.77 |

### Ron Tracker / Sheenam Tracker tabs (one row per week)
| Column | Content |
|---|---|
| A | Week # |
| B | Week ending date |
| C | Hours logged (Cattr) — INPUT cell, this is the only cell to fill in |
| D | Weekly credit = MAX(0, MIN(hours − 40, 20)) |
| E | Weekly allowance (pulled from Config) |
| F | Weekly earned = allowance × (credit / 20) |
| G | Weekly lost = allowance − earned |
| H | Running total earned = cumulative sum of column F to date |
| I | Pre-built email line for that week |

Formulas are already in place through week 60 on both tabs. If the term runs past week 60, select the last filled row and fill formulas down for the next block of weeks.

## Weekly data-entry procedure (run every Monday)
1. Pull Ron's and Sheenam's actual hours worked for the prior week (Mon–Sun) from Cattr.
2. Open `founder_payout_tracker.xlsx`.
3. On `Ron Tracker`, enter Ron's hours in column C of the next unfilled week row.
4. On `Sheenam Tracker`, enter Sheenam's hours in column C of the next unfilled week row.
5. Save the file. Columns D–I recalculate automatically.
6. If Cattr data looks obviously wrong (e.g. missing days, a number far outside their normal range), flag it to Raj instead of entering it — do not guess or estimate a number.

## Daily email automation (run every day)
Send one email, once per day, to all three recipients together: Raj, Ron, Sheenam.

Content is always the most recent completed week's numbers for both people — on days without a new weekly entry, the email repeats the same numbers as the day before. That is expected, not an error; the underlying number only changes on the Monday data-entry day.

**Recipients:** Raj, Ron, Sheenam (same email, same content, sent to all three — this is an intentional shared-visibility decision Raj has made; both co-founders see both numbers.)

**Subject line:**
`Founder Payout Status — Week [N] — [Week Ending Date]`

**Body:**
```
Ron
[Email Line from Ron Tracker, column I, most recent filled row]

Sheenam
[Email Line from Sheenam Tracker, column I, most recent filled row]
```

Example:
```
Ron
Week 2 (week ending Aug 30, 2026): 50 hrs logged. Credit: 10 of 20 hrs. This week: earned $19,231, lost $19,231. Running total: $57,692

Sheenam
Week 2 (week ending Aug 30, 2026): 60 hrs logged. Credit: 20 of 20 hrs. This week: earned $19,231, lost $0. Running total: $47,692
```

## Approval gate (recommended, not yet confirmed with Raj)
Given these numbers are real compensation figures shared between two co-founders, draft the daily email and hold it for Raj's approval before the first send each week (i.e. approval required the day a new weekly number is entered; the repeat-sends on other days of that week can go automatically since the content is unchanged). Raj can turn off the approval step later once the pipeline is proven reliable.

## Open items to confirm with Raj before this runs unattended
1. Exact term start date for each person (Config tab currently defaults to today's date).
2. Whether this applies retroactively to existing Cattr history or starts fresh from signing.
3. Whether Ron and Sheenam each review and sign the underlying agreement before the tracker starts affecting real numbers they see.
4. Whether Raj's own tranche (after Sheenam's $5M and Ron's $10M) follows the same hours-based mechanism, given he also carries a full-time EOXS role.
5. Cattr data-quality check — confirm hours pulled are trustworthy before they're entered as final, not estimated.

Assistant: This spec doesn't cleanly match a specific skill beyond the standard vault check — it's not a sales/GTM question (no sales-strategist trigger) and it's not an EOXS data lookup (no eoxs-db/eoxs-teams query needed, since it's a review of a document you uploaded, not a request for existing records). Flagging per your rule, then proceeding with the review since it's unambiguous what "go through this" means here.

Note first: only the spec markdown was uploaded — `founder_payout_tracker.xlsx` itself isn't in this session, so I can't verify the actual formulas/tabs, only the spec's description of them.

Math check on what's described: Ron $10,000,000 / 260 = $38,461.54/week — correct. Sheenam $5,000,000 / 260 = $19,230.77/week — correct. Weekly credit formula MAX(0, MIN(hours−40, 20)) correctly caps credit between 0 and 20 hours regardless of how much overtime is logged. Earned = allowance × (credit/20) and lost = allowance − earned are internally consistent with "unearned is lost permanently."

One real logic conflict, not just a nitpick: the "first rights order" language ("Sheenam first $5M, then Ron next $10M, then Raj") reads as a sequential waterfall — Sheenam's tranche fills before Ron's starts. But the tracker structure described has both of them earning independently, in parallel, from week 1, each against their own fixed weekly allowance. Those are two different models. If "first rights order" is really about payout priority in case the company can't fund both trances in full (a waterfall for cash-constrained months), that's compatible with parallel accrual. If it means Ron shouldn't start earning until Sheenam's $5M is fully earned out, the current tracker design doesn't do that at all. This needs a definitive answer from Raj before real numbers start accruing — it changes what "Running total earned" is supposed to represent for Ron in the early weeks.

Raj's own tranche isn't tracked anywhere in the file (only Ron/Sheenam tabs exist), and open item 4 already flags this. Worth being blunt: if Raj also carries a full-time EOXS role like Ron and Sheenam, and the same hours-based logic is meant to apply to him, there's no mechanism built for it yet. If it's not meant to apply the same way, that's fine, but it should be stated rather than left implicit.

The five open items listed at the bottom (term start dates, retroactivity, whether Ron/Sheenam have signed the underlying agreement, Raj's own tranche mechanism, Cattr data-quality trust) are all correctly identified as blockers. None of them are things I can resolve — they're Raj-only decisions, and two of them (signing the agreement, retroactivity) affect whether real dollar figures should even start appearing in a shared email at all. Running this before those are settled risks Ron and Sheenam seeing "official" running-total numbers for an agreement they haven't necessarily signed off on yet.

The approval gate is the right call and matches your stated pattern elsewhere: hold the first send of a new number for your sign-off, auto-repeat unchanged numbers on other days. I'd keep that on indefinitely rather than planning to turn it off once "proven reliable" — these are real comp figures shared between co-founders, and a silent wrong number (bad Cattr pull, a broken formula reference) auto-sent to both of them is a harder problem to walk back than a day's delay on your approval.

[AskUserQuestion tool call — two questions:
1. "What do you want done with this spec right now?" — options: Review only (done above) / Start building the automation / Resolve open items first
2. "On the 'first rights order' ambiguity — is Sheenam's $5M and Ron's $10M meant to accrue in parallel (both earning every week from week 1, as the tracker currently does) or sequentially (Ron doesn't start earning until Sheenam's $5M is fully earned out)?" — options: Parallel accrual (as built) / Sequential waterfall]

User answers: "What do you want done with this spec right now?"="Start building the automation", "On the 'first rights order' ambiguity..."="Parallel accrual (as built)"

Assistant: [checked SearchMcpRegistry for Cattr connector — none found; checked ListAgents for device bridge — none reachable]

No Cattr connector is available in this org's registry, and no desktop device bridge is connected right now — so full automation (auto-pulling hours from Cattr) isn't buildable as a hands-off pipeline today. Realistically, the "automation" that's actually buildable is: a scheduled task that reads the xlsx, drafts the daily email in Gmail, and holds first-of-week sends for your approval — while hours entry stays a manual step (you paste in Ron's and Sheenam's numbers from Cattr each Monday, since nothing here can log into Cattr on its own).

That still needs the actual `founder_payout_tracker.xlsx` file, which wasn't part of this upload — only the spec was. And building it for real touches the open items the spec itself flags as blockers.

[AskUserQuestion tool call — four questions:
1. "Where is founder_payout_tracker.xlsx? I need the actual file to wire the automation to." — options: I'll upload it / Build it fresh
2. "Term start date and retroactivity (open items 1-2 in the spec) — how should the 260-week clock start?" — options: Fresh start, today / Fresh start, specific date / Retroactive to a past date
3. "Weekly hours entry (open item 5, and the Cattr-access gap) — since there's no Cattr connector here, how should hours actually get into the tracker each Monday?" — options: You paste hours in, I enter them / Connect a Cattr integration first
4. "Has the underlying founder agreement (the hours-for-equity/payout terms) actually been signed by Ron and Sheenam yet? (open item 3)" — options: Yes, signed / Not yet signed]

User answers: "Where is founder_payout_tracker.xlsx?..."="Attached in the next prompt", "Term start date and retroactivity..."="Fresh start, today", "Weekly hours entry..."="I get an email every monday morning with weekly hours with everyone on the team. You can pick it up from there.", "Has the underlying founder agreement...been signed...yet?"="Not yet signed"

Assistant: [checked ToolSearch for Gmail search/read tools — none found beyond write/action tools: create_draft, update_draft, send_message, reply, forward, label_message, label_thread, mark/unmark spam, trash/untrash, apply_sensitive_label, create/delete/update_label. No search_threads, get_thread, get_message, or list_labels tool actually available despite being referenced in other tools' descriptions.]

Status before the xlsx arrives:

Confirmed: term start is today (week 1 = week ending Sun Aug 23, 2026), hours will come from your existing Monday all-team hours email rather than a live Cattr connector, and the pipeline stays paused — no sends to Ron or Sheenam — until you confirm the agreement is signed.

One more real constraint worth flagging before I build on it: the Gmail connector available in this session only has write/action tools (send, draft, reply, forward, label) — no search or read tool. That means I can't autonomously find and parse your Monday hours email myself; I'd need you to either forward/paste that email's content into this conversation each Monday, or a read-capable Gmail connector would need to be enabled. Worth deciding now since it changes what "automated" means here — right now the realistic version is: you paste hours in (or forward the email), I update the xlsx and prep the draft, you approve, I send.

Waiting on the xlsx file to actually build against. Once it's attached I'll set up the weekly update + daily email logic against the real tabs and formulas, keep everything in draft/preview mode (no auto-send) since the agreement isn't signed yet, and come back with what that looks like before anything goes live.
