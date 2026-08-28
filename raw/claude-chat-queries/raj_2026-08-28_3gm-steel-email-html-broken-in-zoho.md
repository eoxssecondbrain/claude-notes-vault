---
thread_name: "3gm-steel-email-html-broken-in-zoho"
user: "raj"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

**User:** i created this html email using claude design but when I paste it on my zoho, it is showing this. It is not working, can you check what is wrong in the code that is not letting the html show in the email and fix it

[User uploaded a screenshot showing Zoho Mail displaying a blank dark screen with the text "This page requires JavaScript to display." and pasted the full HTML source of a "3GM Steel now runs on AI" customer story email, which was a Claude-Design-generated bundler-wrapped HTML file containing a manifest of two base64 images (a JPEG hero banner and a PNG 3GM Steel logo), a JSON-encoded email template with image src attributes referencing uuid placeholders, and a large JavaScript unpacker script that decodes the base64 assets into Blob URLs and swaps them into the DOM at runtime.]

**Claude:** [Read threads-ov and raj-eoxs-vault skill files per user preference for new threads. Determined this was a technical HTML/email debugging task, not a data-connector or sales-strategy task, so proceeded without invoking those connectors.]

Fixed. Here's what was wrong:

The file Claude Design exported isn't the actual email — it's a self-unpacking JS wrapper. It loads a `<script>` that decodes base64 images into blobs and swaps them into the page at runtime. That works fine in a browser preview, but email clients (Zoho, Gmail, Outlook, etc.) always strip `<script>` tags and never execute JavaScript. So Zoho was left showing the fallback text baked into the file: "This page requires JavaScript to display."

The fix: extracted the real email markup from inside the wrapper and inlined both images directly as base64 `data:` URIs in the `<img src="">` attributes, with zero JavaScript. That's a static file any email client can render as-is.

[Created and presented file: /mnt/user-data/outputs/3gm-steel-email-fixed.html]

One caveat: some corporate email clients strip `data:` image URIs too, treating them like embedded scripts. If it still doesn't render in Zoho, the fallback is hosting the two images (JPEG banner + PNG logo) somewhere public and swapping the `src` to real URLs instead — say the word and I'll do that version too.

## Tribal Knowledge Extracted
- Claude Design's HTML export for artifacts/emails wraps output in a JS "bundler" (base64 asset manifest + Blob-URL unpacker script) meant for browser/artifact rendering — this format is NOT directly usable as email HTML, since email clients strip all `<script>` tags. Any HTML email exported from Claude Design needs images inlined as static `data:` URIs (or hosted image URLs) and the bundler script stripped out before pasting into Zoho/Gmail/Outlook.
