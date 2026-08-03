---
thread_name: "llm-wiki-bootstrap"
user: "jaskeerat"
type: claude-chat
created: 2026-08-03
updated: 2026-08-03
---

# llm-wiki-bootstrap

## User
Pasted the "LLM Wiki" idea file (a pattern for building personal knowledge bases using LLMs — three layers: immutable raw sources, LLM-owned wiki, schema file; three operations: ingest, query, lint; index.md content catalogue + log.md chronological append-only record). Asked Claude to act as the LLM wiki agent, implement the idea as a complete second brain, guide step by step, create a "cloud.mmd" schema file with full rules, set up index.md and log.md, define folder conventions, and show the file as an example. From now on every interaction follows the schema.

## Assistant
Interpreted "cloud.mmd" as CLAUDE.md (the file Claude Code auto-loads each session; .mmd is Mermaid and would not be read automatically). Found the working directory to be an empty Obsidian vault at c:\Users\aastha\Pictures\RANJAN\llm-wiki.

Built the scaffold:
- CLAUDE.md — full schema: §0 Domain (left UNSET pending the user's subject), three-layer table (raw/ immutable, wiki/ agent-owned, CLAUDE.md co-evolved), folder conventions, kebab-case naming, wikilink rules, required YAML frontmatter spec (type/title/created/updated/status/confidence/tags/sources), citation rule with [Synthesis]/[Uncertain]/[Outside wiki] markers, the INGEST/QUERY/LINT procedures, index+log rules, writing style, 9 hard rules, session-start rule.
- Folders: raw/, raw/assets/, wiki/{sources,entities,concepts,questions,synthesis}/, templates/
- templates/{source,entity,concept,question}.md
- index.md (content catalogue, with an "unwritten pages" section) and log.md (append-only, greppable `## [YYYY-MM-DD] kind | title` headers)
- wiki/synthesis/{overview,thesis,open-questions,contradictions}.md
- Demonstrated a real end-to-end ingest using the idea file itself as source #1: raw/2026-08-03-llm-wiki-idea.md -> wiki/sources/2026-08-03-llm-wiki-idea.md + wiki/concepts/persistent-wiki-pattern.md, with index and log updated.

Discovered mid-task that the user had dropped five large sources into raw/ (articles.md 323KB, books.md, festival.md, an Indian street food guide, and "The 22 best things to do in India") — suggesting the wiki's domain is India travel/culture. Flagged these and asked the user to confirm the domain before ingesting, per the schema's discuss-before-writing rule.
