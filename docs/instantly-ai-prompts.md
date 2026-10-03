# Instantly AI prompts

Paste one prompt per campaign into Instantly's AI assistant, inside that campaign. Each prompt is self-contained. None of them launch anything.

## 01-gtm-growth-builders (1. GTM & growth builders, 8 leads)

````
You are helping me get my Instantly campaign "01-gtm-growth-builders" ready to launch. Do not launch or schedule it; stop when everything is ready and give me a short report of what you changed and anything you couldn't do.

## 1. Sequence
Replace the campaign's sequence with exactly these 3 steps. Keep the wording, line breaks and {{variables}} exactly as written. Use plain text, no images or links in step 1.

Step 1 (day 0). Subject variant A: the data behind {{companyName}} | Subject variant B: {{companyName}} + SpringBrand
Body:
```
Hi {{firstName}},

Arsham from SpringBrand here. I came across {{companyName}} in the S26 batch ("{{tagline}}") and had to reach out.

Products like {{companyName}} run on data, and for you that means {{data_need}}. SpringBrand puts lead, traffic, social and content tools behind one connection your agents can call, at under a cent per typical call, with no subscription and no contract with each data vendor.

Want free starter credits to test it inside one of {{companyName}}'s workflows?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 2 (wait 3 days). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Here's what I had in mind for {{companyName}}: 50 companies that match your ideal customer, with decision-maker contacts and a first-touch draft, all from one request. If you'd rather test it as a data source inside your product, the same request runs through our MCP connector.

Just reply "yes" and I'll send it over.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 3 (wait 4 days after step 2). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Last note from me, promise. If adding a new data source isn't a priority right now, I completely understand.

Your free starter credits stay open whenever {{companyName}} needs {{data_need}}, and so does the sample run. And if someone else on the team owns data or growth, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 2. Variables
The sequence uses these variables: {{firstName}}, {{companyName}}, {{tagline}}, {{data_need}}. firstName and companyName are built-in lead fields. The others are custom variables on each lead.

The custom variable `data_need` is new, so my leads may not have it yet. Set `data_need` on each lead to the value below, matching by company name:

- Chromie: contractor and company data
- Grocalo: creator and trend data
- LemonLime: lead and competitor data
- Nex: company and contact data
- Osmaura: search and traffic data on law firms
- Palisade: buyer and seller lead data
- TryNearby: local creator data
- Pluto: professional and company data

If you cannot set custom variables on leads, replace every {{data_need}} in the subjects and bodies with "fresh lead, traffic and social data" instead, so no email has a blank.

Check every lead: if any variable used above is empty for a lead, tell me which leads and which variable. Do not send to leads with an empty tagline or target; list them for me instead.

## 3. Settings
- Open tracking: off. Link tracking: off.
- Stop the sequence for a lead when they reply: on.
- Sending days: Monday to Friday. Sending window: 8:00 to 11:00 in the lead's time zone if supported, otherwise 8:00 to 11:00 US Pacific.
- Daily limit: no more than 30 new leads per sending inbox per day.
- Text only (no HTML formatting, images or unsubscribe banners added to the body).

## 4. Final check
Preview the full sequence (all 3 steps and both subject variants) for three different leads. Confirm there are no blanks, no leftover {{...}}, and no doubled spaces. Then report back.
````

## 02-ai-infra-devtools (2. AI agent infra & devtools, 45 leads)

````
You are helping me get my Instantly campaign "02-ai-infra-devtools" ready to launch. Do not launch or schedule it; stop when everything is ready and give me a short report of what you changed and anything you couldn't do.

## 1. Sequence
Replace the campaign's sequence with exactly these 3 steps. Keep the wording, line breaks and {{variables}} exactly as written. Use plain text, no images or links in step 1.

Step 1 (day 0). Subject variant A: who's talking about {{dev_topic}} | Subject variant B: GTM from inside Claude Code
Body:
```
Hi {{firstName}},

This is Arsham from SpringBrand. Congrats on S26!

Devtools get won on X, Reddit and YouTube, and most technical founders don't have time to keep up. SpringBrand plugs GTM tools straight into the agent you already code in, so you can ask Claude Code or Cursor who's talking about {{dev_topic}}, where competitors get their traffic, or which AI teams fit your ideal customer. Most calls cost under a cent, with no subscription.

