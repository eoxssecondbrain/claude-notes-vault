---
thread_name: "3gm-daily-qa-automation"
user: "ron"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

Human: The 3GM implementation that we have started for AskCruz is something which is very important. I talked to Raj before, and he mentioned that we should understand the North American culture on how they actually deal with support and how they deal with their communication. The communication style is different, and in the scene industry it is more reference-based.
We need to keep all the existing customers in EOXS and also the customers that are going to come in AskCruz happy. The only way to do that is, of course, by doing a flawless and good implementation but also providing good support. If you go in Teams.EOXS, you will see that there is a board for customer 2 - 3GM, which has a bunch of tasks in it, and then you will soon have access to Ron's email for ron@askcruz.com, rajat@askcruz.com, and also for ayan@askcruz, and any other email that is in that company.
If you were to set an automation where every single day you were doing a QA on the client's health and seeing what are all the places that we can improve on and how you can actually make it better, how would you go about building that automation? If required, there is a human approval setup in it, but the AI is ensuring that the client is happy throughout the implementation and after as well with good support.

Assistant: Before diving in — two flags, then a rigor check.

First: your preferences call out a "sales-strategist" skill to stack on raj-eoxs-vault for account-strategy queries, but that skill isn't in my current catalog — I only see raj-eoxs-vault, threads-ov, dps-account-strategist, sabre-account-strategist, and client-email-tone-scale. This 3GM question is support/implementation-health design, not sales/GTM/objection handling, so I don't think sales-strategist would've applied here anyway — but flagging since it's referenced in your preferences and missing.

Second: you mentioned I'll soon have access to ron@askcruz.com, rajat@askcruz.com, and ayan@askcruz.com — I don't have that connector yet. Anything below that would touch actual email content (e.g. checking whether a client already voiced a concern) will need that once it's live. I do have Teams.eoxs (the Customer 2 - 3GM board) available now.

This is a strategic design task, not a lookup, so per your standing instruction — pick a rigor level:

5ft deep — quick sketch of the automation architecture and daily QA checklist based on general implementation-health signals and what I already know, no digging.

10ft deep — same, but I actually pull the 3GM board from Teams.eoxs first (task stages, blockers, open comments) so the checks are designed against what's really there, not assumptions.

50ft deep — verified, plus I look at adjacent angles: how DPS/Sabre/Greer implementations historically went sideways, what "healthy" actually looked like for them, the North American support/communication norms Raj flagged, and specifically where human approval gates should sit vs. where the AI can act on its own — with risks and blind spots named.

100ft depth — same as 50ft but delivered section by section (e.g. data sources → daily check logic → escalation/approval design → communication cadence → rollout plan), one section at a time, you say "next" to continue.

Since this is meant to become the template for AskCruz client health generally, not just 3GM, I'd lean 50ft or 100ft — but your call.

Human: 100ft

Assistant: Good — that's enough grounding to build the outline properly. Here's the structure:

