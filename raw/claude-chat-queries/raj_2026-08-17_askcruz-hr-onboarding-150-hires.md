---
thread_name: "askcruz-hr-onboarding-150-hires"
user: "raj"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

User: I want to build a standard onboarding process for all the people we are going to be hiring in AskCru. My vision is that we will probably hire 150 people in this company in the next 60 days, and we need to have a standard onboarding procedure which helps them understand what our company does. For this, I want to create a task for the HR team to work on. Can you write a detailed description that I can add in the task?

Assistant: This is a strategic/content-creation task (defining how 150 new hires understand the company), so per your rules, pick a rigor level before I start:

**5ft deep** — Quick: I write the onboarding task description from what I already know about AskCruz/EOXS/GFC positioning (from memory of our prior work — brand positioning, ICP, product architecture).

**10ft deep** — Verified: same, but I pull the current AskCruz positioning/homepage copy and any existing onboarding materials from OV2 wiki and cross-check against what's actually live on askcruz.com before writing, so the description reflects the current state, not stale positioning.

**50ft deep** — Deep: verified, plus I check whether any HR onboarding docs/SOPs already exist in the vault (avoid duplicating work), review the hiring plan context (which roles make up the 150 — sales, dev, support, etc.) if that's tracked anywhere, and flag risks in the "150 hires in 60 days" plan itself (e.g., onboarding-at-scale failure modes) as part of the deliverable.

Which one?

User: 50

Assistant: Context first: I checked the vault. Current AskCruz/EOXS onboarding (run by Isha) is purely administrative — signed offer letter, shared Telegram group, one onboarding call, and an askcruz.com mailbox with a shared plaintext initial password (`Cruz12345!`) emailed to everyone. There is no existing content anywhere that explains what AskCruz is or does. So this task fills a real gap, not a duplicate.

Task description to paste in:

Title: Build standard AskCruz onboarding — company/product understanding track

Objective
Every person hired into AskCruz over the next 60 days should leave onboarding with a working understanding of what AskCruz is, why it exists, and how their role contributes — without requiring 1:1 time from Raj or any founder. At 150 hires / 60 days (~2.5/day sustained), this has to be self-serve and repeatable, not a live session per batch.

What currently exists (don't rebuild)
Offer letter signature, Telegram onboarding group, one onboarding call, mailbox setup on askcruz.com. This task is additive — a company/product-understanding layer that plugs into that existing admin flow, not a replacement for it.

Deliverables
1. Written company/product primer (source of truth doc)
 - What AskCruz is: an AI operating system for businesses, built on the experience behind EOXS — ingests a company's ERP, email, call, and internal data and reasons over it. Internally: "Company Brain," with "Cruz" as the named agent.
 - How AskCruz relates to EOXS and GFC — org structure in plain language, since new hires will otherwise conflate the three.
 - The current company goal ($1M ARR in 12 months) and why it's the filter for what gets prioritized.
 - Who the customers are and what problem AskCruz solves for them, at ICP level — not deal-specific detail.
2. Short recorded intro video from Raj or a designated exec — this carries more weight than a doc for "why this company exists."
3. Role-specific tracks layered on top of the shared primer (sales, dev, support, ops — whatever the actual hiring mix is; see open question below).
4. A short comprehension check (quiz, 5-10 questions) at the end of the primer so HR can confirm understanding actually happened, not just attendance.
5. One rollout SOP that sequences this with the existing admin steps (offer letter → primer + video → quiz → Telegram/mailbox → role track) so new hires go through one flow, not two.
6. A tracking sheet: name, start date, role track, completion status, quiz score.

Ownership
One named HR owner for building and maintaining this. One leadership reviewer (Raj or delegate) who signs off on the primer content and re-reviews it whenever AskCruz's positioning changes — this is moving fast enough that a stale primer will actively mislead new hires within weeks.

Open question HR needs from Raj before building role tracks
There's no documented breakdown anywhere of what the 150 hires actually are by function. Role-specific onboarding can't be built without that. Flag this back to Raj rather than guessing.

Two things worth flagging outside the task itself:

The shared plaintext password pattern (Cruz12345! emailed to everyone, "change immediately after login") is a real security hygiene issue, not just a process nit — worth fixing while this gets rebuilt rather than carrying it forward at 30x volume.

150 hires in 60 days is a big number relative to a $1M ARR / 12-month goal. Before HR builds infrastructure for this scale, it's worth confirming the hiring plan itself is sized to the goal rather than just being sized to what's achievable to recruit — that's your call, not HR's, but it's upstream of everything in this task.
