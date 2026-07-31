---
thread_name: "collier-metals-call-prep"
user: "raj"
type: claude-chat
created: 2026-07-30
updated: 2026-07-31
---

# Collier Metals Call Prep & Follow-up Review

## Turn 1
User: we have a call with collier metals right now. ayan spoek with them last week. can you pull up all the info about the people we have a call with, the history of our previous call and then we will create a structure for todays call. give me all the info that i need to prep for this call properly. if we know what technology they use etc.

Assistant: [Pulled Collier Metals info from OV2 wiki, CRM, emails. Confirmed call: Collier / EOXS - AI Brainstorming, Thu Jul 30 12PM EST. Attendees: Rob Drum (sales), Tripp Collier (owner, decision-maker, son takes over in October per CRM note). Company: steel service center, 25-30 employees, Atlanta, runs Microsoft Business Central + PS Data for MTR/quality certs. Recently invested in shop-floor scanners tied to Business Central, reluctant to switch off core ERP but open to AI overlay. Leadership AI-forward (3 of 6 execs use AI daily). July 20 demo (Ayan solo) covered MTR AI (22k records, PDF extraction, spec matching, chatbot) and Second Brain/Turing. Positioning used: overlay not replacement, Rolex/Cadillac framing. Reference points: Sabre Alloys, Brannon Steel (closest precedent - MTR overlay on Business Central), Gerdau/AI Joe. Flagged: CRM lead stale since Nov 2025, still assigned to Scott Begin not Ayan. Ayan got Rs10,000 incentive for converting this cold lead into a discovery call. Eastern States Steel/Rick reference unverified.]

## Turn 2
User: ok

Assistant: Acknowledged, offered to build call structure when ready.

## Turn 3
User: [Uploaded Collier_EOXS_AI_Brainstorming.md - full call transcript from the actual call that already happened - and Proposal_Collier_Metals_-_Quote.pdf - pricing proposal]. Also pasted draft follow-up email to Tripp & Rob. Asked for review, what's missing, what to change/remove, and to "build a council" to execute the task.

