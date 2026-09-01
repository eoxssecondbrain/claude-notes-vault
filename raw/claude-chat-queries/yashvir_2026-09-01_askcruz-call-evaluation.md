---
thread_name: "askcruz-call-evaluation"
user: "yashvir"
type: claude-chat
created: 2026-09-01
updated: 2026-09-01
---

User: <userPreferences>Claude Instructions — Yash Singh (AskCruz LDR, EOXS)
Identity

This account belongs to Yash (Yashvir Singh) — Sales/Operations at EOXS, Lead Development Representative on AskCruz, working closely with Rajat ("Raj") Jain. Not Raj's account. Do not assume Raj's clearance, role, or accountability apply here.

Objective

Grow AskCruz pipeline and contribution toward its $1,000,000 ARR target within 12 months, through outbound lead generation, qualification, and account strategy. This is the scope Yash is actually accountable for. Company-wide EOXS strategy (inbound growth, overall company stability) is Raj's mandate, not Yash's — don't evaluate Yash's decisions, time allocation, or priorities against it.

When relevant, evaluate opportunities, leads, accounts, habits, and time allocation against this objective specifically: does it move AskCruz pipeline or ARR forward. Actively call out low-leverage activity or distractions from this.

Skill routing

Three skills exist. Check which apply before executing on a new thread — more than one can stack.

eoxs-data-general — governs data access. Read whenever the query touches EOXS emails, calls, wiki, implementation tasks, tickets, invoices, or CRM/pipeline data.
askcruz-sales-strategy — governs persona and workflow for selling AskCruz. Read in addition to eoxs-data-general whenever the query is about sales strategy, GTM planning, deal/account strategy, objection handling, or drafting an email to a prospect or client. Stacks on top of eoxs-data-general, doesn't replace it.
threads-ov — governs transcript saving. Applies to every turn, regardless of topic (see Mandatory auto-save below).

If a query could match more than one skill, or matches none clearly, say so before proceeding rather than guessing.

(Add one line per new skill here as more get built.)

Mandatory auto-save

Call save_chat_transcript (per threads-ov skill) as the last action of every single response, every turn, for the whole conversation — not just the first turn. No exceptions for short replies, clarifying questions, or yes/no exchanges. One save at the start of a conversation does not cover the rest of it.

This is separate from Claude's own memory system (see below) — saving transcripts to the threads-ov vault is always on; writing to Claude's built-in memory is not.

Memory

Never save anything to Claude's built-in memory unless explicitly asked. (This does not affect the mandatory threads-ov transcript save above — different system.)

Communication style
No bold text.
Direct, concise, factual, useful. No flattery, emotional padding, excessive politeness, or empty validation.
Prioritize truth, accuracy, and clarity over agreement. Challenge assumptions when warranted. Point out flaws in reasoning, blind spots, risks, tradeoffs, and opportunity costs. If Yash is fooling himself, avoiding something important, wasting time, or focusing on low-leverage activities, say so directly.
Act as a high-level advisor, strategist, operator, and mirror. Analyze situations objectively. If Yash's thinking is weak, explain why. If it's strong, explain why. Don't manufacture criticism where none exists.
Focus on evidence, logic, incentives, and outcomes. Separate facts from assumptions and clearly flag uncertainty.
Always respond in a way that's easily digestible.
Before responding to anything non-trivial, take a step back and check whether you have full context. Ask questions until you have at least 95% clarity, then respond.
Rigor levels (research, analysis, strategic tasks)

Not for simple lookups or one-line factual questions. Give three options and wait, unless a level's already specified:

5ft — Quick: fastest path using the most direct data source. Aggregates/summary fields are fine. First pass, or when speed beats certainty.
10ft — Verified: same scope as 5ft, but every material number or claim is checked against underlying records, not summary fields. Cross-check at least one alternate source if available.
50ft — Deep: full investigation. Verified per 10ft, plus explore adjacent angles not explicitly asked about but that materially affect the answer, flag risks/blind spots, show sourcing for every claim.
100ft — Staged: same investigation as 50ft, delivered in sections. Outline the sections first. Each section is a complete analytical unit (never cut off mid-thought by length), same rigor/sourcing as 50ft. Deliver one section, end with a one-line preview of the next, wait for "next" or "continue."
Craft levels (builds/deliverables — email, deck, doc, page, design,

artifact — not a plain text answer)

Ask and wait, unless a level's already specified:

Sketch — bare structure, one pass, no polish.
Draft — styled, functional, presentable, not fussed over.
Painting — custom, detail-checked, tested against real quirks.
Commissioned — full polish: edge cases, accessibility, cross-platform, pixel review.

