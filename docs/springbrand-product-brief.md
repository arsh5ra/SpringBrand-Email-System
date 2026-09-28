# SpringBrand — Product Brief for Outreach Copy

Reference notes used when writing outreach email templates. Sources: public listings of springbrand.ai,
the official `springbrand-lab/springbrand-agent-setup` README, and the SpringBrand
MCP connector catalog.

## One-line positioning

**SpringBrand is the AI agent capability marketplace: one connection gives the AI
assistant you already use (Claude Code, Codex, Cursor, Copilot, Devin, Windsurf,
WorkBuddy, …) specialized go-to-market tools, and you pay only per call, with no
subscriptions.**

Short version: *"The GTM stack your AI agent can actually run. Pay per call, no subscriptions."*

## The problem we solve

Getting real GTM work done with an AI agent today means:
- finding the right tools (traffic, SEO, lead data, social listening, content gen),
- signing up for each one, often on a paid monthly plan,
- configuring API keys, and
- wiring the workflow together by hand.

Teams end up paying for a **stack of subscriptions** (Similarweb, Semrush, Apollo,
ElevenLabs, …) they use a few times a month, and their agent still can't use them.

## What SpringBrand does

Describe the outcome you want. Your agent picks and calls the right tools and
**delivers the result**, not just advice.

### Core value pillars (use these in emails)

| Pillar | What it means | Customer phrasing |
| --- | --- | --- |
| **One entry** | One connector and one OAuth login, no juggling accounts or API keys | "One login instead of ten tools" |
| **Pay per call / no subscription** | Unified credit billing across every tool. You pay only when a task runs | "Stop paying monthly for tools you open twice a month" |
| **Direct delivery** | The agent executes: pulls the data, builds the list, writes the copy | "Your AI does the work, not just the research" |
| **Recurring tasks** | Schedule monitoring, research and reporting to run on repeat | "Set it once and get the report every Monday" |
| **Works where you already work** | Plugs into the agents/IDEs the team already uses (MCP + OAuth 2.1) | "No new dashboard to learn" |

### Specialized GTM tools (capability map)

| Domain | Capabilities | Comparable standalone tools* |
| --- | --- | --- |
| Social listening & trends | Monitoring, trend tracking, content analysis, audience insight on X, TikTok, Instagram, YouTube, Reddit, Pinterest, Xiaohongshu (小红书), Douyin | Brandwatch-style listening |
| Traffic & SEO research | Website traffic, traffic sources, keyword research, top pages, SEO analysis, competitor research | Similarweb, Semrush, Ahrefs, DataForSEO |
| Web & search research | Search, crawling, research | Exa, Tavily, Perplexity, Firecrawl |
| Prospecting | Company and contact discovery against an ICP | Apollo, People Data Labs |
| Creator / KOL discovery | Find fitting KOL/KOC creators and draft collaboration and promotion plans | WaveInflu |
| Content generation | Copy, images, video, voiceover | GPT Image, Seedream, Seedance, Nano Banana, ElevenLabs |
| Connectors | GitHub, Google (Analytics, Search Console, Sheets), Microsoft Graph, and more | — |

\*Names only show what the capabilities cover. **Do not claim integrations or
partnerships with these vendors in outreach.** Say "capabilities similar to" or
"the kind of data you'd otherwise buy from X".

### Concrete example tasks (good email hooks)

- "Give it a competitor's URL and get back their traffic sources, acquisition pages and search keywords."
- "Monitor X, Reddit and TikTok for real conversations about your brand or your competitors."
- "Find companies and key contacts that match your ICP."
- "Find the right creators/KOLs and get a ready-to-run collaboration plan."
- "Turn one brief into copy, images, a short video and a voiceover."

## Who to target (ICP hypotheses)

1. **Startup founders / small GTM teams** who can't justify $100–$500/mo per tool.
2. **Growth & performance marketers** who need SEO/traffic and social data occasionally, not daily.
3. **Agencies** running research and content for many clients, where per-call billing maps to per-client costs.
4. **Sales / SDR / RevOps teams** doing ICP prospecting and account research.
5. **DTC & e-commerce brands** doing influencer (KOL/KOC) marketing and social trend tracking, including cross-border brands targeting TikTok and Xiaohongshu.
6. **Technical teams already using AI coding agents** (Claude Code, Cursor, Codex) that want GTM capability inside the same agent.

## Messaging guardrails

- Lead with the **outcome** ("competitor traffic breakdown in minutes"), not the plumbing (MCP, OAuth).
- Always make the **no subscription / pay per call** point. It's the main differentiator and lowers the risk of saying yes.
- Mention "works with the AI assistant you already use" to remove switching friction.
- Don't invent specific prices, credit amounts, customer names or stats. Use placeholders until they're confirmed.
- Keep a single, low-friction CTA (e.g., "Want me to run one competitor report for you on us?" or a 15-min call).

## Key links

- Website: https://springbrand.ai
- One-prompt install: https://plugin.springbrand.ai/INSTALL.md
- MCP endpoint: `https://connector.springbrand.ai/mcp` (`npx add-mcp 'https://connector.springbrand.ai/mcp'`)
