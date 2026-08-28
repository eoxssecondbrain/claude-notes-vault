---
thread_name: "askcruz-overview"
user: "ai_interns1"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

**User:** tell me the on going projects of ask cruz

**Assistant:** Two things before I dig further: scope ambiguous (internal dev backlog vs sales pipeline vs both) and I don't have live access to the AskCruz Odoo instance. [ask_user_input_v0 called with scope + rigor level options]

**User:** tell me what ask cruz is about

**Assistant:** AskCruz (product family "Cruz") is EOXS's internal AI-powered company knowledge base and conversational assistant, a second brain turning scattered business info into searchable, synthesized, cited answers. Ten-stage pipeline: Source Systems, Ingestion, Filtering, Sensitivity Classification, Central Knowledge Store, Knowledge Generation, Citation Check, Human Approval, Retrieval, Response. Sources: three Gmail accounts, one Zoho inbox, Fireflies, Fathom, and six clients' Odoo boards (Greer Steel, Eastern States Steel, Discount Pipe and Steel, PPC Metals, 3GM Steel, Sabre Alloys); RW Conklin Steel and Brannon Steel only via email/calls. Support tickets and invoices are explicitly out of scope, handled by eoxs-teams instead. Capabilities: Email, Call and Meeting Data, Client/Implementation Data, Employee Information, Internal Knowledge and Documents, Cross-Source Knowledge and Business Context. Flagged contradiction: product-feature-file calls it steel-industry-specific, product-market-fit doc calls it industry-agnostic, client-facing catalog sides with industry-agnostic. Unreconciled in source material.

**User:** what tools you have access to that can give me information about ask cruz

**Assistant:** Eoxs-Data-General (eoxs-db) is the main useful source: search_wiki/get_wiki_page for synthesized AskCruz pages, search_emails/search_calls for raw mentions, search_assets/get_asset for original source documents verbatim. Eoxs-Teams (EOXS Team Live Odoo, database Eoxteams_12Feb24, steel-distribution company) was checked directly — it has project_project/project_task tables but no project named AskCruz or Cruz, so it cannot see AskCruz's own dev board; it's for EOXS's sales orders/invoices/CRM only. Threads-OV (search_chat_summaries/search_claude_chat_queries/search_analyses) covers past saved Claude conversations, not live data. web_search is general web, unlikely to help since AskCruz is internal. Gap: the live AskCruz Odoo board (teams-askcruz, project_id=6, 39 active tasks as of Aug 17) is on a separate Odoo instance not connected in this session — everything on AskCruz's internal task state is secondhand via email synthesis, not a direct read.

**User:** What's AskCruz's Current Architecture and Market Positioning?

**Assistant:** Architecture: ten-stage pipeline (Source Systems, Ingestion, Filtering, Sensitivity Classification, Central Knowledge Store, Knowledge Generation, Citation Check, Human Approval, Retrieval, Response); ingestion mechanisms vary by source (event-driven, scheduled sweeps, source-specific fetchers, sync jobs). Data sources: three Gmail accounts, one Zoho inbox, Fireflies, Fathom, and Odoo boards for six of eight EOXS clients (Greer Steel, Eastern States Steel, Discount Pipe and Steel, PPC Metals, 3GM Steel, Sabre Alloys); RW Conklin Steel and Brannon Steel only via email/calls; tickets/invoices excluded, handled by eoxs-teams. Flagged unverified: ownership notes (Cruz frontend owned by Jaskeerat; server/DB and Linear credentials held by Ayan, Nidhi also on Linear) come from an Aug 21 self-knowledge doc, not cross-checked against current records.

Market positioning: stated core definition is industry-agnostic, for any business with scattered data needing structuring and single-point access; listed industries (manufacturing, tech, healthcare, finance, retail, logistics, education, construction, real estate, hospitality, consulting) are applicability examples, not existing customers. One-line pitch: an industry-agnostic AI agent connecting scattered business data into organizational knowledge accessed via one conversational interface. Core problem: fragmented knowledge across email, spreadsheets, operational systems, project tools, calls. 3GM Steel is the first confirmed acquired customer, but exact sales pitch, buying criteria, commercial value, measured ROI, usage depth, and retention outcome were never established per the source material. Open contradiction: product-feature-file frames AskCruz as steel-industry-specific; product-market-fit doc and client-facing catalog frame it as industry-agnostic. Unreconciled — matters for positioning outside steel.

