---
thread_name: "eoxs-skills-qa-queries"
user: "nidhi"
type: claude-chat
created: 2026-08-22
updated: 2026-08-22
---

# eoxs-skills-qa-queries

## User

working these skills so far. I am not able to think where it can skip i want comprehensive quiries for qa

(IDE selection: lines 1–32 of `c:\Users\91623\Desktop\eoxs-skills\connector-instructions.txt` — the Threads OV archiving instructions.)

## Assistant

This conversation is archived to Threads OV.

Read both skill files (`eoxs-data-general/SKILL.md`, `threads-ov/SKILL.md`) and wrote a comprehensive QA suite to `QA-QUERIES.md` — ~150 paste-and-run prompts across 17 sections (A–Q), each with what it probes, what passing looks like, and the specific skip signal to watch for. Sections: archiving, session bootstrap/get_index, connector routing, access scope + redaction, read-only boundary, freshness, tool discipline/call efficiency, decision trees, answer shape, injection/exfiltration, unlisted-tool discipline, Threads OV SYNTHESIZE, Threads OV CROSS-LINK, Threads OV guardrails, adversarial/social engineering, multi-turn state, and known spec gaps.

Highest skip-risk areas identified:

1. Archiving on cheap turns — one-word replies, off-topic questions, error turns, refusals, and turns ending in a question. Also trigger-1 crowd-out: on a heavy multi-tool turn the "save first" call is the one that gets displaced.
2. Pre-emptive refusal on sensitive topics — §2 says call the tool first and let the redacted response be the answer; the natural failure is declining before calling anything.
3. Unlisted-tool discipline — with HR, OV2, staging, odoo, and Gmail connectors visible, a request like "list all employees" has a tempting tool sitting right there.
4. Call efficiency — get_client_profile once vs rebuilding from three searches; get_business_schema first on teams.

Twelve genuine spec gaps found (§Q), where the skill text does not settle behaviour:

- Q1 Payload contract conflict: the skills say `save_chat_transcript(thread_name, content)` with the full conversation verbatim because the tool overwrites. The THREADS_DB_RAJ connector's own instructions say `new_messages` = only the new exchange, because the server appends and dedupes. Opposite contracts.
- Q2 Two archive targets: THREADS_DB_RAJ and threads_ov_nidhi both expose save_chat_transcript; nothing says which is the destination.
- Q3 Tool count contradiction: the connectors table says eoxs-db has 17 purpose-built tools; §5 says 20 and lists 20.
- Q4 Redaction on eoxs-teams: §2 says amounts are stripped from "every response", then says the tiering does not apply to eoxs-teams. Biggest ambiguity in the file.
- Q5 Transcript size: content must be the full verbatim conversation with no stated cap.
- Q6 "Plausibly answerable from correspondence" is undefined, making ticket/invoice routing a coin-flip.
- Q7 Duplicate first-turn archive notice — both skills carry the same line.
- Q8 save_analysis ask-first vs an explicit user request.
- Q9 User-pasted confidential data flowing into the archive.
- Q10 get_index() failure has no defined path.
- Q11 "Either connector" wording in §3 doesn't cover the odoo connector's write tools.
- Q12 Push-confirmation conflict between threads-ov §2 step 5 and §0's automatic push.

Also included a 10-minute smoke test of eight prompts covering the paths that matter most.