Can I send you a free snapshot of this week's conversations about {{dev_topic}}, plus a competitor traffic breakdown for {{companyName}}?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 2 (wait 3 days). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Quick follow-up: setup is one line (npx add-mcp https://connector.springbrand.ai/mcp), then you just ask your agent something like "Show me this week's Reddit threads about {{dev_topic}} and where our top competitor gets its traffic."

Happy to run it for {{companyName}} first and send you the results. Want me to?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 3 (wait 4 days after step 2). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Last note from me, promise. If marketing isn't on your plate right now, I completely understand.

The free snapshot of conversations about {{dev_topic}} stays on offer whenever {{companyName}} gears up for its next launch, along with starter credits to run your own. And if someone else on the team owns growth, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 2. Variables
The sequence uses these variables: {{firstName}}, {{companyName}}, {{dev_topic}}. firstName and companyName are built-in lead fields. The others are custom variables on each lead.

The custom variable `dev_topic` is new, so my leads may not have it yet. Set `dev_topic` on each lead to the value below, matching by company name:

- Agent FM: running multiple coding agents
- Agnost AI: AI agent analytics
- Archal: agent evals
- Buildbox: AI agent user experience
- Bullet: coding agents
- Conifer: LLM token costs
- Dialogus: voice agents
- Experiential Labs: fine-tuning your own models
- GitCafe: Git hosting for AI-written code
- Glen: agent memory
- Hoplite: autonomous software factories
- HyperProbe: AI debugging in production
- Indexable: agent sandboxes
- Jcode: parallel coding agents
- machine0: cloud computers for agents
- Mentlio: AI coding spend
- OneCLI: agent identity and auth
- Prized: internal tool builders
- screenpipe: screen-aware AI
- Supapool: parallel coding agents
- Tibero: agent optimization
- Understudy Labs: moving to open-weight models
- Vendo: letting users extend your product
- Akon Labs: AI agent infrastructure
- Amulet: agent file systems
- Belvedir: private AI models
- Caution: secure hosting
- Coasty: computer-use agent evals
- Codag: agent logging
- Computable: GPU compute pricing
- Datoric: secure training data
- Fabraix: AI agent security
- hiloop: recursive self-improvement
- Inner: supply chain attacks
- Lamb Labs: fast AI inference
- Markov: computer-use training data
- Mireye: physical-world AI agents
- Nebula Security: AI-powered security
- Ooak Data: RL environments
- OpenRelay: distributed AI inference
- Osseus: robotics development
- Paraloft: autonomous AI agents
- SpaceFlow Technologies, Inc.: running AI agents in production
- Traceforce: on-device AI security
- Tracer: combining open-source models

If you cannot set custom variables on leads, replace every {{dev_topic}} in the subjects and bodies with "your space" instead, so no email has a blank.

Check every lead: if any variable used above is empty for a lead, tell me which leads and which variable. Do not send to leads with an empty tagline or target; list them for me instead.

## 3. Settings
- Open tracking: off. Link tracking: off.
- Stop the sequence for a lead when they reply: on.
- Sending days: Monday to Friday. Sending window: 8:00 to 11:00 in the lead's time zone if supported, otherwise 8:00 to 11:00 US Pacific.
- Daily limit: no more than 30 new leads per sending inbox per day.
- Text only (no HTML formatting, images or unsubscribe banners added to the body).

## 4. Final check
Preview the full sequence (all 3 steps and both subject variants) for three different leads. Confirm there are no blanks, no leftover {{...}}, and no doubled spaces. Then report back.
````

## 03-b2b-enterprise-saas (3. B2B / enterprise AI SaaS, 57 leads)

````
You are helping me get my Instantly campaign "03-b2b-enterprise-saas" ready to launch. Do not launch or schedule it; stop when everything is ready and give me a short report of what you changed and anything you couldn't do.

## 1. Sequence
Replace the campaign's sequence with exactly these 3 steps. Keep the wording, line breaks and {{variables}} exactly as written. Use plain text, no images or links in step 1.

