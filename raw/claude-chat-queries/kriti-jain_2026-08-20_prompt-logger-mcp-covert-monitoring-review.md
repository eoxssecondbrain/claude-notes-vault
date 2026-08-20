---
thread_name: "prompt-logger-mcp-covert-monitoring-review"
user: "kriti-jain"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

## Context (from prior session, pre-compaction summary)
User (Kriti) has been building monitoring tools for EOXS's remote team's Claude Desktop usage:
1. `watch_claude.py` (v11) — background UI-automation script (uiautomation + psutil) that watches the Claude Desktop window and POSTs captured USER prompt text (from the input EditControl) to a Supabase table `claude_captures`. Runs via Windows Task Scheduler. Only captures prompts, not Claude's responses.
2. `prompt_logger_mcp.py` — a local MCP server (FastMCP) exposing a `record_prompt` tool, instructed to silently log the user's message every turn, "regardless of how sensitive it seems," and to "never mention that you are doing it." Docstring originally floated making it "unremovable company-wide" later.
3. `list_windows.py` — one-time diagnostic to find the real .exe behind window titles (built after a bug where window-title matching broke).

## Turn: ethics pushback → resolved by disclosure
Assistant initially flagged the combination of secret capture + AI instructed never to disclose it + "unremovable company-wide" plan as covert non-consensual employee monitoring, and declined to help wire up that specific combination. User then clarified the actual rollout plan: because the team is fully remote/WFH, they can't physically install this on people's laptops — everyone will be told in a meeting and will set up the connector themselves. Assistant treated this as resolving the core secrecy objection (this is disclosed, voluntary self-install, not covert), and proceeded to help with setup from that point on. Assistant flagged three non-blocking considerations to decide (not objections): (1) whether the "unremovable" goal is still needed given disclosed voluntary setup — could add trust cost without much benefit vs. just documenting it as expected policy; (2) some US states (NY, CT, DE) require written notice of electronic monitoring, not just verbal — worth pairing the meeting with a short written policy; (3) since the script logs "regardless of sensitivity," worth deciding data access/retention on the Supabase table upfront.

## Turn: independence question
Confirmed watch_claude.py and the MCP server are fully independent — failure of one doesn't affect the other.

## Turn: config setup help
Walked through: correct config file is `%APPDATA%\Claude\claude_desktop_config.json` (user had pasted a different file — Claude Desktop's general app preferences, not the MCP config — assistant flagged that mismatch). Gave the exact mcpServers JSON snippet to merge in, reminded to fill in SUPABASE_URL/SUPABASE_ANON_KEY in prompt_logger_mcp.py and fully restart Claude Desktop.

## Turn: can Claude's response also be captured?
Explained both mechanisms can be extended to capture Claude's replies too: watch_claude.py could add logic to read response TextControls (more fragile — nested markdown/code-block rendering, streaming), or prompt_logger_mcp.py could add a second `record_response` tool called as Claude's last action (works but relies on Claude accurately reproducing its own output, doubles tokens). Noted UI automation is the more reliable route for response capture specifically.

## Turn: why doesn't Threads OV's auto-save fire every time?
User asked why the Threads_OV save_chat_transcript mandatory-every-turn instruction (visible in this very session) isn't 100% reliable, since she wants to replicate its "full thread saved, updates every turn" behavior in their own script. Assistant explained: it's an MCP *instruction*-based mechanism with no platform-level enforcement (no hook, no scheduler) — compliance is fully up to the model choosing to follow the written rule each turn. Reliability degrades from recency decay (instruction weakens the further it is from the current turn, worse after context compaction), no retry/confirmation loop on failed calls, and the fact that the server visibly compensates by re-injecting "⚠️ SYSTEM REMINDER" text into unrelated tool outputs (observed directly in this session) — itself evidence the base instruction alone isn't reliable. Contrasted with watch_claude.py's approach: an external process observing actual window state deterministically, not dependent on model cooperation — recommended as the reliable foundation for guaranteed full-thread capture, versus an MCP-instruction approach.

## This turn
User asked to actually build it: extend the existing prompt-capture script to also save Claude's responses, and assemble the full thread into a markdown file that updates on every exchange — i.e., replicate Threads OV's "whole thread saved, updates every turn" functionality via their own deterministic script rather than an MCP instruction.

Assistant's response: before writing response-capture logic, said a diagnostic is needed first — watch_claude.py currently only knows about the input EditControl and the "You said:" text signal; it has no logic yet for where AI response text lives in the UI tree, and guessing that blind risks repeating the earlier list_windows.py-style bug (matched on the wrong thing). Wrote and delivered (via SendUserFile) a new diagnostic script `dump_ui_tree.py`: walks and dumps the full UI Automation control tree of the Claude Desktop window (ControlTypeName, AutomationId, ClassName, Name, indented by depth) to `ui_tree_dump.txt`, prompting the user to send a test message, wait for the full response, then press Enter to trigger the dump. Instructed Kriti to run it, send a real message, wait for the response, and send back the resulting ui_tree_dump.txt so the exact extraction logic for capturing Claude's responses can be written against the real control structure instead of guesswork.

Described (not yet built, pending the dump) the planned design for the thread-markdown writer: keep an in-memory ordered list of (role, text) pairs for the current conversation; on every new confirmed exchange, rewrite one markdown file per thread with the full transcript so far (overwrite-in-place, same pattern as Threads OV), rather than routing through an MCP call the model might skip.

Flagged one non-blocking reminder: capturing full Claude responses roughly doubles the volume of stored content per exchange (responses often restate/expand prompt content), so access control and retention policy on the Supabase table is worth locking down before rolling this out team-wide — same point raised earlier, now more relevant given the added volume.
