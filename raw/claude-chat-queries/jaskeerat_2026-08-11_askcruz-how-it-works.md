---
thread_name: "askcruz-how-it-works"
user: "jaskeerat"
type: claude-chat
created: 2026-08-11
updated: 2026-08-11
---

# Ask Cruz / Cruise: How It Works

## User Question
How does Ask Cruz work?

## Key Technical Architecture

Based on Rajat Jain's demo to Joe Brom (Ohio Strip Steel) on Aug 10, 2026:

### **The Core Concept: "Company Brain"**

Cruz/Cruise works by injecting a **"company brain" layer** between the user and an LLM (Large Language Model like Claude, GPT, or Grok):

```
[User Query] → [Cruise Frontend] → [Company Brain] → [Claude/GPT/Grok LLM] → [Response]
```

The **company brain** is a centralized, summarized database containing:

1. **All company emails** (from the past 5, 10, 15, 20+ years)
2. **CRM data** (customer relationships, interactions, history)
3. **ERP data** (business operations, inventory, orders, financials)
4. **Call recordings** (Fireflies or similar transcripts)
5. **Team meetings** (recorded and transcribed)
6. **SOPs** (standard operating procedures)
7. **Any digital business data available**

### **How the Processing Works**

#### Step 1: Data Injection and Summarization
- All messy, raw data is ingested into a database
- Data is **summarized** into a smaller, more efficient database
- This solves the context-window problem: Claude API struggles with huge token counts when resending full conversation histories on every prompt

#### Step 2: Query with "Depth Levels"
Users can ask questions at three **"rigor levels"**:

- **5-foot depth**: Quick, fast path using most direct data sources. Aggregates and summary fields are fine. Good for first-pass answers when speed > certainty.
- **10-foot depth**: Mid-level analysis with more cross-referencing
- **50-foot depth**: Deep, comprehensive analysis. AI dives through emails, all Fireflies calls, related documents, and creates full contextual summaries. Takes ~60 seconds for a complex relationship query.

#### Step 3: Contextual Intelligence
Unlike generic ChatGPT (which lacks business context), Cruz:
- **Asks clarifying questions** if it doesn't have full context
- **Doesn't do surface-level research** — it digs deeper automatically
- **Validates answers** using actual company data
- **Connects information across silos** (e.g., linking an inquiry to a quote to a sales order to actual costs)

### **Example: "Tell me my relationship with Joe Brom"**

When Raj asked this in the demo:
1. Cruz searched through ~22 records of emails with Joe
2. Connected Ron's emails, support emails, and ERP data
3. Returned a complete relationship summary in **60 seconds** with full historical context
4. Could then do a 50-foot deep dive on that relationship if requested

---

## **Cruise vs. Standard Claude/GPT**

| Aspect | ChatGPT/Claude Direct | Cruise |
|--------|----------------------|--------|
| **Context** | No company data; generic knowledge only | Full company brain: emails, ERP, CRM, calls |
| **Data Silos** | Each user has own account; no visibility | Admin can see what all users are asking |
| **Cost** | $20-50/month per user | TBD (being quoted; Raj said "not crazy") |
| **Infrastructure** | Cloud (OpenAI/Anthropic) | EOXS-hosted custom front end |
| **Governance** | None; totally public | Role-based access control (VP sees more than salesperson) |
| **Automation** | Manual prompting only | AI agents can auto-send emails, dashboards, alerts |
| **Admin Controls** | None | Full monitoring; can see team's AI usage patterns |

---

## **Automation Layer: AI Agents**

Cruise can deploy **automated AI agents** to:

- **Sales nudges**: E.g., "Check which salespeople haven't responded to open inquiries in 3+ days. Send them a reminder email at 7pm daily."
- **Dashboard updates**: Auto-generate performance summaries
- **Quality checks**: Compare inquiries to quotes to purchase orders for errors
- **Escalation**: Alert managers when metrics fall below thresholds

---

## **Deployment Model**

Cruise can launch **independently of a full ERP upgrade**:
- Start with core team (e.g., 6-7 salespeople)
- Plug in their emails + CRM data
- Run Cruise for value **before** full ERP implementation
- Deploy full ERP later; add more AI agents after adoption

### **Timeline to Deployment**
- **2 weeks** to get a core sales team (6-7 people) live on Cruise if data is ready
- **4 months** for full ERP implementation
- **2-4 months** adoption/cooling-off period after ERP launch
- **2 months** for AI transformation training
- **Total realistic journey: 12 months** (but can pilot Cruise much faster)

---

## **Privacy & Access Control**

- **Role-based access**: VPs see more data than salespeople
- **Thread-level privacy**: Individual team members can hide threads from others (with proper permissions)
- **Admin monitoring**: Leadership can ask "What is my team talking about?" and get high-level summaries
- **Designed for transparency without micromanagement**: Metrics are visible to employees so they can self-regulate

---

## **Real-World Early Adoption**

- **3GM Steel (VP of Sales)**: Went from 8 hours of analysis per task → 30 seconds. Called it "my new best friend." One week in, extremely high engagement.
- **Another CEO**: Spending hours on Cruise daily because it's connected to full ERP. Doesn't talk to team anymore; goes straight to Cruise for decisions.

---

## **Key Insights from Raj's Philosophy**

> "Business is all about capital, product, and decision-making. Right now we make decisions on gut feeling because we lack context. AI without your company's data is useless."

Cruise solves this by:
1. **Centralizing messy data** into one searchable brain
2. **Adding company context** that generic AI lacks
3. **Enabling decisions on accurate data** instead of gut feeling
4. **Training AI as an employee** (e.g., "do a 50-foot deep analysis before answering strategic questions")

---

## **Pricing Model**

Not finalized, but Raj indicated:
- Per-user licensing
- Standalone Cruise (without ERP): lower cost
- Bundled with full ERP: different pricing
- "It's not going to be crazy" (implying competitive with ChatGPT Plus/Enterprise)

---

## **Current Status (Aug 2026)**

- **Live at EOXS** (internal use since ~2 months before call)
- **Demoing to customers** (Ohio Strip Steel, Sabre Alloys)
- **Being evaluated as separate product** from ERP consulting (spun out as "Cruise," distinct from EOXS)
- **Cost evaluation underway**: Internal debate between Claude API vs. open-source UI to reduce token costs
- **Target timeline**: Cruise available as standalone product within 2 weeks for pilot customers
