---
thread_name: "n8n-email-automations-askcruz"
user: "jaskeerat"
type: claude-chat
created: 2026-08-17
updated: 2026-08-17
---

# n8n Email Automations & ASKCRUZ Sales Intelligence Engine

## 1. Email to Local DB Automation
User: I have to create an n8n automation for my mail that whenever data comes in, it's stored in a local database. Users authorize an email account (OAuth, secret token/JSON) so the workflow can fetch email and push data to the DB. Build the importable workflow.

Claude asked clarifying questions and confirmed:
- Gmail (OAuth), local PostgreSQL, all inbox emails, full fields (from/to/subject/body/date/message-id), poll every 5 min, on n8n cloud, table auto-created, dedupe/skip on message_id, attachments saved to local disk with only the file path stored in Postgres (two tables: emails, email_attachments).

Claude built `email-to-db-automation.json`: Gmail Trigger -> Prepare Email Fields (Code) -> Check If Exists (Postgres SELECT COUNT) -> Is New Email? (IF) -> Insert Email Row -> Extract Attachments (Code, splits binary attachments into separate items) -> Save Attachment To Disk (Read/Write Files) -> Insert Attachment Record. Plus a manual "Setup - Run Once -> Create Tables" branch for the CREATE TABLE IF NOT EXISTS DDL.

