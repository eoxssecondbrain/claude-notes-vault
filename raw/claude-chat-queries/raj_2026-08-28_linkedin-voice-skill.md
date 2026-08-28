---
thread_name: "linkedin-voice-skill"
user: "raj"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

**User:** I want to make a skill in Claude that will be my LinkedIn voice.

**Assistant:** This is a skill-creator task — capturing your LinkedIn voice as a reusable skill. Before I draft anything, I need a few specifics.

[Called ask_user_input_v0 with three questions:
1. "What should the skill actually do?" — options: "Write full posts from a topic/idea I give it", "Polish/rewrite drafts I already wrote", "Both — draft from scratch and polish existing drafts"
2. "Where should it learn your voice from?" — options: "Analyze my past LinkedIn posts (paste or connect them)", "I'll describe my tone/style manually", "Both — analyze past posts, I'll correct/add nuance"
3. "Craft level for building this skill?" — options: "Draft — functional, presentable, not fussed over", "Painting — custom, detail-checked, tested against real quirks", "Commissioned — full polish, edge cases covered"]

**User:**
Q: What should the skill actually do?
A: Both — draft from scratch and polish existing drafts

Q: Where should it learn your voice from?
A: Analyze my past LinkedIn posts (paste or connect them)

Q: Craft level for building this skill?
A: Commissioned — full polish, edge cases covered

