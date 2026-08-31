---
thread_name: "askcruz-cold-call-script"
user: "yashvir"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

User: I want to start making the cold calls for askcruz today and before that I want to build the cold calling script, I want you to consider yourself a Cold calling and Lead Generation expert with over 15 years of experience cold calling and lead generation in the SaaS industry and you follow some really great coaches and have gained a great experience from the sales books as well and both are mentioned below:-
Sales Coaches:-
Jeremy Miner — 7th Level, NEPQ (Neuro-Emotional Persuasion Questioning)

* Grant Cardone — 10X Sales, broad sales training brand
* Jordan Belfort — Straight Line Persuasion
* Cole Gordon — Closers.io, high-ticket closing/remote sales
* Andy Elliott — The Elliott Group, high-energy sales/closing training
* Dan Lok — High Ticket Closer
* Chris Voss — Black Swan Group, negotiation-based selling (Never Split the Difference)
* Brian Tracy — legacy sales training, Psychology of Selling
* Marc Wayshak — Sales Growth Institute
* Victor Antonio — Sales Velocity Academy


Books:-
Predictable Revenue — Aaron Ross & Marylou Tyler. The origin text for outbound SDR/lead-gen engines; built the Salesforce.com outbound model this whole space descends from.
From Impossible to Inevitable — Aaron Ross & Jason Lemkin. Follow-up focused on SaaS growth mechanics and predictable pipeline building.
The Sales Development Playbook — Trish Bertuzzi. Most tactical book specifically on building/running an SDR function — cadences, hiring, comp, metrics.
Fanatical Prospecting — Jeb Blount. Prospecting discipline across channels (call, email, social, referral); good for outbound cadence design.
Gap Selling — Keenan. Diagnostic/discovery-led selling; useful once leads convert to conversations, not just for generation.
The Challenger Sale — Dixon & Adamson. Research-backed framework on what differentiates high performers in complex B2B sales.
SPIN Selling — Neil Rackham. Older but foundational for structuring discovery calls in larger-deal B2B.
New Sales. Simplified. — Mike Weinberg. Blunt, practical new-business development and account planning.
The SaaS Sales Method — Winning by Design. SaaS-specific, maps sales motion to the customer journey stages (land/expand).
Traction — Gabriel Weinberg & Justin Mares. Not a "sales" book per se, but the standard reference for testing lead-gen channels systematically — relevant if the real question is channel selection, not just book learning.

based on this I want to to create a strategy wto build a cold calling script which can help us generate leads for AskCruz.

Assistant: This is a strategy task (rigor) that also produces a deliverable, the script itself (craft) — picking both before I start.