Assistant: [Read full call transcript in detail via view tool across multiple ranges. Call details: Tripp Collier - second gen owner, dad started business 20 years ago, Tripp took over 3 years ago from construction background, bought it from dad last year, tripling revenue this year, transitioning from toll-only to ~50/50 sales split, running 2 shifts, 9.5 acres, two slitting lines/cut-to-length/edging lines, 95% secondary steel, 2-year-old kid brought to office. On PS Data since 2015, service declining especially after shop floor module rollout. Tripp and Rob personally build AI automations with Claude (slitter tooling setup automation reading emails/work orders, ~10hrs/week saved). Rob asked about auto-importing mechanicals PDFs into PS Data - Raj referenced Brannon Steel MTR solution, Ayan gave live 2-min demo of MTR AI (22k records, spec matching, chatbot). Pricing discussed live: 18 users, range $350-500/user monthly ($6,840 actual in proposal) to $5-7k monthly, implementation $50-70k (proposal: $72,000, 37 days). Raj promised 4-week go-live with $5,000/week penalty for delays - contradicts 37-day (~7-8 week) implementation plan in proposal. Raj promised intro to Ryan/Eastern States Steel as reference - NOT in draft email. Claude integration pricing discussed live: $1,000 one-time per Claude account integration, $100/month pure pass-through per Raj's own words ("we don't make any money out of it"). Agentic/custom AI work priced separately, example: 6-hour deep prompt ~$2,000 compute. Next steps agreed on call: EOXSplore video access (1 week), Google Sheet Q&A doc, intro to Ryan, follow-up call in 2 weeks same time Thursday.

Ran Council mode (GTM strategist, pricing/packaging, RevOps, enterprise sales motion, category positioning, facilitator/critic). Flagged 5 issues:
1. TOP: proposal has zero AI/Claude/MTR pricing despite that being the entire deal driver per call
2. Ryan/Eastern States Steel intro promised on call but missing from draft email
3. 4-week go-live promise (with $5k/week penalty mentioned verbally) contradicts 37-day implementation plan in proposal
4. Payment schedule math doesn't divide cleanly ($20k kickoff + $12k/month against $72k total leaves uneven $4k final month)
5. No explicit next-call date in email despite one being verbally agreed
Also noted: pricing itself doesn't need discounting - Tripp never pushed back on price, precall "cheap buyer" concern proved unfounded. Recommended warmer sign-off than "R." given personal rapport built (kids, family business story).

## Turn 4
User: Clarified: Ryan intro is being done as a separate email (already planned). Shared draft AI/Claude pricing sheet: Claude/AI Integration per User (New User Setup) one-time $3,000; Email Integration one-time $100/GB; Second Brain Maintenance $220/user/month; Historical ERP Data migration in Second Brain one-time $1,800. Asked to go deeper on this pricing structure - what to charge for, one-time vs recurring, what's missing. On point 3 (timeline): clarified Raj quoted 4 weeks early in the call based on an assumption of 8-10 person team, actual is 18 people - suggested clarifying with them it will take 8 weeks (training 18 people takes time). On point 5: call is already on calendar, Tripp accepted invite.

Assistant: Deep dive on AI pricing sheet as pricing/packaging seat:
- Flagged inconsistency: new $3,000/user setup fee is 3x the $1,000 one-time Claude integration fee Raj quoted live on the call - needs bridging explanation or must be revised before Tripp sees both numbers
- $100/month Claude pass-through (Raj's own words: "we don't make any money out of it") isn't visible in the $220/month Second Brain Maintenance line - should be broken out (e.g. $100 pass-through + $120 EOXS maintenance) so the "no markup" claim isn't contradicted
- No ceiling/overage structure for compute-heavy usage - Raj cited a $2,000/6-hour deep prompt as a selling point live on the call; $220/month has no defined boundary for what triggers overage, biggest hole in the sheet
- Custom agent builds (MTR AI took 2 months to build, AP-invoice agent for Monarch, sales-director agent for Houston client) aren't priced anywhere - recommended day-rate/scope-based pricing separate from flat SKUs, likely the real revenue driver for this account given how many specific automations Tripp described wanting
- MTR AI itself (the only module actually demoed live, 10+ minutes) isn't its own line item, buried inside Second Brain - may deserve separate pricing given how central it was to the demo
- Math check: 18 users x $3,000 = $54,000 additional one-time on top of $72,000 base = $126,000 before any agent work or data migration - recommended tiering setup fee by role (Tripp/Rob as power users vs. shop floor/office as lighter tier) rather than flat fee across all 18
- Structural recommendation: mirror GFC/Krinox's platform-fee + per-agent-fee pricing philosophy here rather than trying to make one blended per-user number absorb setup, storage, maintenance, and compute - also keeps pricing philosophy consistent across EOXS and GFC accounts

## Turn 5
User: Asked for a soft line for the email body to address the 4-week to 8-week timeline correction, "something that sounds reasonable." Also asked whether to add the $5,000/week penalty clause to the contract.

Assistant: Provided soft correction line: "One correction from our call — when we talked timeline, I was working off a team of 8-10 for training. With 18 users across office and floor, the realistic go-live window is closer to eight weeks. Wanted to flag that now so the number you're planning around is the right one."

Recommended against adding the $5,000/week penalty clause to the contract, and against repeating it verbally unless prepared to honor it. Reasoning: (1) Tripp reads contracts/details carefully, a liquidated-damages clause invites scrutiny from any advisor he shows it to; (2) already walking back the 4-week number once, attaching a financial penalty to the old number compounds the correction into two retractions instead of one; (3) suggested alternative - frame as a goodwill service credit (e.g. free month of subscription) tied to the corrected 8-week date if go-live slips for reasons within EOXS's control, preserving the confidence signal without the legal/credibility downside.

## Turn 6
User: Asked for two separate emails: one introducing Ryan (Eastern States Steel) and Tripp to each other, and a separate email to Ryan only "giving him the story" - background context relating to Tripp's situation. Asked Claude to analyze how Raj and Ryan actually talk to each other and match that tone/energy.

Assistant: Searched OV2 email history between Raj and Ryan Capinski (Eastern States Steel) to establish authentic tone before drafting. Found: Raj is short/direct with Ryan even when Ryan is high-energy ("LFG baby, I have the vision, I see the potential" got a plain "Sounds good, Ryan. I'll respond shortly" back). Raj's reference-intro pattern is typically just name + phone number, minimal preamble (e.g. Pete Conklin / Joe Brom intros for Ryan in May 2025).

Drafted two emails:
1. Joint intro email (Ryan + Tripp) - short, draws the parallel between their two family-business-succession stories, positions Ryan as the vetted reference who did deep diligence (PS Data, Enmark, Invera) before choosing EOXS, signs "RJ"
2. Solo briefing email to Ryan only - fuller background on Tripp/Collier Metals (family history, revenue tripling, PS Data frustration, in-house AI building, "don't hire into soon-obsolete roles" philosophy, specifically asked for a reference with a similar succession story), positions why Ryan is the right match, signs "RJ"

Recommended sending the solo briefing to Ryan first, then the joint intro a day later so Ryan isn't walking into the group email without more context than Tripp has.