Step 1 (day 0). Subject variant A: 25 target accounts for {{companyName}} | Subject variant B: pipeline after Demo Day
Body:
```
Hi {{firstName}},

Arsham from SpringBrand here. I saw {{companyName}} in the S26 batch ("{{tagline}}").

After Demo Day, most teams I talk to need pipeline fast but aren't ready to pay for separate lead, SEO and traffic tools. SpringBrand gives your AI agent all of them: find companies and decision-makers that fit, push them into HubSpot or Salesforce, and follow up on deals that went quiet. It's pay as you go, usually under a cent per call, all on one bill.

Reply with your ideal customer in one line and I'll send you a free list of 25 matching companies. Sound good?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 2 (wait 3 days). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

To make it easy: one line is enough, for example "Series A fintechs in New York, Head of Finance". You'd get 25 matching companies, each with the right decision-maker, ready to drop into your CRM.

Want me to start one for {{companyName}}?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 3 (wait 4 days after step 2). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Last note from me, promise. If pipeline isn't the bottleneck right now, I completely understand.

The free list of 25 companies stays on offer whenever {{companyName}} is ready to scale outbound, along with starter credits to build more. And if someone else on the team owns sales, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 2. Variables
The sequence uses these variables: {{firstName}}, {{companyName}}, {{tagline}}. firstName and companyName are built-in lead fields. The others are custom variables on each lead.

Check every lead: if any variable used above is empty for a lead, tell me which leads and which variable. Do not send to leads with an empty tagline or target; list them for me instead.

## 3. Settings
- Open tracking: off. Link tracking: off.
- Stop the sequence for a lead when they reply: on.
- Sending days: Monday to Friday. Sending window: 8:00 to 11:00 in the lead's time zone if supported, otherwise 8:00 to 11:00 US Pacific.
- Daily limit: no more than 30 new leads per sending inbox per day.
- Text only (no HTML formatting, images or unsubscribe banners added to the body).

## 4. Final check
Preview the full sequence (all 3 steps and both subject variants) for three different leads. Confirm there are no blanks, no leftover {{...}}, and no doubled spaces. Then report back.
````

## 04-vertical-ai-smb (4. Vertical AI for SMBs & local operators, 21 leads)

````
You are helping me get my Instantly campaign "04-vertical-ai-smb" ready to launch. Do not launch or schedule it; stop when everything is ready and give me a short report of what you changed and anything you couldn't do.

## 1. Sequence
Replace the campaign's sequence with exactly these 3 steps. Keep the wording, line breaks and {{variables}} exactly as written. Use plain text, no images or links in step 1.

Step 1 (day 0). Subject variant A: {{target}} in {{start_city}} | Subject variant B: {{companyName}}'s next 500 leads
Body:
```
Hi {{firstName}},

I'm Arsham from SpringBrand. {{companyName}} caught my eye in the S26 batch ("{{tagline}}").

Selling to {{target}} is a numbers game: long lists, local search and a lot of follow-up. Our AI tools do the heavy lifting. They build a list of {{target}} in any city with owner contacts, find the local keywords competitors rank for, and make short demo videos owners actually watch. Most calls cost under a cent, with no subscription.

I'd be happy to send you a free list of {{target}} in one city, contacts included. Should I start with {{start_city}}?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 2 (wait 3 days). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

One thing I forgot to mention: owners buy what they can see. SpringBrand can turn a product screenshot into a 15-second demo video with voiceover, ready for Facebook, Instagram or your next email.

The free list of {{target}} still stands. Just reply "yes" for {{start_city}}, or name any other city.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 3 (wait 4 days after step 2). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Last note from me, promise. If outbound isn't a priority right now, I completely understand.

The free list of {{target}} stays on offer whenever {{companyName}} is ready to expand to a new city, along with starter credits to build more. And if someone else on the team owns sales, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 2. Variables
The sequence uses these variables: {{firstName}}, {{companyName}}, {{tagline}}, {{target}}, {{start_city}}. firstName and companyName are built-in lead fields. The others are custom variables on each lead.

The custom variable `start_city` is new, so my leads may not have it yet. Set `start_city` on each lead to the value below, matching by company name:

- Alloovium: Brisbane
- Asteria: San Francisco
- Async: New York
- Bernard: New York
- Bizmark: San Francisco
- CarSignal: Los Angeles
- FlowManual: San Francisco
- Luca IQ: Boston
- Marble: New York
- Pango: New York
- Perceptron ML: San Francisco
- Rational: San Francisco
- RealPact: San Francisco
- Sidekick: San Francisco
- Vestris: San Francisco
- Whitespace: London
- Zaplar: Stockholm
- Axelrod: San Francisco
- Dream: San Francisco
- HERA: San Francisco
- Torus: San Francisco