**Assistant:** [Searched MCP registry for a LinkedIn/personal-post-export connector — keywords: "linkedin", "social posts", "content export". Results returned were ad-analytics and B2B lookup tools (Windsor.ai, Supermetrics, Crustdata, Meltwater, etc.) — none suited to pulling the user's own published post history.]

No LinkedIn connector fits pulling your own post history directly — the closest options here are ad-analytics/company-lookup tools, not a personal-post exporter. Paste in your posts instead.

Send me 8–15 of your past LinkedIn posts (the better ones, and a couple you felt were flat — contrast helps). Paste the text directly, or if you have them in a doc/export, upload it and I'll read it.

**User:** [Pasted 10 LinkedIn posts, verbatim, covering topics: (1) "ERP replaced filing rooms" reframe about AI removing the reason to search, with an ops-guy anecdote and "FASTER DECISIONS!!!" closer; (2) short post on AI replacing and creating inside sales jobs; (3) "AI isn't software, it's more like hiring someone" post with forklift analogy and MIT 95%/300 companies stat, ending with a question about real AI learning examples; (4) short post contrasting a 2026 manager (15 humans) vs 2030 manager (50 AI agents, 5 humans); (5) "AI won't replace you, the person/company using AI will" post walking through old ERP assumptions vs new AI-participatory assumptions, ending with "systems of record to systems of action" and a competitor line; (6) "sales problem vs visibility problem" post with Camp A/Camp B framing; (7) short post on three companies met last month (1,400 open quotes / no follow-up process / can't identify lapsed customers); (8) "Steel CEO: We want AI. Me: Where is your data today?" dialogue post about AI scaling chaos, ending with a direct callback line; (9) and (10), identical duplicate posts: "The new ERP is slowing us down" post using the barista/coffee-shop-line analogy, ending with a question about what's behind implementation slowness.]

**Assistant:** Sounds good — send over the posts whenever ready. Once I have them, I'll build out the skill (voice analysis → SKILL.md with your patterns, guardrails, and output format) at Commissioned level, then we'll test it against a couple of real topics before you save it.

[Note: this line was generated before the posts had fully registered in sequence; the actual substantive build followed once the posts were processed, as below.]

[Viewed /mnt/skills/examples/skill-creator/scripts directory to confirm packaging tooling was available. Created /home/claude/linkedin-voice/SKILL.md — a full skill file analyzing the 10 posts, covering: Section 1 "The core move: reframe, not report" (opening thesis pattern with examples); Section 2 "Structural DNA" (one-clause-per-line, short declaratives, concrete scenes, load-bearing analogies, parallel construction, dialogue snippets, single-device closes, quiet optional company mentions); Section 3 "Voice texture" (no hashtags/emoji except rare ALL CAPS, contractions, direct address, dash-list formatting, repeated structural patterns, industry-insider register); Section 4 "What this voice does NOT do" (no hedging, no corporate openers, no stacked analogies, no dense paragraphs, no fabricated stats/quotes, no hashtags/lazy closers); Section 5 "Workflow: drafting from a topic/idea"; Section 6 "Workflow: polishing an existing draft"; Section 7 "Pre-send checklist".]

Built the skill. Two quick test runs against it before you review:

Test 1 — draft from a topic (using the SMU Steel Summit objection you ran into: ERP vendors "already building their own AI"):

> Every ERP vendor at the conference said the same thing this year.
>
> "We're building AI too."
>
> Cool. So is everyone.
>
> Here's the question nobody on the floor was asking back: what does your AI actually know about this specific customer's mill lead times, their pricing quirks, the email thread from March where the deal almost died?
>
> Because "we have AI" and "we have AI that's been trained on your business for six months" are not the same product.
>
> One is a feature.
>
> The other is a hire.
>
> A prospect asked me flat out — how is this different from Microsoft Copilot?
>
> Copilot is smart on day one and stays exactly that smart.
>
> It never learns your grades, your customers, or why that one account calls every Friday at 4pm.
>
> Ours does.
>
> That's the whole bet.

Test 2 — polish an existing rough draft. If you send me a real one of yours you weren't happy with, I'll run it through and show before/after side by side — better proof than me inventing a bad draft to fix.

Checklist pass on Test 1: reframe opener, real conference anecdote, one analogy (feature vs. hire), quiet company mention, closes on a callback line, no hashtags/hedging.

How does Test 1 read — close enough, or is something off (too aggressive on Copilot, wrong anecdote, wrong rhythm)? Once you confirm, I'll package the skill file for you to save.

**User:** In addition, I want to even utilize the intelligence of what we are doing at AskCruz and what we are doing at AI. I want to be careful of not dropping customer names, but I can share any positive customer experiences without sharing the names in the post or in comments to other people's posts.

**Assistant:** [Edited /home/claude/linkedin-voice/SKILL.md via str_replace to add a new bullet under Section 4 — "Never names a customer/client company — not in a post, and not in a comment drafted for someone else's post. This holds even for a purely positive story. See Section 4a." — and a new Section 4a "Using AskCruz/EOXS customer material — anonymize, always" covering: describing accounts by category/size/region/problem rather than name; the rule applying identically to comments on other people's posts; pulling the shape of a story while stripping the identifying wrapper when Raj supplies specific deal/client detail; and a standing note that Sabre Alloys must never appear in external-facing content. Also updated the Section 7 checklist to add "No customer/client company is named or identifiable, in the post or in any comment drafted for someone else's post."]

The skill now has an anonymization rule (section 4a) — customer experiences are usable material, names never are, and it applies equally to comments you drop on other people's posts, not just your own.

Quick check before I lock this in: for the "what we're doing at AskCruz" material — should the skill pull that context from what you paste into the chat each time, or do you want it to be able to reach into deal/client data (OV2) to find real anonymized examples on its own? That changes whether this stays a pure writing skill or also needs data access baked in.

**User:** both

**Assistant:** [Edited /home/claude/linkedin-voice/SKILL.md to add a new Section 4b "Sourcing customer material — chat context or the vault, both fine," covering two sourcing paths: (1) what Raj pastes/describes in chat, used directly and anonymized per 4a; (2) pulled proactively from EOXS/AskCruz data via the raj-eoxs-vault skill's tools (get_client_profile, search_implementation_tasks, search_calls, search_emails on eoxs-db; eoxs-teams for tickets/CRM/pipeline shape) when Raj hasn't supplied a specific example, anonymized before reaching the draft, following raj-eoxs-vault's access-tier and connector rules. Also specified that either way only the anonymized shape of the story (size band, problem, number, outcome) lands in the post, never the source detail, and that a vault-sourced pull should be flagged plainly to Raj when presenting the draft. Caught and fixed an accidental deletion of the Sabre Alloys standing-rule bullet during the edit, restoring it with correct spacing before the new Section 4b.]

Fixed. Also updated the Section 7 checklist to reflect this — worth showing you the whole current file before we test it again.

[Viewed the full current /home/claude/linkedin-voice/SKILL.md file (191 lines) to confirm the edits landed correctly.]

**User:** no, but I wanted to create a separate skill for this, and I wanted just the write-up with which I can create the skill and connect it with my Claude account. Can you undo whatever you did right now and just give me the skill write-up

**Assistant:** [Edited /home/claude/linkedin-voice/SKILL.md via str_replace to remove the entire Section 4b "Sourcing customer material — chat context or the vault, both fine" that had just been added, reverting the file to only Section 4a's chat-context-based anonymization rule, with no vault-sourcing content.]

Reverted — the skill now only covers what you paste/describe in chat, anonymized per 4a. The vault-sourcing piece is out; that's its own skill for later.

Here's the full write-up to create the skill with (name: linkedin-voice):

```markdown
---
name: linkedin-voice
description: Write or polish LinkedIn posts in Raj Jain's voice — steel-industry-insider reframes on AI/ERP, short punchy line-broken sentences, concrete anecdotes over abstractions, contrarian openers, dialogue snippets, closing questions. Use whenever Raj asks to draft a LinkedIn post, turn a topic/idea/note into a post, polish or tighten an existing LinkedIn draft, or asks "how would I say this on LinkedIn." Trigger even if he just pastes a rough idea and says "make this a post."
---

# Raj's LinkedIn Voice

Built from 10 of Raj's actual posts (steel ERP / AskCruz content). This is a
voice skill, not a fact skill — the job is to sound like him, not to verify
industry claims (though never invent a stat, study, or number he didn't give you).

---

## 1. The core move: reframe, not report

Almost every post opens by taking a common belief and inverting or sharpening
it in one line, stated as flat fact — not "I think" or "in my opinion."

- "ERP replaced filing rooms. AI will replace the reason people went into the filing rooms."
- "AI won't replace you. The person / company using AI WILL."
- "Everybody keeps calling AI 'software.' It isn't."
- "Most steel distributors think they have a sales problem. True. But — most have a visibility problem. Also true."

The opener is the thesis. Everything after it proves, complicates, or lands
that one line. If you can't compress the point into one sharp sentence first,
the topic isn't ready yet — go back and find the reframe before drafting.

## 2. Structural DNA

- **One clause per line.** Sentences get broken across multiple lines even
  when they'd fit on one. This isn't random — it controls pacing and forces
  a beat between ideas. Don't write dense paragraphs and call it done.
- **Short declaratives, no hedging.** "That's not an intelligence problem.
  It's a filing room problem." Not "This might suggest..." He states things.
- **A concrete scene, not an abstraction.** A call with a specific ops guy
  at a specific-sized company. A steel CEO conversation happening for the
  18th time in 4 months. A vendor who "walks in here selling AI." Real
  numbers when he has them (1,400 open quotes, 95% from an MIT study of
  300 companies). If you don't have a real anecdote or number, don't
  invent one — ask Raj for the specific or write the post structurally
  sound but flag the gap rather than fabricating a stat or quote.
- **A load-bearing analogy.** Filing room. Forklift vs. hiring someone.
  The barista who won't let you cut the line. One analogy per post,
  developed for 2-4 lines, not decoration — it usually carries the whole
  argument.
- **Parallel construction as a rhythm device**, especially for 3-beat lists:
  "Instead of: 'Can my software tell me how much inventory I have?'
  Companies will ask: 'What do I need to buy next week?'"
  repeated 2-3 times with the same sentence shape.
- **Dialogue snippets**, quoted directly, often 1-2 lines:
  "Steel CEO: We want AI. Me: Where is your data today?"
- **The close is either a question or a callback to the opener** — rarely
  both. Question: "Tell me — what reasons have you uncovered..." Callback:
  "AI is not a faster way into the filing room. AI is the thing that
  removes the reason anyone opens it." Pick one, don't stack them.
- **The company mention is optional and quiet.** EOXS/Cruz shows up in
  maybe half the posts, almost always as a single understated line near
  the end ("That's why we built Cruz," "At EOXS, we're seeing this shift
  happen in real time") — never a pitch, never more than one line, never
  first. Don't add a plug if the topic doesn't naturally earn one.

## 3. Voice texture

- No hashtags. No emojis (one exception seen: sparing use of ALL CAPS for
  a single punch line or tagline, e.g. "FASTER DECISIONS!!!" — rare, use
  once per post at most, and only right at the end).
- Contractions throughout (it's, doesn't, won't) — never stiff or corporate.
- Occasional direct address to the reader ("Before you hire another
  salesperson, make sure you're not leaking revenue from customers you
  already have").
- Numbers as bare list items with a leading dash, no bullet formatting:
  ```
  - some in the system
  - some in Excel
  - some in people's heads
  ```
- Willing to repeat a structural pattern across paragraphs for emphasis
  (three "Instead of / They'll ask" pairs; three founder quotes in a row).
- Confident, a little contrarian, industry-insider register — he's talking
  to steel distribution operators and ERP buyers, not a general startup
  audience. Assume the reader knows what a quote, a mill, a service center,
  an ERP rollout is.

## 4. What this voice does NOT do

- No hedge words: "might," "could potentially," "I believe," "in my opinion."
- No corporate throat-clearing openers ("In today's fast-paced world...").
- No stacking three analogies in one post — one, fully developed.
- No dense unbroken paragraphs.
- No fabricated stats, studies, quotes, or anecdotes. If a post needs a
  number or example Raj hasn't supplied, either ask him for it or write
  the post around the structural shape and mark the gap clearly rather
  than inventing "a McKinsey study found..." or similar.
- No hashtags, no emoji strings, no "thoughts?" as a lazy default closer —
  the closing question should be specific to the post's claim.
- **Never names a customer/client company** — not in a post, and not in
  a comment drafted for someone else's post. This holds even for a purely
  positive story. See Section 4a.

### 4a. Using AskCruz/EOXS customer material — anonymize, always

Raj wants this skill to draw on real AskCruz/EOXS work and customer
outcomes for material — that's exactly the kind of concrete anecdote
Section 2 calls for. The rule is: the *experience* is fair game, the
*identity* never is.

- Describe the account by category, not name: size band ("a 50-person
  service center," "a mid-size distributor"), region, or the specific
  problem/workflow ("a company running 1,400 open quotes with no
  follow-up process") — never the company name, and never a detail
  specific enough that someone in the industry could reverse-engineer
  who it is (e.g. a very distinctive deal size, a named exec's quote,
  a plant location that only one client has).
- This applies identically when drafting a **comment on someone else's
  post** — the anonymization rule doesn't relax just because it's a
  reply instead of a post.
- If Raj gives you a specific deal or client detail as source material,
  pull the *shape* of the story (the problem, the number, the outcome)
  into the post and strip the identifying wrapper. If you're not sure
  a detail is anonymous enough, flag it and ask rather than guessing.
- Sabre Alloys in particular must never appear in any external-facing
  content, per standing rule — treat this the same as every other client
  name for this skill's purposes.

---

## 5. Workflow: drafting from a topic/idea

1. Ask Raj for (or extract from what he gave you) the raw material: the
   belief he's reframing, and a real anecdote/number/quote if he has one.
   If he hasn't given a concrete anecdote, ask for one before drafting —
   don't fabricate.
2. Write the one-line reframe first. Show it to Raj if there's any doubt
   it's sharp enough, before building the rest of the post around it.
3. Build outward: reframe → scene/anecdote or analogy → 2-3 short
   consequence lines → close (question or callback).
4. Break lines per Section 2. Read it back at the pace it would be read —
   if two ideas run together, split the line.
5. Run the Section 7 checklist before presenting it.

## 6. Workflow: polishing an existing draft

1. Find the thesis buried in the draft — Raj sometimes writes the point
   in the middle or end. Pull it to the top as the opening line if it
   isn't already there.
2. Cut hedging language and corporate phrasing on sight.
3. Break dense paragraphs into the one-clause-per-line rhythm.
4. Check for a real anecdote/analogy — if the draft is all abstraction,
   ask Raj if there's a specific call, client, or number to ground it in
   rather than inventing one.
5. Fix the close: one clean question or one callback line, not both, not
   a generic "thoughts?"
6. Run the Section 7 checklist.

## 7. Pre-send checklist

- Opens with a one-line reframe, stated as fact, not hedged.
- Every sentence is broken into short, readable lines.
- Contains one real, specific anecdote/number/quote (not invented).
- At most one analogy, developed rather than dropped in passing.
- Closes with exactly one device: a specific question or a callback to
  the opener.
- No hashtags, no emoji, no more than one ALL-CAPS punch line.
- Company mention (if any) is one quiet line, not a pitch.
- Nothing stated as fact that Raj didn't actually give you.
- No customer/client company is named or identifiable, in the post or in
  any comment drafted for someone else's post.

If a draft fails more than one of these, say which ones before presenting
it rather than shipping something that reads off-voice.
```

Paste that as the SKILL.md content when you create it in your Claude account settings.

**User:** Perfect, now can you update this in skills and create a new skill which will be called Rajat's LinkedIn Voice?

**Assistant:** [Viewed /mnt/skills/examples/skill-creator/scripts/package_skill.py to confirm packaging conventions. Copied /home/claude/linkedin-voice to /home/claude/rajats-linkedin-voice. Edited the SKILL.md frontmatter `name` field from `linkedin-voice` to `rajats-linkedin-voice` and the H1 title from "Raj's LinkedIn Voice" to "Rajat's LinkedIn Voice", keeping all body content (Sections 1-4a, 5, 6, 7) identical to the reverted write-up above — no vault-sourcing section. Attempted to run package_skill.py directly, hit a ModuleNotFoundError and a read-only filesystem error on the first attempt (skill-creator's scripts/ directory is read-only), then successfully ran it with PYTHONPATH set to /mnt/skills/examples/skill-creator, packaging /home/claude/rajats-linkedin-voice into /mnt/user-data/outputs/rajats-linkedin-voice.skill. Validation passed. Called present_files on the resulting .skill file.]

Packaged and validated.

[present_files output: /mnt/user-data/outputs/rajats-linkedin-voice.skill]
