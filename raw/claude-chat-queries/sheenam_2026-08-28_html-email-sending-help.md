---
thread_name: "html-email-sending-help"
user: "sheenam"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: I have created an HTML email on Claude designs, and I want to send that HTML email now. How do I send it through my own email? I want it to go into the exact same format as it is visible in the HTML email design in Claude, but I don't know how to send those emails or how to embed it in my email.

Assistant: Depends on how you want to send it — quick and rough, or exact.

Sending as-is through your regular email client (Gmail/Outlook, etc.)

1. Open the HTML design so you can see it rendered (not the source code).
2. Select all the rendered content (Ctrl/Cmd+A) and copy it (Ctrl/Cmd+C) — copy what's displayed, not the HTML markup itself.
3. Open a new email in Gmail or Outlook and paste (Ctrl/Cmd+V) into the compose body.

Gmail and Outlook compose windows read inline CSS, so most layout, colors, images, and fonts carry over reasonably well. What tends to break: custom web fonts (falls back to a default), CSS grid/flexbox layouts, and any background set via CSS instead of an actual <img> tag. This is fine for a one-off but won't be pixel-perfect.

Sending the raw HTML directly (exact match)

Webmail compose boxes don't accept raw HTML source, so if you need it to render exactly as designed, you need to send it through something that takes HTML as the actual email body — a transactional/marketing email API like Resend, Mailchimp, or SendGrid. You paste the HTML source in and it goes out unmodified, so what you built is what recipients see.

You already have Resend connected here. If you give me the recipient address(es), from address, and subject line, I can send this email through Resend right now using the exact HTML from the design.

Which route do you want — paste-in instructions for your own inbox, or should I send it via Resend?
