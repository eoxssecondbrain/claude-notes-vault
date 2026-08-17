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

Assistant: Saved. Let me know if you want me to also draft the recorded-video script or the quiz questions once HR has the role breakdown.

User: 50

Assistant: Video script (60–90 sec, delivered by Raj or a designated exec) and a comprehension quiz for the company-level primer. Both are company-wide — they don't need the role breakdown, since that's role-track content layered on top.

Video script — "What AskCruz Is"

Opening
Welcome to AskCruz. I want to spend two minutes on what we actually do, because it's easy to hear "AI product" and assume something generic.

The core idea
AskCruz is an AI operating system for businesses. It's built on the experience behind EOXS — the ERP platform we've run in the steel industry for years. AskCruz takes that same idea and generalizes it: it ingests a company's ERP data, emails, calls, and internal knowledge, and reasons over all of it as one connected system. Internally we call this the Company Brain, and the agent that sits on top of it is named Cruz.

Why this matters
Most businesses have their knowledge scattered — in someone's inbox, in a call nobody wrote notes on, in a spreadsheet one person understands. AskCruz turns that scattered knowledge into something you can actually query and act on.

How it relates to EOXS and GFC
EOXS is the steel-industry ERP company. Ganesh Fruit Company, GFC, is the holding company. AskCruz is GFC's flagship product — the thing we're building the business around. If you're new here, that's the org chart: EOXS proved the idea works in one industry, AskCruz is us taking it everywhere else.

Where we are right now
Our goal for the next 12 months is $1M in annual recurring revenue. That number is the filter for almost every decision we make — what we build, who we sell to, where time goes. Whatever your role, it connects back to that number somehow, and it's worth understanding how.

Close
That's the short version. The written primer goes deeper on the product and our customers. Welcome aboard.

Comprehension quiz — company primer

1. What does AskCruz do, in one sentence?
 Correct: ingests a company's ERP, email, call, and internal data and reasons over it as one connected system.

2. What is AskCruz's internal name for this system, and what is the agent called?
 Correct: Company Brain / Cruz.

3. What is the relationship between EOXS, GFC, and AskCruz?
 Correct: EOXS is the steel ERP company; GFC is the holding company; AskCruz is GFC's flagship product.

4. What is AskCruz's current top-line company goal?
 Correct: $1M ARR within 12 months.

5. Why does that goal matter day to day?
 Correct: it's the primary filter for time, priorities, and decisions company-wide.

6. True or false: AskCruz is the same product as EOXS.
 Correct: false — AskCruz is built on the experience behind EOXS, not the same product.

7. What kind of business problem does AskCruz solve?
 Correct: scattered company knowledge (in inboxes, calls, spreadsheets) that's hard to query or act on.

If you want, I can turn this into an actual interactive quiz widget instead of plain text, or draft the role-track outlines once you have the hiring mix from wherever that plan is being built.
