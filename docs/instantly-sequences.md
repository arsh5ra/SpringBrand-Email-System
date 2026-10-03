# Instantly sequences

One Instantly campaign per lead file in `private/instantly/`. Paste each step below into the campaign's sequence.
Variables: `{{firstName}}`, `{{companyName}}` (built in), `{{tagline}}`, `{{target}}`, `{{agent_need}}`, `{{creator_niche}}`, `{{dev_topic}}`, `{{subject_a}}`, `{{subject_b}}` (custom columns in the lead file).
Use subject A and B as two variants of step 1 to A/B test. Steps 2 and 3 are sent as replies in the same thread (leave their subject blank).

## 01-gtm-growth-builders (1. GTM & growth builders)

**Step 1 (day 0)**, subject variant A: `{{subject_a}}`, variant B: `{{subject_b}}`

```
Hi {{firstName}},

Arsham here, growth marketing manager at SpringBrand. I came across {{companyName}} in the S26 batch ("{{tagline}}") and had to reach out.

Products like yours run on data: leads, traffic, social signals, content. We put all of it behind one connection your agents can call. A typical call costs less than a cent, with no subscriptions, no contract with each data vendor, and everything on one bill.

I'd love to set you up with free starter credits and build a quick sample around a workflow you care about. Worth a look?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 2 (wait 3 days, same thread)**

```
Hi {{firstName}},

Here's what I had in mind for {{companyName}}: 50 companies that match your ideal customer, with decision-maker contacts and a first-touch draft, all from one request.

If it's more useful as a product feature, I can show you the same thing running through the API instead.

Just reply "yes" and I'll send it over.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 3 (wait 4 more days, same thread)**

```
Hi {{firstName}},

Last note from me, promise. If growth tooling isn't a priority right now, I totally understand.

Your free starter credits aren't going anywhere, so they're there whenever {{companyName}} needs a lead list, a competitor scan or some fresh content. And if someone else on the team owns growth, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 02-ai-infra-devtools (2. AI agent infra & devtools)

**Step 1 (day 0)**, subject variant A: `{{subject_a}}`, variant B: `{{subject_b}}`

```
Hi {{firstName}},

This is Arsham from SpringBrand. Congrats on S26!

Devtools get won on X, Reddit and YouTube, and most technical founders don't have time to keep up. SpringBrand plugs GTM tools straight into the agent you already code in, so you can ask Claude Code or Cursor who's talking about {{dev_topic}}, where competitors get their traffic, or which AI teams fit your ideal customer. Most calls cost under a cent, with no subscription.

Can I send you a free snapshot of this week's {{dev_topic}} conversations, plus a competitor traffic breakdown for {{companyName}}?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 2 (wait 3 days, same thread)**

```
Hi {{firstName}},

Quick follow-up: setup is one line (npx add-mcp https://connector.springbrand.ai/mcp), then you just ask your agent something like "Show me this week's Reddit threads about {{dev_topic}} and where our top competitor gets its traffic."

Happy to run it for {{companyName}} first and send you the results. Want me to?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 3 (wait 4 more days, same thread)**

```
Hi {{firstName}},

Last note from me, promise. If marketing isn't on your plate right now, I completely understand.

The free snapshot of {{dev_topic}} conversations stays on offer whenever {{companyName}} gears up for its next launch, along with starter credits to run your own. And if someone else on the team owns growth, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 03-b2b-enterprise-saas (3. B2B / enterprise AI SaaS)

**Step 1 (day 0)**, subject variant A: `{{subject_a}}`, variant B: `{{subject_b}}`

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

**Step 2 (wait 3 days, same thread)**

```
Hi {{firstName}},

To make it easy: one line is enough, for example "Series A fintechs in New York, Head of Finance". You'd get 25 matching companies, each with the right decision-maker, ready to drop into your CRM.

Want me to start one for {{companyName}}?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 3 (wait 4 more days, same thread)**

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

## 04-vertical-ai-smb (4. Vertical AI for SMBs & local operators)

**Step 1 (day 0)**, subject variant A: `{{subject_a}}`, variant B: `{{subject_b}}`

```
Hi {{firstName}},

