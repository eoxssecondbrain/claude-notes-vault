---
thread_name: "cruz-godaddy-custom-domain"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# Cruz — pointing the GoDaddy domain at the Render service

**User:** The service is currently hosted on Render, and we have purchased a new domain in GoDaddy. I want to host the service with our domain. What are the steps?

**Claude:**

Context from the repo: `render.yaml` defines a single web service `cruz` (Docker, Standard plan, region singapore, branch `deploy/render`), currently reachable at `https://cruz-dsvf.onrender.com`. `WEBUI_URL` is `sync: false` and set in the dashboard. No OAuth provider is configured, so there are no redirect URIs to update.

## 1. Pick the hostname
Recommend a subdomain — `chat.<domain>` or `cruz.<domain>`. Subdomains use a CNAME, which is what Render actually wants. Apex/root (`<domain>` with no prefix) needs an A record and is more fragile. If the apex is wanted, add both and let Render redirect apex → subdomain.

## 2. Render: add the custom domain
Dashboard → `cruz` service → **Settings** → **Custom Domains** → **Add Custom Domain**. Enter `chat.<domain>`. Render then displays the exact DNS record to create — use the value it shows, not a remembered one.

- Subdomain → `CNAME` pointing at `cruz-dsvf.onrender.com`
- Apex → `A` record at Render's anycast IP (currently `216.24.57.1`)

Custom domains are free on all Render plans.

## 3. GoDaddy: create the DNS records
First confirm the domain still uses GoDaddy nameservers (Domain Settings → Nameservers). If they were moved to Cloudflare or elsewhere, edit DNS there instead.

GoDaddy → **My Products** → domain → **DNS** → **Manage DNS**.

Delete GoDaddy's parked defaults first, or they will conflict:
- the `A` record on `@` pointing at a GoDaddy parking IP
- the `CNAME` on `www` pointing at `@`

Then add:

| Type | Name | Value | TTL |
|---|---|---|---|
| CNAME | `chat` | `cruz-dsvf.onrender.com` | 600 |
| A (only if apex is wanted) | `@` | value Render displays | 600 |

Two cautions:
- **Do not use GoDaddy "Domain Forwarding"** for this. It serves a GoDaddy redirect page and blocks Render's certificate issuance.
- Name is just the label (`chat`), not the full hostname — GoDaddy appends the domain.

## 4. Wait for verification and the certificate
Render polls DNS and flips the domain to **Verified**, then issues a Let's Encrypt cert automatically. Usually minutes; GoDaddy propagation can take up to an hour. No action needed for HTTPS.

## 5. Update WEBUI_URL — including the persistent-config trap
Set `WEBUI_URL=https://chat.<domain>` in the Render Environment tab (per `DEPLOY-RENDER.md` step 6).

**Gotcha:** `webui.url` is a *persistent* config key. In `backend/open_webui/models/config.py:139`, `Config.get` reads the DB row first and only falls back to the env-var default when no row exists. The production DB was seeded from the local `webui.db`, where `WEBUI_URL=http://localhost:5173`. If a row was written, the env var will be silently ignored.

Fix either way:
- change it in **Admin Settings → General** in the running app (writes the DB row), or
- set `ENABLE_PERSISTENT_CONFIG=false` so env vars always win — cleaner for a Render deploy where env is the source of truth, but it makes every other admin-settings change env-only too.

Then redeploy.

## 6. Verify
- `https://chat.<domain>` loads, padlock valid
- log in as `ijassandhu.dev@gmail.com`; Workspace → Models shows both `eoxs-vault-assistant` models
- `+` menu in a chat lists the vault tools (bridges are on `127.0.0.1:909x`, unaffected by the domain)
- streaming responses work (websocket upgrade through the new host)

The `.onrender.com` URL keeps working; Render does not redirect it. Set the custom domain as primary in Render if you want the old one to redirect.

## 7. Optional follow-ups
- Add `domains: [chat.<domain>]` to the web service in `render.yaml` so the domain is reproducible from the blueprint rather than dashboard-only state.
- Tighten `CORS_ALLOW_ORIGIN` — it currently defaults to `*`. Production is same-origin, so `https://chat.<domain>` is sufficient.
- Update `DEPLOY-RENDER.md` step 6 and `PROJECT_SOT.md` (service table + the `WEBUI_URL` notes) once the domain is live.

Nothing in the app code needs to change. The MCP upstreams (`raj-vault-mcp-server.onrender.com`, `claude-notes-vault.onrender.com`) are separate services and are not affected.