[Asked for rigor level (5ft deep / 10ft deep / 50ft deep / 100ft depth) and craft level (Sketch / Draft / Painting / Commissioned) via interactive selection. Awaiting user's picks.]

User: Q: Rigor level for the cold-calling strategy?
A: 100ft depth — Staged

Q: Craft level for the script itself?
A: Commissioned — full polish

Assistant: Outline for the AskCruz cold-calling strategy — six sections, each a complete unit:

1. Diagnostic — where AskCruz and the pipeline actually stand (grounds everything else)
2. Framework — which coaches/books actually fit this situation, and why the rest don't
3. Call structure — opener through close, mapped to MEDDIC/BANT
4. The script itself — full text: opener, discovery, gatekeeper path, voicemail, close (Commissioned craft)
5. Objection-handling playbook
6. Cadence, tracking, and risks/blind spots

Section 1 — Diagnostic

Product reality
AskCruz has exactly one external client, 3GM, and it's mid-implementation. There is no second client, no retention data, no measured ROI, no case study, no reference customer you can name on a call. This isn't a caveat to soften — it eliminates an entire category of cold-call opener ("companies like yours are already seeing X"). Any script built assuming social proof will get exposed the first time a sharp buyer asks "who else uses this." Source: askcruz-product-market-fit asset, sections 18–19, 23.

ICP is unresolved, not just undocumented
Three different numbers exist for who AskCruz is even for:
- EOXS's general ICP asset: steel/metals distributors, 10–200 employees, North America.
- AskCruz's own canonical positioning doc: industry-agnostic, no employee band at all — ICP defined by "data fragmentation," not vertical or size.
- Your own prior working assumption (in memory): standalone play at 20–60 employees, or an add-on to existing EOXS ERP clients.

Your memory file already flags the ICP as unconfirmed with Rajat and the standalone-vs-add-on question as an open strategic risk. That's still true. The askcruz-sales-strategy skill resolves this operationally for pitch material — steel/metals distributors only, never mention the parent company — and I'll build the script on that, but it's worth naming that this is a GTM choice layered on top of a product that's officially positioned as industry-agnostic, not a resolved fact.

Pipeline as it stands
Active accounts: 3GM Steel (client, not a prospect), Ohio Strip Steel, Collier Metals, Sabre Alloys, and one legal-services prospect (Sarah — outside the steel ICP entirely, which is its own signal about motion discipline). Zero deals closed. Sabre Alloys currently has open elevated support tickets and a credit dispute history sitting alongside active sales conversation — a live account, not a clean slate. There is no AskCruz pipeline tracking in Odoo; every touch lives in email and call transcripts, which means nothing about call volume or outcomes is measurable yet.

What this means for the script
No case studies, no proof, and a product still mid-first-implementation means the script can't be built on authority or social proof. It has to be built on diagnostic curiosity — surfacing a real, specific operational pain the prospect already has, and letting the conversation itself be the evidence, not a claim about other customers. That's the design constraint everything downstream inherits.

Next: which sales frameworks actually fit that constraint, and which of the listed coaches/books get overruled by it.

User: [Uploaded file excerpt_from_previous_claude_message.txt, content: "which sales frameworks actually fit that constraint, and which of the listed coaches/books get overruled by it."]

you tell me?

Assistant: Section 2 — Framework: what fits, what gets overruled

The diagnostic in Section 1 sets one hard constraint: no case studies, no reference customers, a product one implementation deep. Every framework below gets filtered through that.

Adopted, and why

Jeremy Miner, NEPQ — Core spine of the call. NEPQ works by asking diagnostic, curiosity-driven questions that let the prospect surface their own pain, rather than asserting authority or proof you don't have. This is the only framework on the list built to work without social proof. It's also the direct mechanism for MEDDIC's "identify pain" and BANT's "need" — and it matches the skill file's explicit instruction: consultative, not pitch-and-close.

The Challenger Sale, Dixon & Adamson — Second pillar. Since you can't win credibility by naming customers, you win it by teaching the prospect something sharp and specific about their own operation — a Challenger "commercial insight" replaces "trusted by X companies" as the credibility mechanism. This is the answer to "why should I believe you" when the honest answer is "you're one of our first."

Gap Selling, Keenan — Gives the diagnostic questions in NEPQ a destination: establish current state, desired state, and the size and cause of the gap between them. This is what turns "curious questions" into a qualified MEDDIC pain, not just a friendly chat.

SPIN Selling, Rackham — The underlying mechanical skeleton (Situation, Problem, Implication, Need-payoff) that NEPQ and Gap Selling both descend from. Useful mainly as the ordering logic behind the actual question sequence in Section 4.

Chris Voss, Black Swan / Never Split the Difference — Not used for negotiation in the deal-closing sense — there's no deal to negotiate yet. Used narrowly for two things: getting past gatekeepers (calibrated questions, not asking permission), and labeling early resistance in the first ten seconds ("Sounds like this is a bad time"), which lowers defensiveness better than pushing through it.

Mike Weinberg, New Sales. Simplified. — Account-planning discipline. Your pipeline is five named accounts, not a list to spray. Weinberg's blunt, targeted-account approach fits your actual situation better than any high-volume framework — this shapes call prep, not phrasing.

Aaron Ross / Trish Bertuzzi / Jeb Blount (Predictable Revenue, Sales Development Playbook, Fanatical Prospecting) — Not phrasing, process. Cadence, call volume discipline, and the operating rhythm around the calls. Held for Section 6, since your memory already flags that there's no CRM tracking for AskCruz outbound — the process gap is real, not theoretical.

Explicitly overruled, and why

Grant Cardone (10X), Andy Elliott — Built on high-energy, assumptive-close, volume-first pitching. The skill file's own buyer psychology note — US/Canadian steel buyers are commercially sharp and efficiency-focused — is a bad match for hype delivery, and hype invites the exact question you can't answer well yet: "who else is using this." Rejected for tone and close mechanics.

Dan Lok, High Ticket Closer — Built for guru/info-product high-ticket sales with scarcity and status framing. Wrong motion entirely for a B2B SaaS tool being sold into operational buyers on a MEDDIC/BANT process. Rejected outright.

Cole Gordon, Closers.io — Built for high-ticket remote closing off inbound funnels (webinar, DM, application). This is outbound cold calling into a cold ICP — different channel, different motion. Rejected outright.

Jordan Belfort, Straight Line — Partial use only. The tonality and certainty-in-delivery elements are transferable and worth keeping in how the script sounds when read aloud. The assumptive, compressed close is rejected — it presumes a level of proof and momentum you don't have on a discovery-first first call with zero deals closed.

Brian Tracy, Victor Antonio, Marc Wayshak — Generalist sales-training material with no technique here that NEPQ, Gap Selling, and SPIN don't already cover better and more specifically. Including them would just be the "generic sales talk" the skill file explicitly warns against. Skipped.

Traction (Weinberg & Mares) — A channel-testing framework. Your channel is already decided — cold calling, today. Not relevant to this deliverable; would matter if the question were which channel to prioritize.

Next: the call structure itself — opener through close, mapped against MEDDIC/BANT gap by gap.

User: next

Assistant: Section 3 — Call structure, mapped to MEDDIC/BANT

One structural point has to be flagged before the phases: your active pipeline isn't actually cold. Ohio Strip Steel, Collier Metals, and Sabre Alloys already have contact history — Sabre Alloys has an active proposal, support tickets, and a resolved credit dispute in the relationship already. Calling Joe Brom or Tripp Collier with a stranger's cold-open would be a downgrade, not an opener. So the structure below has two entry points: a warm-account variant (skips straight past the pattern-interrupt into a reference to existing context) and a true cold variant (net-new companies off the ICP list you haven't touched yet). Everything after the opener is the same MEDDIC/BANT sequence for both.

Phase-by-phase structure

Phase 1, Opener, first 10 seconds
Warm accounts: reference the specific last touchpoint by name (the proposal, the demo, the open ticket) — never a generic "just checking in," which is banned outright by the skill's email rules and shouldn't survive on calls either.
Cold accounts: pattern interrupt plus immediate self-labeling of the interruption, Voss-style — naming that this is an unannounced call defuses the reflex to say "not interested" before you've said anything.
Goal: earn 20 more seconds. Not pitch. Nothing here touches MEDDIC/BANT yet — this phase exists only to get past the reflexive brush-off.

Phase 2, Reason for the call, 10–20 seconds
State the specific, researched reason you're calling this company, not a category reason. This is where Weinberg's account-specific discipline shows up — a reason that could apply to any steel distributor is a reason that gets hung up on.
Maps to: nothing directly yet, but it's the precondition for Economic Buyer / Authority — you need to know, or confirm, who you're actually speaking to before the diagnostic phase means anything.

Phase 3, Diagnostic questioning, the bulk of the call
This is SPIN's skeleton run through NEPQ's tone and Gap Selling's destination:
Situation — light, framed as "based on what I found," not basic fact-finding (fact-finding reads as unprepared).
Problem — surfaces felt pain. Grounded in the skill file's named industry pain points: quoting delays, inventory blind spots, data silos, MTR compliance burden, scheduling complexity, and so on — the question has to name one of these specifically, not ask "any challenges?"
Implication — Gap Selling's cost-of-inaction question. This is where Metrics (MEDDIC) gets built: what does this pain cost them, in their own words, not yours.
Need-payoff — what solving it would be worth, and who else internally would care. This is a soft, indirect probe at Economic Buyer and Champion — you're not asking "who signs checks," you're asking who else feels this.

Phase 4, Insight, one sharp sentence
The Challenger teach moment. Since there's no case study to lean on, this is a specific, credible observation about the operational problem itself — something that makes the prospect think "they've actually looked at this," not "they're reading a script." This is the substitute for social proof, and it only works if it's true and specific, not a repackaged pain point they already said.

Phase 5, Bridge to AskCruz, brief
Only now does the product get named — tied directly to the exact pain surfaced in Phase 3, never as a generic feature list. Standalone framing, no parent-company mention, per the skill's positioning rule. This is the shortest phase, deliberately.

Phase 6, Close, low-friction ask
Not a hard close — there's nothing to close yet. The ask moves exactly one MEDDIC/BANT gap forward: confirm the economic buyer if it's unclear, or confirm a timeline/trigger, or get 20 minutes on the calendar with the right person. One ask, not a list.

What this call is deliberately not trying to do
Budget and Decision Process/Criteria are explicitly out of scope for a first call. Asking about budget before pain is established is a common failure mode this structure is built to avoid — if a rep jumps there early, that's a sequencing error worth catching in call review, not a personal failing.

Gap-to-phase map

Gap | Framework source | Call phase | First-call goal
Identify Pain (MEDDIC) / Need (BANT) | NEPQ, Gap Selling | Phase 3, Problem | Primary objective
Metrics (MEDDIC) | Gap Selling | Phase 3, Implication | Get a real cost in their words
Economic Buyer (MEDDIC) / Authority (BANT) | — | Phase 2, Phase 6 | Confirm or find out who
Champion (MEDDIC) | NEPQ | Phase 3, Need-payoff | Identify a candidate, don't name it as such
Timeline (BANT) | — | Phase 6 | One direct ask, only if pain is real
Decision Criteria / Process (MEDDIC) | — | Not this call | Explicitly deferred
Budget (BANT) | — | Not this call | Explicitly deferred

Next: the script itself, word for word — cold opener, warm opener, the full discovery question set, gatekeeper path, voicemail, and close.

User: next.

Assistant: Section 4 — The script itself

This is a template with decision branches, not a rigid word-for-word read — Commissioned craft here means every edge case is covered, not that the wording is fixed. The bracketed pain options let you pick the one your pre-call research actually supports; picking the wrong one is worse than picking none, since a wrong guess reads as not having done homework.

COLD OPENER — net-new account, first touch

"Hi [Name], this is Yash — you don't know me, and this is a cold call, so feel free to tell me if now's a bad time. I'll be quick either way."
[pause — let them respond. Naming the interruption defuses the reflex to say "not interested" before you've said anything.]

If they say "go ahead" or "what's this about":
"I've been looking at how [Company] runs [specific researched detail], and I had one specific question. Got 30 seconds?"

WARM OPENER — existing pipeline account (Ohio Strip Steel, Collier Metals, Sabre Alloys)

"Hi [Name], it's Yash from [name the actual last touchpoint — the proposal, the demo, the open ticket]. Got a couple minutes?"
Never "just checking in" or "following up" — both are banned in the skill's email rules, and they're a worse tell on a call than in writing.

GATEKEEPER PATH

"Hi, I'm trying to reach [Name] — is this something you handle, or is [Name] the right person for [specific operational area]?"
Calibrated question, not permission-seeking. "Can I speak to..." invites an easy no; this doesn't.

If pushed for a reason:
"Sure — I had a specific question about how [Company] handles [pain area], and wanted [Name]'s take directly, since it's not really a call I can do justice to secondhand."

REASON FOR THE CALL

"The reason I'm calling — most steel service centers I talk to are dealing with [pick one, matched to research]:
— quotes taking longer than they should because pricing and inventory data live in different systems
— finding out about an inventory problem after a customer's already been promised something
— MTR pulling and matching eating more time than it should on certified orders
— a production change rippling downstream before everyone who needs to know actually knows
I wanted to ask how that shows up for you, if at all."

DISCOVERY — Situation

"Walk me through how [quoting / inventory checks / MTR handling — match to the pain above] works today. Is that info sitting in one place, or scattered across a few systems?"

DISCOVERY — Problem, branch to the pain named above

Quoting delays: "When a customer needs a fast quote, how long does that usually take end to end?"
Inventory blind spots: "How often does someone find out about an inventory issue after a customer's already been promised something?"
Data silos: "If someone needed the full picture on an order — pricing, inventory, MTR, customer history — how many places would they have to check?"
MTR compliance: "How much time goes into pulling and matching mill test reports for orders that need them?"
Scheduling complexity: "When something in production shifts, how far does that ripple before everyone downstream knows about it?"

DISCOVERY — Implication, cost in their own words

"When that happens — [restate their answer] — what does it actually cost you? Time, an annoyed customer, an order that slips?"
"Is that a once-a-month thing, or closer to daily?"

DISCOVERY — Need-payoff

"If that friction just disappeared — if whoever needed that answer could just ask and get it — what would that be worth to you?"
"Besides you, who else feels this the most? Ops, sales, whoever's fielding the customer calls?"

INSIGHT — Challenger teach moment

"Here's what I've noticed talking to distributors like yours — the real cost usually isn't the time spent searching, it's the decisions made on incomplete information because nobody wanted to wait for the full picture. That's usually the bigger number, and it's the one nobody's tracking."
This has to be tailored live to what they actually said in Implication — read verbatim, it stops working.

BRIDGE — first and only mention of the product

"That's actually the exact problem AskCruz is built around — it connects the systems you're already using and lets anyone on your team ask a plain question and get the answer, instead of hunting across four logins. Given what you just described, I think it's worth a real look."
No parent-company mention, standalone framing, per the skill's positioning rule.

CLOSE — pick exactly one ask, whichever MEDDIC/BANT gap is still open

Confirm economic buyer: "Is this something you'd be evaluating yourself, or more of a [owner/GM/ops director]-level call?"
Confirm timeline: "Is this something you're actively looking to fix, or more of a someday problem right now?"
Book time: "I'd like to show you how this would work against what you just described — 20 minutes this week or next?"

VOICEMAIL — 15 seconds, no pitch

"Hi [Name], it's Yash — calling about [specific pain area], not a general check-in. I'll try again, but if you want to save us both the back-and-forth, my number's [number]. Talk soon."

Next: the objection-handling playbook — including the one you'll get most often given the diagnostic: "who else is using this."

User: let's prepare a script around the cold openers, gatekeepers path, and in the reason of calls lets keep it around quotes and inventory problem ?

Assistant: Cold-calling script — narrowed to quotes and inventory

Reason for the call, narrowed to two pain options

"The reason I'm calling — most steel service centers I talk to are dealing with one of two things:
— quotes taking longer than they should because pricing and inventory data live in different systems
— finding out about an inventory problem after a customer's already been promised something
I wanted to ask how that shows up for you, if at all."

Cold opener, net-new account, first touch

"Hi [Name], this is Yash — you don't know me, and this is a cold call, so feel free to tell me if now's a bad time. I'll be quick either way."
[pause]

If they say "go ahead" or "what's this about":
"I've been looking at how [Company] handles quoting and inventory, and I had one specific question. Got 30 seconds?"

Gatekeeper path

"Hi, I'm trying to reach [Name] — is this something you handle, or is [Name] the right person for quoting and inventory?"

If pushed for a reason:
"Sure — I had a specific question about how [Company] handles quoting turnaround and inventory visibility, and wanted [Name]'s take directly, since it's not really a call I can do justice to secondhand."

Discovery, narrowed to match the two pain options

Situation: "Walk me through how quoting works today — is pricing and inventory info sitting in one place, or scattered across a few systems?"

Problem, branch on whichever the prospect leans toward:
Quoting delays: "When a customer needs a fast quote, how long does that usually take end to end?"
Inventory blind spots: "How often does someone find out about an inventory issue after a customer's already been promised something?"

Implication: "When that happens, what does it actually cost you — time, an annoyed customer, an order that slips? Is that a once-a-month thing, or closer to daily?"

Need-payoff: "If that friction just disappeared, what would that be worth to you? Besides you, who else feels it the most — sales, ops, whoever's fielding the customer calls?"

Insight, tailored live to their actual answer

"Here's what I've noticed talking to distributors like yours — the real cost usually isn't the time spent searching, it's the decisions made on incomplete information because nobody wanted to wait for the full picture on pricing or stock. That's usually the bigger number, and it's the one nobody's tracking."

Bridge

"That's actually the exact problem AskCruz is built around — it connects the systems you're already using so anyone on your team can ask a plain question about pricing or inventory and get the answer, instead of hunting across four logins. Given what you just described, I think it's worth a real look."

Close, pick one

Confirm economic buyer: "Is this something you'd be evaluating yourself, or more of a [owner/GM/ops director]-level call?"
Confirm timeline: "Is this something you're actively looking to fix, or more of a someday problem right now?"
Book time: "I'd like to show you how this would work against what you just described — 20 minutes this week or next?"

I dropped MTR compliance and scheduling complexity from the discovery branches too, since a reason-for-call that only names quotes and inventory but then pivots discovery to MTR would contradict itself on the call. Say the word if you want a third branch added back in instead of just narrowing to two.

Still pending: objection handling (Section 5) and cadence/tracking/risks (Section 6). Say "next" when ready.
