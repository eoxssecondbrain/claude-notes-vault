---
thread_name: "study-time-kickoff"
user: "hashir"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

User: Hi, 
Lets talk about what we can learn today, we have our first 1 hour study time.

Assistant: That doesn't clearly match either skill on file — eoxs-data-general is for EOXS business data (emails, calls, wiki, tickets, CRM), and threads-ov is for saving/synthesizing chat transcripts. "Study time" doesn't fall under either as a task itself.

Before I proceed: what's this study time actually about — EOXS-related material (product, market, ops, wiki content), or a separate subject entirely (finance, strategy, technical skill, something else)? And what's the goal — build understanding of something specific, or open-ended exploration?

User: This study time is dedicated to study about claude and how we can with the optimised input get the maximum output, like these could be the start point from where we can lead on this.

Assistant: Good starting point. Since this isn't a one-off research/analysis task but an ongoing session, I'll skip the rigor-level menu and just start teaching — we can go as deep as you want per topic.

Here's how I'd structure the hour: build the foundational principles first (what actually moves output quality), then apply them to a real prompt you're currently using, so you leave with something improved, not just theory.

Core principle, stated first because everything else builds on it: Claude responds well to clear, explicit instructions, and being specific about desired output can help enhance results — if you want above-and-beyond behavior, request it explicitly rather than relying on the model to infer it from vague prompts. The mental model Anthropic gives for this: think of Claude as a brilliant but new employee who lacks context on your norms and workflows — the more precisely you explain what you want, the better the result. A useful test: show your prompt to a colleague with minimal context and ask them to follow it — if they'd be confused, Claude will be too.

Five levers, in order of impact for most day-to-day use:

1. Clarity and directness — specify the output format and constraints, use numbered steps when order matters.
2. Context — explaining why a behavior matters helps Claude generalize from the explanation rather than pattern-match narrowly.
3. Examples — a few well-crafted examples (few-shot/multishot) are one of the most reliable ways to steer format, tone, and structure. Best practice is 3-5 examples that are relevant, diverse, and wrapped in example tags so Claude can distinguish them from instructions.
4. XML structuring — wrapping different content types in their own tags (instructions, context, input) reduces misinterpretation when a prompt mixes several kinds of content.
5. Role-setting — even a single sentence assigning a role in the system prompt focuses tone and behavior for the use case.

One formatting note worth internalizing early since it changes how you phrase constraints: tell Claude what to do instead of what not to do — "your response should be composed of smoothly flowing prose paragraphs" works better than "do not use markdown."

That's the base layer. For the rest of the hour I'd suggest: pick one prompt you actually use regularly (a recurring EOXS task, a report format, anything real), and we rebuild it live against these five levers so you see the before/after rather than working in the abstract.

What's a real prompt you'd want to bring in?

User: I need to learn more about the things which are related to my role.

Assistant: What's your role — I don't have that on file. And "things related to your role" could mean a few different directions: how to use Claude more effectively for the actual work you do day to day, or something narrower like a specific task type (writing, analysis, coding, client comms, data queries). Give me both and I'll tailor the session to real examples from your work instead of generic prompting tips.
