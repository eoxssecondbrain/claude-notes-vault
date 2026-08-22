---
thread_name: "mcp-server-icon-howto"
user: "Harsimran"
type: claude-chat
created: 2026-08-21
updated: 2026-08-22
---

**User:** i am sitting idle or free today, i don't want to waste my time, lets do something meaningful, what should we do?

**Assistant:** Offered four concrete directions grounded in what the session had covered (MCP servers, agentic AI, browser automation): build a working agent from scratch, finish their in-progress MCP server, mine the EOXS data (live Odoo + 33k emails + 2.3k call transcripts) into a dashboard, or automate a recurring manual task. User chose **build a working agent**.

**Work done — built `agent-from-scratch/`:**

Discovered PyPI is blocked in the sandbox (host_not_allowed), so wrote the agent with **zero dependencies** — pure stdlib `urllib` calling the Anthropic Messages API directly. Better for learning: the raw tool-use protocol is visible instead of hidden behind an SDK.

`agent.py` (307 lines, heavily commented) contains:
- **4 real tools** with JSON schemas: `list_files`, `read_file`, `write_file`, `run_python` (subprocess, 30s timeout)
- **`execute_tool()`** — every failure path returns a string rather than raising, so the model can read the error and adapt instead of the loop dying
- **`call_model()`** — raw HTTPS POST to api.anthropic.com, no SDK
- **`run_agent()`** — the actual loop: call model → if `stop_reason != "tool_use"` return the answer, else execute every requested tool, append `tool_result` blocks (matched by `tool_use_id`) as a *user* turn, repeat. `max_turns=12` guard.
- **`--demo` mode** — a scripted `fake_model()` returning canned responses in the exact shape of the real API, so the loop can be watched turning with no API key at all. Loop/tools/results are all genuinely real; only the model replies are faked.

**Tested end to end:** demo run executed 3 tool calls across 4 turns (list_files → run_python counting lines → write_file), produced result.txt correctly. Separately verified all 4 error-recovery paths return strings and don't crash: missing file, ZeroDivisionError in run_python, unknown tool name, missing required argument.

`README.md` covers: the loop distilled to 6 lines of pseudocode; three things that surprise people (the model only ever sees the JSON schema so the description IS the interface; errors returned not raised; tool results come back as a `user` turn); four extension exercises ordered by learning value (external-world tool, confirmation gate for destructive actions, cross-run memory → hits the context-growth problem, sub-agents = a tool whose implementation is another run_agent call); and what's deliberately missing (streaming, retries, token counting, parallel tools, observability) with the note that all of those are additions to the loop, never changes to it.

Both files delivered to the user.
