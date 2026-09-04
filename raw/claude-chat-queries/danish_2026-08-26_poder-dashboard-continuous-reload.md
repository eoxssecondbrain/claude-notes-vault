---
thread_name: "poder-dashboard-continuous-reload"
user: "danish"
type: claude-chat
created: 2026-08-26
updated: 2026-08-26
---

# PODER dashboard — continuous browser reload

## User
"it is being reloaded continuously"

## Investigation

Clarified symptom: **browser page full-reloads** (not dev-server restarts, not network polling).

### Theories tested and disproved
1. **Turbopack root scoped to repo root** (`dashboard/next.config.ts` had `root: path.resolve(__dirname, '..')`).
   Hypothesis: dev watcher watched `poder-tools/__pycache__`, `reports/`, `db/` and reloaded on backend writes.
   A/B tested by reverting the config and running identical file-write stress against both configs while
   listening on the HMR websocket (`/_next/webpack-hmr`). **Both configs emitted zero reload events — disproved.**
2. **Dev-server worker crash-loop.** Sampled `next-server` PID over time; stable. The one restart observed
   was self-inflicted (editing `next.config.ts` restarts the worker).
3. **Client-side reload code.** Grepped all of `dashboard/src` for `location.reload`, `router.refresh`,
   `http-equiv=refresh`, remount-triggering `key=` props. **None exist.**

### Actual root cause
Route timing test exposed it — most routes were hanging:
```
/sessions /raj /reports /company /analytics /errors /notion /send  -> timeout at 25s
/approvals 23.8s   /schedule 13.9s   /agents 5.6s
```
Three compounding facts:
- `.next/dev` had grown to **3.0 GB**
- **~48 MB free RAM** on a 16 GB machine (`Pages free: 3043` × 16KB) — system thrashing
- `next-server` RSS 1.7–3.8 GB

The dev server was memory-starved and blocking. Next's dev client full-reloads the page whenever the
HMR websocket drops and reconnects — a thrashing server drops it repeatedly, producing the continuous reloads.

## Fix applied
1. Scoped Turbopack to the dashboard: `root: __dirname` in `dashboard/next.config.ts` (kept — prevents the
   cache re-ballooning by tracing the whole monorepo; also silences the multi-lockfile root inference).
2. Killed `next dev`, deleted the 3.0 GB `.next`, restarted.

## Verified after fix
- Free RAM: 48 MB → 6.4 GB immediately after cache delete
- `Ready in 249ms`, no workspace-root warning
- All 14 routes HTTP 200, every one sub-second (was 8 timing out)
- `.next` now 48 MB (was 3.0 GB)
- Worker PID stable, RSS flat at ~1.95 GB, zero HMR reload events over 60s

## Caveats
- Worker still ~1.95 GB RSS; on a 16 GB machine running Postgres/mysqld, Python tools, Express, Next and VS Code
  this can re-tighten over a long session. Watch `.next` size — if it climbs into the GBs again, clear and restart.
- `start.sh`'s `NEXT_PID` refers to the old process; the dashboard is now a separately-launched `next dev`.
  A clean `./start.sh` run resets everything.
