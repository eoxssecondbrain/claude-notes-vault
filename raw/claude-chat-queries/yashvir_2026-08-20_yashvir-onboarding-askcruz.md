---
thread_name: "yashvir-onboarding-askcruz"
user: "yashvir"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

User: HI my name is yashvir, i just got hired here as an Lead Developement Representative, it's my first day here. make me a road map of how i should proceed with the day and  make me a roadmap for i i should understand what AskCruz is since i'll be generating lead for the askcruz, please do not overwhelm me with the roadmap and instructions, we'll take it slow and step by step.

Assistant: Quick flag before the roadmap: internal records here show a Yashvir Singh already active at EOXS since 2024, doing recruiting ops, sales onboarding, and LDR contact work. That doesn't line up with "first day." If you're a different Yashvir, worth flagging a possible name collision in the system. If it's you, worth knowing why today reads as day one on your end — not going to assume either way.

Two things this touches: eoxs-data-general (for pulling the actual AskCruz reading material) and threads-ov (auto-saves this thread, no action needed from you).

Day 1 roadmap — 5 steps, not all today:

1. Access — confirm email, Odoo/CRM login, calendar access from Rajat or HR
2. People — meet Rajat (you'll work closely with him) and whoever runs sales ops day to day
3. Read the EOXS Company Overview doc — what EOXS actually sells, in plain terms
4. Read the EOXS ICP doc — what a good-fit prospect looks like
5. Listen to one recent AskCruz sales call to hear how it's actually pitched live

AskCruz understanding roadmap — separate track, your pace:

1. What it is — one-liner, and how it's different from EOXS ERP / IRIS
2. Who buys it — AskCruz's own ICP, not just EOXS ERP's
3. How it's pitched — a real call (Ohio Strip Steel or 3GM Steel calls exist in the system)
4. Where it sits in the pipeline right now — live deals in motion
5. Objections you'll actually hit as an LDR making cold contact

Tell me which single step you want to start on and we'll do just that one.

User: Before we proceed further, i want you to know that i'm a complete fresher to the LedGen role.

Assistant: Good to know — I'll explain things plainly and won't assume prior sales/lead-gen vocabulary.

One adjustment: given you're new to LDR itself, it might make more sense to start even before AskCruz — a quick "what does an LDR do day-to-day" grounding, so the AskCruz roadmap makes sense once we get to it.

So, pick one:

1. What an LDR does — the actual job, day to day
2. Day 1 step 1 — access/logins
3. AskCruz step 1 — what AskCruz is, one-liner

Which one first?

User: let's start with 3. since i'm already aware about 1. and 2. ?

Assistant: AskCruz, one line: an AI layer that reads across a company's ERP, email, and call data and reasons over all of it — turning scattered business information into one thing you can ask questions to. Internally it's often called "Company Brain."

How it's different from EOXS ERP: EOXS ERP is the system of record — where the actual data lives (orders, inventory, invoices, operations). AskCruz sits on top of that and reasons over it — it doesn't replace the ERP, it makes sense of what's already in it plus emails and calls.

How it's sold, based on live deals: mostly as an add-on/upsell to existing EOXS ERP customers right now — 3GM Steel is a live example, pitched to their CCO as a Company Brain add-on. But it's also being pitched standalone to non-EOXS companies — there's an active conversation with a legal-services firm that has nothing to do with steel or EOXS ERP.

That's the whole first step. Next up would be who buys it (step 2) — want to keep going, or sit with this first?

User: So if any company opts to implement AskCruz whay all information or access would we want from them to implement it end to end?

Assistant: Based on actual EOXS/AskCruz deals in the system, there's no single formal "implementation checklist" document — but the pattern across live deals is consistent. What gets asked for:

ERP data — either their existing EOXS ERP data if they're already a client, or, if not, a direct data pull covering sales, purchase, and invoicing records. That's literally what was asked of 3GM Steel's CCO for a similar AI preload: "send sales, purchase, and invoicing data — whatever you want to ingest."

Email access — company email accounts get connected so email becomes a feed into the system, not just a communication channel. One rollout email to a client put it directly: "Email and Zoom feed directly into this system, hence going forward those will be our primary channels of communication."

Call/meeting data — Zoom or call recordings, run through a transcription layer (Fireflies/Fathom on the EOXS side), so call content becomes reasoning material too.

Scope/seats — how many people will actually use it. This gets negotiated per deal — 3GM Steel's live deal landed at a reduced 2-user scope, not company-wide.

Timeline — the email-integration piece alone has been quoted at 2-3 weeks of implementation work in internal planning; a fuller build (ERP + email + calls) takes longer.

Caveat: I'm not finding one canonical "here's exactly what we collect from a new AskCruz client" SOP — this is reconstructed from how actual deals (3GM Steel, Sabre Alloys) have gone. If you want, I can dig further into whether a formal intake process exists, or move to step 2 (who buys it).
