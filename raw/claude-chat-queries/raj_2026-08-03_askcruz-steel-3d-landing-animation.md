---
thread_name: "askcruz-steel-3d-landing-animation"
user: "raj"
type: claude-chat
created: 2026-08-03
updated: 2026-08-03
---

USER: I want an animation on my landing page for Ask Cruise. I want you to build a council of experts and read some books around the psychology of building landing pages, and then use creative ideas from people instead of using your own creativity. Give me a prompt that I can use to create a 3D animation for the landing page of this website.
I want this to be done in a detailed, extensive way. For example, how we have the 50-foot-deep rigor level, I want you to take a step back and think how you could do this exercise at a 500-foot-deep rigor level, and then give me the prompt. I can put it in some AI animation 3D builder and get an animation for our screws.
Be mindful that at this point we are only going to be focused on steel, so the animation can look steel-specific also. Our ICP in steel is mostly people from steel coils, steel bars, and plates. How can we show someone, with the help of an animation visually, what we are doing with our screws, where they come on the website and they see the landing page? In less than 4 seconds, they have that "ah" moment that they understood exactly what we were doing.

ASSISTANT: Skill note already flagged above — proceeding as a standalone creative/research task, sales-strategist voice applied only where it's genuinely about positioning claims.

## The council (real people, real books — not invented)

| Seat | Source | Core principle pulled in |
|---|---|---|
| Attention scientist | Nielsen Norman Group / Carleton University eye-tracking research | Aesthetic judgment forms in 17-50 milliseconds, driven by parallel visual processing before language centers even activate, and it takes about 2.6 seconds for a viewer's eyes to land on the single area that dominates their first impression. Your 4-second budget is actually generous by this data — the real constraint is under 1 second for the "what is this" read. |
| Usability elder | Steve Krug, Don't Make Me Think | Design web pages like billboards — a clear, concise message understood in a few seconds, because users scan rather than read word-for-word. Familiar conventions reduce cognitive load — use patterns the visitor already recognizes rather than teaching a new one. |
| Cognitive design theorist | Don Norman, The Design of Everyday Things | Affordances determine what actions are possible; signifiers communicate where the action should take place — you need both. An animation that looks beautiful but doesn't signify "ask this thing a question" has failed at the signifier layer even if it nails the affordance. |
| Messaging strategist | Donald Miller, Building a StoryBrand | A confused mind says no — clarity beats cleverness, and the customer, not the brand, has to be positioned as the hero. Miller's hitchhiker analogy: the visitor has one burning question — "where are you going" — and anything else you lead with, they tune out. |
| Behavioral economist | Rory Sutherland, Alchemy | Uber didn't make cars arrive faster — it just showed the map, removing the agonizing uncertainty of waiting; efficiency isn't always what user experience design should optimize for, visibility is. This is the direct model for what your animation should do: make invisible AI reasoning visible, not just claim it exists. |
| Memory/attention researcher | Hedwig von Restorff, isolation effect | One distinctive element against a uniform field is what gets noticed and remembered — the isolation effect works by making the surroundings uniform, not by making the target louder. One glowing focal point, not five. |

## The uncomfortable data point the council surfaces

Before the concept — a finding that should change your brief, not just decorate it. Current 2026 SaaS landing page data shows the opposite of what you're about to commission: prior to 2026 most SaaS sites leaned on abstract 3D graphics or illustration in the hero, and that approach is losing ground as companies see stronger results from showing the actual product early and clearly, because buyers convert on whether they can tell how complex the product is and whether it fits their workflow, not on how polished the visual is. Separately, the highest-converting 2026 heroes (Notion, Linear) use narrative headlines plus workflow visuals to show transformation within the first few seconds — not standalone abstract art.

Translation: a pure abstract 3D sequence with no product reveal is a known underperformer in 2026 data, however good it looks. Krug and Norman above are both making the same point from a different angle — self-evidence and signifiers, not spectacle. So the brief below isn't "make a beautiful 3D loop," it's "make a 4-second metaphor that resolves into a signifier of the actual product" — animation as a 2-second cold open, cutting into a 2-second reveal of the real interface answering a real steel question. That hybrid structure is what the evidence actually supports.

## The concept: "Mill to Mind"

Applying the council directly rather than inventing from scratch: your ICP (coil, bar, plate buyers and sellers) already has one universal, unteachable visual vocabulary — the mill. Coil unspooling, a bar being drawn straight, a plate being stacked and squared off. Krug's "use conventions the audience already has" points straight at this: you don't need to teach steel people what a mill process looks like, so anchor the metaphor there instead of a generic abstract data-particle cloud, which is what every other AI SaaS site is already doing and which is exactly the genre that's losing effectiveness per the 2026 data above.

The sequence, in beats:

0.0–1.2s — Raw material state. A slightly chaotic pile/stack of steel forms — a coil, a stack of plates, loose bar stock, rendered dark, industrial, slightly disordered — visually standing in for the chaos of scattered orders, emails, calls, ERP data. This is the visitor's current reality, shown, not described (Norman: show the state, don't caption it).

