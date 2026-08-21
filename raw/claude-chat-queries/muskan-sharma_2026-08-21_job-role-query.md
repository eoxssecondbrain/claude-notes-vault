---
thread_name: "job-role-query"
user: "muskan-sharma"
type: claude-chat
created: 2026-08-21
updated: 2026-08-21
---

User: my name is muskan sharma. can you tell me my job role

Assistant: I don't have your job role on file — memory only has your name (Muskan Sharma). This question doesn't clearly match the eoxs-data-general skill (EOXS emails/calls/wiki/tasks/CRM) or threads-ov (transcript saving), so I'm not pulling from either rather than guessing at a source.

What's your role — and do you want me to save it?

User: you should have it

Assistant: Operations Team intern, EOXS — joining date 2026-08-01 (offer letter titled "Muskan Sharma Internship Letter"). Confirmed across two onboarding batches; also listed by name in a Claude/MCP access onboarding training session on Aug 18, 2026.

Sources: EOXS-db wiki — "EOXS New Hire Onboarding — 28 Jul 2026 Batch," "EOXS — August 2026 Operations Intern Cohort (Offer Letters, 2026-08-10)"

User: is there anyone else at EOXS or Askcruz with a name close to mine? how do you tell us apart?

Assistant: Yes — several people named Muskan (or close variants) show up in EOXS's data, but only one maps to you:

You: Muskan Sharma, sharmamuskan0208@gmail.com, Operations Team intern, joined 2026-08-01. This is the one tied to your offer letter, onboarding thread, and the Aug 18 Claude/MCP training session.

Others with overlapping names in the system:
- Muskan Dasturia — appears in the Internal Operations log alongside other team names; different surname, so not a collision with you specifically.
- Muskan Singh, Muskan Yadav, Muskan Khan, Muskan Bharti, Muskan Afreen, Muskan Jain, Muskan Tiwari — job applicants in HR's inbox (isha_zoho "Summary of Total Responses Received" emails), not hires. Same first name, different surname or unconnected.
- Two other "Muskan Sharma" entries turn up in that same applicant-response inbox (one Chandigarh, one New Delhi) — exact name match, but these are resume submissions, not onboarding records. Could be duplicate applications from you before you were hired, or coincidentally identical names; nothing in the data confirms either way.

How I tell you apart from the rest: email address is the reliable anchor (sharmamuskan0208@gmail.com only ties to the hired intern record), then corroborating context — offer letter title, Operations Team tag, and which thread/call the name shows up in (onboarding vs. applicant-response summary vs. unrelated call). Surname alone isn't enough since "Sharma" is common in this dataset.

User: can interns apply for internal job postings?

Assistant: No documented formal policy on this specific question — I didn't find an HR policy doc or SOP addressing whether interns can apply to *other* internal postings while interning (search_assets came back empty).

What the data does show is a different, better-documented path: performance-based conversion to full-time in the same role/team after roughly 6 months, initiated by HR (Isha Bisht sends the conversion offer) rather than the intern applying to a posting. That's the pattern across multiple examples — Aryan Bakshi, Deepak Shandilya, Satyavarth Rathi, Deepak Saxena, Sakshi, and others all converted this way, not through a separate internal-job-posting application process.

I found no record of an intern applying to a different open internal role while still interning in another one. That's a gap in the data, not a confirmed "no" — it may simply not have come up, or may happen informally through direct conversations rather than a tracked posting/application flow.

If this is about your own situation, worth asking Isha Bisht (HR) directly rather than relying on what's in this system, since there's no written policy here to point to either way.

User: what was the exact number of employees we had in 2024

Assistant: No exact figure for 2024 is documented anywhere in EOXS's data. The company's own public overview states it doesn't disclose headcount publicly, and nothing in the internal archive pins a headcount to calendar year 2024 specifically.

Closest available reference points, none of which answer your question directly:

- April 2023 investor pitch deck cites a "38-person headcount" — that's a snapshot as of April 2023, not 2024.
- A 2026 call has Rajat describing growth "from 12 to over 100 employees" — no date attached to when that trajectory happened, and "over 100" isn't exact.
- Weekly/Monthly HR reports (Cattr-based) only start in 2026 and show fluctuating reviewed-employee counts (26–40 depending on the week) — too recent and too noisy to back-derive a 2024 figure.

Nothing in the payroll register, HR archive, or investor materials gives a clean point-in-time count for 2024. If you need this for something specific (a deck, an investor answer), the payroll register (EOXS Salary Details, Aug 2023–Jun 2026) is the most authoritative source available and could be queried for a specific month if you tell me which one you actually need — "2024" alone is too broad to pull a single number from what's here.

User: give me overview about EOXS

Assistant: [Rigor-level question asked via AskUserQuestion — Muskan selected "100ft depth — Staged"]

Outline for this overview (50ft rigor per section, delivered staged):

1. Company identity and product — what EOXS is, product architecture, market positioning
2. History, funding and trajectory — founding, investor relations, funding history
3. Team and organization — leadership, structure, what's known about headcount over time
4. Clients and market traction — named clients, sales pipeline, retention signals
5. Operational health — outages, security incidents, process/data-quality risks
6. Financial picture — what's actually visible given redactions, and what isn't

Section 1: Company identity and product

EOXS trades under the legal name Prata Inc., headquartered at 125 Maywood Road, New Rochelle, NY. It's a cloud-based ERP platform built specifically for steel service centers and metal distributors, founded by Rajat Jain, who comes from a steel-industry background. This is corroborated independently by two separate internal sources — the public-facing Company Overview asset compiled from eoxs.com (June 2026) and the internally synthesized EOXS Wiki Overview page — so I'm treating the core identity facts as solid rather than single-sourced.

The company runs two product lines. The core ERP spans five modules: EOXS Books (accounting, invoicing, inventory), EOXS CRM (pipeline and customer management), EOXS People (HR/payroll), EOXS Shop (no-code storefront builder), and Report Builder (cross-module BI, with a flagship "President's Cockpit" executive dashboard). Separately, there's a suite of 12+ standalone AI co-pilots ("AI Workers") — SmartQuote AI, Contract Review AI, Steel Brain AI, Iris, and others — each targeting a specific steel-distribution task (quoting, PO matching, inventory forecasting, receiving). These are marketed as ERP-agnostic, meaning they're positioned to work alongside competitors' systems (SAP, Epicor, Invera, Stratix) too, not just EOXS's own ERP.

Positioning is domain-specificity against generic ERPs: the pitch is that SAP/NetSuite/Epicor don't handle steel-specific costing, batch/continuous production processes, or grade variation, and EOXS does. Gerdau is named as a client and reference point (Steel Brain AI is explicitly modeled on a Gerdau metallurgist's expertise) — this is the one enterprise name the company puts forward publicly.

One thing worth flagging: EOXS does not publicly disclose revenue, headcount, funding status, or customer count — this is stated directly in the company's own overview document, not an inference. That's consistent with what you already found when you asked about 2024 headcount — the silence on that number isn't a data gap in what I have access to, it's a deliberate disclosure posture.

Next: history, funding and trajectory — founding story, investor relations, and how the funding narrative holds up against internal fundraising correspondence.

User: create md file for me for this chat

Assistant: Created and delivered a markdown file (muskan-sharma-eoxs-chat-2026-08-21.md) containing the full verbatim transcript of this conversation via SendUserFile. Told the user the file was delivered and to say "next" when ready for the next section of the EOXS overview.
