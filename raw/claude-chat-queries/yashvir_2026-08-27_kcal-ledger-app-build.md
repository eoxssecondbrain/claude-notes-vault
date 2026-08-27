---
thread_name: "kcal-ledger-app-build"
user: "yashvir"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

# Kcal Ledger — personal calorie tracker app build

**User:** i want to make an app
**Assistant:** Clarified: personal project (not EOXS/AskCruz-related), a daily calorie tracker.

**User:** my daily calorie tracker → can i use it on my phone also? → Does it has a built in food database?
**Assistant:** Built as a mobile-first single-file web app (Artifact), Commissioned craft level, built-in food database, calories + macros, local-only storage (no account/backend).

**User:** Don't limit it to 100 food items add 1000-10,000 food items, i dont wnat any stone unturned.
**Assistant:** Expanded database to full USDA SR28 (8,789 items), sourced via pip package `django-usda-nutrition`.

**User:** DOes your database has patrode and siddu a himachali cuisine → i want all the indian food items in the database specially from the north India i want even a small item added in the database like himachli siddu, patrode and all
**Assistant:** Added India's official IFCT 2017 government database (542 items, via npm `@ifct2017/*` packages) plus 139 curated North Indian/Himachali dishes (including siddu, patrode). Fixed a data bug where 14 pure-fat IFCT items (ghee, cooking oils) had enerc=0 despite real fat content, via Atwater-factor fallback. Total DB: 9,470 items.

**User:** can we make an app not for playstore but for android apk?
**Assistant:** Chose "Full offline Android project" (Capacitor-wrapped, vs. PWABuilder). Built `/home/claude/kcal-ledger-android/` — Capacitor project embedding the full app + database, custom app icon/splash, README with Android Studio build steps. Confirmed via `gradle -p android help` that the project itself is valid but the actual APK compile can't finish in this sandbox (dl.google.com/maven.google.com blocked by egress allowlist) — communicated this limitation honestly; user completes the build in Android Studio on their own machine. Delivered as `kcal-ledger-android.zip` (1.4MB, node_modules excluded).

**User:** Can we integrate voice assistance to it like we don't need to type we can narrate it and it could track it down?
**Assistant:** Built full voice logging: local rule-based parser (numbers, meal detection, food-name matching against the 9,470-item DB), native Android speech recognition via `@capacitor-community/speech-recognition` (bundled through a custom esbuild bridge since the app has no build step), Web Speech API fallback for the browser version, and a mandatory review-before-logging screen (since this is health data and the parser is heuristic, not AI). Found and fixed several real matching bugs via Playwright testing (e.g. "two rotis" → matching "Turkey...rotisserie" instead of roti; "a cup of coffee" → "Coffeecake"; plural "idlis" not matching singular "Idli") via word-boundary-first ranking, plural→singular fallback, and a verified alias map for ~25 common words. Flagged honestly that live microphone capture on Android is untested (no mic/device in this sandbox) even though the parsing logic itself was tested thoroughly.

**User:** can we make it for mac book intel and newer version
**Assistant:** Given Auto Mode (bias toward proceeding rather than blocking on a clarifying question), made the reasonable call: user wants an installable Mac desktop app equivalent to the Android build, working on both Intel and Apple Silicon Macs without needing two separate downloads. Built `/home/claude/kcal-ledger-mac/` — an Electron wrapper around the same `kcal-ledger.html` source (UI, logic, 9,470-item DB, voice parser all identical/unchanged), with:
- `main.js` — Electron main process, single BrowserWindow, native Mac menu bar (About/Quit/Edit with working copy-paste)
- `tools/build-www.py` — wraps `kcal-ledger.html` into `www/index.html` (keeps the floating-card look, unlike Android's edge-to-edge strip)
- `package.json` — electron-builder config targeting `--mac --universal` (single build running natively on both Intel and Apple Silicon, via dmg + zip targets)
- `build/icon.png` — reused the existing 1024×1024 app icon (electron-builder auto-generates the .icns)
- `README.md` — build steps (npm install → npm start to preview / npm run dist to build the universal .dmg), and an honest limitation: Electron's bundled Chromium lacks the speech-recognition backend key desktop Chrome has, so the Voice tab likely won't work in this build even though it works on web and Android — flagged clearly rather than silently shipped as "supported." Also noted (as with Android) that this sandbox has no macOS host, so the actual `.app`/`.dmg` build must happen on the user's own Mac.
Verified `package.json` is valid JSON and the generated `www/index.html` is structurally well-formed before removing the build artifact and zipping the source project (214KB, `node_modules`/`dist`/`www` excluded). Delivered as `kcal-ledger-mac.zip` via SendUserFile.
