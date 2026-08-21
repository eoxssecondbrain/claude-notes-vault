---
thread_name: "buildix-mailcow-mcp-setup"
user: "Harsimran"
type: claude-chat
created: 2026-08-21
updated: 2026-08-21
---

**User:** what is buildix

**Assistant:** The Thread_OV connector failed to connect this session, so I can't call `save_chat_transcript` right now — flagging per your preference rather than silently skipping it.

**Buildix**: a vertical-marketing website EOXS built for the plastics industry, part of Sheenam Rawat's marketing vertical-expansion project (code name "Operation Helios," started March 2026), later folded into the "EOXS Media Division." Kriti Jain was onboarded in June to work on it.

---

**User:** i want to connect my mail cow mail with you , how i can do that?

**Assistant:** No Mailcow-specific connector exists in the registry. Options:

- **No native "Mailcow" integration** — it's self-hosted, so there's no plug-and-play connector like there is for Gmail/Outlook.
- If Mailcow exposes IMAP/SMTP (it does by default), you'd need a generic IMAP/SMTP MCP connector — none is currently installed or in the registry results I found.
- Easiest path: check if your org admin can add a custom MCP connector pointing at Mailcow's SOGo/IMAP API, or set up a generic email connector via claude.ai admin settings → Capabilities.

Want me to search more specifically (e.g. "IMAP", "SOGo", "custom connector setup") or should I stop here?

---

**User:** its a smpt mail, i want to connect it with connector

**Assistant:** No generic SMTP connector exists in the registry either — connectors in claude.ai are pre-built integrations (Gmail, Resend, AgentMail, etc.), not raw protocol connections like SMTP/IMAP.

For a self-hosted Mailcow account, your options:

- **Custom MCP server**: your org admin builds/hosts a small MCP server that talks to your Mailcow's SMTP/IMAP, then registers it as a custom connector in claude.ai admin settings → Capabilities. This is the real "connect it with a connector" path but needs someone to write it — there's no ready-made one.
- **AgentMail or Resend**: these give an agent-controlled inbox but won't connect to your *existing* Mailcow mailbox — they're separate email services.
- No-connector workaround: none really — SMTP isn't something Claude can dial into directly without an MCP server in front of it.

Want me to sketch what that custom MCP server would need to do (send via SMTP, read via IMAP)?

---

**User:** ok then create a mcp server for that mail, also where we should host that, i want to host it for free

**Assistant:** [Asked via AskUserQuestion tool]

Question 1: "What should the MCP server be able to do with your Mailcow mailbox?"
- Send only (SMTP) — Compose and send emails through Claude. Simplest, needs only SMTP credentials.
- Send + Read (SMTP + IMAP) — Send emails and also search/read your inbox. Needs both SMTP and IMAP credentials.

Question 2: "Where should this MCP server be hosted for free?"
- Render (Recommended) — Free web service tier, easy Node.js deploys, supports outbound SMTP/IMAP. Downside: spins down after 15 min idle, so first request after idle is slow (~30-60s cold start).
- Fly.io — Free allowance (small VM), stays warm, generally reliable outbound network access. Slightly more setup (flyctl CLI, credit card required even for free tier).
- I'll decide later / just build the code — Skip hosting choice for now, just write the MCP server code, I'll figure out where to run it.

**User (answers):** "Send + Read (SMTP + IMAP)"; "Render (Recommended)"

**Assistant:** [Built the MCP server project: package.json, server.js (Streamable HTTP MCP server with tools send_email, list_folders, list_recent_emails, search_emails, get_email, using nodemailer for SMTP and imapflow/mailparser for IMAP, bearer-token auth, /healthz endpoint), .env.example, .gitignore, render.yaml, README.md with GitHub push + Render deploy + Claude connection instructions. Zipped and delivered via SendUserFile.]

Built it — sent as `mailcow-mcp-server.zip` above. It's a Node MCP server exposing `send_email`, `list_folders`, `list_recent_emails`, `search_emails`, `get_email`, secured with a bearer token, with a `render.yaml` for one-click Render free-tier deploy.

Next steps (all in the README inside the zip):
1. Push the folder to a GitHub repo.
2. Deploy to Render (free web service) — Render auto-detects `render.yaml`.
3. Set env vars in Render: your Mailcow SMTP/IMAP host+port, mailbox user/pass, and a random `MCP_AUTH_TOKEN` (generate with `openssl rand -hex 32`).
4. Connect it to Claude — easiest via Claude Code: `claude mcp add --transport http mailcow-mail <your-render-url>/mcp --header "Authorization: Bearer <token>"`. If the Desktop app's custom-connector UI doesn't accept a header, use the Claude Code route instead.

One honest caveat: I built and syntax-checked this in a sandbox with no npm registry access, so I couldn't actually run `npm install` and hit the live endpoint here — test it once after deploying (or locally) before relying on it. Free Render tier also sleeps after 15 min idle, so the first request after a gap takes ~30-60s.
