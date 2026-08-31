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
