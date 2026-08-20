---
thread_name: "craft-fidelity-level-framework"
user: "raj"
type: claude-chat
created: 2026-08-20
updated: 2026-08-20
---

User: I like the rigor level, feature I have set up in Claude instructions. 

This really helps in the depth of analysis  

Let’s talk about something different. So let’s say if I want to actually get a work done, let’s say I want to create a Html email.  I want to make a painting. There could be different levels at the end result would look like.  
A horse painted can be a sketch can be a watercolour can be a painting can be a drawing made by sketch pen. Html email would also have that attention to detail about every little thing. 

You understand what I mean  it’s not the same as rigor level.

Assistant: That's a real distinction, and it's not one my current setup captures. Rigor governs how much I verify before I answer. It says nothing about how much craft goes into what I actually build.

Right now if you ask for an HTML email, I pick a fidelity level by guessing — usually landing somewhere in the middle, which is often wrong in both directions. Sometimes you want a 10-minute functional draft to unblock a send. Sometimes you want something that looks like it came out of a real design system, with hover states, dark-mode-safe colors, tested rendering across Outlook/Gmail/Apple Mail quirks, the works.

A rough analogy to your sketch → watercolor → painting scale, applied to a build task like an HTML email:

Level 1, sketch — plain structure, minimal inline CSS, gets the message and CTA across. Built in one pass, no client-compatibility testing.

Level 2, draft — branded colors/fonts, single-column layout, decent spacing, functional but not obsessed over. What most "good enough" marketing emails look like.

Level 3, painting — custom layout, responsive breakpoints, tested against major email client rendering quirks, considered copy hierarchy, real attention to whitespace and visual rhythm.

Level 4, commissioned piece — everything in level 3 plus interactive elements where supported, accessibility pass, A/B-test-ready variants, dark mode handling, pixel-level review.

This applies beyond email too — same axis for a slide deck, a landing page, a proposal doc.

Two questions before I'd treat this as a standing framework rather than a one-off:

Do you want this as a second axis you declare alongside rigor level each time ("10ft rigor, level 3 craft"), or should I infer craft level from context (internal draft vs. client-facing) and just state my assumption before building?

And do you want me to write this into your instructions now, or just apply it ad hoc for today and see if it holds up before making it permanent?
