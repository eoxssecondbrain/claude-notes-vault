---
thread_name: "claude-memory-feature-explainer"
user: "ron"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: The new memory that we have in Claude can you tell me more about it?

Assistant: Claude's memory here works as a set of plain-text files it reads and writes across conversations, not a single blob or database entry.

How it's structured: there's a `/profile.md` (who you are, role, employer), `/people/*.md` (one file per person you mention), `/areas/*.md` (ongoing projects or responsibilities), `/topics/*.md` (habits, recurring subjects), and `/preferences.md` (how you want Claude to behave — tone, format, etc). Each file has frontmatter (name, description) and tagged fact lines.

How it gets written: after each turn, a background process reviews what was said and files anything durable — a new fact, a correction, a project update. I don't do this filing live during the conversation; it happens after. The exception is if you explicitly say "remember this" or "forget that" — then I act on it in that same turn.

What decides if something gets filed: it has to be something you actually stated, not something I inferred or recommended. A one-off mention of liking a show doesn't get filed; a stated fact about your role, a person, or an ongoing project usually does. Health data, financial specifics, protected attributes (religion, race, orientation, etc), and anything covered by a "never store" list (SSNs, card numbers, minor status, criminal history, self-harm) are excluded outright, even if you ask directly.

How it gets used: at the start of a conversation I have a listing of what files exist (paths + one-line descriptions), plus your `/profile.md` and `/preferences.md` injected directly. I only read a specific file if it's relevant to what you're asking — I don't dump everything into every response. And I'm not supposed to narrate that I'm pulling from memory ("based on what I know about you") — it should just show up naturally in the answer.

Separately, there's "Search and reference past chats" — a different mechanism that lets me search your actual conversation history by keyword, rather than the synthesized fact files. Both are toggleable in Settings, and I can't turn either off myself — that's a setting you'd change.

That's the mechanism as it applies to me directly, not a third-party description of the claude.ai product page, since some of what's floating around publicly is outdated or written by SEO blogs rather than Anthropic.

User: What are all the things that you can save in your memory.

Assistant: Here's the full breakdown of what can be filed, by category:

Profile (/profile.md)
Stable identity facts — name, role, employer, what you work on at a level that stays true for months. Not day-to-day task status.

People (/people/name.md)
Anyone whose context helps future conversations — family, colleagues, clients, contacts. Their relationship to you, what you work on together. Not their private health/legal/personal details.

Areas (/areas/name.md)
Ongoing projects, responsibilities, or recurring commitments — a client account, a build, an oncall rotation, a formation you're setting up. Decisions, constraints, deadlines, current status.

Topics (/topics/domain.md)
Recurring patterns about you — habits, routines, tool preferences, communication style — once something comes up more than once or you dwell on it. A single passing mention doesn't get filed on its own.

Preferences (/preferences.md)
How you want me to behave — format, tone, verbosity, what to skip. This is meta-feedback about my responses, not facts about you.

What never gets filed, even if you explicitly ask:

- Protected attributes: race, ethnicity, religion, sexual orientation, gender identity, disability, serious illness, union membership
- Sensitive info: political beliefs, financial details (income, net worth, debts, credit scores), health data (diagnoses, therapy, medications, allergies)
- Absolute no-gos regardless of setting: SSNs/government IDs, financial account or card numbers, caste, immigration status, sexual history, abuse history, criminal history, suicide/self-harm/disordered eating (in any personal sense), psychological/personality inferences I or another AI made that you haven't confirmed as your own, and anything that would itself be a usage-policy violation

Also excluded on principle, not privacy:

- Anything I fetched (search results, calendar/email/drive data) — that's re-queryable, not memory
- My own suggestions, drafts, or reasoning — only what you actually said or decided
- Today's specific task status — the area persists, but "fixed the bug at 3pm" doesn't

And a filing only happens if it clears a bar: a single "sounds good" doesn't file ten unstated specifics, and a one-off preference gets filed as a one-off, not upgraded into a generalization.
