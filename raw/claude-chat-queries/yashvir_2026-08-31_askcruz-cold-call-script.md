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

Assistant: Section 3 — Call structure: opener through close, mapped to MEDDIC/BANT

The call has one job on a cold first touch: surface a real MEDDIC pain and advance one BANT gap. Not close, not demo, not pitch. That constrains the whole structure.

Stage-by-stage skeleton

Stage 1 — Pattern interrupt (0–10 seconds)
Purpose: survive the first ten seconds without triggering a hangup reflex. No "how are you today," no company-name-drop pitch. Voss-style labeling used pre-emptively — naming the awkwardness of a cold call defuses it faster than powering through it.
Gap addressed: none yet — this stage exists to earn Stage 2.
Success criteria: prospect responds instead of hanging up or auto-deflecting to "not interested."

Stage 2 — Reason-for-call framing (10–25 seconds)
Purpose: give a specific, plausible reason for the call tied to an operational reality of steel/metals distribution — not a generic "quick call to introduce ourselves." This is where the Challenger teaching instinct starts: lead with an observation about their world, not your product.
Gap addressed: sets up Identify pain (MEDDIC) without asking a pain question yet.
Success criteria: prospect doesn't shut it down in the first sentence; you get permission to ask one question.

Stage 3 — Diagnostic questioning (25 seconds–3 minutes)
Purpose: the core of the call. SPIN/Gap Selling ordering — Situation question first (low-friction, easy to answer), then Problem question (surfaces friction), then Implication question (makes the cost of the friction explicit in their own words), then Need-payoff (lets them state why fixing it matters — you don't state it for them). NEPQ discipline throughout: ask, then stay quiet, don't fill silence with your own answer.
Gap addressed: Identify pain (MEDDIC), Need (BANT) — this is the stage that either produces a real qualified pain or ends the call honestly.
Success criteria: prospect names a specific, current operational friction in their own words — not a hypothetical, not a shrug.

Stage 4 — Insight moment (only if Stage 3 lands)
Purpose: one sharp, specific reframe of what they just told you — the Challenger substitute for proof you don't have. This is the one place in the call where you talk more than you ask.
Gap addressed: Decision criteria (MEDDIC) — starts shaping what "a good solution" looks like in their head, on your terms.
Success criteria: prospect engages with the reframe rather than going flat or repeating themselves.

Stage 5 — Authority check
Purpose: find out, without asking "are you the decision maker" directly, whether you're talking to someone who can act — Economic buyer (MEDDIC), Authority (BANT). Phrased as a process question, not a status question, since a direct authority question this early reads as dismissive.
Gap addressed: Economic buyer, Authority.
Success criteria: you know whether the next step is "keep going with this person" or "get referred."

Stage 6 — Timeline check (light touch)
Purpose: is there an actual trigger forcing a decision, or is this evergreen pain with no urgency. One question, no pressure.
Gap addressed: Decision process, Timeline (BANT).
Success criteria: you know whether the next step should be scheduled soon or nurtured.

Stage 7 — Close
Purpose: one low-friction ask that advances whichever gap is most open — never "let me send you a proposal," since there's nothing to propose yet on a first call with no case studies behind it. The ask is proportional to what actually happened in the call.
Gap addressed: whichever of the above is still open.
Success criteria: a concrete next action with a date attached — not "sounds good, send me something."

Three branches, same skeleton

Live decision-maker — runs the full seven stages.
Gatekeeper — Stages 1–2 only, redirected: the goal isn't to sell past the gatekeeper, it's to get named and get through, using a calibrated question rather than asking permission ("What's the best way to get five minutes with [name] about [specific operational issue]?").
Voicemail — Stage 1–2 compressed into fifteen seconds, ending in a specific callback reason, never "give me a call back."

Next: the full script text for all three branches, with the actual language for each stage.

User: next

Assistant: [This response — Section 4 delivery is pending in the same turn as this save.]
