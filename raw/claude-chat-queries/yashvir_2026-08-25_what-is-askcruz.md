---
thread_name: "what-is-askcruz"
user: "yashvir"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

User: What is ask cruz?

Assistant: AskCruz is EOXS's Claude-based AI agent product, internally called "Company Brain," renamed from Krinox on August 5, 2026.

It's sold two ways:
- Standalone, targeting businesses with roughly 20–60 employees
- As an add-on to existing EOXS ERP clients

It's distinct from IRIS (a lighter read-only ERP BI module) and AI Joe (a Gerdau-specific proof-of-concept). No deals have closed yet as of mid-August 2026. Active pipeline: 3GM Steel, Ohio Strip Steel, Collier Metals, Sabre Alloys, and a legal-services prospect (Sarah).

Open risks on it: no formal ICP document (the 20–60 employee figure is undocumented, worth confirming with Rajat), two conflicting sales motions running at once (steel/metals upsell vs. cross-vertical standalone), unresolved unit economics on API cost per interaction, and no CRM pipeline tracking — deal activity only lives in emails and call transcripts.

User: On the scale of 10 what level of information do you have about AskCruz?

Assistant: Around a 4 out of 10.

What I have: the product definition, positioning (standalone vs. add-on), pricing tiers relative to who it's sold to, the current pipeline accounts, competitive/internal distinctions (IRIS, AI Joe), and the known strategic risks (no ICP doc, conflicting sales motions, unresolved unit economics, no CRM tracking).

What I don't have, which matters more for a 1M ARR outbound motion:
- No qualified/documented ICP — the 20–60 employee figure is unconfirmed
- No visibility into actual sales script, objection handling, or what's converting vs. stalling in live conversations
- No pricing model or unit economics (API cost per interaction is explicitly unresolved)
- No CRM data — pipeline stage, deal velocity, conversion rates don't exist anywhere structured
- No sense of what's actually said on calls beyond what's been surfaced in threads so far
- No competitive landscape for AskCruz specifically (who else sells this to 20–60 person shops)

The gaps aren't me being under-briefed — they're gaps in the business itself (no ICP, no CRM tracking) that would cap anyone's information level, not just mine. If you want this higher, the fastest lever is closing those two — not me reading more emails.

User: Whats the main source of your information?

Assistant: Two sources, mixed together:

1. My stored memory file on AskCruz (`/areas/askcruz-ldr.md`) — this holds facts already gathered and filed from prior conversations/sessions. It's not raw data, it's a compressed summary of what's been established so far.

2. For anything not already in that file, the underlying source would be the EOXS data connectors (eoxs-db: emails, calls, wiki, implementation tasks; eoxs-teams: live CRM/pipeline/ticket data) — but I haven't queried those live in this conversation. Everything I've told you so far came from the memory file, not a fresh pull.

That's worth flagging: my "4/10" answer is only as current as that memory file's last update (Aug 23). If pipeline accounts have moved, new emails have come in, or Rajat has clarified the ICP since then, I wouldn't know unless I query eoxs-db/eoxs-teams directly. Want me to pull current state from the live connectors rather than relying on the stored summary?

User: Are you aware if askcruz has a website?

Assistant: No, there's no public marketing site at askcruz.com — none of these results are EOXS's product. That's an unrelated "Ask Cruz AI" feature on a car-shopping site (Cruz.com), plus an Instagram account for a clothing store, both coincidental name matches.

What I found internally is a mail server subdomain — `mailcow.askcruz.com` — used for internal AskCruz mailboxes (referenced in an IT provisioning email from Aug 18). That confirms EOXS owns the `askcruz.com` domain, but there's no evidence of a live public-facing marketing/product site on it, and nothing in the wiki or product docs references one.

That's itself a gap worth flagging: if you're doing outbound as an LDR, a prospect who gets curious and googles "AskCruz" currently finds nothing — no landing page, no positioning, nothing to reinforce the pitch after the call. Worth raising with Rajat if it isn't already on someone's list.

User: Does Eoxs has a website?

Assistant: Yes. https://www.eoxs.com

That's the ERP company site (EOXS/Prata Inc.), separate from AskCruz, which — as established last turn — has no public marketing site of its own, only an internal mail subdomain (mailcow.askcruz.com).

Quick contrast worth noting for your work:
- EOXS site is built out: full company overview, product breakdown (5 ERP modules + 12 AI Worker co-pilots), blog, book, testimonials, demo booking via Calendly
- AskCruz has none of that — no landing page, no product page, no way for a prospect to self-serve information after a call

That gap is more concrete now that I've seen how developed the EOXS site is by comparison — reinforces the point from last turn that AskCruz outbound currently has zero web presence to back it up.
