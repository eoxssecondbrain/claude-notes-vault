---
thread_name: "supervision-autopilot-zoom"
user: "danish"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

# Supervision Autopilot — Zoom support

## Turn 1

**User:** can we do the [same] for Zoom meetings?

**Assistant:** Investigated `/Users/raven/Developer/Supervision Meeting` — a Google Apps Script "Supervision Autopilot" (`SupervisionAutopilot.gs`, 4,254 lines) that runs monthly supervision sessions: creates two recurring Google Calendar events (third Tuesday, morning + evening) with Google Meet links, syncs guest lists from a Participants sheet, sends reminders at 7d/1d/1h, reads attendance automatically from the Google Meet API, nudges morning no-shows to the evening session, escalates to anyone who attended neither, emails a summary, and runs a daily self-health-check.

### Verdict: yes, and most of the script doesn't care

**The Meet-specific surface is small** — about eight functions out of 4,254 lines:

| What | Where |
|---|---|
| Attach a conference to the series | `SupervisionAutopilot.gs:698-701`, `:791-794` |
| `waitForMeet_` / `meetLink_` / `meetCode_` | `:800-826` |
| `readAttendance_` — the conference-record query | `:1895` |
| `meetApi_` / `meetError_` | `:1980`, `:2016` |
| Field names in `resolveParticipant_` | `:2045-2050` |
| `liveCode_` / `probeAttendance` | `:3098`, `:3109` |
| Two Dashboard health rows | `:2597-2621` |

Everything downstream — cycle maths, ledger, reminders, evening nudge, escalation, report, test mode, dry run, and the whole name-matching/learning chain — works on `{email, display, userId}` and never touches Meet.

The Calendar side stays: still need a recurring Calendar event for invites, guest-list sync and privacy flags. Only change is the Zoom join URL goes in the event body instead of Google provisioning `conferenceData`.

### The three things that genuinely change

**1. Attendance needs a paid Zoom plan.** `GET /report/meetings/{uuid}/participants` is Pro-and-above only, needs `report:read:admin`, and the role behind the Server-to-Server app needs Dashboard and Reports ticked in Role Settings.

**2. Auth gets simpler.** Server-to-Server OAuth app replaces the entire Google Cloud project dance in README step 5 — no linked Cloud project, no Internal consent screen, no `meetings.space.readonly`.

**3. The host constraint loosens.** An account-level Zoom token reads any meeting in the account, replacing the "script must run as the event organiser" check.

### Gotchas
- Report lag up to ~30 min vs `GRACE_MINUTES = 10`
- Zoom UUID double-encoding (`/` and `//` in UUIDs)
- Use `type: 3` recurring-no-fixed-time meetings (Zoom's own recurrence caps at 60 occurrences)
- Rejoins produce duplicate rows — `joined[email] = true` already dedupes
- Zoom returns `user_email`, which Meet never does

### Recommendation
Dual-provider shim behind a `Meeting platform (Meet/Zoom)` Setup cell rather than replacing Meet. ~400–600 new lines.

Sources: [Zoom report API prerequisites](https://developers.zoom.us/docs/api/meetings/), [report:read:admin scope and role permissions](https://devforum.zoom.us/t/api-scope-reportadmin-not-available-in-business-plan/111204), [reports on Pro and above](https://devforum.zoom.us/t/not-able-to-use-reports-api-on-a-pro-account/88471)

## Turn 2

**User:** we do have paid zoom

**Assistant:** Began a deeper read of the codebase to build the dual-provider shim. Mid-turn the user said **"don't make changes yet"** — stopped before writing anything. Zero edits made. Presented the following plan for approval.

### What the deeper read changed about the plan

**`link_()` is a hard blocker, and the important one.** `SupervisionAutopilot.gs:1760-1770` refuses any URL that isn't `https://meet.google.com/...` — a Zoom link would render in every email as *"(link looks wrong — check the calendar event)"*. Its real job is stopping an arbitrary conferencing URI reaching an `href`, so widen it to a two-host allowlist (Meet **or** Zoom) rather than making it platform-conditional, and put the "your platform says Zoom but this link is Meet" question on the Dashboard instead. Keeps the injection guard as strong and keeps the self-test green.

**The directory lookup must be gated.** `peopleEmail_()` (`:2172`) looks up a *Google* person id. Fed a Zoom user id it fails every time and burns the two-refusal `PEOPLE_FAILS` budget for nothing.

**Zoom gives `user_email` for signed-in participants** — stronger than anything in the current chain, so it slots in at position 2 of `resolveParticipant_`: after remembered-by-id, before the directory.

**Learned matches need a namespace split.** `meet:<id>` keys would collide with Zoom user ids. Ids get a `zoom:` prefix; `meetname:<name>` keys stay shared deliberately — same person, same name, either platform.

**Two timing constants are Meet-shaped.** `GRACE_MINUTES = 10` (`:268`) and the `past_(s.end, 60)` "call it empty" rule in `collect_` (`:1863`) both become platform-dependent functions.

### The plan (awaiting approval)

1. **Setup tab** — `Meeting platform (Meet/Zoom)` (defaults to `Meet`, so the existing install is untouched) and `Zoom host email`.
2. **Credentials in Script Properties, not on the sheet** — a `Zoom` submenu with *Connect Zoom* / *Forget the Zoom credentials*. Anyone with edit access to the sheet could otherwise read the account secret.
3. **Provider shim** — `ensureConference_`, `conferenceLink_`, `conferenceCode_`, and `joiners_(s)` returning a normalised `{display, userId, email}` list. Everything downstream untouched.
4. **Zoom API layer** — Server-to-Server OAuth token cached in `CacheService`, `zoomApi_` retrying on 429/5xx like `meetApi_`, `zoomError_` translating plan/scope/role failures into the same plain-English style, UUID double-encoding as its own tested function.
5. **Attendance** — `past_meetings/{id}/instances` filtered to the session window, then `report/meetings/{uuid}/participants`.
6. **Health checks** — Zoom connection, reports API reachable, both meetings resolvable, warning if a converted event still carries a Google Meet conference (two links in one invite is how someone joins the wrong one and gets marked absent).
7. **Migration to schema v7** so existing sheets get the new Setup rows from the engine without re-running `install`.
8. **Self-test additions** and a README section.

### Two judgment calls flagged for the user

- **Would not strip the Meet conference** off an existing event when switching to Zoom — warn loudly on the Dashboard, leave removal to a human. Destroying a bookmarked link is the user's call.
- **New Zoom meetings would be `type: 3`** (recurring, no fixed time) — one permanent join URL, script keeps owning the date arithmetic.

**Status: waiting on the user's go-ahead before any code is written.**
