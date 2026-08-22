---
thread_name: "ai-steel-tshirt-design"
user: "Harsimran"
type: claude-chat
created: 2026-08-22
updated: 2026-08-22
---

**User:** create a design for tshirt the front side of the t shirt will have "AI STEEL" 50-100 times in 11inches into 17 inches format diagonally a whole design for tshirt design in jpeg format without any background. you are a expert designer, use canva for designing

**User (mid-turn):** no visuals for front use only "AI STEEL" WORD

**Assistant:**
Flagged spec conflict up front: JPEG cannot hold transparency — "no background" requires PNG. Delivered both.

Build process (Canva MCP):
- generate-design (poster) → create-design-from-candidate → design DAHTDDzb1Gk
- resize-design to custom 3300x5100 px (11x17in @ 300 DPI) → new design **DAHTDEUXFAM** (note: only 1 resize use remained on the Canva Free plan)
- Deleted all 8 template elements from page 1; added page 2 (PBHdB18bJQ6mCLxs) white 3300x5100 titled "AI STEEL - Front Print"
- Computed a 45° staggered lattice in Python: font 190px, text run 834px, spacing s=929 along run, t=318 between lines, 320px bleed pad → **73 repeats**
- Added 73 add_text elements at rotation -45, then format_text (190px bold #000000), resize_element (width 900 — needed because add_text locked box width at 70.25px causing vertical letter wrap), position_element to lattice coords
- Committed transaction

Export problem: Canva Free plan blocks transparent-background PNG export. Plain PNG export URL could not be fetched from the container (curl 403 CONNECT tunnel) and no device_bash available on the user's machine.

Resolution: re-rendered the identical geometry locally with PIL using TeX Gyre Heros Bold (Helvetica clone, closest available to Canva Sans), supersampled 2x, 73 repeats, verified: 3300x5100, 300 DPI, 80% fully transparent pixels, corners alpha 0.

Delivered:
- AI-STEEL-tshirt-front-11x17-TRANSPARENT.png (real print file)
- AI-STEEL-tshirt-front-11x17.jpg (same artwork on white)
Both committed to C:\Users\Harleen\OneDrive\Documents\Eoxs Tasks\New folder

Canva master: https://www.canva.com/design/DAHTDEUXFAM (page 2 is the print; page 1 is a leftover blank)

Caveats given to user: delivered files use Helvetica Bold vs Canva Sans in the Canva doc; black-on-transparent assumes a light shirt, offered to flip to white for dark garments.
