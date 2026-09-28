"""SpringBrand outreach templates, one per YC S2026 category.

Merge fields: {first_name}, {company}, {tagline}, {target} (category 4:
who the company sells to; category 5: the incumbents it competes with),
{sender_name}. Rendered by render.py into docs, a PDF and a mail-merge CSV.
"""

PRICE_LINE = "A typical call costs less than one cent. No subscription, and everything is on one bill."

SIGNATURE = "{sender_name}\nMarketing Director, SpringBrand\nspringbrand.ai"

FOLLOW_UP_2 = """Hi {first_name},

Last note from me. If GTM tooling isn't a priority right now, no problem at all.

Your free starter credits don't expire, so they're there whenever {company} needs a lead list, a competitor scan or a batch of content. And if someone else on the team owns growth, I'd be grateful for a pointer.

Rooting for you this batch."""

TEMPLATES = [
    {
        "key": "gtm",
        "category": "1. GTM & growth builders",
        "angle": "Your product runs on GTM data. Use SpringBrand for your own pipeline, or call it inside your product.",
        "subjects": ["the data layer behind {company}", "{company} + SpringBrand", "five data contracts, or one"],
        "email_1": """Hi {first_name},

Saw {company} on the S26 list: "{tagline}." Products like yours run on data: leads, traffic, social signals and content.

SpringBrand puts those GTM tools behind one connection your agents can call: company and contact discovery, traffic and SEO research, social listening, and copy, image and video generation. {price}

Two ways it could help: run {company}'s own pipeline with it, or power features inside your product without signing a contract with each data vendor.

I'd be happy to load free starter credits and build a sample around one workflow you care about. Worth a look?""",
        "follow_up_1": """Hi {first_name},

To make it concrete, here's the sample I'd build for {company}: 50 companies that match your ideal customer, with decision-maker contacts and a first-touch draft, all from one request to your agent.

If you'd rather test it as a product feature, I can show the same call running through the API instead.

Reply "yes" and I'll send it over, with free credits to keep going.""",
    },
    {
        "key": "dev",
        "category": "2. AI agent infra & devtools",
        "angle": "Developer tools are won on X, Reddit and YouTube. Do your GTM research from inside the coding agent you already use.",
        "subjects": ["who's talking about {company}'s space", "GTM from inside Claude Code", "{company}'s competitors' traffic"],
        "email_1": """Hi {first_name},

Congrats on S26. "{tagline}" is a sharp pitch.

Devtools are won on X, Reddit and YouTube, and most technical founders don't have time to track it. SpringBrand plugs GTM tools into the agent you already code in (Claude Code, Cursor, Codex):

- see who's discussing your category and competitors on X and Reddit
- find where rival tools get their traffic and which keywords your docs miss
- find AI teams that match your ideal customer

{price}

I'd like to send you a free sample: this week's conversations about your category plus a competitor traffic breakdown, with starter credits to keep going. Want it?""",
        "follow_up_1": """Hi {first_name},

Quick follow-up. Setup is one command (npx add-mcp 'https://connector.springbrand.ai/mcp') or one prompt in Claude Code, then you just ask:

"Show me the Reddit and X threads about [your category] this week, and where [competitor] gets its traffic."

Happy to run that for {company} first and send you the output, free. Want me to?""",
    },
    {
        "key": "b2b",
        "category": "3. B2B / enterprise AI SaaS",
        "angle": "You need pipeline after Demo Day, without paying for Apollo, Semrush and Similarweb separately.",
        "subjects": ["50 target accounts for {company}", "pipeline after Demo Day", "{company}'s ideal customers, in your CRM"],
        "email_1": """Hi {first_name},

Saw {company} on the S26 list: "{tagline}." After Demo Day, most teams need pipeline fast but can't yet justify a separate subscription for lead data, SEO and traffic tools.

SpringBrand gives your AI agent all of them in one place: find companies and decision-makers that fit your ideal customer, push them into HubSpot or Salesforce, draft follow-ups for stalled deals, and see which keywords competitors win on. {price}

Free offer: describe your ideal customer in one line and I'll send back a sample list of matching accounts and contacts, plus starter credits. Interested?""",
        "follow_up_1": """Hi {first_name},

One more idea for {company}: most early B2B teams lose deals to silence, not to "no."

SpringBrand can find deals that haven't moved in two weeks and draft the follow-ups, alongside the prospect lists. It's all from the agent you already use, at under a cent per typical call.

Still happy to build your sample account list for free. Just reply with your ideal customer.""",
    },
    {
        "key": "smb",
        "category": "4. Vertical AI for SMBs & local operators",
        "angle": "Selling to small operators is a volume game. Build city-by-city lead lists and local content.",
        "subjects": ["{company}'s first city", "{company}'s next 500 leads", "a lead list of {target}"],
        "email_1": """Hi {first_name},

Saw {company} on the S26 list: "{tagline}." Selling to {target} is a volume game: long lists, local search, and follow-up that never stops.

SpringBrand gives your AI agent the tools for it: build a list of {target} in any city with owner contacts, add them to your CRM, find the local keywords competitors rank for, and make short demo videos operators actually watch. {price}

Free sample: pick a city and I'll send back a list of {target} with contacts and a first outreach draft, plus starter credits. Which city should I start with?""",
        "follow_up_1": """Hi {first_name},

One thing I didn't mention: operators buy what they can see. SpringBrand can turn a product screenshot into a 15-second demo video with voiceover, ready for Facebook, Instagram or a cold email.

The offer stands: name a city and I'll build a free list of {target} there with contacts. You'll also get starter credits to run the next hundred yourself.""",
    },
    {
        "key": "svc",
        "category": "5. AI-native service firms",
        "angle": "Incumbent firms own the search results. Show where they get their clients and which keywords you can take.",
        "subjects": ["where {target} get their clients", "keywords {company} can take", "{company} vs. {target}"],
        "email_1": """Hi {first_name},

Saw {company} on the S26 list: "{tagline}." Taking clients from {target} usually comes down to search: they've spent years owning the keywords your future clients type.

SpringBrand lets your AI agent see that directly: where incumbents get their traffic, which keywords you can win, and cost per lead on Google vs. Meta. It can also build lead lists and explainer videos when you need them. {price}

Free sample: I'll pull the top keywords and traffic sources for three {target} in your market and send them over with starter credits. Want them?""",
        "follow_up_1": """Hi {first_name},

As client volume grows, one more thing becomes a problem for service firms: questions sitting unanswered in the inbox and DMs.

SpringBrand can find those questions, draft replies to the common ones and summarize the week's complaints, on top of the search research. It's all under one bill at less than a cent per typical call.

The free keyword breakdown of three {target} is still yours. Just reply 'send it'.""",
    },
    {
        "key": "con",
        "category": "6. Consumer, health & creator apps",
        "angle": "Consumer growth runs on creators and short video. Find the creators, see the trends, make the content.",
        "subjects": ["20 creators for {company}", "{company} on TikTok", "UGC concepts for {company}"],
        "email_1": """Hi {first_name},

Saw {company} on the S26 list: "{tagline}." Love it.

Consumer growth right now runs on creators and short video, and both eat time. SpringBrand gives your AI agent the tools: find creators with 20K–100K followers already talking about your category (TikTok, Instagram, YouTube, RedNote), see what's trending, and turn a product shot into a 15-second video ad or five UGC concepts. {price}

Free sample: I'll send 20 creators who fit {company} plus three ad concepts, with starter credits to make more. Want them?""",
        "follow_up_1": """Hi {first_name},

Quick add: SpringBrand can also show your best-performing posts from the last 30 days and turn this week's trends into ready-to-post content, so you always know what to make next.

The free creator list and ad concepts for {company} are still on offer. Reply "yes" and they're yours.""",
    },
    {
        "key": "deep",
        "category": "7. Deep tech, hardware, defense & bio",
        "angle": "You need GTM research in bursts. Pay for it only when you use it.",
        "subjects": ["buyer research for {company}, no subscription", "a buyer list for {company}", "the research you'd need twice a year"],
        "email_1": """Hi {first_name},

Saw {company} on the S26 list: "{tagline}." Deep-tech teams usually need GTM research in bursts: a buyer list before a pilot push, a competitor scan before a raise, a demo video for launch. Paying monthly for tools you use twice a quarter rarely makes sense.

SpringBrand gives your AI agent those tools on demand: find the right buyer organizations and decision-makers, research competitors, and produce demo videos with voiceover. {price}

Free sample: name one target buyer type and I'll send back a list of organizations and contacts, plus starter credits. Useful?""",
        "follow_up_1": """Hi {first_name},

Following up with one concrete example: for a team like {company}, the sample would be the procurement and R&D leads at 25 target organizations, plus a one-page competitor scan.

It's free to try, and after that you only pay per call (typically under a cent). Want me to put it together?""",
    },
    {
        "key": "partner",
        "category": "★ Partner candidates (any category)",
        "angle": "Your product is a capability agents go looking for. Use SpringBrand for your launch, and talk about listing on it.",
        "subjects": ["agents looking for {company}", "{company} on the SpringBrand marketplace", "distribution for {company}"],
        "email_1": """Hi {first_name},

Saw {company} on the S26 list: "{tagline}."

SpringBrand is a capability marketplace for AI agents. People in Claude Code, Cursor, Codex and others describe an outcome, and their agent finds and calls the right tool, paying per call on one bill. {company} looks like exactly the kind of capability those agents go looking for.

Two things I'd love to explore:
1. Using SpringBrand's GTM tools for your own launch. Free starter credits are included, and a typical call costs less than one cent with no subscription.
2. Listing {company} so agents can discover it and pay for it per call.

Open to a quick chat about either?""",
        "follow_up_1": """Hi {first_name},

Following up on the partnership idea. Agents on SpringBrand search the catalog by outcome, so a well-described {company} listing gets found at the exact moment someone needs it, with billing handled for you.

Happy to walk you through it in 15 minutes, or send starter credits so you can see it from the user side first. Which would you prefer?""",
    },
]