1. Data sources & signals — what actually feeds the daily QA (project board reality check included)
2. Daily check logic — what gets evaluated each day and how a "health score" gets derived
3. What "unhealthy" has actually looked like at EOXS clients — grounding the checks in real failure history (3GM's own past, plus DPS/Sabre/Greer patterns)
4. North American / steel-industry communication norms — how that reshapes tone, cadence, and what the AI is allowed to say directly to a client
5. Escalation & human-approval design — where the AI acts alone vs. where it stops and asks
6. Risks, blind spots, and rollout plan — sequencing from 3GM to an AskCruz-wide template

Section 1: Data Sources & Signals

What's live right now, checked directly rather than assumed:

The 3GM implementation board (askcruz Odoo, "Customer 2 - 3GM," project_id 14) has 21 tasks. Of those, 14 have sat untouched in "Intake" since they were created on 2026-08-21 — a full week with zero movement. Only a handful have actually progressed: platform review (Assigned), Outlook email integration (in QA), onboarding email and the Gmail-approval doc (Complete), SOP ingestion (on Hold since 8/24). That's a real, checkable signal today — not a hypothetical one — and it's exactly the kind of thing a daily QA pass should be catching and asking about, rather than something Ron notices three weeks in when Travis asks why nothing's moved.

Sources available to the automation now:
- teams-askcruz (Odoo, read + scoped write) — the implementation task board itself: stage, owner, last-updated timestamp, deadline, description.
- Fireflies/Fathom — call transcripts and summaries, if 3GM calls are being recorded through either.
- OV2 (eoxs-db) — the synthesized history of 3GM as an existing EOXS client: past support tickets, past churn-risk episodes, contact turnover. This is old-system history, not the AskCruz relationship itself, but it's the closest thing to "how has this specific client behaved when unhappy" that exists.

Not yet available: ron@askcruz.com / rajat@askcruz.com / ayan@askcruz.com. This matters more than it might seem — a huge share of "is the client happy" signal in a relationship-based, reference-driven industry lives in email tone and response latency, not in task-board state. Until that connector is live, the daily QA is structurally blind to the actual client-facing conversation and can only watch internal execution. I'd flag that gap explicitly in whatever you show Raj, rather than let the automation look more complete than it is.

One adjacent risk worth naming now: the board itself mixes internal build/infra tasks (MCP whitelisting, server setup, skill files) with client-facing implementation milestones (onboarding email, training materials). A daily QA that just reports "14 of 21 tasks stale" without separating internal plumbing from client-visible commitments will either cry wolf or hide the one that actually matters. Section 2 covers how to split those.

Next: what the automation actually checks every day, and how "stale," "at risk," and "healthy" get defined in a way that's specific enough to act on.

Human: We can go to the next, but before I do that, there is something that I would like to flag, something that we should actually think about. This is more of a brainstorming session. For 3GM, since we are doing a company-wide implementation, there are going to be things which the board is right now maintaining on Teams.askcruz.com. Since it is maintained on an internal board at askcruz, Travis and the team will never have proper visibility on what is actually going on in any one of those tasks. It is, of course, visible to the people that are in askcruz, but it would not be visible to them since they do not have access to the board. There are two ways I can see it:

1. We can actually make access, where we can assign specific people access to specific boards in the project management module so that they are able to see that there.
2. There should be an automatic email that is sent to Travis every single day with the progress that has been made. We will have everyday calls with them, but there should be an everyday email that is sent to Travis, C-Sing, and Rajat if required.

 After implementation, if everything is working smoothly, there should be maybe a weekly call that is set up with Travis. It could be a 15-minute check-in. If he can join, great. If he can't, he can send a text or something that says, "Okay, everything is working fine." They always feel that they are being hurt, right? If, two months down the line, they have stabilised after the weekly calls, then we can move to the monthly calls. A call a month is like a 30-minute call with the client, or a 15-minute call, which is not a lot of time. At the same time, it does give them comfort that yes, there is someone there who is going to be on the call that did the implementation and will be there for them whenever anything is required. With weekly or daily updates, I'm trying to see if there is a way where we can build something on Teams.askcruz itself, where Travis can have visibility on his own board. Maybe we can see if we have a functionality like that already in base Odoo. If we do not have that, then we can build something like this so that we can make a credential for Travis so that he can go. Whenever he only has access to the project management board, he is able to see what is going on with this project. Maybe simpler and much more straightforward. Now, does that make sense to you, like having a credential for Travis and askcruz and giving him access only to that board, or whatever he sees there? Whatever he sees on that board can be defined in settings, where maybe there is a dropdown. It's a many-to-one field which shows all the projects, and then we can select whichever one he is allowed to see.

Assistant: Confirmed a few things worth knowing before deciding between the two options:

Project 14 ("Customer 2 - 3GM") already has privacy_visibility set to "portal" and has an access_token — Odoo's native portal-sharing mechanism is already switched on for this project. So yes, base Odoo does exactly what you're describing: you invite a specific partner as a follower/customer of a specific project (or set them as the project's partner_id), and record rules scope their portal view to only that project — not a new dropdown field you'd need to build, the mechanism already exists at the project level.

That said — nothing is actually set up yet. I checked res_partner for Travis and there's no record for travis@3gmsteel.com in the askcruz database at all (there are unrelated prospect contacts named Travis from other work, but not him), so no portal user, no invite, no partner_id on the project. This would be built from scratch, not flipped on.

Given that, here's the tradeoff as I see it, not just "can it be done":

Portal access — pro: self-serve, no ongoing writing burden on Ron, Travis can look whenever he's anxious rather than waiting for a scheduled touchpoint. Con: what he'd actually see today is the raw internal board — task names like "MCP Whitelisting," "AI interns," fail_state/QA jargon, and a mix of client-visible milestones with pure internal plumbing. Handing a client raw Odoo kanban with internal shorthand is more likely to confuse or alarm Travis than reassure him — it would need a genuinely curated, filtered view (hide internal-only tasks, translate stage names into plain language) before it's safe to expose, which is real scoping work, not just an invite.

Daily/weekly email — pro: this is the one that actually matches what Raj flagged about North American, reference-based support culture. In that world, the relationship is carried by someone actively reaching out, not by a dashboard Travis has to remember to check. A daily note that says "here's what moved, here's what's next, here's who to call" does the reassurance work a passive portal can't — it's proof someone's watching, not just a place he could look. Con: it's writing overhead, unless the daily QA automation (the thing we're already designing) generates the digest as a byproduct — which it should, since the data is the same either way.

My actual read: don't treat these as either/or. Use the daily/weekly email as the primary relationship touchpoint during implementation — it's the one that matches the culture Raj described and it falls straight out of the automation we're building anyway. Treat portal access as a secondary, optional channel you offer once it exists ("and if you ever want to peek in yourself, here's a link") rather than the main mechanism — because right now it isn't safe to expose as-is, and building the curated version is its own separate task, not a quick toggle.

On the cadence step-down (daily during build → weekly 15-min post-launch → monthly after ~2 stable months, with a "just text me thumbs up if the call's not needed" option) — that matches the reference-based-industry read well: the ask isn't for more of Ron's time, it's for a standing, low-friction proof that someone's still accountable. I'd fold that into section 4 when we get there, since it's really the same design question as the email cadence.

Want to keep going on this thread, or should I move to section 2?

Human: yes we can go to Section 2.

Assistant: Section 2: Daily Check Logic

Four layers, from currently-available to future-once-email-lands. Each layer needs its own definition of "stale" or "at risk" — a single global threshold doesn't work across all of them.

Board layer (available today — teams-askcruz)

- Staleness: last write_date exceeding a threshold, but the threshold has to depend on stage, not be one number. A task sitting in "Intake" isn't inherently a problem — right now 14 of 3GM's 21 tasks are there, created in a single batch on 2026-08-21, which reads like normal backlog-seeding at kickoff, not 14 things simultaneously neglected. Staleness only means something once a task has actually started moving and then stalls — e.g. something that sat in "QA" or "Assigned" untouched for several days is a real flag; something still in Intake a week after a bulk seed is not, unless it's blocking a committed date.
- Deadline risk: date_deadline approaching or passed with stage != Complete. Right now none of 3GM's 21 tasks have a date_deadline set at all — worth flagging on its own: an implementation with zero dated commitments makes "are we on track" unanswerable by the board alone. That's a real gap, not just a data-quality nit.
- Blocked state: kanban_state = blocked, surfaced same-day, no threshold needed.
- Ownership gaps: tasks past Intake with no user_id.
- Client-visible vs. internal split: this is a prerequisite, not a nice-to-have. The board currently mixes client-facing milestones (onboarding email, training materials) with pure internal plumbing (MCP whitelisting, server setup, skill files). A daily check that reports "9 of 21 stale" without that split will either alarm Travis over things he was never going to see, or bury the one client-facing item that actually matters. Practically: tag_ids already exists on project_task — use it to mark client-visible vs internal, seeded now by a one-time pass (heuristic keyword match reviewed by Ron once) rather than trusted blindly. This is exactly the kind of classification I'd want a human to eyeball before it drives anything client-facing.

Call/meeting layer (Fireflies/Fathom, once linked to 3GM calls)

- Action items mentioned on a call but never turned into a board task — the single best leading indicator of things falling through cracks.
- The same question or concern surfacing across more than one call — a sign the last answer didn't land, which matters more in a relationship-based culture than it would elsewhere, since it reads as not being heard rather than just a process hiccup.

Communication layer (blocked until the email connector lands)

- Response latency on anything inbound from Travis/Stefan — this is probably the single highest-leverage signal in a reference-based industry, and it's the one layer we can't build yet.
- Any client message that went unanswered in-thread.
- Tone shift — frustration, repeated phrasing, escalation language.

Cross-client pattern layer (OV2, checked weekly not daily — this is background context, not a daily trigger)

- Whether current 3GM signals match known churn patterns already on record: 3GM itself has a documented 2024 churn-risk episode and bugs that recurred rather than stayed resolved; that's the specific failure mode to watch for here, not a generic one. More on this in section 3.

Output, not a score

I'd avoid a single numeric "health score" — it invites false precision and hides the reasoning behind a number Ron then has to unpack anyway. Better: a daily status of Green / Yellow / Red per client, where Yellow or Red always comes with the specific triggering fact attached ("Outlook integration task untouched 4 days in QA stage," not "board activity down 30%"). Green means nothing surfaced; the report can be one line. That internal digest is also the raw material for the client-facing email from our earlier tangent — same data, two audiences.

Next: section 3 — what "unhealthy" has actually looked like at real EOXS clients, so these thresholds are calibrated against real failure patterns rather than guesses.
