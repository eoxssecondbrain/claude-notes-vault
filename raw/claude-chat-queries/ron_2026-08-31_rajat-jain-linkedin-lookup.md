---
thread_name: "rajat-jain-linkedin-lookup"
user: "ron"
type: claude-chat
created: 2026-08-31
updated: 2026-08-31
---

User: Can you go on LinkedIn and find me Rajat jain from EOXS?

Assistant: Found him — Rajat Jain, Founder and CEO of EOXS, based in Toronto. Crunchbase lists two LinkedIn URLs tied to him:

- linkedin.com/in/rajat-jain-eoxs
- linkedin.com/in/rajat-eoxs

Both trace back to the same person/company — his Crunchbase bio also notes a mechanical engineering background moving into enterprise solution development and technical sales in the steel industry. Worth clicking both since Crunchbase sometimes has stale slugs; one is likely his current active profile and the other an older one.

User: "linkedin.com/in/rajat-jain-eoxs" 

Are you able to go on his profile and get all the posts that he has posted in the last 30 days and any comments that he might have made?

Assistant: I can't get to that. Two things are blocking it:

1. LinkedIn's recent-activity feed (posts + comments) sits behind a login wall — every route I tried (direct fetch, search results) hits a "sign in to view" page with no content.
2. The browser-automation tools I have access to (claude-in-chrome, Control Chrome) both timed out with no response — likely because this chat session isn't connected to a live Chrome browser/extension right now.

If you want this pulled together, your options are:

- Open his profile yourself, scroll through the last 30 days of activity, and paste the text here — I can then summarize themes, engagement, topics, etc.
- Check whether your Claude desktop app has an active Chrome connection (list_connected_browsers is what failed) — if that gets reconnected, I could try navigating and reading the page directly next time.
