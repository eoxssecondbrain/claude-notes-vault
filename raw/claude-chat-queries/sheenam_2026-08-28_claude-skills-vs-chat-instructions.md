---
thread_name: "claude-skills-vs-chat-instructions"
user: "sheenam"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: how are skills in claude different from providing it an instruction in the chat itself. for example, if i want claude to write emails in a certain way, in a certain person's tone. that is something that I can install as a skill or I can make that addition in the prompt. How are the 2 approaches different.

Assistant: A few real differences, not just "same thing, different box":

Persistence and scope. An instruction typed into a chat lives only in that conversation. A skill is a file that exists independent of any conversation — usable from the first message of any new thread, by you or (if shared in a team catalog) anyone else on your team. Saved preferences (like the ones you already have set) are a third option — always injected into every chat, but as plain text, not a bundle of resources.

What it can hold. A chat instruction is just prose: "write like Raj — direct, no filler, short sentences." A skill is a folder — it can hold that same prose plus actual reference material: sample emails Raj has sent, a glossary of terms he uses, maybe even a script that checks draft length or formality. For tone-matching specifically, this matters a lot — a handful of real example emails as reference material gives far better grounding than a paragraph describing "his tone" in the abstract. Description-only tone instructions tend to produce something generically "professional," not something that actually reads like a specific person.

When it loads. A skill is read only when it's relevant — I see the task, match it to the skill's description, and pull the file in. An always-on chat instruction (or something in preferences) is injected into every single turn whether the task needs it or not, which quietly costs context space over a long conversation. A skill only costs anything when it's actually triggered.

Maintenance. If Raj's tone shifts, or you want to add another department's sales email style, you edit one skill file once — it's live for every future thread. A chat instruction has to be re-pasted or you rely on preferences, which is one global block, not something you can cleanly organize per-person or per-context without it growing unwieldy.

Trigger risk, the actual tradeoff. A skill only fires if its description is written well enough for me to recognize "this is an email-tone task." A chat instruction fires with certainty because you typed it directly in front of the task. So skills win on reusability and richness, chat instructions win on guaranteed application in the moment.

For "write emails in Raj's tone" specifically: skill, with 3-5 real example emails as reference material, not a description of his style — that's the part that actually transfers voice, not the instruction wrapper around it.

One thing worth flagging given your own setup: you already have a rule that any query matching more than one skill or none clearly should be surfaced before proceeding. This question didn't touch EOXS data, sales strategy, or transcript-saving logistics — it was a general product question, so no department skill applied here beyond the mandatory threads-ov read/save.