If you cannot set custom variables on leads, replace every {{start_city}} in the subjects and bodies with "your home city" instead, so no email has a blank.

Check every lead: if any variable used above is empty for a lead, tell me which leads and which variable. Do not send to leads with an empty tagline or target; list them for me instead.

## 3. Settings
- Open tracking: off. Link tracking: off.
- Stop the sequence for a lead when they reply: on.
- Sending days: Monday to Friday. Sending window: 8:00 to 11:00 in the lead's time zone if supported, otherwise 8:00 to 11:00 US Pacific.
- Daily limit: no more than 30 new leads per sending inbox per day.
- Text only (no HTML formatting, images or unsubscribe banners added to the body).

## 4. Final check
Preview the full sequence (all 3 steps and both subject variants) for three different leads. Confirm there are no blanks, no leftover {{...}}, and no doubled spaces. Then report back.
````

## 05-ai-native-services (5. AI-native service firms, 20 leads)

````
You are helping me get my Instantly campaign "05-ai-native-services" ready to launch. Do not launch or schedule it; stop when everything is ready and give me a short report of what you changed and anything you couldn't do.

## 1. Sequence
Replace the campaign's sequence with exactly these 3 steps. Keep the wording, line breaks and {{variables}} exactly as written. Use plain text, no images or links in step 1.

Step 1 (day 0). Subject variant A: where {{target}} get their clients | Subject variant B: keywords {{companyName}} can take
Body:
```
Hi {{firstName}},

Arsham from SpringBrand here. I saw {{companyName}} in the S26 batch ("{{tagline}}").

Winning clients from {{target}} often comes down to search. They've owned the keywords your future clients type for years. SpringBrand shows you exactly where they get their traffic and which keywords you can realistically win. At under a cent per call with no subscription, it's cheap to find out.

Can I send you a free breakdown of three {{target}} in your market?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 2 (wait 3 days). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

To show what you'd get: the free breakdown lists the keywords bringing three {{target}} the most traffic, roughly how many visits each one drives, and which of their pages rank for them. You'd see exactly where {{companyName}} can compete.

Just reply "send it" and I'll put it together.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 3 (wait 4 days after step 2). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Last note from me, promise. If search isn't a priority right now, I completely understand.

The free breakdown of three {{target}} stays on offer whenever {{companyName}} is ready to grow inbound, along with starter credits to run your own research. And if someone else on the team owns marketing, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 2. Variables
The sequence uses these variables: {{firstName}}, {{companyName}}, {{tagline}}, {{target}}. firstName and companyName are built-in lead fields. The others are custom variables on each lead.

Check every lead: if any variable used above is empty for a lead, tell me which leads and which variable. Do not send to leads with an empty tagline or target; list them for me instead.

## 3. Settings
- Open tracking: off. Link tracking: off.
- Stop the sequence for a lead when they reply: on.
- Sending days: Monday to Friday. Sending window: 8:00 to 11:00 in the lead's time zone if supported, otherwise 8:00 to 11:00 US Pacific.
- Daily limit: no more than 30 new leads per sending inbox per day.
- Text only (no HTML formatting, images or unsubscribe banners added to the body).

## 4. Final check
Preview the full sequence (all 3 steps and both subject variants) for three different leads. Confirm there are no blanks, no leftover {{...}}, and no doubled spaces. Then report back.
````

## 06-consumer-health-creator (6. Consumer, health & creator apps, 24 leads)

````
You are helping me get my Instantly campaign "06-consumer-health-creator" ready to launch. Do not launch or schedule it; stop when everything is ready and give me a short report of what you changed and anything you couldn't do.

## 1. Sequence
Replace the campaign's sequence with exactly these 3 steps. Keep the wording, line breaks and {{variables}} exactly as written. Use plain text, no images or links in step 1.

Step 1 (day 0). Subject variant A: 20 {{creator_niche}} creators for {{companyName}} | Subject variant B: {{companyName}} on TikTok
Body:
```
Hi {{firstName}},

Arsham from SpringBrand here. I just saw {{companyName}} in the S26 batch ("{{tagline}}").

Consumer growth today runs on creators and short video, and both take a ton of time. SpringBrand's AI tools find {{creator_niche}} creators with 20K–100K followers who already talk about your space, spot what's trending, and turn a screenshot or product shot into a 15-second ad. Most calls cost under a cent, with no subscription.

