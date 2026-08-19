---
thread_name: "employee-report-card-parameters"
user: "ron"
type: claude-chat
created: 2026-08-19
updated: 2026-08-19
---

Human: Based on the discussion we had tell me what do you think should be the parameters here.

Assistant: Based on everything from the session plus what I actually verified against the systems, here's what I'd keep, reframe, or drop.

Keep as core scoring inputs, ready or near-ready:

- Task completion & QA pass/fail rate in the live environment — Aryan's metric is the closest thing anyone offered to a real quality signal. This should be the primary quality parameter, not log notes or email tone.
- Deadline adherence via date_deadline — native field, just needs to actually get populated and used as the ETA parameter people asked for.
- Actual vs expected hours (via resource_calendar), with extra hours flagged positively — buildable now, matches what both Ron and Yashviri asked for.
- Ownership — one accountable name per task, not the whole assignee list. Needs a definition decided once (e.g. "whoever moved it to done, or whoever it's currently sitting with"), then it's a native field.
- Designation-based segmentation — right approach, but gate it behind actually populating job_title/job_id first. Don't let the report card launch generalize one scoring rubric across roles that don't have comparable work (this also resolves Jaee's CLAUDE.md point — that becomes one of the dev-specific sub-parameters, not a universal one).
- Cattr-reconciliation as a standing audit rule applied to every other input above, not a standalone bullet. This is your defense against every other metric being gamed — treat it as a validation layer the AI runs against all the other numbers, not one line item competing for attention with the rest.

Keep, but only after a prerequisite fix:

- Leave — keep it in the framework, but only once it's a real leave record instead of a task titled "Time off." Don't build the exclusion logic against the task-title workaround; it'll break the first time someone titles it differently.

Reframe or narrow scope:

- Emails sent — I wouldn't use this as a scoring input at all. Use it as context the AI can reference in the narrative summary ("responded to client X within a day"), not as a number that adds to the score. Volume-based email metrics get gamed fastest and reward the wrong behavior.
- Log notes / daily snippet — same treatment as email: qualitative context that helps a manager read the score, not a quantitative parameter itself. Otherwise you're rewarding whoever writes the longest snippet.
- Camera-off / late-joining — pull this out of the productivity score entirely. Track it as a separate compliance flag. Blending etiquette into a productivity number muddies both.

Drop or explicitly exclude:

- Raw task count — the team already said this themselves (Kriti, Vanshi). Don't let it sneak back in as a hidden weight inside "task completion."

On visibility: given how gameable most of these inputs are, I'd lean toward manager-visible detail with team-visible only at a rolled-up level (not a ranked leaderboard) — but that's a call for the team to make explicitly, not something to default into.

That leaves three things still undecided before this is buildable: the numeric weighting between QA-pass-rate and hours/deadline metrics, whether leave gets fixed to a real record before or after v1 ships, and the visibility question above.

Human: /markitdown-to-drive - Convert the entire thread above. DO NOT leave anything out and give me an MD file with all the information in it.

Assistant: [Checked markitdown-to-drive SKILL.md and loaded Google Drive tools]

Human: Give me the file here.

Assistant: [Created full verbatim markdown transcript of the entire thread (all turns from the original screenshot upload through this point) as employee-report-card-parameters.md and presented it directly in chat via present_files, rather than uploading to Google Drive, per the user's redirect to "give it here."]
