---
thread_name: "biodiversity-wiki-mcp-corrections"
user: "ai_interns1"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

[... earlier turns already saved ...]

User: the mcp llink is created and now we have to create it in three tire 1st will containe all data 2nd will contain more credential base data high priority and 3rd will contain more more credential data with much higher priority. the data will be divided into priority wise . after deploying it on render connect the mcp key with connector of claude

Assistant: Implemented tiered credential-based access control in server.py:

- Three separate API keys via env vars: MCP_API_KEY_TIER1 (unlocks Tier 1 only), MCP_API_KEY_TIER2 (unlocks Tier 1+2), MCP_API_KEY_TIER3 (unlocks Tier 1+2+3, including poaching risk / protected breeding zones).
- Added a ContextVar-based clearance check (current_clearance / require_clearance) so each tool function (get_tier1_sightings, get_tier2_interactions, get_tier3_risk_intelligence) enforces its own minimum required tier and returns an "Access denied" message if the connecting key's clearance is too low.
- Replaced the old single-key middleware with TieredApiKeyMiddleware: reads x-api-key (or ?api_key=) on every request (both /sse and /messages), looks it up in TIER_KEYS, sets the per-request clearance level. If no tier keys are configured at all, server stays open at full clearance (dev/local mode); once any tier key is set, unrecognized/missing keys get a 401 instead of silently defaulting to no access.
- Updated README: Render env var section now lists all three MCP_API_KEY_TIER1/2/3 vars with guidance on who should get which; Claude Desktop config section explains that whichever key you paste into x-api-key determines that connection's clearance — use the Tier 3 key for your own full-access setup, hand out Tier 1/2 keys for restricted access.

Files updated and written back to the connected folder: server.py, README.md.

Note: this makes access per-connection, not per-individual-query — whichever key a given Claude Desktop config uses determines what that whole connection can see across the session.
