---
thread_name: "invera-recommendation-email-search"
user: "raj"
type: claude-chat
created: 2026-07-30
updated: 2026-07-30
---

# Invera Recommendation Email Search

## User
Can you do a deep dive in my email and find something where I recommended Invera to a prospect

## Assistant
[Offered three rigor-level options via ask_user_input_v0: 5ft quick, 10ft verified, 50ft deep]
Question: "Rigor level for this email search?"
Options: "5ft — quick search, fastest hit", "10ft — verified, cross-check against raw threads", "50ft — deep, includes adjacent context (who, deal outcome, related mentions)"

## User
10 ft

## Assistant
Confirmed. Verified against the raw email, not just the wiki summary.

**Yes — one instance found.**

**Where:** Email to Sam Jenkins (ACI, `sjenkins@acihq.com`), May 27, 2026 — subject "Vendor Invoices AI"
`raw/emails/raj_gmail/2026-05/2026-05-27-vendor-invoices-ai.md`

**Context:** You pitched an AP-automation add-on ("Vendor Invoice AI") where the AI reads inbound vendor invoices and drafts AP entries directly in "Invera" — priced $18K one-time + $1.50/invoice, 4–6 week timeline. ACI's Jamie Vilcheck later introduced Sam Jenkins to you at ACI, and this pitch followed.

**Important flag:** "Invera" here is not the third-party ERP competitor. Every other mention of "Invera" in your email history refers to the actual competitor (Heidtman, Energy Alloys, Salt Creek/All Metals, Majestic all evaluated or chose the real Invera against EOXS). This ACI pitch used "Invera" as the name of your **own** AP-automation module — later corrected/renamed to "Invex" in the April 2026 Imperial MS pitch, and confirmed as "Invex" again when ACI (Monarch Steel) went live with it in July 2026.

So you didn't recommend the competitor's product — you accidentally reused their name for your own product in at least one client-facing pitch. Worth checking whether "Invera" ever went out in writing to ACI again after the rename, since that's a real confusion risk with a client who also evaluates real ERP competitors.

ACI declined the pitch at the time, citing bandwidth mid-ERP-rollout, but the relationship stayed warm — Invex went live at Monarch/ACI two months later.
