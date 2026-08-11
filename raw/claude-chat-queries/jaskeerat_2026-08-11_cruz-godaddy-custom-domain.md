---
thread_name: "cruz-godaddy-custom-domain"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# Cruz — pointing the GoDaddy domain at the Render service

## Turn 1 — the plan

**User:** The service is currently hosted on Render, and we have purchased a new domain in GoDaddy. What are the steps to host the service with our domain?

**Claude:** Repo context: `render.yaml` defines one web service `cruz` (Docker, Standard, region singapore, branch `deploy/render`), live at `https://cruz-dsvf.onrender.com`. No OAuth configured, so no redirect URIs to update. No app code needs to change.

1. Pick a subdomain (CNAME) rather than apex (A record).
2. Render → Settings → Custom Domains → Add. Render shows the exact record.
3. GoDaddy → Manage DNS → add the record. Delete parked `@`/`www` defaults if they collide. **Never use GoDaddy Domain Forwarding** — it serves a GoDaddy redirect page and blocks certificate issuance.
4. Wait for Render to verify; it issues a Let's Encrypt cert automatically.
5. Set `WEBUI_URL`, minding that `webui.url` is a *persistent* config key (`models/config.py:139` reads the DB row before falling back to the env var).
6. Smoke test on the new host.

## Turn 2 — domain chosen

**User:** *(screenshot)* Added `eoxs.askcruz.com` in Render — Hostname `eoxs`, Target `cruz-dsvf.onrender.com`. What next?

**Claude:** Checked DNS: `askcruz.com` is on `ns07/ns08.domaincontrol.com` (GoDaddy), and `eoxs.askcruz.com` did not resolve yet.

Add in GoDaddy: CNAME, Name `eoxs`, Value `cruz-dsvf.onrender.com`, TTL 600. Name is the label only. Then click Verify in Render.

Repo edits made: added `domains: [eoxs.askcruz.com]` to `render.yaml`; updated `DEPLOY-RENDER.md` step 6 with the real URL, the persistent-config trap, and a "The custom domain" subsection.

## Turn 3 — CNAME added

**User:** Added CNAME in GoDaddy, what next?

**Claude:** Verified via diagnostics:

| Check | Result |
|---|---|
| CNAME at GoDaddy authoritative NS | OK |
| Public resolvers (8.8.8.8) | OK, full chain to Render's edge |
| `https://cruz-dsvf.onrender.com/health` | 200 |
| `http://eoxs.askcruz.com/health` | **409** — Render's "domain not verified" response |
| `https://eoxs.askcruz.com/health` | TLS handshake rejected — no cert yet |

Next: click **Verify** in Render.

Side observation: `cruz-dsvf.onrender.com` resolves via `gcp-us-west1-1.origin.onrender.com`, but `render.yaml:16` declares `region: singapore` — the service may actually be running in Oregon, which would mean avoidable latency for a Delhi team. Unrelated to the domain work.

## Turn 4 — WEBUI_URL turned out to be unnecessary

**User:** *(screenshot of Render env vars)* There is no `WEBUI_URL` — it started working without adding it.

**Claude:** Correct, and I overstated it as required. The frontend is entirely same-origin in production (`docs/FRONTEND-ARCHITECTURE.md:122-123` — `WEBUI_BASE_URL` is `''` outside dev), so nothing on the serving path needs an absolute base URL.

`WEBUI_URL` only feeds things that must name the site from outside it: OAuth redirect URIs (not configured), channel webhook links (`routers/channels.py:917`), chat-event webhook links (`utils/middleware.py:3750`), and `/opensearch.xml` (`main.py:2738`).

**The persistent-config trap did not materialise.** `/opensearch.xml` on the live site rendered `<moz:SearchForm></moz:SearchForm>` — the stored value is empty, not `http://localhost:5173`. The seed DB carried no `webui.url` row.

**But a real finding surfaced:** the env list had no `ENV`. `env.py:133` defaults it to `dev`, and `main.py:466-467` gates the FastAPI docs on that. Confirmed live: `/docs`, `/openapi.json`, `/redoc` all returned 200 on the public domain — the full backend API schema, unauthenticated.

## Turn 5 — can the Render link be turned off?

**User:** Can I turn that render link off now?

**Claude (partly wrong, corrected next turn):** Said the `.onrender.com` URL can't be disabled and Render has no switch. Also flagged that one login plus one question is not a complete smoke test, and that `ENV` was still unset.

## Turn 6 — Render does have a switch

**User:** *(screenshot)* **Render Subdomain — Enabled.** "Disable to serve exclusively from custom domains."

**Claude:** That toggle is exactly it; my "no switch" claim was wrong.

Disabling is safe for the custom domain: the toggle controls which `Host` headers Render's router serves, not DNS. `cruz-dsvf.onrender.com` keeps resolving so the CNAME chain stays intact.

**The one thing it breaks:** `PROJECT_SOT.md:1346-1349` — the Capacitor Android shell QA'd on the Pixel 6 / Android 15 image runs in remote mode with `server.url` pointed at `https://cruz-dsvf.onrender.com`. Any installed APK would load a Render error page. The Capacitor config is not in this repo.

## Turn 7 — recommendation

**User:** Should I turn it off?

**Claude:** Yes. Grepped the repo for `cruz-dsvf` — it appears only in `render.yaml`, `DEPLOY-RENDER.md` and `PROJECT_SOT.md`; no code depends on it. The toggle is reversible in seconds and re-enabling does not depend on DNS, which dissolves the "keep it as a fallback" argument. Order: set `ENV=prod` first, check the APK situation, then flip, then verify both hosts.

## Turn 8 — /docs now 404s

**User:** *(screenshot)* `eoxs.askcruz.com/docs` shows "404: Not Found".

**Claude:** That is the fix working — but from outside, `/docs` still measured **200**. Both are true:

| Check | Result |
|---|---|
| `/docs` body markers | `sveltekit` only — no `swagger`, no `redoc` |
| `/openapi.json` Content-Type | `text/html`, not `application/json` |
| `/openapi.json` body | the SvelteKit app shell, not the API schema |

The schema is genuinely gone. Added an "ENV must be set to `prod`" section to `DEPLOY-RENDER.md` recording that the *correct* output is HTTP 200 with `<!doctype html>`, so nobody re-flags this by checking for a literal 404.

## Turn 9 — why 404 in the browser but 200 from curl

**User:** Why am I getting 404 and you 200 on hitting /docs?

**Claude:** Not a conflict — two different layers, both explained by code:

1. `ENV=prod` → `main.py:466` sets `docs_url=None`, so the `/docs` route is never registered.
2. The request falls through every API route to the SPA mount (`main.py:2880-2882`).
3. `SPAStaticFiles.get_response('docs', ...)` finds no such file; `StaticFiles` raises 404.
4. `main.py:288-293` catches that 404 and — because the path does not end in `.js` — returns `index.html` instead, **with status 200**.
5. The browser receives 200 + app shell, runs SvelteKit, whose client-side router finds no `/docs` route and *paints the text* "404: Not Found".

So curl reports step 4's status code; the browser shows step 5's rendered output. The "404" on screen is drawn by JavaScript, not sent by the server. DevTools → Network → the `docs` document confirms Status 200.

The `.js` exception in step 4 is deliberate: a missing bundle returns a real 404 rather than HTML, which would otherwise surface as a confusing MIME-type error.

Practical consequence: "is `/docs` exposed?" cannot be answered by status code on this app — you have to check the body or Content-Type.

**Still open:** Render Subdomain toggle is still Enabled (`https://cruz-dsvf.onrender.com/` returns 200).
