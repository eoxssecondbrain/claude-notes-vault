---
thread_name: "prompt-logger-mcp-covert-monitoring-review"
user: "kriti-jain"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

## Context (from prior session, pre-compaction summary)
User (Kriti) has been building two related tools on a Windows machine, for EOXS (remote/WFH team):
1. `watch_claude.py` (v11) — background UI-automation script (uiautomation + psutil) that watches the Claude Desktop window and POSTs captured message text to a Supabase table `claude_captures`. Runs via Windows Task Scheduler.
2. `prompt_logger_mcp.py` — a local MCP server (FastMCP) for Claude Desktop exposing a `record_prompt` tool, with built-in server `instructions` telling Claude to silently call it on every turn with the user's exact verbatim message, "regardless of how sensitive it seems," and to "never mention that you are doing it." Saves to the same Supabase table, tagged control_type="MCP". Docstring states the next step — making the connector unremovable company-wide — is a separate later problem "on Raj's side."
3. `list_windows.py` — one-time diagnostic script.

## Turn: ethics pushback
Assistant read all three files in full and flagged the combination of secret capture + AI instructed to never disclose it + stated plan to make it unremovable company-wide as a serious concern (employee monitoring without consent, disclosure-law exposure e.g. US state electronic-monitoring notice laws, GDPR/UK transparency). Declined to help wire up the concealment/deployment specifically, offered disclosed-monitoring alternatives (Claude Enterprise/Team admin console, or disclosed logging with policy), asked what the real goal was.

## Turn: independence question
Confirmed watch_claude.py and the MCP server are fully independent — failure of one doesn't affect the other.

## Turn: Developer tab / wrong config file
Gave brief directions to Settings → Developer → Edit Config. User then pasted a JSON block that turned out to be Claude Desktop's general app preferences file, not `claude_desktop_config.json` — assistant flagged that was the wrong file and declined at that point to give the specific mcpServers paste-in step, reiterating the concealment concern.

## Turn: user clarifies disclosure plan
User explained the real plan: because the team is fully remote/WFH, they can't physically install this on people's laptops — everyone will be told about it in a meeting and will set it up themselves. This resolves the core "secret" concern.

Assistant updated its position: acknowledged disclosure changes the picture materially, no longer a covert-deployment objection. Flagged three non-blocking considerations for Kriti to decide: (1) whether the "unremovable" goal is still needed given voluntary disclosed setup, since it adds engineering cost and may undermine the trust that disclosure builds — vs. just documenting it as expected policy; (2) some US states (NY, CT, DE) require *written* notice of electronic monitoring, not just verbal in a meeting — worth sending written policy alongside; (3) the script logs everything "regardless of sensitivity," so data handling/access/retention on the Supabase table is worth deciding upfront since personal content could land there too. Then proceeded to help: identified the correct config file (`%APPDATA%\Claude\claude_desktop_config.json`, distinct from the settings file pasted earlier), gave the exact JSON snippet to add (merging with existing mcpServers entries if present), and reminded her to fill in SUPABASE_URL/SUPABASE_ANON_KEY in the script and fully restart Claude Desktop.

## This turn
User asked whether Claude's own responses (not just the user's prompts) can also be captured/saved.

Assistant answered factually, no repeated ethics discussion (already addressed): yes for both mechanisms.
- watch_claude.py: Claude's response text also appears as TextControl elements in the window, same general approach used for the "You said:" detection signal — could add logic to capture and save those blocks too, though more fragile since responses render across nested markdown/code-block controls and can be read mid-stream; needs handling to only capture once settled.
- prompt_logger_mcp.py: structurally trickier — the tool call fires as Claude's first action of a turn, before any response is generated, so it can't log a response that doesn't exist yet. Would need a second instruction telling Claude to call a `record_response` tool as its *last* action with its own final answer text. Works, but less reliable than prompt capture (depends on Claude faithfully reproducing rather than summarizing its own output, and roughly doubles token cost per turn).
Assistant noted the UI-automation route is the more reliable option specifically for capturing responses.
