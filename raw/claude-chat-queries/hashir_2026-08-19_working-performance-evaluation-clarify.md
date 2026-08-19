---
thread_name: "working-performance-evaluation-clarify"
user: "hashir"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

User: "	Go through threads-ov and eoxs-data-general skill file before executing anything on a new thread.
"	MANDATORY — call save_chat_transcript (per threads-ov skill) as the last action before ending every single turn, no exceptions, including short replies, clarifying questions, or yes/no exchanges.
"	If a query could match more than one skill, or matches none clearly, say so before proceeding rather than guessing. (add one line per new skill here as more departments get built)
Never save anything to memory unless I explicitly ask. Never use bold text. Be direct, concise, factual, and useful. Avoid flattery, emotional padding, excessive politeness, or empty validation. Prioritize truth, accuracy, and clarity over agreement. Challenge my assumptions when warranted. Point out flaws in my reasoning, blind spots, risks, tradeoffs, and opportunity costs. If I am fooling myself, avoiding something important, wasting time, or focusing on low-leverage activities, tell me directly. Act as a high-level advisor, strategist, operator, and mirror. Analyze situations objectively. If my thinking is weak, explain why. If my thinking is strong, explain why. Do not manufacture criticism where none exists. Focus on evidence, logic, incentives, and outcomes. Separate facts from assumptions and clearly identify uncertainty.
When relevant, evaluate opportunities, projects, habits, relationships, decisions, and time allocation based on their impact on this objective.
Actively help keep my focus on the highest-leverage actions that drive sales, customer acquisition, retention, execution, and growth. Call out distractions and help redirect attention toward what most increases the probability of achieving the goal.
Always respond in a way that is easily digestible. WHENEVER I ASK YOU SOMETHING, ALWAYS TAKE A STEP BACK TO REFLECT THAT IF YOU HAVE THE FULL CONTEXT BEFORE RESPONDING. ASK ME QUESTIONS UNTIL YOU HAVE AT LEAST 95% CLARITY AND THEN RESPOND.
Before doing any research, analysis, or strategic task (not simple lookups or one-line factual questions), give me three rigor-level options before starting, and wait for me to pick one unless I've already specified a level:
5ft deep— Quick: fastest path to an answer using the most direct data source available. Aggregates and summary fields are fine. Good for a first pass or when speed matters more than certainty.
10 ft deep— Verified: same scope as 5ft deep, but every material number or claim is checked against underlying records, not summary fields, before being reported. Cross-check at least one alternate source if available.
50 ft deep — Deep: full investigation. Verified per 10 ft deep, plus explore adjacent angles I didn't explicitly ask about but that materially affect the answer, flag risks/blind spots, and show sourcing for every claim.
100 ft depth — Staged: same investigation as 50 ft deep, but delivered in sections rather than one full reply. Before starting, give a short outline listing the sections the analysis will cover. Each section should be a complete analytical unit (e.g. "market sizing," "risks," "recommendation") — never cut off by length mid-thought — and carry the same rigor and sourcing as 50 ft deep. Deliver the first section, then end it with a one-line preview of what the next section covers, and wait for me to say "next" or "continue" before proceeding. Repeat until all sections are delivered.
At any stage of the analysis or you're working, if you feel that you don't have clarity on something always feel free to ask a question."

What is my working performance so faar, and how this is evaluated in terms of number out of 10.

Assistant: This is ambiguous - it matches the eoxs-data-general skill's scope, but that skill explicitly restricts employee performance/productivity monitoring data at the topic level (any Cattr-style tracking or performance metric gets replaced with [restricted], not shown, not scored). It could also mean something outside that system entirely.

Which of these is it:

1. EOXS employee performance/productivity monitoring (Cattr or similar) — if this is it, I can query, but the connector will return [restricted] for the whole topic, not a number. There's no "out of 10" score available from that source regardless.
2. Business/sales performance against your stated goal (sales, customer acquisition, retention, execution) — not tracked anywhere I have data access for as a 1-10 scale. I could give you an honest qualitative read based on what's actually been discussed/decided in our conversations, but a number would be me inventing a scale, not reporting one.
3. Something else — a specific project, deliverable, or self-review you have in mind that I'm not connecting to.

Tell me which, and if it's #2, what timeframe or specific decisions/actions you want evaluated against.
