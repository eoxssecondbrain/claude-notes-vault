---
thread_name: "alley-gym-app-status"
user: "jaskeerat"
type: claude-chat
created: 2026-08-02
updated: 2026-08-02
---

# Alley gym app — project status review

## User
go through this and tell me what are we up to

## Assistant

**What it is:** `gym-alley-app/` — Alley, a gym calorie tracker with a chat coach. Node/Express API (`backend/`) + one Expo codebase for web/iOS/Android (`app/`). Backend serves the built web bundle same-origin, so one URL, no address compiled into the build.

Key design decision: the AI is the last resort, not the product. A chat message falls through three tiers in `routes/chat.js`: (1) questions answered from the user's own logged data, (2) a ~1250-line deterministic parser against 638 foods / 163 exercises, (3) only then a model call. Nothing guesses a calorie — the model extracts what and how much, arithmetic is always local (ACSM equations, MET tables, sets×reps under load).

**Last two work sessions:**
- Jul 31, 2026 — "make it hostable" pass: Postgres storage as a single JSONB row (`storage.js`), migration script, HTTP Basic over everything, `/health` reporting persistence, Dockerfile, `render.yaml`, local launcher page.
- Aug 1, 2026 — "text-only + web polish" pass: voice removed entirely (STT, TTS, `@react-native-voice/voice`, `expo-speech`, MicButton, VoiceOrb, mic permissions). Grepped the tree — removal is clean, zero dangling references. Chat tab icon became a speech bubble (`Glyph.js:49`). Added `theme/interaction.js` to stop react-native-web text-selecting button labels on slow taps. Upshot: no native module dependency, runs in plain Expo Go. `app/dist` rebuilt 19:22 same evening, matches current source.

**Current runtime config:** `AI_PROVIDER=openai` with gpt-4o key set; Anthropic key empty. Password gate on. `ANTHROPIC_MODEL` still defaults to `claude-sonnet-4-6`, a generation behind the Claude 5 family.

**Four flags:**
1. `README.md` is several passes stale — describes light `#F5F5F7` Apple Health theme (app is dark by default now), "~70 foods" (638), "no bundled webfont" (Chakra Petch bundled for numerals), "three tools" (seven), and lists "not a Mifflin-St Jeor calculation" as a limitation when `targets.js` does exactly that. CLAUDE.md is accurate; README contradicts it.
2. 55.7 MB `db.corrupt-backup.json` still on disk in `backend/data/` from the Jul 31 incident (gitignored).
3. `db.json` has 115 users, ~100 throwaway test ids (`keytest`, `eggtest`, `sim-...`, `x`). One key is literally `[object Object]` — predates the `ensureUser` regex, since a space fails validation today.
4. No test runner, no lint. Verification is still "run it and exercise the routes."

Offered: bring the README in line with reality, or clear out the test users and corrupt backup.