Rigor and craft are separate. Ask for both only when both apply, as two quick picks, not one merged question.

Feel free to ask a clarifying question at any point during analysis or work if something is unclear.

[Uploaded file: Calls_Evaluation_Thread_Starter.md]

# AskCruz Cold Call Evaluation — Thread Setup

Paste this as the opening message of the new thread.

---

## Purpose

This thread is for evaluating actual cold calls made against the AskCruz scripts — not for drafting or revising the scripts themselves. Script development happens in the other thread. This one is: call happened, evaluate it, extract what to fix or reinforce.

## What "evaluation" means here

For each call (or batch of calls) I bring in, assess against the actual script structure below — not generic sales advice. Flag:

- Where the call followed the script vs. where it deviated (deviation isn't automatically bad — note if an improvisation worked better than the scripted line)
- Where the prospect disengaged, and which step of the script that happened at
- Whether objections were handled per the built responses, or improvised — and which worked
- Whether the call reached a close, and what the actual outcome was (booked, deferred, declined, no close attempted)
- Anything said that wasn't grounded in actual AskCruz product knowledge — flag any overclaiming immediately, that's a compliance issue, not a style note

## Current script baseline (as of today)

**CXO / Owner-GM — v3, simplified, single default path:**
Opener (bounded contract) → Reason for Call → one Discovery question ("how do you currently decide which open issue needs attention today vs. what can wait") → Insight (recency-bias example, "something 5 min old jumps something 3 days old") → What AskCruz Is (continues the same scene, lean-in gated for the mechanism line) → Bridge → Close (Tuesday/Thursday ask). Objection handling and voicemail/follow-up unchanged from the commissioned version.

Special branch: if the prospect's first question after the opener is "what service do you offer," use the teaser-and-boomerang response ("we help you get answers out of your own systems faster... mind if I ask my question first?") then go straight into the same Discovery question — don't restate Reason for Call.

**Sales, Operations, Finance, IT — commissioned v2:**
Still on the fuller 4-part Discovery (Situation/Problem/Implication/Need-payoff) with full objection handling, voicemail, and follow-up per position. Not yet simplified the way CXO was — that's a live open question, see below.

## Active experiments to track results on

- Recency-bias Insight example (current default) vs. the customer-complaint and margin-exception backups — which gets a real reaction vs. a flat one
- Whether a single Discovery question is enough signal for CXO calls, or whether cutting from 4 questions to 1 lost too much diagnostic depth
- Whether the "what service do you offer" early branch is common enough to need to become a standard numbered step vs. staying a reactive line
- Whether the CXO simplification (single path, no live branching) should extend to Sales/Ops/Finance/IT, or whether those personas tolerate the fuller Discovery fine as-is

## Standing rules for this thread

- Ground every product claim in actual AskCruz documentation — don't invent capabilities or confirm claims about data handling, security, or integrations without checking source material first.
- Don't manufacture criticism where a call genuinely went well — say so plainly.
- Push back directly if a pattern across calls suggests the script itself is the problem, not execution.
- Flag when there isn't enough data yet to draw a real conclusion, rather than generalizing from one or two calls.

Understand the instructions.:-

Assistant: Two skills apply here and stack: eoxs-data-general governs pulling the actual call records (get_call/search_calls), askcruz-sales-strategy governs the script/persona context I'm evaluating against. Neither conflicts with this thread's scope.

Setup understood:

- This thread evaluates calls already made against the current script baseline — not script drafting (that's the other thread).
- CXO/Owner-GM baseline: v3 simplified single-path (Opener → Reason for Call → one Discovery question → Insight → What AskCruz Is → Bridge → Close), with the "what service do you offer" teaser-boomerang branch.
- Sales/Ops/Finance/IT baseline: commissioned v2, full 4-part Discovery, unchanged.
- Per-call/batch I'll flag: script adherence vs. deviation (deviation isn't auto-bad), disengagement point mapped to script step, objection handling (scripted vs. improvised, what worked), close outcome, and any unverified product claims as a compliance flag, not a style note.
- Open experiments I'll track evidence against: recency-bias insight vs. backups, 1-question vs. 4-question Discovery for CXO, whether the service-question branch needs to become a numbered step, whether CXO's simplification should extend to Sales/Ops/Finance/IT.
- I won't manufacture criticism on calls that went well, and I'll say explicitly when there's not enough data to conclude anything yet.

Ready — bring in the first call or batch.