1.2–2.5s — The mill pass. The material moves through a single glowing pass line (Von Restorff: one bright, isolated element against the dark industrial field) — the AI "reading" it in real time. This beat is the visualization of the invisible reasoning process, the Sutherland move: don't claim intelligence, show the progress bar equivalent for it.

2.5–4.0s — Resolved state. What comes out the other end isn't more steel — it's a clean, structured answer card or chat interface, materializing with real steel-industry language on it (e.g., a heat number, a PO, an inventory count, "your Coil #4471 ships Thursday"). This is the signifier — it tells the visitor exactly what to do next (ask it something) and exactly what kind of answer they'll get. This is also the hero as the customer, not AskCruz — the card answers their question, not a mission statement.

One glowing color, one motion axis (linear, mill-line direction — left to right or top to bottom, not swirling particles), one payoff. Everything else in the frame stays uniform and dark so the pass line reads as the isolate.

## The prompt

This is written for a text-to-3D/motion generator (Spline AI, Runway Gen-4.5, Luma, or similar). Structure follows the field-tested format — [subject] + [shape/form] + [material/surface] + [style] + [purpose/context] — with motion described as what happens next rather than restating what's already visible, since Gen-4.5-class models treat the opening frame as fixed composition and the prompt as instructions for motion, and shot type and lighting stated up front, since 2026-era models resolve camera terminology and lighting physics with much higher fidelity when they're the first things named.

```
SCENE: "Mill to Mind" — 4-second hero loop for a steel-industry AI product landing page.

SHOT: Close-up, straight-on tracking shot, camera moves left to right at a
constant slow speed, matching the direction of material travel. No orbit,
no dolly zoom — motion stays on a single horizontal axis to keep the eye
locked on one line of action.

LIGHTING: Low-key industrial. Near-black background (#0a0a0a), single hard
key light from upper-left simulating mill-floor sodium lighting, practical
sparks and dust motes catching the light. High contrast, minimal ambient
fill — the darkness is intentional negative space.

BEAT 1 (0.0–1.2s) — SUBJECT: A slightly disordered stack of raw steel forms
— one coil (unspooling loosely at the edge), a few bar lengths at
mismatched angles, one stack of plate offcuts. MATERIAL: brushed dark
steel, visible mill scale, cool blue-grey specular highlights, faint rust
edges. STYLE: photorealistic industrial, not stylized/cartoon. The
composition should read as slightly chaotic — uneven spacing, no grid.

BEAT 2 (1.2–2.5s) — MOTION: a single thin line of intense cyan-white light
(the "pass line") sweeps left to right through the stack, exactly like a
rolling mill pass or a scanning laser. Everywhere the light passes, the
material behind it snaps into clean, aligned, glowing geometric order —
coil becomes a perfect cylinder, bars align into a parallel row, plates
square into a stacked grid. Only the pass line itself is the bright
saturated color in the frame; everything else stays desaturated steel-grey.
Add fine particle sparks trailing the light line, physically-based, falling
with gravity.

BEAT 3 (2.5–4.0s) — RESOLUTION: as the light line exits frame-right, it
resolves into a thin, sharp-edged glass/glowing UI card floating just
above the now-organized steel, displaying a short readable line of text
in a clean sans-serif — a real, specific steel-operations line such as
"Coil #4471 — 3.2 tons, ships Thursday" or "12 open orders, 2 need review."
The card should look native to the material (steel-blue glow, subtle
reflection on the polished steel below it) rather than a generic floating
app screenshot. End on a held final frame, camera settled, card fully
legible.

STYLE REFERENCES: industrial product photography (think Bloomberg/WSJ
steel-mill photojournalism) crossed with a minimal fintech dashboard
reveal — not sci-fi, not neon-cyberpunk, not particle-cloud abstract art.

NEGATIVE PROMPT: no human figures, no text logos, no swirling/orbiting
camera, no rainbow gradients, no glassmorphism clutter, no generic
floating data-particle cloud, no blurry/morphing geometry, no watermark.

LOOP: should read cleanly as a loop or as a fixed 4-second hero clip —
avoid a hard cut; end state should hold for a beat before restarting.
```

Two practical notes for whichever tool you actually use it in. If you're on Spline AI, generate the coil/bar/plate geometry and the UI card as two separate text-to-3D objects first — Spline's guidance is explicit that it performs much better generating one object at a time than a full composed scene in one pass — then animate the pass-line and camera move yourself in the Spline editor, since its native animation timeline will give you far more control over the exact 1.2s/2.5s/4.0s beat timing than a single text prompt can guarantee. If you're going straight to Runway or Luma for a rendered video instead of an interactive 3D scene, drop this in as one continuous prompt — those models are tuned to read a single flowing motion description rather than a discrete beat sheet, so I'd collapse the three beats into one paragraph before pasting if you go that route. Happy to rewrite it in that collapsed form if that's the tool you're actually using.

One last flag, not a hedge: the ending card content is the highest-leverage 20% of this whole animation. Krug and Norman above both point at the same thing — the metaphor gets attention, but the card is what tells the visitor what AskCruz actually does and what to do next. If that end-card line is generic ("AI-powered insights") instead of a specific, plausible steel-operations sentence, you'll have a beautiful 4 seconds that still fails the StoryBrand test — clear metaphor, unclear offer.