User hit a Postgres credential error in n8n cloud: "Couldn't connect with these settings," Host=localhost. Claude explained: n8n cloud's `localhost` refers to the cloud container itself, not the user's machine — for a genuinely local DB, n8n needs to run self-hosted (e.g. on the user's VPS) alongside Postgres, or Postgres needs to be reachable via a public/tunnel address. Later, user asked generally "how to connect a hosted n8n server to localhost database server" — Claude gave 4 options (expose Postgres publicly with restrictions, SSH reverse tunnel, Cloudflare Tunnel/ngrok, or self-host n8n on the same VPS as Postgres) and recommended self-hosting n8n on the existing VPS as the cleanest fit.

## 2. Email Filter (Spam/Promo) + Store to Local DB
User: create a new workflow where it filters out spam and promotional mails and deletes them, rest data stored in local database.

Claude clarified: detection method = Gmail's own labels (SPAM + CATEGORY_PROMOTIONS), "delete" = move to Trash (not permanent), and this should be a new standalone workflow (not extending the first one).

Built `email-filter-and-store.json`: Gmail Trigger (includeSpamTrash: true) -> Is Spam or Promo? (IF, checks labelIds) -> true: Trash Spam/Promo Email (Gmail trash operation); false: same pipeline as workflow 1 (Prepare Email Fields -> Check If Exists -> Insert -> Attachments).

User then asked to add a verification step: "after filtering, another AI agent should verify and then delete the spam/promotional messages." Claude rebuilt as `email-filter-ai-verified.json`: Is Spam or Promo? (label check) -> AI Verify Spam/Promo (HTTP Request to Anthropic API, claude-sonnet-5, asks it to confirm/override the label-based classification using sender/subject/snippet) -> Parse AI Verdict (Code, defaults to "legitimate"/do-not-delete if the AI response is unparseable - fail-safe) -> AI Confirms Spam? (IF) -> true: Trash; false: falls through to the normal save-to-database pipeline (treated as a Gmail false-positive).

## 3. Query-to-Email Draft (Gmail + Odoo + eoxs-wiki-db)
User: Build an automation where typing a query fetches all data from Gmail, the EOXS Odoo platform (teams.eoxs.com), and a database regarding that query, and creates an email; also store a copy in Google Sheets.

Claude clarified via Q&A:
- Trigger: n8n chat trigger (typed message)
- Data sources: Gmail, Odoo (EOXS Teams live MCP), eoxs-wiki-db/Cruz knowledge base (OV2 MCP)
- Output: save as Gmail draft only (never auto-send)
- Log copy to: Google Sheets only
- Recipient: typed directly in the query text by the user (e.g. "draft an email to john@client.com about...")

Built `query-to-email-draft.json`: When Chat Message Received (LangChain chatTrigger) -> Email Research Agent (LangChain AI Agent, Claude Sonnet 5 as the language model) with three tools: Gmail Search Tool (gmailTool node), Odoo (EOXS Teams) MCP Tool (mcpClientTool, https://eoxsteammcp.lancerdevops.me/mcp, httpStreamable transport), eoxs-wiki-db (OV2) MCP Tool (mcpClientTool, https://5.223.44.95/mcp/.../sse, sse transport). Agent's system prompt: extract recipient from the query text, research via tools, don't fabricate, output strict JSON {to, subject, body}. -> Parse Agent Output (Code, fail-safe parsing) -> Create Gmail Draft (resource: draft, operation: create) -> Log to Google Sheets.

User later asked why the Gmail draft-creation output only showed `{id, threadId, labelIds: ["DRAFT"]}` and wanted the full draft (body, sender, etc.) saved. Claude explained the DRAFT label confirms success but the API returns a minimal stub; the full content was already being logged to Sheets from Parse Agent Output. User wanted the raw Gmail message object's full details too (including sender), so Claude added: Get Full Draft Message (Gmail node, resource: message, operation: get, messageId from Create Gmail Draft's output id) -> Parse Full Draft (Code, extracts From/To/Subject/Date/body from headers/payload) -> updated Log to Google Sheets with columns timestamp | query | from | to | subject | body | date | gmail_draft_id | gmail_thread_id.

### Debugging round
User hit "Could not connect to your MCP server" on the Odoo (EOXS Teams) MCP Tool node in their self-hosted n8n (v1.121.3). Claude's top diagnosis: the SSE Endpoint field pointed at a URL ending in `/mcp` (Streamable HTTP) but the node might be using SSE transport - transport/endpoint mismatch, plus gave general troubleshooting (curl test, network reachability, auth requirement check, compare against other MCP connectors).

User then uploaded their actual live-exported workflow JSON. Claude diffed it against what it had built and found 5 real issues:
1. **Get Full Draft Message node lost its config** - reset to `operation: getAll` with empty filters, no `resource: message`, no `messageId` - meaning it fetched a generic message list instead of the specific just-created draft. (Most serious bug.)
2. **Both MCP Tool nodes lost their transport settings** - only `sseEndpoint` + empty `options` remained, no explicit `serverTransport`/`authentication`/`include`. Very likely the actual cause of the earlier "Could not connect" error (defaulting to SSE against the Odoo endpoint that needs Streamable HTTP).
3. **Log to Google Sheets reverted to `autoMapInputData`** instead of the explicit column mapping - would produce blank `timestamp`/`query` columns and mismatched field names (`from_address` vs `from` etc.).
4. **Create Gmail Draft had no explicit `operation`** field (just `resource: draft`), relying on an implicit default.
5. **Gmail Search Tool had `disabled: true` set** - agent silently skipping Gmail search.

Claude fixed all 5 in a corrected file `query-to-email-draft-fixed.json`, preserving the user's real credential IDs and Google Sheet reference (`Mail Draft` sheet, `gid=0`) so no reconnection needed. Explicitly set: Get Full Draft Message to `resource: message, operation: get, messageId: {{ $json.id }}`; Odoo MCP Tool to `serverTransport: httpStreamable`; OV2 MCP Tool to `serverTransport: sse`; Log to Google Sheets back to `defineBelow` with columns matching Parse Full Draft's renamed output fields (timestamp, query, from, to, subject, body, date, gmail_draft_id, gmail_thread_id); Create Gmail Draft given explicit `operation: create`; Gmail Search Tool re-enabled.

Claude then gave the user two test prompts to try in the n8n chat trigger - a short version and a longer, more detailed version instructing the agent to explicitly search all three sources (Gmail, Odoo, eoxs-wiki-db), reference specific found details, honestly flag gaps rather than fabricate, and end with a clear next step.

## 4. ASKCRUZ Sales Intelligence & Outreach Engine
User provided a full detailed spec: identify steel-industry contacts from 3 years of calendar meetings, analyze their previous Fireflies conversations, generate personalized ASKCRUZ outreach emails, store for human review (not auto-sent), scale to hundreds of contacts, track via a status flow (Identified -> Analyzed -> Email Generated -> Reviewed -> Approved -> Sent -> Replied -> Meeting Booked), plus a separate meeting-prep workflow triggered when a prospect books a meeting. Requested a skill file, a fresh automation, and step-by-step instructions.

Claude searched for and confirmed real Fireflies GraphQL API details (endpoint https://api.fireflies.ai/graphql, Bearer auth, `transcripts(participants, fromDate, toDate, limit)` and `transcript(id) { summary { overview action_items } sentences { text speaker_name } }` fields) before building, and flagged that Fireflies' free tier caps at 50 API calls/day - a real constraint at the target scale (hundreds of contacts).

Clarified via Q&A: Google Calendar as the source, Google Sheets as storage (Contacts/Company_Classifications/Not_Qualified/Meeting_Prep_Briefs tabs), industry classification and email/brief generation via Claude (Anthropic API, httpHeaderAuth), no auto-send ever.

Delivered three files:
- `askcruz-sales-intelligence-skill.md` - architecture/data model/status flow/traceability rules/known constraints reference doc.
- `askcruz-outreach-pipeline.json` (28 nodes) - Config -> Get Calendar Meetings -> Extract Participants -> Filter Internal & Dedupe -> Remove Already-Tracked (cross-referenced against existing Contacts sheet) -> Loop Over New Contacts (per contact: domain classification with a Company_Classifications cache to avoid re-classifying, IF steel industry -> Fireflies search latest call -> IF has call -> get transcript -> analyze via Claude -> generate personalized email via Claude using an editable approved-template Config field -> store in Contacts sheet with status; non-qualified contacts logged to Not_Qualified; no-call contacts logged with status Identified).
- `askcruz-meeting-prep.json` (11 nodes) - Google Calendar Trigger (event created) -> Extract Attendees -> Loop -> Lookup Contact History in the same Contacts sheet -> IF found -> Claude generates a call-prep brief (software used, prior discussion points, pain points, suggested opening line); if not found, notes plainly that there's no prior history -> stores to Meeting_Prep_Briefs sheet + creates a Gmail draft notification.

Claude gave a detailed step-by-step setup card (spreadsheet/tabs setup, import, credentials incl. a reused Anthropic Header Auth credential and a Fireflies Header Auth credential with the "Bearer " prefix reminder, filling in placeholders, testing on a small date-range slice first before the full 3-year pull, running the pipeline in batches given the Fireflies rate limit, activating meeting-prep only once Contacts has real data, and manual review/send process), and flagged this as the most complex/least field-tested workflow built in the conversation - likely needing a debugging pass on Fireflies query field names and Calendar attendee field names on first real run.

## Key ongoing facts
- User is Raj, CEO/founder of EOXS (Prata Inc.), an AI-first ERP on Odoo 13 for steel service centers.
- Uses a self-hosted n8n instance (confirmed v1.121.3) alongside their VPS (5.223.44.95) infrastructure.
- Has existing MCP connectors: `EOXS Teams live` / `eoxsteammcp.lancerdevops.me/mcp` (Odoo, Streamable HTTP), `OV2` (eoxs-wiki-db, SSE).
- ASKCRUZ is a separate outreach/product initiative from the core EOXS ERP business.