I'm Arsham, growth marketing manager at SpringBrand. {{companyName}} caught my eye in the S26 batch ("{{tagline}}").

Selling to {{target}} is a numbers game: long lists, local search and a lot of follow-up. Our AI tools do the heavy lifting. They build a list of {{target}} in any city with owner contacts, find the local keywords competitors rank for, and make short demo videos owners actually watch. Most calls cost less than a cent.

Pick a city and I'll send you a free list of {{target}} there, contacts included. Where should I start?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 2 (wait 3 days, same thread)**

```
Hi {{firstName}},

One thing I forgot to mention: owners buy what they can see. SpringBrand can turn a product screenshot into a 15-second demo video with voiceover, ready for Facebook, Instagram or your next email.

The free lead list still stands. Just name a city.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 3 (wait 4 more days, same thread)**

```
Hi {{firstName}},

Last note from me, promise. If growth tooling isn't a priority right now, I totally understand.

Your free starter credits aren't going anywhere, so they're there whenever {{companyName}} needs a lead list, a competitor scan or some fresh content. And if someone else on the team owns growth, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

## 05-ai-native-services (5. AI-native service firms)

**Step 1 (day 0)**, subject variant A: `{{subject_a}}`, variant B: `{{subject_b}}`

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

**Step 2 (wait 3 days, same thread)**

```
Hi {{firstName}},

To show what you'd get: the free breakdown lists the keywords bringing three {{target}} the most traffic, roughly how many visits each one drives, and which of their pages rank for them. You'd see exactly where {{companyName}} can compete.

Just reply "send it" and I'll put it together.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 3 (wait 4 more days, same thread)**

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

## 06-consumer-health-creator (6. Consumer, health & creator apps)

**Step 1 (day 0)**, subject variant A: `{{subject_a}}`, variant B: `{{subject_b}}`

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

**Step 2 (wait 3 days, same thread)**

```
Hi {{firstName}},

Quick idea while you think it over: SpringBrand can also show your best-performing posts from the last 30 days and turn this week's {{creator_niche}} trends into ready-to-post content, so you always know what to make next.

The 20 free creators are still yours. Just reply "yes".

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 3 (wait 4 more days, same thread)**

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

## 07-deep-tech-hardware-bio (7. Deep tech, hardware, defense & bio)

**Step 1 (day 0)**, subject variant A: `{{subject_a}}`, variant B: `{{subject_b}}`

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

**Step 2 (wait 3 days, same thread)**

```
Hi {{firstName}},

To make it concrete: for {{companyName}}, the free sample would be 25 target organizations with their procurement or R&D leads, plus a one-page scan of who else is selling to them.

Just reply with the buyer type, for example "Tier 1 auto suppliers" or "US utilities", and I'll take it from there.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 3 (wait 4 more days, same thread)**

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

## 08-partner-candidates (★ Partner candidates (any category))

**Step 1 (day 0)**, subject variant A: `{{subject_a}}`, variant B: `{{subject_b}}`

```
Hi {{firstName}},

Arsham from SpringBrand here. I saw {{companyName}} in the S26 batch and immediately thought of our marketplace.

SpringBrand is where AI agents find tools. People in Claude Code, Cursor and Codex describe what they need, and their agent picks the right tool for the job. Listing {{companyName}} puts it in front of those agents the moment one of them {{agent_need}}.

Worth a quick chat about listing {{companyName}}?

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 2 (wait 3 days, same thread)**

```
Hi {{firstName}},

Quick follow-up. Listing {{companyName}} is a new way to get discovered with no extra sales work: agents search by the outcome they need, so {{companyName}} shows up exactly when it's relevant.

Would 15 minutes this week work for a walkthrough? If you'd rather look first, I can send free credits so you can try SpringBrand as a user.

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```

**Step 3 (wait 4 more days, same thread)**

```
Hi {{firstName}},

Last note from me, promise. If a new distribution channel isn't a priority right now, I completely understand.

The offer to list {{companyName}} stays open, and so do your free credits. And if someone else on the team handles partnerships, I'd really appreciate a pointer.

Rooting for you this batch!

Best,
Arsham
Growth Marketing Manager, SpringBrand
springbrand.ai
```
