---
thread_name: "3gm-outlook-oauth-integration"
user: "ayan"
type: claude-chat
created: 2026-08-25
updated: 2026-08-25
---

**User:**
I am ok with 60secs delay, as long as system runs smooth. Given this info, make a final prompt on which claude code can build this automation..

**Assistant:**
[Wrote and saved the final build prompt to /mnt/user-data/outputs/outlook-oauth-automation-build-prompt.md, presented to the user, and summarized it in chat.]

Final locked decisions baked into the prompt:
- Microsoft Graph official APIs only, no third-party platform, no MCP servers.
- No push subscriptions/webhooks/renewal jobs — real-time replaced with Microsoft Graph delta query polling every 60 seconds (confirmed accepted by user), using the same mechanism for both historical backfill (first call, no cursor = full paginated backfill) and ongoing sync (subsequent calls replay the saved @odata.deltaLink cursor).
- Scope: this targets 3GM's own new, separate AskCruz database/deployment only — explicitly does not touch or extend EOXS's internal eoxs-db/Cruz knowledge base (a different, separate deployment with its own Gmail/Zoho/Fireflies/Fathom sources, confirmed via the AskCruz self-knowledge architecture asset in Raj-Vault).
- Account label convention: <client_slug>_<person>_outlook, e.g. 3gm_travis_outlook, 3gm_jessica_outlook (not a single shared "owner" label, since 3GM's accepted scope covers two distinct mailbox owners).
- Dedup: unique constraint on Microsoft Graph's internetMessageId field, with a provenance-tracking join table (outlook_message_sightings) recording every mailbox that received a copy of the same message, rather than silently discarding that information — reasoning tied to the AskCruz architecture's own citation-checking pipeline stage, which needs per-source provenance.
- Instructed Claude Code to check for and defer to a real docs/raw-ingestion.md schema convention in 3GM's actual deployment if one exists, rather than treating the proposed sightings-table schema as fixed.
- Open questions flagged in the prompt for Claude Code to raise rather than assume: whether 3GM's own repo already has an existing OAuth connect flow to mirror, whether an EOXS Microsoft Entra tenant already exists, whether 3GM is confirmed to be on Microsoft 365/Exchange Online, and whether a real raw-ingestion doc exists with a different schema convention.

Full content of the final build prompt file (as written to /mnt/user-data/outputs/outlook-oauth-automation-build-prompt.md):

# Build brief: 3GM Outlook/Microsoft 365 ingestion for AskCruz

## Context — read before writing anything

3GM Steel is getting its own dedicated AskCruz deployment, on its own new, separate database. This build does not touch, extend, or share schema with EOXS's internal eoxs-db / Cruz knowledge base — that is a different deployment entirely, with its own Gmail/Zoho/Fireflies/Fathom sources, and nothing here should modify it.

Before writing any code:
1. Check whether 3GM's own repo/deployment already has an existing OAuth connect flow (Gmail, Zoho, or otherwise) to mirror conventions from. If one exists, match its naming, error handling, file layout, and logging style exactly.
2. If no existing connect flow exists in this deployment yet, mirror the general pattern described below — it's based on a working Gmail OAuth implementation elsewhere in the company (one-click consent link, PKCE, server-side refresh-token storage, plain confirmation page) — but implement it fresh, against 3GM's own database.
3. Look for a raw-ingestion / storage-architecture doc in this deployment (something like docs/raw-ingestion.md or docs/postgres-database.md). If one exists, follow its schema conventions for the dedup/provenance table below rather than inventing a new shape — this brief proposes a reasonable default, not a mandate, in case one isn't found.

## Goal
Give a 3GM mailbox owner a one-click Microsoft consent experience — click a link, log into Microsoft directly, approve read-only mail access — after which their full mail history gets pulled into 3GM's AskCruz raw ingestion layer, and new mail keeps landing automatically going forward, with duplicates across multiple connected 3GM mailboxes collapsed to one record.

## Decisions already made — do not re-litigate these
- Microsoft Graph official APIs only. No third-party unified email platform — client mail data does not flow through any vendor besides Microsoft.
- No MCP servers, no external connector SDKs. Direct HTTPS calls to Microsoft's identity platform and Graph API.
- No push subscriptions, no webhooks, no /subscriptions API, no renewal job, no lifecycle-notification handling. Real-time delivery is via polling, not push.
- 60-second poll interval is accepted and confirmed. Do not tighten or loosen it without checking back.
- No calendar or contacts sync. Mail only, read-only, one direction.

## Part 1 — OAuth connect flow
New module: oauth_outlook. CLI invite command generates a random, single-use, expiring token. Account label convention: <client_slug>_<person>_outlook, e.g. 3gm_travis_outlook, 3gm_jessica_outlook. GET /oauth/outlook/connect builds the Microsoft authorization URL (login.microsoftonline.com/common/oauth2/v2.0/authorize, scope openid offline_access https://graph.microsoft.com/Mail.Read, PKCE S256, prompt=consent). GET /oauth/outlook/callback exchanges the code, checks for refresh_token (hard error if missing), upserts into account storage with source_type='outlook', triggers initial backfill. One-time app registration: Entra app, multitenant + personal accounts, Web platform, redirect URI registered exactly, new env values OUTLOOK_OAUTH_CLIENT_ID/SECRET. Note: confirm 3GM's Microsoft 365 tenant consent policy and admin contact before sending the first real invite link.

## Part 2 — Backfill + ongoing sync (single mechanism, no webhooks)
New module: outlook_fetcher, using Microsoft Graph delta query. sync_mailbox looks up stored delta cursor; if none, full paginated backfill via /me/mailFolders('inbox')/messages/delta; if cursor exists, incremental sync via that cursor. Save new deltaLink after each run. On 410/stale cursor, discard and re-run full backfill, logging it. Scheduler runs sync_mailbox for every connected outlook account every 60 seconds. Standard access-token refresh via stored refresh_token. Alert on repeated sync failures for a mailbox (likely revoked access, discovered reactively since there's no webhook lifecycle signal). Rate limits not a concern at this scale.

## Part 3 — Deduplication across mailboxes
Unique constraint on internet_message_id (Microsoft Graph's internetMessageId field). Default recommendation: track provenance via a join table rather than silently discarding it:
CREATE TABLE outlook_message_sightings (id SERIAL PRIMARY KEY, internet_message_id TEXT NOT NULL, account_label TEXT NOT NULL, seen_at TIMESTAMPTZ NOT NULL DEFAULT now(), UNIQUE (internet_message_id, account_label));
Table/column names should match a real docs/raw-ingestion.md convention if found. Rationale: the pipeline's citation-checking stage may need to reference which mailbox specifically received a copy.

## Deliverables
OAuth connect flow module, fetcher/sync module, schema for account storage + delta cursor + message-sightings join table, setup documentation covering Entra app registration and the 3GM tenant-consent caveat.

## Acceptance criteria
1. Invite link redirects to a real Microsoft consent screen scoped to Mail.Read only.
2. Completing consent produces a stored refresh_token and triggers a full backfill.
3. New test email ingested within roughly 60-90 seconds, no manual trigger.
4. Same email sent to two connected 3GM mailboxes produces one canonical record, two sightings rows.
5. Forced 410/stale-cursor response recovers via fresh full resync rather than failing permanently.
6. Revoking app access causes the next poll cycle to fail loudly (alert fires), not silently.

## Open questions to raise back, not guess at
- Does 3GM's own deployment/repo already have an existing OAuth connect flow to mirror, or is this the first one built for it?
- Does EOXS already have a Microsoft Entra tenant to register the app in?
- Is 3GM's mail actually on Microsoft 365 / Exchange Online?
- Does a real docs/raw-ingestion.md-equivalent exist in 3GM's deployment with a different schema convention than the sightings-table default proposed above?