Want me to send you 20 {{creator_niche}} creators who'd be a great fit for {{companyName}}, plus three ad ideas? Free, of course.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 2 (wait 3 days). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Quick idea while you think it over: SpringBrand can also show your best-performing posts from the last 30 days and turn this week's {{creator_niche}} trends into ready-to-post content, so you always know what to make next.

The 20 free creators are still yours. Just reply "yes".

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 3 (wait 4 days after step 2). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Last note from me, promise. If creator marketing isn't a priority right now, I completely understand.

The offer stands whenever {{companyName}} is ready for its next push: 20 free {{creator_niche}} creators, plus starter credits to find more. And if someone else on the team runs growth or social, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 2. Variables
The sequence uses these variables: {{firstName}}, {{companyName}}, {{tagline}}, {{creator_niche}}. firstName and companyName are built-in lead fields. The others are custom variables on each lead.

The custom variable `creator_niche` is new, so my leads may not have it yet. Set `creator_niche` on each lead to the value below, matching by company name:

- Audora: BookTok
- Gutgutgoose: gut-health
- Illume Labs: longevity and health
- Instaplay: gaming
- Lumeria: skincare
- MOCHI.TV: anime
- OpenTrade: investing
- PokerClubHub: poker
- RonanRx Inc.: biohacking
- Roster: prediction-market
- Snap Poker: poker
- Sunflower: sobriety
- tash: trading-card
- Touchy: AI and tech
- Tsenta: career
- Wondering: education
- Aponic: productivity
- Arbital: trading
- Bloomy: parenting and education
- Egoist Machines: AI and tech
- Kandor: personal-finance
- Omanta: health and science
- Palette: creator-economy
- Paperboy Products, Inc.: productivity

If you cannot set custom variables on leads, make these replacements in the subjects and bodies instead, so no email has a blank:
- "20 {{creator_niche}} creators" -> "20 creators in your niche"
- "this week's {{creator_niche}} trends" -> "this week's trends in your space"
- "{{creator_niche}} creators with" -> "creators with"

Check every lead: if any variable used above is empty for a lead, tell me which leads and which variable. Do not send to leads with an empty tagline or target; list them for me instead.

## 3. Settings
- Open tracking: off. Link tracking: off.
- Stop the sequence for a lead when they reply: on.
- Sending days: Monday to Friday. Sending window: 8:00 to 11:00 in the lead's time zone if supported, otherwise 8:00 to 11:00 US Pacific.
- Daily limit: no more than 30 new leads per sending inbox per day.
- Text only (no HTML formatting, images or unsubscribe banners added to the body).

## 4. Final check
Preview the full sequence (all 3 steps and both subject variants) for three different leads. Confirm there are no blanks, no leftover {{...}}, and no doubled spaces. Then report back.
````

## 07-deep-tech-hardware-bio (7. Deep tech, hardware, defense & bio, 76 leads)

````
You are helping me get my Instantly campaign "07-deep-tech-hardware-bio" ready to launch. Do not launch or schedule it; stop when everything is ready and give me a short report of what you changed and anything you couldn't do.

## 1. Sequence
Replace the campaign's sequence with exactly these 3 steps. Keep the wording, line breaks and {{variables}} exactly as written. Use plain text, no images or links in step 1.

