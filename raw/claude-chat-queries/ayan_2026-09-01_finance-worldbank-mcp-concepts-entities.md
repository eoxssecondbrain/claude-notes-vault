---
thread_name: "finance-worldbank-mcp-concepts-entities"
user: "ayan"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

USER:
go through the finance bank MCP and list down the concepts and entities that are present in it.

ASSISTANT:
No existing skill covers the Finance World Bank connector specifically (threads-ov is for chat-transcript saving, raj-eoxs-vault is for EOXS data) — flagging that per your instruction, then proceeding since you named the connector directly.

The connector currently holds:

**Entities (countries)**: 100 countries/regions returned (alphabetically capped at "Honduras" — this is a page limit, not the full set; use the `filter` param to search beyond H if you need specific countries later). Includes individual countries plus aggregates like "Africa Eastern and Southern," "Euro area," "European Union," "East Asia & Pacific," "Heavily indebted poor countries (HIPC)."

**Indicators (12)**:
- Access to electricity (% of population)
- Current health expenditure per capita (current US$)
- External debt stocks, total (DOD, current US$)
- GDP (current US$)
- Government expenditure on education, total (% of GDP)
- Individuals using the Internet (% of population)
- Inflation, consumer prices (annual %)
- Life expectancy at birth, total (years)
- Military expenditure (% of GDP)
- Population, total
- Poverty headcount ratio at national poverty lines (% of population)
- Unemployment, total (% of total labor force) (modeled ILO estimate)

**Documents**: 1 — `worldbank_data.csv` (imported, listed as filetype "pdf" in metadata, added 2026-08-31).

**Concepts**: 0. `total_concepts` is 0 — no wiki-graph concepts have been written yet via `save_analytical_brief`. The 3,180 "sections" and 3,180 "tables" are raw structured data rows, not synthesized concepts.

Note: this is raw World Bank indicator data, not concept/entity synthesis — nothing to trace via `trace_concept_graph` or `get_related_concepts` until briefs get saved.