**User:** how many Active Task are there on the AskCruz dev board for the Ai Interns

**Assistant:** Numbers I have (from the AskCruz board scrum reports — synthesized from emails, not a live query, 10 days old as of today Aug 28): AskCruz board (project_id 6) as of Aug 18: 41 total tasks, 11 completed, so 30 active/open. Separately, "50 MBA Interns Cohort" is a different board entirely: 20 total tasks, no completion stage exists on that board, so effectively all 20 read as open.

One clarification needed: I don't see any group literally labeled "AI Interns" as an assignee on the AskCruz board itself. The assignees there are individuals (Ayan Dutta, Nidhi Rana, Ron, Sheenam, Yashvir Singh Thakur, Rajat Jain) plus bot/shared accounts and the separate "MBA Cohert 1" bucket. There's a mention elsewhere (Hiring Funnels task #114, "Hire 20 Ai devs") of sourcing "AI Engineer interns," but that's a hiring task, not a task-assignee group on the AskCruz board.

Which do you mean by "the AI Interns" — the 50 MBA Interns Cohort board (which isn't the AskCruz dev board), a specific set of engineering interns among the individuals above, or something else?

**User:** what is the wiki structure looks like

**User:** what does the wiki structure look like like how many data points it has

**Assistant:** The eoxs-db wiki holds 1,857 pages total, split across six page types (from get_index(), scoped to this connection's access): analysis — 646 pages (one-off synthesized write-ups on specific events/decisions, e.g. AskCruz scrum-report pages, deal-call summaries); entity — 691 pages (people, companies, clients); source — 306 pages (synthesized summaries of underlying source documents/assets); concept — 158 pages (internal processes/mechanisms, e.g. AskCruz Board Scrum Reporting, internship extend-relieve cycle); prospect — 33 pages (sales prospects specifically); overview — 23 pages (high-level product/company overviews, e.g. the three AskCruz overview pages). Alongside the wiki, the same index shows 33,241 email threads, 2,246 Fireflies calls, 134 Fathom calls, 828 implementation tasks, and 8 registered clients — all scoped to this connection's tier2/tier2_confidential clearance, not a database-wide total.

**User:** So, Tell me what does the wiki actually contains what data points it signifies

**Assistant:** Two layers: the six content categories, and the metadata fields attached to every page.

Content categories: entity (691) - profiles of people, companies, clients (role, employment terms, current work; e.g. Jaskeerat Singh, Three D Metals). concept (158) - internal processes/mechanisms not tied to one event (e.g. AskCruz Board Scrum Reporting, EOXS Internship Extend-Relieve Cycle). analysis (646, largest bucket) - one-off synthesized write-ups of specific events/decisions/incidents with timeline and a flags section (e.g. 3GM Steel AskCruz Proposal Call, AskCruz API Cost Pause). overview (23) - high-level non-event-based reference summaries (e.g. the three AskCruz pages: architecture, capabilities, market positioning). prospect (33) - sales-pipeline entities distinct from won clients (e.g. Three D Metals as prospect, legal-firm AI diagnostic). source (306) - synthesized summaries of underlying reference assets (SOPs, product-feature file, PMF doc); get_asset pulls the original document text behind these.

Per-page metadata fields: id, title, page_type, entity_class; tags (free-text labels); sources_raw (which emails/calls/assets it was synthesized from); created_date/updated_date plus separate created_at/updated_at timestamps; access_tier (tier2 or tier2_confidential); body_preview/body_length/body_truncated (get_wiki_page returns only first ~1500 chars by default); outbound_links (links to other wiki pages); flags (explicit call-out of contradictions or unverified claims baked into the page itself - encountered twice already: the AskCruz positioning contradiction, and the unverified credential-ownership note). The flags field means the wiki surfaces where its own source material disagrees with itself or hasn't been independently checked, rather than just asserting facts.
