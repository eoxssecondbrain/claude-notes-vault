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

**User:** How do I connect with you with my LinkedIn??

**Assistant:** [Searched MCP registry again with keyword "linkedin" to check for any personal-account connector.]

There's no direct "connect your personal LinkedIn account" connector in the registry — nothing here reads your own post history or profile directly. The closest are:

- Crustdata — has a `crustdata_company_linkedin_posts` tool, but it's built for looking up company/people data (research/enrichment), not for authenticating as you and pulling your own posts.
- Windsor.ai / Supermetrics — pull LinkedIn Ads performance data, not personal post content.

None of these give me your published post history the way, say, Gmail or Google Drive connect your own account. Realistically the path for this skill is: you paste your posts in (or export them from LinkedIn's own "Get a copy of your data" tool under Settings → Data privacy, which gives you a CSV/file of your posts) and upload that file here.

Want me to walk you through the LinkedIn data export, or do you want to just paste in a handful of posts directly and skip the export?
