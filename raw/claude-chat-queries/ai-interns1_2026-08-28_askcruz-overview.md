---
thread_name: "askcruz-overview"
user: "ai_interns1"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

**User:** tell me the on going projects of ask cruz

**Assistant:** Two things before I dig further:

Scope is ambiguous — "ongoing projects" could mean (a) internal product/dev backlog (the AskCruz Odoo board — 39 active tasks as of Aug 17), or (b) active sales/GTM deals (3GM Steel, Sabre Alloys, Three D Metals, legal-firm diagnostic, etc.), or both. Also flagging: I don't have live access to the AskCruz Odoo instance (`teams-askcruz`, project_id=6) — only synthesized wiki pages built from emails about it, which are not necessarily current to today.

[ask_user_input_v0 tool called with:
Q1: "Which do you mean by 'ongoing projects'?" — options: Internal AskCruz dev/product backlog / Active sales deals / GTM pipeline / Both
Q2: "Rigor level?" — options: 5ft - Quick / 10ft - Verified / 50ft - Deep / 100ft - Staged]

**User:** tell me what ask cruz is about

**Assistant:** AskCruz (product family name "Cruz") is EOXS's internal AI-powered company knowledge base and conversational assistant — a "second brain" that turns scattered business information into searchable, synthesized, cited answers.

Architecture: a ten-stage pipeline — Source Systems -> Ingestion -> Filtering -> Sensitivity Classification -> Central Knowledge Store -> Knowledge Generation -> Citation Check -> Human Approval -> Retrieval -> Response. Ingestion pulls from three individual Gmail accounts, one shared Zoho support inbox, Fireflies call transcripts, Fathom recordings, and client Odoo implementation/onboarding boards for six clients (Greer Steel, Eastern States Steel, Discount Pipe & Steel, PPC Metals, 3GM Steel, Sabre Alloys). RW Conklin Steel and Brannon Steel have no configured Odoo instance, so they only show up via email/calls. Support tickets and invoices/sales orders are explicitly out of AskCruz's native scope — that data lives in the separate eoxs-teams Odoo connection.

Capabilities are organized into: Email, Call & Meeting Data, Client/Implementation Data, Employee Information, Internal Knowledge & Documents, and Cross-Source Knowledge & Business Context. Operational records/transactions are explicitly not natively collected by AskCruz.

One open contradiction worth flagging: internal docs disagree on positioning. The product-feature-file describes AskCruz narrowly as "a company-specific AI product for steel businesses." The product-market-fit doc says the opposite -- "industry-agnostic, designed for any industry" -- and warns against single-vertical positioning. The client-facing capability catalog sides with the industry-agnostic framing. These haven't been reconciled in the source material, so if you're using external-facing positioning language, worth confirming which one is current before it goes out.

**Assistant (continuing after save confirmation):** Saved. Let me know which scope you want on the "ongoing projects" question when ready — internal dev backlog, sales pipeline, or both.

**User:** what tools you have access to that can give me information about ask cruz

**Assistant:** Four tool sources are available, but they don't cover AskCruz evenly:

Eoxs-Data-General (eoxs-db) — the main useful one. search_wiki / get_wiki_page surfaces synthesized pages about AskCruz (architecture, capabilities, market positioning, board-reporting behavior). search_emails and search_calls can pull raw correspondence/call mentions. search_assets / get_asset can pull the original source documents (the product-feature file, the PMF doc) verbatim rather than the synthesized summary. This is where everything I told you earlier came from.

Eoxs-Teams (EOXS Team Live Odoo — the steel-distribution company's live DB, database Eoxteams_12Feb24) — I checked: it has project_project / project_task tables, but no project named AskCruz or Cruz in there. So this connector cannot see AskCruz's own dev board. It's built for EOXS's steel-distribution sales orders, invoices, and CRM data, not AskCruz's internal task tracker.

Threads-OV — search_chat_summaries / search_claude_chat_queries / search_analyses. These are past Claude conversations and analyses saved in this vault, not a live data source — useful only if AskCruz came up in an earlier saved thread.

web_search — general web, unlikely to carry much since AskCruz is an internal product.

Gap: the actual live AskCruz Odoo board (`teams-askcruz`, project_id=6, 39 active tasks as of Aug 17) sits on a separate Odoo instance that isn't connected in this session at all. Everything I can give you on AskCruz's internal task state is secondhand — synthesized from emails about that board, not a direct read of it. If you want real-time task status, that instance would need to be connected as its own connector.
