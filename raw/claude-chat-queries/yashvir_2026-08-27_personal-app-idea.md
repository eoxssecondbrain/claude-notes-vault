---
thread_name: "personal-app-idea"
user: "yashvir"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

User: my daily calorie tracker

Assistant: [AskUserQuestion: "What platform should this run on?" -> Mobile app; "How much polish do you want on this build?" -> Commissioned]

Assistant: One flag before I start: "mobile app" + "commissioned" polish is a real tension. True native (Swift/Kotlin, App Store deployment) isn't something I can build and test end-to-end in this environment — no device, no app store account, no Xcode. What I can actually deliver at commissioned-level polish is a mobile-first web app (PWA) — installs to your home screen, works offline, feels native, no app store needed. If you specifically need App Store/Play Store presence, that's a different toolchain and a longer path. Assuming PWA is fine unless you say otherwise.

Now the actual feature set — this is what determines scope:

[AskUserQuestion: "How should food logging work?" -> Built-in food database; "What else should it track besides calories?" -> Calories + macros; "Does this need to save your data permanently, or is local-only fine for now?" -> Local only (this device)]

Assistant built a single-file HTML app "Kcal Ledger": calorie ring + macro bars vs goals, meal-grouped logging (breakfast/lunch/dinner/snacks), searchable built-in food database (100+ items with calories/protein/carbs/fat per serving), manual entry with optional preset saving, day navigation, localStorage persistence, light/dark theme support, mobile-first responsive shell.

Published via Artifact tool: https://claude.ai/code/artifact/45e71348-70c7-43b9-adc6-0a452be72f08

Assistant: Published: Kcal Ledger — https://claude.ai/code/artifact/45e71348-70c7-43b9-adc6-0a452be72f08

It's a mobile-first web app (add it to your phone's home screen for an app-like icon and launch), with:
- A calorie ring + protein/carb/fat bars against your daily goals, all editable in Settings
- Meal-grouped logging (breakfast/lunch/dinner/snacks) with a built-in searchable database of 100+ common foods (calories + macros per serving, adjustable serving count)
- Manual entry for anything not in the database, with an option to save it as a one-tap preset for repeat meals
- Day-by-day navigation, and everything stored locally in your browser — no account, no backend, per your call earlier

Two honest caveats since you picked "commissioned" polish: it works offline once loaded but isn't a true installable PWA with a service worker (that needs a manifest + hosting setup beyond what a published artifact can do), and "local only" means clearing your browser data on that device wipes your history — there's no sync or backup. If either of those becomes a real problem once you're using it daily, that's the point where a proper backend/account layer earns its cost — worth revisiting then, not now.
