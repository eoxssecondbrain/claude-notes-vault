---
thread_name: "supervision-autopilot-zoom"
user: "danish"
type: claude-chat
created: 2026-09-05
updated: 2026-09-05
---

# Supervision Autopilot — Zoom support feasibility

## User

can we do the [same] for Zoom meetings?

## Assistant

Investigated `/Users/raven/Developer/Supervision Meeting` — a Google Apps Script "Supervision Autopilot" (`SupervisionAutopilot.gs`, 4,254 lines) that runs monthly supervision sessions: creates two recurring Google Calendar events (third Tuesday, morning + evening) with Google Meet links, syncs guest lists from a Participants sheet, sends reminders at 7d/1d/1h, reads attendance automatically from the Google Meet API, nudges morning no-shows to the evening session, escalates to anyone who attended neither, emails a summary, and runs a daily self-health-check.

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

Everything downstream — cycle maths, ledger, reminders, evening nudge, escalation, report, test mode, dry run, and the whole name-matching/learning chain — works on `{email, display, userId}` and never touches Meet. All of it survives untouched.

The Calendar side also stays: still want a recurring Calendar event for invites, guest-list sync and privacy flags. Only change is the Zoom join URL goes in the event body instead of Google provisioning `conferenceData`.

### The three things that genuinely change

**1. Attendance needs a paid Zoom plan.** `GET /report/meetings/{uuid}/participants` is Pro-and-above only, needs the `report:read:admin` scope, and the role behind the Server-to-Server app needs Dashboard and Reports ticked in Role Settings. On Free there's no participant readout at all — back to ticking by hand, which is the one thing the script exists to avoid. **This is the question to settle before any code gets written.**

**2. Auth gets simpler, not harder.** A Server-to-Server OAuth app (account_id + client_id + secret → 1-hour token) replaces the entire Google Cloud project dance in README step 5 — no linked Cloud project, no Internal consent screen, no `meetings.space.readonly`. Credentials go in Script Properties, not the Setup tab where any sheet editor can read them. Need to be a Zoom account admin to create the app.

**3. The host constraint loosens.** Today the health check must verify the script runs as the event organiser, because Meet only reports attendance to the host (`:2597`). An account-level Zoom token reads any meeting in the account, so that check becomes "the meeting is owned by someone in this Zoom account" — much easier to satisfy.

### Gotchas to design around up front

- **Report lag.** Zoom report data can take ~30 minutes to settle. `GRACE_MINUTES = 10` at `:268` is too tight — but the 15-minute engine trigger and `needsRead_` already retry, so it's a constant change, not a rework.
- **UUID double-encoding.** Zoom meeting UUIDs can contain `/` and must be URL-encoded *twice* in the path. The classic silent 404.
- **Recurrence.** Use a `type: 3` meeting (recurring, no fixed time) — one permanent join URL, script keeps doing its own date arithmetic. Matches the existing "link is permanent, notice if it changes" design better than Zoom's own recurrence, which caps at 60 occurrences.
- **Rejoins.** Someone who drops and reconnects appears as several rows. `joined[email] = true` already dedupes for free.
- **Bonus:** Zoom returns `user_email` for signed-in participants, which Meet never does. For external candidates that's a stronger identifier than anything in the current chain — would slot in ahead of the directory lookup.

### Recommendation

Add a `Meeting platform (Meet/Zoom)` cell on Setup and put a thin provider shim behind it — `ensureConference`, `link`, `code`, `readJoiners(code, from, to)` — rather than swapping Meet out. The Meet install keeps working while Zoom is proved, and the Dashboard can show which one is live. Roughly 400–600 new lines plus README changes; contained, not a rewrite.

### Open questions put back to the user

1. Build it as a dual-provider shim, or replace Meet entirely (full migration)?
2. Is the Zoom account Pro or above?

Sources: [Zoom report API prerequisites](https://developers.zoom.us/docs/api/meetings/), [report:read:admin scope and role permissions](https://devforum.zoom.us/t/api-scope-reportadmin-not-available-in-business-plan/111204), [reports on Pro and above](https://devforum.zoom.us/t/not-able-to-use-reports-api-on-a-pro-account/88471)
