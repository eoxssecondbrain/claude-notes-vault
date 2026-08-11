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
Recommend a subdomain — `chat.<domain>` or `cruz.<domain>`. Subdomains use a CNAME, which is what Render actually wants. Apex/root needs an A record and is more fragile.

## 2. Render: add the custom domain
Dashboard → `cruz` service → **Settings** → **Custom Domains** → **Add Custom Domain**. Render then displays the exact DNS record to create.
- Subdomain → `CNAME` pointing at `cruz-dsvf.onrender.com`
- Apex → `A` record at Render's anycast IP (currently `216.24.57.1`)

## 3. GoDaddy: create the DNS records
Confirm the domain still uses GoDaddy nameservers. Delete GoDaddy's parked defaults (`A` on `@`, `CNAME` on `www`) first. Do **not** use GoDaddy "Domain Forwarding" — it serves a GoDaddy redirect page and blocks Render's certificate issuance.

## 4. Wait for verification and the certificate
Render polls DNS, flips the domain to **Verified**, then issues a Let's Encrypt cert automatically.

## 5. Update WEBUI_URL — including the persistent-config trap
`webui.url` is a *persistent* config key. `Config.get` (`backend/open_webui/models/config.py:139`) reads the DB row first and only falls back to the env default when no row exists. The production DB was seeded from the local `webui.db`, where `WEBUI_URL=http://localhost:5173`. Fix by changing it in Admin Settings → General, or setting `ENABLE_PERSISTENT_CONFIG=false`.

## 6. Verify
Load the domain, log in as `ijassandhu.dev@gmail.com`, confirm both `eoxs-vault-assistant` models and the vault tools in the `+` menu, and check streaming works (websocket upgrade).

## 7. Optional follow-ups
Add `domains:` to `render.yaml`; tighten `CORS_ALLOW_ORIGIN`; update `DEPLOY-RENDER.md` and `PROJECT_SOT.md`.

---

**User:** *(screenshot of Render's "Add Custom Domain" dialog)* — domain `eoxs.askcruz.com`, Hostname `eoxs`, Target value `cruz-dsvf.onrender.com`. Added this in Render, what next?

**Claude:**

Checked DNS: `askcruz.com` nameservers are `ns07/ns08.domaincontrol.com` (GoDaddy, so DNS is edited there), and `eoxs.askcruz.com` does not resolve yet — the record isn't in.

## Next: add the CNAME in GoDaddy

GoDaddy → **My Products** → `askcruz.com` → **DNS** → **Manage DNS** → **Add New Record**:

| Field | Value |
|---|---|
| Type | `CNAME` |
| Name | `eoxs` |
| Value | `cruz-dsvf.onrender.com` |
| TTL | Custom, 600 seconds |

Name is `eoxs` only, not the full hostname — GoDaddy appends `askcruz.com`. No trailing dot on the value. Nothing to delete: the parked `@` and `www` records don't collide with the `eoxs` label. Do not use Domain Forwarding.

## Then click Verify in Render

Once the record resolves, hit **Verify** in the dialog still open. Render marks the domain Verified and issues a Let's Encrypt certificate — typically a few minutes after DNS propagates, though the dialog warns it can take 24 h.

Check propagation with:
```
nslookup eoxs.askcruz.com
```
Expect `cruz-dsvf.onrender.com` in the answer. Until then, the CNAME is simply not published yet — clicking Verify early is harmless, it just fails.

## Then set WEBUI_URL

`WEBUI_URL=https://eoxs.askcruz.com` in the Render Environment tab, and mind the persistent-config trap from step 5 above: check Admin Settings → General actually shows the new URL after the redeploy, because a `webui.url` row in the DB silently wins over the environment variable.

## Repo changes made

- `render.yaml` — added a `domains: [eoxs.askcruz.com]` block to the `cruz` service so the domain is reproducible from the blueprint rather than dashboard-only state.
- `DEPLOY-RENDER.md` — step 6 now names the real URL, documents the persistent-config trap with the `config.py:139` reference, and adds a "The custom domain" subsection recording the GoDaddy CNAME, the nameservers, and the Domain-Forwarding warning.

`PROJECT_SOT.md` gets its entry once the domain is verified and serving, rather than recording an intention.