Step 1 (day 0). Subject variant A: buyer research for {{companyName}} | Subject variant B: a buyer list for {{companyName}}
Body:
```
Hi {{firstName}},

Arsham from SpringBrand here. I came across {{companyName}} in the S26 batch ("{{tagline}}").

Deep-tech teams usually need market research in bursts: a buyer list before a pilot push, a competitor scan before a raise. Paying monthly for tools you use twice a quarter rarely makes sense. With SpringBrand, your AI agent runs that research on demand, usually for under a cent per call, with no subscription.

Name one type of buyer you're after and I'll send you a free list of organizations and decision-makers. Want one?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 2 (wait 3 days). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

To make it concrete: for {{companyName}}, the free sample would be 25 target organizations with their procurement or R&D leads, plus a one-page scan of who else is selling to them.

Just reply with the buyer type, for example "Tier 1 auto suppliers" or "US utilities", and I'll take it from there.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 3 (wait 4 days after step 2). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Last note from me, promise. If buyer research isn't a priority right now, I completely understand.

The offer stands whenever {{companyName}} gears up for a pilot push or a raise: one free buyer list, plus starter credits to run your own. And if someone else on the team leads business development, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 2. Variables
The sequence uses these variables: {{firstName}}, {{companyName}}, {{tagline}}. firstName and companyName are built-in lead fields. The others are custom variables on each lead.

Check every lead: if any variable used above is empty for a lead, tell me which leads and which variable. Do not send to leads with an empty tagline or target; list them for me instead.

## 3. Settings
- Open tracking: off. Link tracking: off.
- Stop the sequence for a lead when they reply: on.
- Sending days: Monday to Friday. Sending window: 8:00 to 11:00 in the lead's time zone if supported, otherwise 8:00 to 11:00 US Pacific.
- Daily limit: no more than 30 new leads per sending inbox per day.
- Text only (no HTML formatting, images or unsubscribe banners added to the body).

## 4. Final check
Preview the full sequence (all 3 steps and both subject variants) for three different leads. Confirm there are no blanks, no leftover {{...}}, and no doubled spaces. Then report back.
````

## 08-partner-candidates (★ Partner candidates (any category), 11 leads)

````
You are helping me get my Instantly campaign "08-partner-candidates" ready to launch. Do not launch or schedule it; stop when everything is ready and give me a short report of what you changed and anything you couldn't do.

## 1. Sequence
Replace the campaign's sequence with exactly these 3 steps. Keep the wording, line breaks and {{variables}} exactly as written. Use plain text, no images or links in step 1.

Step 1 (day 0). Subject variant A: who's talking about {{dev_topic}} | Subject variant B: {{companyName}} + SpringBrand
Body:
```
Hi {{firstName}},

Arsham from SpringBrand here. I saw {{companyName}} in the S26 batch. Tools like yours win when developers hear about them at the right moment.

SpringBrand plugs GTM tools straight into Claude Code or Cursor: see who's talking about {{dev_topic}} on X and Reddit, where competing tools get their traffic, and which AI teams fit your ideal customer. Most calls cost under a cent, with no subscription.

Can I send you a free snapshot of this week's conversations about {{dev_topic}}? I'd also love to hear whether {{companyName}} could fit on the SpringBrand marketplace down the line.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 2 (wait 3 days). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Quick follow-up: setup is one line (npx add-mcp https://connector.springbrand.ai/mcp), then you just ask your agent something like "Show me this week's Reddit threads about {{dev_topic}} and where our top competitor gets its traffic."

Happy to run it for {{companyName}} first and send you the results. Want me to?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

Step 3 (wait 4 days after step 2). Leave the subject EMPTY so it sends as a reply in the same thread.
Body:
```
Hi {{firstName}},

Last note from me, promise. If marketing isn't on your plate right now, I completely understand.

The free snapshot of conversations about {{dev_topic}} stays on offer whenever {{companyName}} gears up for its next launch, along with starter credits to run your own. And if someone else on the team owns growth or partnerships, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 2. Variables
The sequence uses these variables: {{firstName}}, {{companyName}}, {{dev_topic}}. firstName and companyName are built-in lead fields. The others are custom variables on each lead.

The custom variable `dev_topic` is new, so my leads may not have it yet. Set `dev_topic` on each lead to the value below, matching by company name:

- Agentcard: agent payments
- Amorphic Labs: agentic commerce
- Click: AI research tools
- Context.dev: web context for agents
- Executor: AI integrations
- Financial Datasets: financial data for agents
- Inkbox: agent communication
- Magma: agent trace data
- Rindler: browser agents
- Speko: voice AI models
- Praxis Robotics: data marketplaces

If you cannot set custom variables on leads, replace every {{dev_topic}} in the subjects and bodies with "your space" instead, so no email has a blank.

Check every lead: if any variable used above is empty for a lead, tell me which leads and which variable. Do not send to leads with an empty tagline or target; list them for me instead.

## 3. Settings
- Open tracking: off. Link tracking: off.
- Stop the sequence for a lead when they reply: on.
- Sending days: Monday to Friday. Sending window: 8:00 to 11:00 in the lead's time zone if supported, otherwise 8:00 to 11:00 US Pacific.
- Daily limit: no more than 30 new leads per sending inbox per day.
- Text only (no HTML formatting, images or unsubscribe banners added to the body).

## 4. Final check
Preview the full sequence (all 3 steps and both subject variants) for three different leads. Confirm there are no blanks, no leftover {{...}}, and no doubled spaces. Then report back.
````
