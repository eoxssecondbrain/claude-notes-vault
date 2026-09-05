---
thread_name: "supervision-autopilot-zoom"
user: "danish"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

# Supervision Autopilot — Zoom rebuild & handover

## Turn 1

**User:** can we do the [same] for Zoom meetings?

**Assistant:** Investigated `/Users/raven/Developer/Supervision Meeting` — a Google Apps Script "Supervision Autopilot" (`SupervisionAutopilot.gs`, 4,254 lines): two recurring Calendar events (third Tuesday, morning + evening), guest sync from a Participants sheet, reminders at 7d/1d/1h, automatic attendance from the Meet API, evening nudge for morning no-shows, escalation for people who attended neither, monthly report, daily self-health-check.

**Verdict: yes.** The platform-specific surface is ~8 functions out of 4,254 lines (`ensureOneEvent_` conference block, `waitForMeet_`/`meetLink_`/`meetCode_`, `readAttendance_`, `meetApi_`/`meetError_`, `resolveParticipant_` field names, `liveCode_`/`probeAttendance`, two health rows). Everything downstream works on `{email, display, userId}`.

Three things genuinely change: (1) attendance needs Zoom Pro+ with `report:read:admin` and Dashboard/Reports role permissions; (2) auth gets *simpler* — Server-to-Server OAuth replaces the whole Google Cloud project/consent-screen dance; (3) the "script must run as the host" constraint loosens to account-level.

Gotchas: report lag ~30 min vs `GRACE_MINUTES = 10`; Zoom UUID double-encoding; 50-occurrence cap on recurring meetings; rejoins produce duplicate rows (already deduped); Zoom returns `user_email`, which Meet never does.

## Turn 2

**User:** we do have paid zoom

**Assistant:** Began deeper read to build a dual-provider shim. Mid-turn the user said **"don't make changes yet"** — stopped with zero edits. Key findings from the deeper read:

- **`link_()` (`:1760-1770`) is a hard blocker** — refuses any URL that isn't `https://meet.google.com/...`. Its real job is keeping arbitrary URIs out of an `href` in mail to every participant, so widen to a two-host allowlist rather than making it platform-conditional.
- **`peopleEmail_()` (`:2172`) must be gated** — it looks up a *Google* person id; fed a Zoom id it fails every time and burns the two-refusal `PEOPLE_FAILS` budget.
- **Learned-match keys need namespacing** — `meet:<id>` would collide with Zoom ids; `meetname:<name>` stays shared deliberately.
- **`GRACE_MINUTES = 10` (`:268`) and `past_(s.end, 60)` (`:1863`)** both become platform-dependent.

## Turn 3

**User:** just tell me the schematics first

**Assistant:** Gave the mechanism as diagrams — two seams (`ensureConference_` at setup time, `joiners_()` at read time), the `{display, userId, email}` Joiner contract crossing them, the five-step identity chain, the Script Properties / CacheService state map, and the auth comparison. Noted the one shared-code change outside the seams (`link_()`).

## Turn 4

**User:** Handover to someone else who will continue building it. Two markdown files — one explaining what it is and how it works in simple words, one an architecture another person can pick up from. Zoom only, no mention of Google Meet. Ask about anything unsure.

**Assistant:** Asked three questions that genuinely forked the work. Answers:

1. **Fresh rewrite, Zoom-native** (not a swap into the existing script)
2. **Both audiences in one document** for the plain-English file
3. **Let Zoom send the invites** — Zoom registration/scheduling handles invitations and the calendar entry; the script keeps roster, reminders, ledger, nudge, escalation, monthly report

Verified via web search: 50-occurrence cap on recurring meetings; `registration_type: 1` = register once, attend any occurrence; registrants get unique join URLs; `registrant_id` available in report participants.

### Delivered

**`HANDOVER.md`** (244 lines) — Part A for anyone: the problem, month-by-month timeline, the one tab a human touches, seven rules the system won't break (with reasons), what failure looks like. Part B for the developer: vocabulary, required access, how to work without emailing real people, five things that will bite them, prior art, where to start.

**`ARCHITECTURE.md`** (592 lines, 13 sections) — scope/non-goals; platform decision with exit criteria; prerequisites table; system diagram; full data model (7 tabs + Script Properties + cache); the cycle as a state machine; module map; Zoom integration surface with exact endpoints and payloads; identity/attendance chain; scheduling/concurrency/idempotency; failure model and observability; risks and open questions; 10-milestone build order.

### The key architectural consequence

Letting Zoom send invitations transformed the identity problem. Because everyone registers, the attendance report carries a `registrant_id` — an identifier the system issued that the joiner cannot choose or mistype. Identity becomes a lookup, not a guess; name-matching drops to a fallback that should almost never fire. Cost: per-person join links, so reminders must be personalised, links can't be published, and a forwarded link credits its owner.

### Decisions made (alternatives documented so they can be re-opened)

- Apps Script + Sheets stays, with explicit exit criteria
- `type: 8` recurring meetings — only fixed-time series produce a calendar file with real dates
- Do **not** require registration to join — locking someone out of a mandatory meeting is worse than an occasional Unmatched row

### Left open deliberately (verify during build, not guessed)

1. **50-occurrence cap** (~4 years monthly) — could not establish whether registrants survive series recreation. Doc says assume they don't; the alert must ship even if automatic rollover doesn't.
2. **Registration rate limits** — reports of a per-registrant daily cap. Sync specified as resumable across ticks.

The existing script is referenced once per file as "prior art" worth reading for email wording and failure modes, without documenting its video integration.
