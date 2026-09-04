---
thread_name: "askcruz_ux_learning_architecture_50ft_sept3"
user: "ai_interns1"
type: claude-chat
created: 2026-09-03
updated: 2026-09-03
---

AskCruz UX Learning Architecture — 50ft Deep Analysis (Sept 3, 2026)

CONTEXT:
- User type: Sales reps at steel distributors (Sabre Alloys primary pilot)
- Cognitive profile: Email + CRM literate, low AI experience, 30-90 sec attention window per task
- Current friction: 120+ RFQs/day, manual scoring/quoting kills time, slow response loses deals

CORE INSIGHT:
Cognitive load is the adoption killer. Rep thinks "Claude is slower than my manual process" if UX adds steps. Solution: Reduce extraneous load (UI friction) + maximize germane load (learning value).

LEARNING SCIENCE FRAMEWORK:
1. Spacing & retrieval: 14-day spaced onboarding, not 1-day training
2. Cognitive load theory: Show 1 feature/day, minimize options, 1-line explanations
3. Transfer learning: Teach principles ("close odds tied to material + timing"), not procedures

SIX CORE UX FEATURES (with implementation specs):

1. SMART ONBOARDING SEQUENCE (Spaced over 14 days)
   - Day 1: 2-min welcome video + templated "Score this RFQ?" prompt on first incoming RFQ
   - Days 3, 5, 7, 10, 14: Micro-lessons triggered by rep's actual tasks (not calendar)
   - Measurement: Time to first use <2 min, 80%+ feature discovery by day 14
   - Why: Spaced retrieval builds memory; task-triggered learning reduces cognitive load

2. CONTEXTUAL HELP (One-line reasons + progressive disclosure)
   - Layer 1 (visible): "65% close odds. Why: Matched to 12 similar deals (8 closed, 4 lost)."
   - Layer 2 (optional [Why?] button): Full math showing how odds were calculated
   - Personalization: Rep can disagree + train Claude ("I close 70% on this customer")
   - Measurement: 40-50% engage with [Why?] in week 1, drops to 15-25% by week 4 (sign of confidence)
   - Why: Builds trust by showing logic; validates expert rep; transfers principle of how Claude thinks

3. TEMPLATED PROMPTS (Remove blank-page paralysis)
   - Instead of "Ask Claude anything," grid of 6 templated prompts (role-specific)
   - Sales rep sees: "Score RFQ," "Cost lookup," "Why did we lose," "Price suggestion," "Contact," "Material template"
   - Auto-fills 80% of prompt; rep fills 1-2 blanks
   - Measurement: 70%+ of new user actions from templates (week 1-2), drops to 50% by week 4 (exploration)
   - Why: Reduces cognitive load (rep doesn't have to think of the question), anchors in workflow

4. FIRST-VALUE MICRO-DEMOS (Experience > instruction)
   - First 3 RFQs trigger 1-min demos: "Watch Claude score this" / "Try auto-pricing" / "Use template"
   - Rep sees real output, feels time saved (8 sec scoring, 2 min pricing, 5 min templating)
   - By mid-day Day 1, rep has felt 3 moments of value
   - Measurement: 70%+ engage with ≥2 demos, 60%+ adopt feature again in week 2
   - Why: Removes doubt ("Does Claude actually work?"). Experience builds intrinsic motivation

5. GUIDED FAILURE RECOVERY (When Claude gets it wrong)
   - Rep marks Claude output wrong or edits it
   - System asks: "Freight/tax? Contract rate? Mistake? Other?"
   - Rep selects [Contract rate] → system learns, next quote uses updated rate
   - Pattern detection: if 3+ reps mark same error, escalate to data/content team
   - Measurement: 30%+ error feedback rate, 70%+ adoption of correction, <7 days resolution time
   - Why: Converts errors into learning; rebuilds trust; teaches rep that Claude is improving

6. PROGRESS VISIBILITY & MASTERY SIGNALS (Intrinsic motivation)
   - Weekly digest: "47 RFQs scored (you'd normally spend 8 hours), saved ~1.2 hours, 1 custom template"
   - Badges: RFQ Master (100+), Precision Quoter (0 errors in 50), Template Creator (3+)
   - Manager dashboard: peer comparison (Rachel 80% active, Mike 60%, Keanu 40%)
   - Measurement: 15-25% engagement lift after earning badge, 75% retention if badge vs 50% if none
   - Why: Intrinsic motivation (progress visible), social proof (peer comparison), durable engagement

INTEGRATION WITH SABRE DEAL (Sept 15 - Dec 31):
- Week 1 (Sept 15-21): 5-min POC demo → pilot decision (goal: Dave + Michael agree Claude saves time)
- Weeks 2-4 (Sept 22 - Oct 12): 5 reps embedded pilot, spaced learning + real RFQs + error recovery
  * Target: 60% DAU week 2 → 75% DAU week 3 → 85% DAU week 4
  * Time saved: 45 hours week 2 → 80 hours week 3 → 120 hours week 4
  * Error rate: 15% week 1 → 8% week 2 → 3% week 4
  * Feature adoption: scoring (100%), pricing (60%), templates (40%), lost-deal analysis (20%)
- Weeks 5-6 (Oct 13-26): Michael negotiates contract (positioning: $4,200/month time savings vs $2,500/month cost)
- Weeks 7+ (Oct 27 - Nov 26): Scale to 25-30 reps in cohorts of 5, peer mentoring, badge social proof
- Nov 27 - Dec 31: Production scale (1,200+ RFQs/month, $4,200+ ROI/month, close rate +3-5%)

MEASUREMENT FRAMEWORK (Weekly dashboard):
1. Adoption: DAU %, feature breadth (# features used per rep)
   - Target: Week 1: 40% DAU / 1 feature, Week 4: 85% DAU / 3-4 features
2. Proficiency: Time to action (Claude output → rep's next step), error rate, customization
   - Target: Week 1: 60 sec to action / 15% error, Week 4: 15 sec to action / 3% error
3. Impact: Time saved per task, close rate lift
   - Target: Week 4: 120+ hours saved/month, close rate +2-5% on Claude-scored deals

COGNITIVE OVERLOAD PREVENTION CHECKLIST:
Before shipping any new feature to Sabre:
- Intrinsic load: Does feature reduce task complexity? ROI >2x?
- Extraneous load: Can rep discover it without training? 1-line explanation? <2 options?
- Germane load: Does first use feel valuable? Can skill transfer to new scenarios?

REPEATABLE FOR NEXT CUSTOMERS:
- Onboarding sequence (14-day spaced) is portable
- Feature set (scoring, pricing, templates, lost-deal, alerts) is industry-agnostic
- Metrics are portable (DAU, feature breadth, time saved, close rate lift)
- Only customization is domain knowledge (Sabre's materials/margins → next industry's equivalent)
