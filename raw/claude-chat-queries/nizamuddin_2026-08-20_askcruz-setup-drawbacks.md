---
thread_name: "askcruz-setup-drawbacks"
user: "nizamuddin"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

USER: If I ask any prompt what the architecture it is following, like how much data it is going to record and what the steps are going on like that.

CLAUDE: [Researched via mcp__EOXS_data_general tools: search_assets x2, search_wiki x2, get_asset "ai-joe-project-overview", get_wiki_page "IRIS" (returned unrelated "3GM Steel — IRIS AI Historical Data Preload" page), get_client_file on "wiki/concepts/Second Brain Initiative.md" to retrieve the FULL body (not just the 1500-char preview) — this was the key source.]

Final response delivered to user:

Based on the internal record, the clearest source is Rajat's own live architecture walkthrough to a Sabre Alloys client call (2026-07-14), corroborated by two internal team calls and a rollout email. This describes the same underlying system AskCruz/"Company Brain" is built on.

Layers, in Rajat's own words on that call: raw data (all emails and call transcripts, unfiltered) sits on the outside; a "wiki" layer inside it holds summarized/synthesized versions of that raw data; an index file sits on top as a table of contents. At query time the AI reads the index first, follows the most relevant link, reads that one page, and only then answers — it does not scan the entire dataset per prompt.

Steps, in order:
- Ingest — email capture is fully automated/scheduled. Call transcript capture (Fireflies) was still manual as of mid-2026, with a plan to automate it as a daily job. ERP data is meant to feed in too, per the standard pitch to new clients ("inject real-time ERP database").
- Synthesize — raw data gets turned into the summarized wiki pages. This step is explicitly not automatable via API; it requires a local Claude Code session, roughly 35-40 minutes per run. It's the one deliberately manual step in the whole pipeline.
- Index — a table-of-contents file gets updated so the AI knows which wiki page answers a given topic.
- Retrieve/answer — the AI reads the index, follows the most relevant page, reads it, answers from that.

How much gets recorded: functionally everything, on an ongoing basis, not a snapshot. EOXS's own message to a client (Sabre Alloys, June 2026) states it plainly: "we've successfully implemented an AI Second Brain... that consolidates context from our emails and Zoom calls into a single resource... Email and Zoom feed directly into this system, hence going forward those will be our primary channels of communication." That's total capture of both channels, positioned as the canonical record going forward, not a selective assistant. Separately, the client-facing "Prompt History" feature is described as saving every chat and every question, including prompts that get edited after the fact — the edit itself is retained, not just the final version.

The parts that actually matter for reliability and record-keeping risk:
- A real ingestion failure already happened: a key email thread got silently dropped because the pipeline was filtering by a hardcoded per-client contact list — anything from a sender not on that list was never captured at all. The documented fix is to fetch everything unfiltered; that rule is now written into the system's governing doc, but no dated record confirms exactly when it went live.
- A second, unconfirmed concern flagged internally but never verified: whether the AI-generated summaries sometimes drop real content when compressing raw data into the wiki layer.
- Access control was unsolved as of mid-July: Rajat said he personally couldn't safely share his own account internally because role-based access (full access vs. a role scoped to one module) hadn't been built yet — which is the same root cause behind the intern/functional-team access confusion flagged in the last answer.
- Scalability is genuinely ambiguous in the record: a team call mentions a SQL server "finished, locally" because the git-based structure "would have broken at a certain point," but it's unclear whether that refers to this internal system or the separate client-facing ERP backend (which is confirmed moving to Postgres on that same call). The transcript itself doesn't resolve which one.
- A cost-tiering system, meant to let a user choose cheap/shallow vs. expensive/deep per query, was discussed as something still in development — meaning today there's no confirmed way to control what a given prompt costs before sending it.

Net: near-total, continuous capture of both channels, run through one manual synthesis step and an index-driven retrieval step — with a documented instance of data silently going missing, and no finished access-control layer as of the last update on record.

Source: wiki page "Second Brain Initiative" (eoxs-db), citing the 2026-07-14 Sabre Alloys architecture walkthrough, the 2026-07-01/02 and 2026-07-31 internal team calls, and the 2026-06-02 rollout email to Sabre Alloys.
