---
thread_name: "eoxs-salary-promotion-structure"
user: "danish"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: i want to know about salary and promotion structure in EOXS, what do you know about it which you can share with me

Assistant: No memory or context available on this. Flagged that this looks like an HR policy question, not something in transactional EOXS DB tables. Asked whether to check EOXS docs for existing policy vs help draft one from scratch.

User: yes

Assistant: Asked clarifying question (ambiguous "yes") via options tool: check existing docs vs draft from scratch.

User: Check EOXS docs for an existing policy

Assistant: Searched EOXS Data General repo docs (search_repo_docs for "salary", "promotion", "compensation") and list_repo_docs (full catalog) — all returned empty. Conclusion: no documented salary or promotion structure exists in accessible EOXS repo docs. Flagged this as an operational risk given company growth objectives, and asked whether user wants to prioritize building this now or if it's lower priority. Noted would need real inputs (team size, roles, pay bands) to draft anything — will not invent numbers.

User: are you using all the connectors that has been configured?

Assistant: Reported connector usage: used EOXS Data General and Team EOXS MCP (searches came up empty) for this task; other connectors (Fireflies, Gmail, Team EOXS MCP query, Zoho Mail) not used as not relevant to this query. Flagged self-correction: had not been following two of Danish's standing preferences — (1) consulting threads-ov skill at start of new thread, (2) calling save_chat_transcript as last action of every turn. Acknowledged the miss and proceeded to load Thread OV tools and save this transcript.

Status: EOXS salary/promotion structure confirmed to be undocumented in accessible systems. Open question to Danish: build one now (low priority given AskCruz/EOXS stability focus) or drop it. No decision made yet.
