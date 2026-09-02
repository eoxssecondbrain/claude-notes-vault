---
thread_name: "3gm-outlook-ingestion-beginner-explainer"
user: "innovation_interns"
type: claude-chat
created: 2026-09-02
updated: 2026-09-02
---

User: go through these files and explain me everything aas explaining to a beginner who knows nothing about this

[Uploaded files: cruz-3gm-linear-setup-guide.md, cruz-3gm-wiki-ingestion-setup-guide.md, ARCHITECTURE.md, CLAUDE.md]

Assistant: This system pulls email from Outlook/Microsoft 365 mailboxes into a database, for 3GM Steel. Here's what everything means, piece by piece.

## The big picture

Think of it as a pipe: emails live in Microsoft's servers (Outlook/365). This system reaches in, copies the emails out, and stores them in a database (Postgres) here. It's read-only — it never sends, deletes, or modifies anything in the actual mailbox. Downstream, some other system uses that stored email data to build a "knowledge base" (searchable info about what's in those emails).

## The two programs

There are two separate Python programs that run all the time, independently:

1. **The web app (app.py)** — a small website whose only job is handling the "connect your mailbox" process (OAuth). Nothing else lives on this website.
2. **The sync engine (outlook_fetcher.py)** — runs in the background, checks Microsoft's servers every 60 seconds for new email, and saves it to the database.

They never talk to each other directly. They only communicate by both reading/writing the same database.

## How a mailbox gets connected (step by step)

1. Someone runs a command to generate an invite link for a specific mailbox (e.g., "connect Travis's inbox"). This link expires in 48 hours.
2. That person clicks the link, which sends them to Microsoft's login/consent screen, asking permission to read their mail (nothing more).
3. After they approve, Microsoft sends back a "refresh token" — a long-lived credential letting the app read that mailbox going forward, without needing the person to log in every time. If Microsoft doesn't return this token, the whole thing fails on purpose rather than silently working half-broken.
4. Immediately after that, the system does its first full email sync for that mailbox.

PKCE, mentioned in the docs, is a security technique tying steps 2 and 3 together so nobody can hijack the process in between. Not important to remember in detail — just know it's a security measure, not extra clutter.

## How ongoing syncing works

- Every 60 seconds, the sync engine checks each connected mailbox for new mail.
- Microsoft's API gives it a "delta" — basically "here's what changed since last time you asked," using a bookmark called a cursor.
- First time syncing a mailbox: no cursor exists yet, so it pulls everything since September 1, 2025 (a hardcoded start date), one page at a time.
- After that: it just asks "what's new since my last cursor" — much cheaper than re-pulling everything.
- Important quirk: if a developer later changes what fields get pulled, or changes that start date, it does NOT retroactively apply to mailboxes already connected. Their cursor "locked in" the old settings. To fix it, someone has to manually wipe that mailbox's cursor, forcing a full re-pull.

Also: Microsoft's API can only give deltas per-folder (inbox, sent items), not for the whole mailbox at once — that's why there's a separate tracking table per folder.

## How duplicate emails are handled

If the same email lands in two different connected mailboxes (e.g., someone CC'd both Travis and Stefan, and both are connected), the system:
- Stores the actual email content once (deduped by a unique ID Microsoft gives every message).
- But still records, in a separate table, that "this mailbox also saw this email" — so no information about who-saw-what is lost, even though the email itself isn't duplicated.
- Which mailbox's copy becomes the "main" stored version is essentially random (whichever synced first) — not meaningful, don't read anything into it.

## Attachments

When a genuinely new email (not a duplicate sighting) has an attachment, the file is downloaded and stored as raw bytes. The system also tries to extract readable text from it (PDF, Word, Excel, etc.) and stores that alongside — but if text extraction fails, it just quietly skips that part; the raw file is still saved either way.

## The database

7 tables, all prefixed outlook_, kept isolated from anything else in the database:

- outlook_connect_tokens — the invite links (single-use, expiring)
- outlook_accounts — one row per connected mailbox, plus health info (is it failing?)
- outlook_folder_sync_state — the "bookmark" (cursor) per mailbox/folder
- outlook_messages — the actual emails, one row each
- outlook_message_sightings — who-saw-what (the duplicate tracking mentioned above)
- outlook_attachments — files, raw bytes + extracted text

## Deployment (where this actually runs)

There are two completely separate copies of this whole setup: Staging (testing only, domain 3gmstaging.askcruz.com) and Production (real data — Travis, Stefan's actual mail — domain 3gm.askcruz.com). Same code, separate servers, separate databases. This is deliberate — Microsoft's login flow is tied to which domain the request came from, so you can't easily share one server for both. The docs specifically warn: production's setup docs have previously said "this is configured" when it actually wasn't on the real server — so if working on production, verify directly rather than trusting the paperwork.

## Things this system deliberately does NOT do

- Doesn't touch calendar or contacts, only mail.
- Doesn't reflect deleted emails (if you delete an email in Outlook, it stays in this archive — it's a permanent record, not a live mirror).
- Doesn't page/alert anyone on failure — it only writes an error to a log file. No Slack ping, no email.
- BCC visibility is limited by Microsoft itself, not this system's fault: you only see who was BCC'd if you're looking at the sender's copy.

## For anyone touching the code

- There's no automated test suite — changes get verified by reasoning through the code or checking against a real database/API response.
- Database schema changes are plain .sql files, applied by hand — there's no auto-migration tool, so each change has to be manually run on staging and production separately.
- .env files (containing secrets) are never committed to the code repository.

Anything above you want me to go deeper on?
