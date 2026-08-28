---
thread_name: "askcruz-what-is-it-explainer"
user: "danish"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: The eoxs-db connector's dedicated tools (get_index, search_wiki, search_assets) aren't loading via search - why these tools are not available to me?

Assistant: Good question to dig into rather than let slide. Let me check what's actually happening instead of guessing.

[Called tool_search "get_index eoxs-db wiki assets search" -> returned Team EOXS MCP:list_tables, Team EOXS MCP:query, Thread OV:search_ov2_wiki, EOXS Data General:search_repo_docs, EOXS Data General:list_repo_docs. No eoxs-db, get_index, search_wiki, or search_assets tools found.]

Confirmed, same result as before. Here's the actual answer, not a guess:

The eoxs-data-general skill describes an eoxs-db connector with 20 tools — get_index, search_wiki, get_wiki_page, search_emails, search_assets, get_client_profile, etc. That connector is not in your connector list. Your actual connected MCP servers, per the system context, are: AskCruz MCP, EOXS Data General, Gmail, Team EOXS MCP, Thread OV, and Zoho Mail. There is no server named eoxs-db among them.

What you have instead, under similar-sounding names, are two different things:

- EOXS Data General — only 2 tools (search_repo_docs, list_repo_docs). Per its own description, this covers "docs/*.md, ARCHITECTURE.md, and a synthesized codebase overview" — source-code repository documentation, not business data. It's also marked "tier1 only (Raj/`full` identity)" — worth noting given the attribution issue we just discussed: if this connector is scoped to a Raj identity and this session is resolving as Danish, that could independently affect what it returns, though the empty results I got earlier looked like the doc store itself being empty rather than an access denial.
- Team EOXS MCP — only 4 tools (list_tables, describe_table, get_business_schema, query) — raw SQL against EOXS Team Live Odoo, same shape as the AskCruz MCP connector. No wiki, no email search, no asset search.

So the honest answer: the eoxs-data-general skill file is describing a connector (eoxs-db, 20 tools: index, wiki, emails, calls, assets, client profiles) that either was never connected to this account, has been renamed/replaced by "EOXS Data General," or was deprecated and the skill file wasn't updated to match. I can't tell which from here — I can only see that the skill's tool inventory and your actual connected tools don't line up. That's a config/documentation mismatch on the EOXS side, not something fixable from this chat, and not something I should paper over by pretending the tools exist.
