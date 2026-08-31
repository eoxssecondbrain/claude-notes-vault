---
thread_name: "kcal-ledger-app-build"
user: "yashvir"
type: claude-chat
created: 2026-08-27
updated: 2026-08-31
---

## Continued — major pivot

**User:** "Lets keep this simple and lets also do the calorie tracking not based on the information of the food existing anywhere but from the open ai to maintain accuracy, i want a structure that tracks the calorie intake for a day, week, and month where i can have see the calorie and macros tracking how i want and i want to keep the interface very simple."

**Assistant:** Asked 3 clarifying questions per user's build-clarification preference: (1) OpenAI tradeoff — confirmed user is OK bringing their own API key stored locally, calling OpenAI directly from the browser, accepting the internet+cost tradeoff since there's no backend; (2) scope — web only for now (not Android/Mac); (3) craft level — Commissioned.

Backed up the old food-database + voice-logging build to `/home/claude/kcal-ledger-v1-fooddb-backup.html`, then built a full replacement of `/home/claude/kcal-ledger.html` from scratch:
- Dropped the 9,470-item local food DB and voice logging entirely.
- New flow: single free-text "what did you eat?" box → calls OpenAI (`gpt-4o-mini`, structured JSON-schema output) for calorie/macro estimates → mandatory editable review screen before saving (kept the review-before-log pattern from the voice feature since AI estimates need the same human check).
- API key entered in Settings, stored in localStorage only, sent directly to OpenAI's API from the browser — no backend.
- Added Day / Week / Month views: Day = ring + macro bars + meal-grouped entry list (carried over from v1's look); Week = bar chart of daily kcal vs. goal line with hover tooltips + stat tiles; Month = calendar heatmap colored by status (on target/a bit over/well over/no entries) vs. goal, plus monthly macro averages.
- Manual-entry fallback path for when no API key is set or the user wants to enter something by hand.
- Followed the dataviz skill for chart form/color choices (kept the same validated protein/carb/fat categorical triple from before) and the artifact-design skill for a UI/tool-appropriate (not editorial) treatment — same petrol-teal brand identity as before for continuity.
- Full Playwright regression testing (settings, manual log, delete/undo, week/month rendering, day nav, no-key banner path, dark mode) — found and fixed one real bug (an unsized sparkle icon SVG blowing up to fill the "Estimate with AI" button) via screenshot inspection that DOM-only assertions had missed. Also fixed a JS syntax error (unescaped apostrophe in a string) caught by the same test pass, and added chart headroom so the week view's dashed goal line isn't flush against the container edge when goal is the current max.
- Published as a new version of the existing "Kcal Ledger" artifact (same URL, https://claude.ai/code/artifact/45e71348-70c7-43b9-adc6-0a452be72f08) rather than forking a new one — read the live artifact first per the Artifact tool's required-read-before-republish rule, confirmed it was the old v1 content (matches the local backup), and intentionally did NOT merge it back in since this is a deliberate full replacement per the user's explicit request, not an incremental edit.
