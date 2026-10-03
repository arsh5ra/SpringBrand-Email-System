"""SpringBrand outreach templates, one per YC S2026 category.

Merge fields: {first_name}, {company}, {tagline}, {target} (category 4:
who the company sells to; category 5: the incumbents it competes with).
Rendered by render.py into docs, a PDF and a mail-merge CSV.

Voice: Arsham, Growth Marketing Manager. Warm, short, one ask per email.
"One bill" appears only where consolidating vendors is the actual pitch
(GTM builders, B2B SaaS, partners); elsewhere the price point is simply
"under a cent per call, no subscription".
"""

SENDER = "Arsham"

PRICE_LINE = "Most calls cost less than one cent, with no subscription."

SIGNATURE = "Best,\nArsham\nGrowth Marketing Manager, SpringBrand\nspringbrand.ai"

FOLLOW_UP_2 = """Hi {first_name},

Last note from me, promise. If growth tooling isn't a priority right now, I totally understand.

Your free starter credits aren't going anywhere, so they're there whenever {company} needs a lead list, a competitor scan or some fresh content. And if someone else on the team owns growth, I'd really appreciate a pointer.

Rooting for you this batch!"""

TEMPLATES = [
    {
        "key": "gtm",
        "category": "1. GTM & growth builders",
        "angle": "Your product runs on GTM data. Use SpringBrand for your own pipeline, or call it inside your product.",
        "subjects": ["the data behind {company}", "{company} + SpringBrand", "five data vendors, or one"],
        "email_1": """Hi {first_name},

Arsham here, growth marketing manager at SpringBrand. I came across {company} in the S26 batch ("{tagline}") and had to reach out.

Products like yours run on data: leads, traffic, social signals, content. We put all of it behind one connection your agents can call. A typical call costs less than a cent, with no subscriptions, no contract with each data vendor, and everything on one bill.

I'd love to set you up with free starter credits and build a quick sample around a workflow you care about. Worth a look?""",
        "follow_up_1": """Hi {first_name},

Here's what I had in mind for {company}: 50 companies that match your ideal customer, with decision-maker contacts and a first-touch draft, all from one request.

If it's more useful as a product feature, I can show you the same thing running through the API instead.

Just reply "yes" and I'll send it over.""",
    },
    {
        "key": "dev",
        "category": "2. AI agent infra & devtools",
        "angle": "Developer tools are won on X, Reddit and YouTube. Do your GTM research from inside the coding agent you already use.",
        "subjects": ["who's talking about {company}'s space", "GTM from inside Claude Code", "your competitors' traffic, in your terminal"],
        "email_1": """Hi {first_name},

This is Arsham from SpringBrand. Congrats on S26! "{tagline}" is a sharp pitch.

Devtools get won on X, Reddit and YouTube, and most technical founders don't have time to keep up. SpringBrand plugs GTM tools straight into the agent you already code in, so you can ask Claude Code or Cursor who's talking about your category, where competitors get their traffic, or which AI teams fit your ideal customer.

Most calls cost less than a cent, and there's no subscription.

Can I send you a free sample of this week's conversations in your space, plus a competitor traffic breakdown?""",
        "follow_up_1": """Hi {first_name},

Quick follow-up: setup is one line (npx add-mcp https://connector.springbrand.ai/mcp), then you just ask your agent something like "Show me this week's Reddit threads about [your category], and where [competitor] gets its traffic."

Happy to run it for {company} first and send you the results. Want me to?""",
    },
    {
        "key": "b2b",
        "category": "3. B2B / enterprise AI SaaS",
        "angle": "You need pipeline after Demo Day, without paying for Apollo, Semrush and Similarweb separately.",
        "subjects": ["50 target accounts for {company}", "pipeline after Demo Day", "{company}'s next customers"],
        "email_1": """Hi {first_name},

Arsham from SpringBrand here. I saw {company} in the S26 batch ("{tagline}"). Really cool.

After Demo Day, most teams I talk to need pipeline fast but aren't ready to pay for separate lead, SEO and traffic tools. SpringBrand gives your AI agent all of them: find companies and decision-makers that fit, push them into HubSpot or Salesforce, and follow up on deals that went quiet.

It's pay as you go, usually under a cent per call, with everything on one bill.

Tell me your ideal customer in one line and I'll send you a free sample list. Sound good?""",
        "follow_up_1": """Hi {first_name},

One more thought: early B2B deals usually die from silence, not a "no." SpringBrand can spot deals that haven't moved in two weeks and draft the follow-ups for you.

The free sample list is still yours. Just reply with your ideal customer and I'll get it started.""",
    },
    {
        "key": "smb",
        "category": "4. Vertical AI for SMBs & local operators",
        "angle": "Selling to small operators is a volume game. Build city-by-city lead lists and local content.",
        "subjects": ["{company}'s first city", "{company}'s next 500 leads", "a lead list of {target}"],
        "email_1": """Hi {first_name},

I'm Arsham, growth marketing manager at SpringBrand. {company} caught my eye in the S26 batch ("{tagline}").

Selling to {target} is a numbers game: long lists, local search and a lot of follow-up. Our AI tools do the heavy lifting. They build a list of {target} in any city with owner contacts, find the local keywords competitors rank for, and make short demo videos owners actually watch. Most calls cost less than a cent.

Pick a city and I'll send you a free list of {target} there, contacts included. Where should I start?""",
        "follow_up_1": """Hi {first_name},

One thing I forgot to mention: owners buy what they can see. SpringBrand can turn a product screenshot into a 15-second demo video with voiceover, ready for Facebook, Instagram or your next email.

The free lead list still stands. Just name a city.""",
    },
    {
        "key": "svc",
        "category": "5. AI-native service firms",
        "angle": "Incumbent firms own the search results. Show where they get their clients and which keywords you can take.",
        "subjects": ["where {target} get their clients", "keywords {company} can take", "{company} vs. {target}"],
        "email_1": """Hi {first_name},

Arsham from SpringBrand here. I saw {company} in the S26 batch ("{tagline}") and loved the idea.

Winning clients from {target} often comes down to search. They've owned the keywords your future clients type for years. SpringBrand shows you exactly where they get their traffic and which keywords you can realistically win. At less than a cent per call, it's cheap to find out.

Can I send you a free breakdown for three {target} in your market?""",
        "follow_up_1": """Hi {first_name},

As client volume grows, unanswered questions start piling up in the inbox and DMs. SpringBrand can find them, draft replies to the common ones, and summarize the week's complaints, alongside the search research.

The free breakdown of three {target} is still on the table. Just reply "send it".""",
    },
    {
        "key": "con",
        "category": "6. Consumer, health & creator apps",
        "angle": "Consumer growth runs on creators and short video. Find the creators, see the trends, make the content.",
        "subjects": ["20 creators for {company}", "{company} on TikTok", "UGC ideas for {company}"],
        "email_1": """Hi {first_name},

It's Arsham from SpringBrand. I just saw {company} in the S26 batch ("{tagline}") and loved it.

Consumer growth today runs on creators and short video, and both take a ton of time. SpringBrand's AI tools find creators with 20K–100K followers already talking about your space, spot what's trending, and turn a product shot into a 15-second ad. Most calls cost less than a cent, and there's no subscription.

Want me to send 20 creators who'd be a great fit for {company}, plus three ad ideas? Free, of course.""",
        "follow_up_1": """Hi {first_name},

One more idea: SpringBrand can also pull your best-performing posts from the last 30 days and turn this week's trends into ready-to-post content, so you always know what to make next.

The free creator list is still yours. Just say the word.""",
    },
    {
        "key": "deep",
        "category": "7. Deep tech, hardware, defense & bio",
        "angle": "You need GTM research in bursts. Pay for it only when you use it.",
        "subjects": ["buyer research for {company}", "a buyer list for {company}", "research you only need twice a year"],
        "email_1": """Hi {first_name},

This is Arsham, growth marketing manager at SpringBrand. I came across {company} in the S26 batch ("{tagline}"). Impressive work.

Deep-tech teams usually need GTM research in bursts: a buyer list before a pilot push, a competitor scan before a raise, a demo video for launch. Paying monthly for tools you use twice a quarter rarely makes sense. With SpringBrand you pay only when you use it, usually under a cent per call.

Tell me one type of buyer you're after and I'll put together a free list of organizations and contacts. Useful?""",
        "follow_up_1": """Hi {first_name},

Just to make it concrete: for {company}, I'd pull the procurement and R&D leads at 25 target organizations, plus a one-page competitor scan.

It's free to try. Want me to put it together?""",
    },
    {
        "key": "partner",
        "category": "★ Partner candidates (any category)",
        "angle": "Your product is a capability agents go looking for. List it on SpringBrand to get discovered by agent users at the moment they need it (listed tools are not paid per call).",
        "subjects": ["agents looking for {company}", "{company} on SpringBrand", "a new channel for {company}"],
        "email_1": """Hi {first_name},

Arsham from SpringBrand here. I saw {company} in the S26 batch and immediately thought of our marketplace.

SpringBrand is where AI agents find tools. People in Claude Code, Cursor and Codex describe what they need, and their agent picks the right tool for the job. Listing {company} puts it in front of those agents the moment one of them {agent_need}.

Worth a quick chat about listing {company}?""",
        "follow_up_1": """Hi {first_name},

Quick follow-up. Listing {company} is a new way to get discovered with no extra sales work: agents search by the outcome they need, so {company} shows up exactly when it's relevant.

Would 15 minutes this week work for a walkthrough? If you'd rather look first, I can send free credits so you can try SpringBrand as a user.""",
        "follow_up_2": """Hi {first_name},

Last note from me, promise. If a new distribution channel isn't a priority right now, I completely understand.

The offer to list {company} stays open, and so do your free credits. And if someone else on the team handles partnerships, I'd really appreciate a pointer.

Rooting for you this batch!""",
    },
]
