---
thread_name: "personal-app-idea"
user: "yashvir"
type: claude-chat
created: 2026-08-27
updated: 2026-08-27
---

User: i want all the indian food items in the database specially from the north India i want even a small item added in the database like himachli siddu, patrode and all

Assistant: [Researched available network-reachable sources for a bulk Indian nutrition database, since general web (USDA.gov, agdatacommons, Google Docs, jsr.io) was blocked by egress allowlist but npm registry and raw.githubusercontent.com were reachable.]

[Found and downloaded India's official government nutrition database — IFCT 2017 (Indian Food Composition Tables), published by ICMR-National Institute of Nutrition, Hyderabad — via its npm packages (@ifct2017/compositions, /codes, /descriptions, /columns, /groups). 542 raw/ingredient-level foods with verified energy (converted from kJ to kcal), protein, fat, and carbohydrate values per 100g.]

[Also found and inspected an npm package "indian-food-nutrition-mcp" which documented the landscape clearly via its DATA_SOURCES.md: IFCT 2017 (AGPL, redistributable) + USDA SR Legacy (public domain, redistributable) are usable; INDB (Indian Nutrient Databank, ~1,014 cooked Indian recipes from Jaacks Lab) has NO specified license and its own maintainers explicitly do NOT redistribute it for that reason. Followed the same conservative approach — did not scrape or embed INDB data.]

[Since no licensed bulk source exists for composite Indian dishes (curries, breads, chaat, regional specialties), hand-built a curated set of 139 North Indian and regional dishes with estimated macros based on standard recipe proportions — explicitly including Himachali Siddu and Himachali Patrode as requested, plus ~18 Himachali items total (Chana Madra, Rajma Madra, Dham, Kullu Trout Curry, Babru, Sepu Vadi, Chha Gosht, Bhey, Aktori, Chuk, etc.), Punjabi/North Indian curries, dals, breads, rice dishes, tandoor items, street food/chaat, sweets, and a smaller set of South Indian and other regional staples (Bihar, Gujarat, Maharashtra, Rajasthan, Kashmir). Tagged every one of these with "(Estimated)" in its category field to visually distinguish them from the lab-verified USDA/IFCT entries in search results.]

[Merged all three sources — USDA (8,789) + IFCT (542) + curated Indian dishes (139) = 9,470 total foods — into the app's embedded FOODS array. Updated search placeholder and empty-state text to reflect the new count and mixed provenance. Validated the merged JSON parses correctly (9,470 entries) and confirmed key terms resolve: siddu, patrode, rajma, butter chicken, dal makhani, biryani, samosa, gulab jamun all found. Ran a full Playwright functional test — searched "siddu", "patrode", "dal makhani", added an entry, confirmed it logged correctly and the calorie ring updated. No errors.]

[Republished the same artifact URL.]

Assistant: Done. Same link, now with 9,470 foods from three sources — worth understanding the difference between them since they're not equally reliable:

USDA SR28 (8,789 items) and IFCT 2017 (542 items, India's official government food composition database from ICMR-National Institute of Nutrition — this is the real deal for Indian ingredients: bajra, toor dal, methi, karela, Indian fish/dairy, etc.) are both lab-measured, authoritative data. I found IFCT as an npm package while looking for exactly this — it's the closest thing India has to USDA's database.

139 curated North Indian / Himachali dishes (including Himachali Siddu and Patrode, both confirmed searchable now) — this is different. There's no equivalent official database for cooked composite dishes like these. I looked for one (there's a research dataset called INDB with ~1,000 Indian recipes, but its authors haven't published a redistribution license, so I didn't copy it in — that would've been reusing data without clear rights, not something I'll do quietly). So this set is my own estimate based on standard recipe proportions, covering Himachali specialties, Punjabi curries, dals, breads, rice dishes, tandoor items, street food/chaat, sweets, and a handful of South Indian and other regional staples. In the app, these show "(Estimated)" in their category line so you can see at a glance which entries are lab-verified versus my best estimate.

If precision on a specific dish matters — say for a Siddu recipe your family makes a particular way — the estimate is a reasonable starting point, not a substitute for measuring or calculating it yourself. Tell me if anything specific is missing (more Himachali dishes, Kashmiri, Bengali, South Indian depth) and I'll add it the same way.
