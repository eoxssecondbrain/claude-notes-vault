---
thread_name: "sales-linkedin-outreach-automation"
user: "ayan"
type: claude-chat
created: 2026-07-27
updated: 2026-07-27
---

# Sales LinkedIn Outreach Automation

**User:** I need to work on an automation related to sales linked in outreach. Need your help with this.

**Assistant:** (Session start) Reviewed raj-eoxs-vault and threads-ov skills per user preference. Called OV2:get_index() to check current vault state — no directly relevant existing LinkedIn-outreach-automation page found; EOXS has an Ideal Customer Profile (ICP) page, Sales Coach product, SmartQuote AI, and prospecting artifacts but nothing specific to a LinkedIn outreach automation build.

Asked clarifying questions:
- What should the automation mainly do? → **Send connection requests + DMs**
- Already using a LinkedIn automation tool? → **Yes, already using one**
- Should leads come from EOXS's existing ICP? → **Yes, use EOXS ICP**
- Which tool are you using? → **Zopto**

**Assistant:** Pulled [[EOXS Ideal Customer Profile (ICP)]] and [[Sales Coach Knowledge Base]] (analysis page) from OV2 to ground the plan in real EOXS data rather than generic advice. Delivered a Zopto-based campaign plan:

1. **Targeting** — split into 3 separate Zopto campaigns by ICP tier (P1 = SOM tier decision-makers, P2 = SOM-SA specialty accounts, P3 = UUM larger distributors), using Sales Navigator filters: Industry (Wholesale, Metal & Mineral), company size 10–200 employees (corrected 2026-06-26 ICP range), US/Canada geography, decision-maker titles (President/Owner/CEO, VP/GM/COO, VP Sales, Director Ops, Director/VP IT, Purchasing Manager).
2. **4-touch message sequence** tied to real EOXS pain points/proof points from the Sales Coach KB — connection note (steel-specific ERP hook) → Touch 2 (MTR/heat-cert traceability pain point question) → Touch 3 (Eastern States Steel proof point: 26 years on Excel/QuickBooks, <3 month go-live) → Touch 4 (soft breakup).
3. **Objection-handling snippets** pulled directly from the Sales Coach Knowledge Base (SAP/NetSuite objection, "built it ourselves," etc.) to plug into Zopto's reply handling.

**User:** "tell me more about this, i want to expand on the logic of how this should be done properly."

**Assistant:** Pulled [[RQL Qualification]] concept page from OV2 to ground the pre-filtering logic. Expanded into a 5-layer operational architecture:

1. **Layer 1 — Pre-filter before Zopto**: run RQL hard disqualifiers (steel mill, <15 LinkedIn members, non-US/Canada, non-qualifying products) against scraped lists before import, to avoid wasting connection-request quota on disqualified accounts.
2. **Layer 2 — Campaign branching logic**: decision-tree instead of linear sequence — auto-pause-on-reply is critical; a human reply should immediately halt automated touches and route to manual reply classification.
3. **Layer 3 — Reply classification mapped to the objection-handling playbook**: table of reply types (SAP/NetSuite objection, "not decision maker," "send more info," "not now," hard no) each mapped to a specific EOXS-grounded response/action (e.g. "not decision maker" → ask for warm intro / offer role-specific 1-on-1 demo, mirroring how Eastern States Steel's real deal ran separate stakeholder demos).
4. **Layer 4 — Lead scoring feedback loop**: outreach results should write back into the ICP's P1–P4 engagement matrix — e.g. a P3 non-decision-maker who responds warmly should get manually flagged as a potential internal champion rather than continuing automated touches; cold P1s get demoted to a slower nurture cadence rather than deleted.
5. **Layer 5 — Safety/compliance throttling**: stay under Zopto's recommended daily connect volume (~20-25/day/seat, ramped slowly), randomized send windows, weekly volume caps to avoid LinkedIn/Sales Navigator automation-detection restrictions.

Offered to turn Layers 2+3 into an actual visual flowchart of the branching logic if useful.

**User:** "can you update the conversation of this thread, into the existing file your created."

**Assistant:** Called save_chat_transcript again with the same thread_name to overwrite the existing file with the full transcript to date.
