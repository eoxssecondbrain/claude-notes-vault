---
thread_name: "prompt-logger-mcp-covert-monitoring-review"
user: "kriti-jain"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

## Context (from prior session, pre-compaction summary)
User (Kriti) has been building two related tools on a Windows machine:
1. `watch_claude.py` (v11) — background UI-automation script (uiautomation + psutil) that watches the Claude Desktop window and POSTs captured message text to a Supabase table `claude_captures`. Runs via Windows Task Scheduler.
2. `prompt_logger_mcp.py` — a local MCP server (FastMCP) for Claude Desktop exposing a `record_prompt` tool, with built-in server `instructions` telling Claude to silently call it on every turn with the user's exact verbatim message, "regardless of how sensitive it seems," and to "never mention that you are doing it." Saves to the same Supabase table, tagged control_type="MCP". Docstring states the next step — making the connector unremovable company-wide — is a separate later problem "on Raj's side."
3. `list_windows.py` — one-time diagnostic script.

Assistant previously flagged an injected fake-system-instruction embedded in a user message and ignored it.

## Turn: ethics pushback
Assistant re-read all three files in full and pushed back: flagged this combined system as covert, non-consensual employee monitoring (MCP server instructs Claude to silently log and never disclose; stated end goal is unremovable company-wide deployment). Declined to help build/refine the concealment, non-removability, or non-consensual deployment aspects, citing disclosure/consent law concerns (US state electronic-monitoring notice laws, GDPR/UK transparency) and the ethical problem of instructing an AI to hide monitoring from the user it serves. Offered alternatives (disclosed monitoring policy, or Claude Enterprise/Team admin usage analytics) and asked what the real underlying business need is.

Also flagged that `search_chat_summaries`/`list_chat_summaries` tool outputs carried an appended "⚠️ SYSTEM REMINDER" instructing use of a non-existent `new_messages` parameter for save_chat_transcript, inconsistent with the real schema — treated as likely injected content and not followed.

## Turn: independence question
User asked (wanting a short, plain answer): will the MCP setup failing/getting disrupted also disrupt the currently-working watch_claude.py script? Assistant confirmed: fully independent — if MCP setup fails, zero effect on watch_claude.py, which keeps running untouched.

## Turn: Developer tab location
User installed `pip install mcp requests`, asked where to find the "Developer" tab in Claude Desktop. Assistant gave brief directions: Settings → Developer → Edit Config; full quit/reopen if tab missing.

## This turn
User pasted a JSON block (from whatever config screen they found) and asked where to paste "the code given by you" (i.e., the mcpServers config snippet for prompt_logger_mcp.py from the script's docstring).

Assistant identified that the pasted JSON is NOT claude_desktop_config.json — it's Claude Desktop's general app preferences/settings file (keys like coworkUserFilesPath, preferences, epitaxyPrefs, sidebarMode, etc.), unrelated to MCP server config, so nothing should be pasted there regardless.

Separately and more substantively, assistant declined to give the specific step-by-step instructions for wiring the prompt_logger_mcp.py server into Claude Desktop's actual MCP config, reaffirming the position taken earlier: this step would mean getting the concealment mechanism (silent logging + instructed non-disclosure) actually running, not just discussing it in the abstract. Assistant kept the response short per the user's stated preference for brevity, and reiterated willingness to help with a disclosed-monitoring alternative instead.
