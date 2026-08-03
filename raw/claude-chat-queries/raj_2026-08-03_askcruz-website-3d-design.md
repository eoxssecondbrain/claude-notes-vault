---
thread_name: "askcruz-website-3d-design"
user: "raj"
type: claude-chat
created: 2026-08-03
updated: 2026-08-03
---

User: https://www.instagram.com/reel/DYIZUEtxesT/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==
I want to make a website for cruz which has 3D animations in it. I want you to watch this reel as a creative director, get an idea of how this website design has been curated for their product. Simulate a council of 4 people who are experts in creative design, website UI/UX, etc. and tailor a website design for cruz.
give me the prompt that I can use in claude code to build the website.

Assistant: Quick blocker before I can do this properly: I can't actually watch that reel. Instagram blocks fetches (robots disallowed), and there's no audio transcript since it's likely a visual/music-only design showcase — the transcription tool came back empty.

Also, flagging per your skill-routing preference: this task doesn't clearly match any of your loaded skills (not EOXS vault data, not a sales/prospect email). I'm treating it as a standalone creative/GTM task for AskCruz.

To actually simulate the council and reverse-engineer the design, I need one of these from you:

1. Screenshots — 4-5 frames from the reel (upload them here), or
2. A description — what it's a website for, the visual style (glassmorphism, brutalist, dark/light, particle effects, scroll-triggered 3D, product-in-a-box style like Linear/Vercel/Stripe, etc.), and what the 3D elements actually are (a 3D object, an abstract shader background, animated UI mockups...), or
3. The account/creator name or product name — if it's a known SaaS/AI product site, I can web-search for press coverage, Awwwards features, or a case study describing the design, which would give me real material to work from instead of guessing.

Guessing at "what a cool reel probably looked like" and presenting that as a council-derived analysis would be fabrication — I'd rather you give me 30 seconds of real input than hand you a generic "glassy dark AI website" template dressed up as analysis.

Which one do you want to do?

User: would it work if i upload the video in question here

Assistant: Yes — upload the video file directly. Once it's in the upload folder I can pull frames from it with ffmpeg and view those as images, which gets me the actual visual reference instead of guessing. Go ahead and upload it.

User: [uploaded /mnt/user-data/uploads/Video-63668.mp4]

Assistant: Got it — clear picture now. This is a "Claude Code is insane" demo reel for a fictional luxury tea brand ("Assam Tea"), not an existing SaaS product. Useful reference regardless — the technique is what matters, not the tea. Here's what the reel actually does, frame by frame:

Design DNA extracted
- Hero: a single product object (tea bag) glowing on pure black, hangs mid-air, no chrome, no nav clutter — object IS the hero, not a photo of it
- Scroll-triggered narrative: the bag opens → ingredients orbit and bloom → pour into a glass cup → steam rises → copy appears in sync ("Three minutes. That is all it takes.") — every scroll tick reveals a new physical event, not a new screen
- Poetic, deliberately non-corporate microcopy replacing default e-commerce language: "Add to Ritual" instead of "Add to Cart," "Choose your ritual" instead of "Shop now," "Join the ceremony" instead of "Subscribe"
- Product grid styled as artifacts, not SKUs: Dawn / Dusk / Night, each color-graded differently (mint, rose, indigo), gold hairline rule dividers, serif display type throughout
- Ingredient "explosion" section — particles scatter and settle, paired with a craft/provenance claim ("Six ingredients. Centuries of craft.")
- Footer as ritual close, not a form: email capture styled as "Begin →"
- Palette: near-black background, single warm gold/amber accent doing all the emotional work, no secondary colors competing

The council

Creative Director (brand/narrative): This whole reel works because it commits to one emotion — reverence — and never breaks it. Every microcopy choice reinforces "ritual." For AskCruz, the equivalent emotion isn't reverence, it's trust and competence. If we copy the poetic tone literally ("Add to your ritual" for an AI tool) it reads as try-hard. We keep the technique — one emotion, zero corporate language — but the emotion becomes calm authority, not indulgence.

3D/Motion Designer: The tea bag works as a hero object because it's simple, recognizable, and has one dramatic action (opening). AskCruz has no physical product. The equivalent hero object is Cruz itself — render it as a single glowing core/constellation, not a mascot. On scroll: the core stays static while particles (small labeled fragments — an email icon, an invoice line, a call waveform) fly in from the edges and get absorbed into it. That's the direct translation of "ingredients pour into cup" — data becomes the ingredient, Cruz becomes the cup.

UI/UX architect: The tea site can afford pure vibes because the ask is emotional (buy tea). AskCruz's ask is a qualified B2B lead (book a fit call) from a skeptical mid-market CEO. That means the cinematic sections earn their place, but they can't replace information — every scroll section needs a real claim underneath the visual, not just mood. Also: this reel format is single-page, scroll-only. AskCruz needs the scroll story to end in one unambiguous CTA, not a product grid — there's nothing to browse, there's one thing to book.

Frontend/technical lead: This is React Three Fiber (or Spline embedded) plus GSAP ScrollTrigger, near-certainly — that orbiting-particle-into-object choreography is a classic R3F + custom shader pattern, not CSS. Buildable in Claude Code, but flag the real cost up front: WebGL scroll-linked 3D is expensive to get smooth on mobile and on low-end laptops, which matters if actual prospects are opening this on a work Chromebook mid-triage. Ship a lightweight fallback (static gradient + fade-in) below a device/perf check, don't gate the whole page on WebGL loading.

Converged direction for askcruz.com
One-page cinematic scroll, black background, single accent color (I'd suggest a cool electric blue/white instead of gold — gold reads luxury-retail, blue reads intelligence/precision and still pops on black). Hero: Cruz rendered as a glowing neural core. Scroll sequence: core idle → data fragments (email, order, call icons) fly in and get absorbed → core brightens → hero line resolves ("Cruz has read every order, every email, and every call in your business. Ask him anything.") → a section demonstrating a real answered question (not decorative, an actual example) → a short "how it connects" section (3 data sources as glowing nodes, not a stock illustration) → single closing CTA, "Book a fit call," no product grid, no pricing tiers on this page.

I'll write the full Claude Code build prompt as a file so you can paste it straight in.

[Created file: askcruz-website-claude-code-prompt.md — full Claude Code build prompt covering stack (Next.js + TypeScript + Tailwind + React Three Fiber/drei + GSAP ScrollTrigger), design direction (near-black background, single electric blue accent, no stock illustration/glassmorphism, calm non-hypey copy), five page sections (Hero with neural core 3D object and "Cruz has read every order, every email, and every call in your business. Ask him anything." headline and "Book a fit call" CTA; Data absorption scroll sequence with email/order/call particles flying into the core; Proof section with a real mocked Q&A example; How it connects section with three glowing data-source nodes; Closing CTA section reprising the core and CTA), technical/UX constraints (reduced-motion and low-end device fallback, mobile shader simplification, lazy-loaded canvas, accessibility), and an explicit "what not to do" list (no pricing table, no product grid, no testimonial carousel, no anthropomorphized robot character). File presented to user via present_files.]
