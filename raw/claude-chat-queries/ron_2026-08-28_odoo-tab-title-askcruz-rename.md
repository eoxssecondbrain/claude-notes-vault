---
thread_name: "odoo-tab-title-askcruz-rename"
user: "ron"
type: claude-chat
created: 2026-08-28
updated: 2026-08-28
---

User: [uploaded screenshot: Odoo Settings > Employees page, browser tab reading "New - Odoo"] In the bar above, you will see a new - Odoo written. I'm trying to understand: how can I get rid of it and instead it say new - AskCruz?

Assistant: The "- Odoo" suffix comes from the company name field (`res.company.name`) in this Odoo instance, not from the app or database name.

To change it:

1. Go to Settings > Users & Companies > Companies
2. Open the company record (probably still named "Odoo" or default demo name)
3. Rename it to "AskCruz"
4. Save

The tab title format is "{page/action} - {company name}", so once the company record's name is "AskCruz", every tab will read "New - AskCruz" instead of "New - Odoo" going forward, across the whole instance, not just this page.

If you also want the favicon or browser tab icon changed, that's a separate setting (Settings > General Settings > favicon upload), but that's not what's causing this text.

User: I need to create a favicon for AskCruz, just like there is for Odoo. Can you please make one for me? For Odoo, we have the O. For AskCruz, we do have a logo. You can find that on the vault. Maybe it can be something which is simple. I just need a simple image. Can you give me something like that?

Assistant: [Found the "AskCruz logo" file on Google Drive.] Found the "AskCruz logo" file. Before I build this, quick pick on craft level:

- Sketch — simple crop/reduce of the logo mark to a square icon, one pass, no polish
- Draft — cropped and cleaned up, proper favicon sizes generated, presentable
- Painting — custom-simplified icon derived from the logo (removes fine detail that won't read at 16px), tested at multiple sizes

Which one, or should I just go with Draft?

User: Yes, I think her sketch would work. Give me one sketch and one painting, and then I'll see which one is better.

Assistant: [Downloaded the AskCruz logo PNG from Google Drive, cropped it tightly and centered it on a white square canvas for the sketch version. Built a custom flattened redraw for the painting version: simplified the claw from three prongs to two, removed the 3D gradient/shine, thickened the strokes into solid navy shapes, cropped and centered on a white square canvas. Generated 16/32/48px previews of both to check legibility, then exported both as PNG and ICO favicon files.] Sketch is just the logo cropped tight and centered on a square — it holds up at 512px but blurs into a smudge by the time it's shrunk to actual favicon size (16-32px), since it keeps the 3D shine and all three prongs.

Painting is a flattened, single-color redraw — dropped one prong, killed the gradient/shine, thickened the strokes — so it still reads clearly at 32px and should hold at 16px too.

For an actual browser tab favicon, painting is the one that'll work. Sketch is really only useful as a full-size logo mark, not a favicon.

Files delivered: askcruz-favicon-sketch.png, askcruz-favicon-painting.png, askcruz-favicon-sketch.ico, askcruz-favicon-painting.ico
