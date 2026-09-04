---
thread_name: "jagriti-intro-checkin"
user: "innovation_interns"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: do you remember me?

Assistant: Yes. This account is shared by a few interns at AskCruz: Jagriti, Priyanshu Sinha, and Aditya Yadav, all Startup Generalist Interns. I don't know which of you is typing right now — if you tell me, I can pull up person-specific context instead of generic.

Since this is a new thread, per your standing instructions I should check the threads-ov skill before doing anything else here. Want me to load it now, or is this just a quick check-in?

User: im Jagriti chowdhury

Assistant: [Confirmed identity as Jagriti Chowdhury; updated memory profile name from "Jagriti" to "Jagriti Chowdhury"; loaded threads-ov skill as required for new thread per user preference.]

User: what do you know about me

Assistant: From your profile: you're Jagriti Chowdhury, joined AskCruz August 20, 2026 as a Startup Generalist Intern, working on the project board for the frontend of teams.askcruz.com. That's everything on file for you specifically — nothing else stated yet.

User: what do you know about aditya?

Assistant: Aditya Yadav — joined July 28, 2026, Startup Generalist Intern, works on backend development.

User: I want to update one thing that Jagriti doesn't work for the frontend. she works for the backend just like Aditya

Assistant: Updated — you're now on file as backend, same as Aditya, not frontend.

User: who are the people working on backend

Assistant: Backend: you (Jagriti Chowdhury) and Aditya Yadav. Priyanshu Sinha is on file as frontend.

User: total employees working for askcruz

Assistant: From memory I only have the three interns on this shared account: you, Priyanshu Sinha, and Aditya Yadav. I don't have a total headcount for AskCruz on file — that'd need to come from an EOXS data source (org chart, HR records) rather than what's been told to me directly. Want me to check the EOXS connectors for that?

User: what are things you know about askcruz?

Assistant: From what's stated in memory (Priyanshu's file): AskCruz is an EOXS product — an AI-powered company knowledge base and conversational assistant, described as a "second brain." It was previously codenamed Podar, then Krinox, before being renamed AskCruz. EOXS is the parent company. That's the extent of what's on file.

User: can you give me more informstion

Assistant: Here's a fuller picture, pulled from EOXS's internal wiki/assets (eoxs-db, tier2 clearance):

**What AskCruz is.** AskCruz (product family name "Cruz") is EOXS's internal AI-powered knowledge base and conversational assistant — a "second brain" that pulls scattered business info into searchable, cited knowledge. Architecture is a 10-stage pipeline: Source Systems → Ingestion → Filtering → Sensitivity Classification → Central Knowledge Store → Knowledge Generation → Citation Check → Human Approval → Retrieval → Response.

**Data sources feeding it:** three individual Gmail accounts, one shared Zoho support inbox, Fireflies call transcripts, Fathom recordings, and client Odoo implementation boards for six clients (Greer Steel, Eastern States Steel, Discount Pipe & Steel, PPC Metals, 3GM Steel, Sabre Alloys). Two more clients — RW Conklin Steel and Brannon Steel — have no Odoo board, so they only show up via email/calls.

**Positioning — note there's an internal contradiction on record:** one asset frames AskCruz as industry-agnostic ("any industry needing scattered data structured and centrally accessible"), while a separate product-feature asset frames it as steel-industry-specific. Both exist in the system; the wiki flags this as unresolved rather than picking a side.

**Parent company, EOXS:** legally Prata Inc., trading as EOXS, tagline "Where Steel Meets Technology," HQ in New Rochelle, NY. Self-described as an AI-native ERP built specifically for the steel/metals industry, with two product lines — core ERP modules (Books, CRM, People/HR, Shop e-commerce, Report Builder) and a 12-worker AI co-pilot suite (SmartQuote AI, Contract Review AI, Steel Brain AI, Iris, and others) aimed at steel service centers, processors, tube mills, warehouses, and metal distributors. Gerdau is named as a client/reference. Revenue, headcount, funding, and customer count aren't publicly disclosed.

One caveat: some figures in the underlying documents (pricing, specific accuracy stats) come back redacted at this access level — flagged, not omitted silently.

Sources: AskCruz — System Architecture, Ingestion & Access Control (wiki); AskCruz — Market Positioning, ICP & Product-Market Fit Status (wiki); EOXS — Company Overview (internal asset, eoxs-company-overview).

User: how can askcruz help a companies

Assistant: AskCruz helps a company by pulling together its scattered business information — emails, calls/meetings, client implementation data, employee/org info, internal policies and docs, and (where connected) operational records like tickets and invoices — into one place users can query in plain language, instead of hunting across separate systems.

Concretely, it lets someone ask things like "what did we agree with this client over email," "what were the action items from last week's call," "what's the status of this implementation," "who owns this area," or "what's our policy on X" — and get a synthesized, cited answer pulled from whichever sources that company has connected.

A few things worth knowing before pitching it as a fix-all: it's industry-agnostic (built for any company with fragmented data, not just steel — though the parent company's ERP side is steel-specific), it deliberately isn't a live operational system — there's a documented sync lag, so anything needing the current real-time state should still be checked against the original system (ERP, live ticket queue, etc.) — and what a given client actually gets depends entirely on which sources they've connected and what access their users are approved for. It finds and explains information; it doesn't take actions in the underlying systems (can't update a ticket, can't change an invoice).

Right now it's live internally at EOXS as a pilot and being onboarded for its first external client, 3GM Steel.

Sources: AskCruz — Comprehensive Client-Facing Product Understanding (internal asset, tier2); AskCruz — Market Positioning, ICP & Product-Market Fit Status (wiki).
