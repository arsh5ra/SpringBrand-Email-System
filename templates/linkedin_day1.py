"""LinkedIn outreach, day 1: 20 high-fit YC S2026 companies.

Each entry: who to contact, a connection note (<= 200 chars, the limit for
personalised invites on free accounts) and a DM to send once they accept.
Run to validate note lengths and write docs/linkedin-outreach-day-1.md and
private/linkedin-tracker.csv.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LEADS = [
    # --- GTM & growth builders ---
    dict(company="LemonLime", category="GTM & growth builders", contact="Daniela Muñoz", backup="Jordan Zietz",
         note="Hi Daniela, Arsham from SpringBrand. Fully automated GTM for small business is a big swing. We build GTM tools for AI agents and I'd love to swap notes. Congrats on S26!",
         dm="Thanks for connecting, Daniela!\n\nLemonLime caught my eye because it sits right where we work. SpringBrand gives AI agents GTM tools (lead and contact discovery, traffic and SEO research, social listening, content generation) through one connection, at under a cent per call with no subscription.\n\nCould be useful for your own pipeline, or as a data layer inside LemonLime. Happy to load free credits and build a sample around one workflow. Worth a look?"),
    dict(company="Nex", category="GTM & growth builders", contact="Nazz Mohammad", backup="Francisco Dias",
         note="Hi Nazz, Arsham here from SpringBrand. Claude Cowork for GTM workflows is a great wedge. We give agents GTM tools per call and I think there's overlap worth a chat. Congrats on S26!",
         dm="Thanks for connecting, Nazz!\n\nNex's GTM-first angle is exactly what we're building for. SpringBrand plugs GTM capabilities into AI agents: find companies and contacts, research competitor traffic, monitor social, generate content. It's pay per call, typically under a cent.\n\nIf your workflows ever need that data, we could be the layer underneath. Want free credits to test it inside a Nex workflow?"),
    dict(company="TryNearby", category="GTM & growth builders", contact="Obaida Albaroudi", backup="Ahmad Ibrahim",
         note="Hi Obaida, Arsham from SpringBrand. Local creators for local businesses is such a smart market. We help AI agents find creators and make content. Would love to connect!",
         dm="Thanks for connecting, Obaida!\n\nTryNearby's model lines up with what SpringBrand does well: creator discovery across TikTok, Instagram and YouTube, plus turning a brief into short video and copy. It's pay per call, usually under a cent, with no subscription.\n\nI'd be happy to pull a free list of local creators in a city you're launching in, to see if it speeds up your matching. Which city should I try?"),
    dict(company="Osmaura", category="GTM & growth builders", contact="Jity Woldemichael", backup="Kali Abeje",
         note="Hi Jity, Arsham from SpringBrand. An AI growth engine for law firms is a sharp niche. We give AI agents SEO and content tools, so I'd love to connect and trade notes. Congrats on S26!",
         dm="Thanks for connecting, Jity!\n\nGrowth for law firms is mostly search, which is where SpringBrand helps: competitor keyword gaps, where rival firms get their traffic, cost per lead on Google vs. Meta, plus content generation. It's under a cent per typical call, with no subscription.\n\nHappy to run a free keyword and traffic breakdown for one of your client markets. Want me to?"),
    # --- AI agent infra & devtools ---
    dict(company="HyperProbe", category="AI agent infra & devtools", contact="Shailendra Singh", backup="Karan Raina",
         note="Hi Shailendra, Arsham from SpringBrand. \"Let your coding agent fix prod too\" is a great line. We put GTM tools inside coding agents. Would love to connect!",
         dm="Thanks for connecting, Shailendra!\n\nDevtools like HyperProbe get won on X, Reddit and Hacker News-style threads. SpringBrand lets you research that from inside Claude Code or Cursor: who's talking about prod debugging, where competitors get their traffic, which teams fit your ideal customer. Most calls cost under a cent.\n\nCan I send you a free snapshot of this week's conversations in your space?"),
    dict(company="Agnost AI", category="AI agent infra & devtools", contact="Parth Ajmera", backup="Shubham Palriwala",
         note="Hi Parth, Arsham from SpringBrand. Product analytics for AI agents is overdue. We build tools that agents call per use, so we think about this a lot. Would love to connect!",
         dm="Thanks for connecting, Parth!\n\nWe're on the other side of your market: SpringBrand gives AI agents GTM tools (social listening, traffic and SEO research, lead discovery) that they call per use, all from inside Claude Code or Cursor.\n\nFor your launch, I'd be happy to pull a free breakdown of who's discussing agent analytics on X and Reddit, plus where competing tools get their traffic. Interested?"),
    dict(company="Mentlio", category="AI agent infra & devtools", contact="Ashank Shah", backup="Ahmet Demirbas",
         note="Hi Ashank, Arsham from SpringBrand. Token optimization for AI coding teams is a real pain point. We run GTM tools inside coding agents. Would love to connect!",
         dm="Thanks for connecting, Ashank!\n\nEngineering leaders are exactly who Mentlio sells to, and finding them is where SpringBrand helps. Your agent can pull companies and eng leads that fit your ideal customer, track token-cost conversations on X and Reddit, and see competitor traffic. Calls are typically under a cent, with no subscription.\n\nWant a free sample list of 25 teams that match your ideal customer?"),
    dict(company="Conifer", category="AI agent infra & devtools", contact="Michael Jeffords", backup="Charles Muehlberger",
         note="Hi Michael, Arsham from SpringBrand. Cutting token spend 80% will sell itself if the right devs hear about it. We help with that part. Would love to connect!",
         dm="Thanks for connecting, Michael!\n\nWe're pay-per-call too, so Conifer's cost story resonates. SpringBrand plugs GTM tools into the agent you already code in: find the Reddit and X threads where devs complain about token bills, see where competing routers get their traffic, and find teams worth reaching out to. Typical calls cost under a cent.\n\nWant me to pull this week's token-cost threads for you, free?"),
    # --- B2B / enterprise AI SaaS ---
    dict(company="Litmus", category="B2B / enterprise AI SaaS", contact="Elena Zhao", backup="Shaivi Rau",
         note="Hi Elena, Arsham from SpringBrand. Async work trials for every engineer is a great hiring unlock. We help S26 teams build pipeline fast. Would love to connect!",
         dm="Thanks for connecting, Elena!\n\nLitmus sells to engineering and talent leaders, and SpringBrand can find them for you: companies that are actively hiring engineers, with the right decision-makers, pushed straight into your CRM. It's pay as you go, under a cent per typical call, with everything on one bill.\n\nWant a free sample list of 25 companies hiring engineers right now?"),
    dict(company="Rence", category="B2B / enterprise AI SaaS", contact="Frans Paborn", backup="Jonas Rosengren",
         note="Hi Frans, Arsham from SpringBrand. An AI coach that rides along every sales visit is a great idea. We build GTM tools for AI agents. Would love to connect!",
         dm="Thanks for connecting, Frans!\n\nField sales orgs are a specific crowd to find, which is where SpringBrand helps. Your AI agent can pull companies with in-person sales teams, find the sales leaders, and add them to your CRM, then draft follow-ups when deals go quiet. Calls are under a cent, with no subscription.\n\nWant a free sample of 25 field-sales companies in Europe or the US?"),
    # --- Vertical AI for SMBs ---
    dict(company="CarSignal", category="Vertical AI for SMBs", contact="Michael Muzzin", backup="Junaid Popalzai",
         note="Hi Michael, Arsham from SpringBrand. An OS for auto shops is a huge, underserved market. We help AI agents build local lead lists fast. Would love to connect!",
         dm="Thanks for connecting, Michael!\n\nSelling to auto shops is a numbers game, and SpringBrand does the heavy lifting: lists of auto repair shops in any city with owner contacts, local keyword research, and short demo videos owners actually watch. Most calls cost under a cent.\n\nPick a city and I'll send you a free list of auto shops there, contacts included. Where should I start?"),
    dict(company="Marble", category="Vertical AI for SMBs", contact="Aakar Khanna", backup="Arjun Chaliha",
         note="Hi Aakar, Arsham from SpringBrand. An autonomous back-of-house for restaurants is a big idea. We help AI agents find and reach local operators. Would love to connect!",
         dm="Thanks for connecting, Aakar!\n\nRestaurants are hard to reach at scale, and SpringBrand helps: lists of restaurants by city and cuisine with owner contacts, the local keywords competitors rank for, and short demo videos for Instagram. Most calls cost under a cent, with no subscription.\n\nWant a free list of 50 independent restaurants in NYC to test with?"),
    dict(company="RealPact", category="Vertical AI for SMBs", contact="Erik Peterson", backup="Ranvir Deshmukh",
         note="Hi Erik, Arsham from SpringBrand. An AI-native OS for brokerages is a smart wedge. We help AI agents build broker lead lists city by city. Would love to connect!",
         dm="Thanks for connecting, Erik!\n\nBrokerages are a volume sale, and SpringBrand can build the list: brokerages in any metro with broker-owner contacts, straight into your CRM, plus follow-up drafts. Most calls cost under a cent.\n\nPick a metro and I'll send you a free list of brokerages there, contacts included. Which one?"),
    dict(company="Zaplar", category="Vertical AI for SMBs", contact="Douglas Solberg", backup="Axel Andersson Lingbert",
         note="Hi Douglas, Arsham from SpringBrand. An agentic hotel OS is a great bet. We help AI agents find and reach independent hotels. Would love to connect!",
         dm="Thanks for connecting, Douglas!\n\nIndependent hotels are scattered and hard to reach, and SpringBrand helps your agent find them: hotels by city with GM and owner contacts, local search research, and short demo videos. Most calls cost under a cent, with no subscription.\n\nWant a free list of independent hotels in Stockholm (or any city you're targeting) to start with?"),
    # --- AI-native service firms ---
    dict(company="Wingman Law", category="AI-native service firms", contact="Sun Woo Lee", backup="Mohini Tangri",
         note="Hi Sun, Arsham from SpringBrand. An AI-native personal injury firm is bold. That market lives on search. We help with exactly that. Would love to connect!",
         dm="Thanks for connecting, Sun!\n\nPersonal injury is one of the most competitive search markets there is. SpringBrand shows you where established PI firms get their traffic and which keywords you can realistically win, and compares cost per lead on Google vs. Meta. At under a cent per call, it's cheap to find out.\n\nWant a free breakdown of three established PI firms in your market?"),
    dict(company="Billow AI Labs", category="AI-native service firms", contact="Philip Moniaga", backup="Joanathan McIntosh",
         note="Hi Philip, Arsham from SpringBrand. Replacing the Big-4 with an AI-native firm is a great mission. We help AI agents win search and leads. Would love to connect!",
         dm="Thanks for connecting, Philip!\n\nTaking clients from the Big-4 comes down to being found. SpringBrand shows where traditional accounting firms get their traffic, which keywords you can win, and can build lead lists of companies that fit your ideal client. Calls are under a cent, with no subscription.\n\nWant a free keyword breakdown of three accounting firms you compete with?"),
    # --- Consumer, health & creator ---
    dict(company="Snap Poker", category="Consumer & creator", contact="Neel Gadde", backup="Dillon Mehta",
         note="Hi Neel, Arsham from SpringBrand. A social network for online poker is so fun. We help AI agents find creators and trends. Would love to connect!",
         dm="Thanks for connecting, Neel!\n\nPoker content is huge on TikTok, YouTube and X, and SpringBrand's tools find creators with 20K–100K followers already in that world, spot trending formats, and turn clips into short ads. Most calls cost under a cent, with no subscription.\n\nWant a free list of 20 poker creators who'd be a great fit for Snap Poker?"),
    dict(company="Lumeria", category="Consumer & creator", contact="Anthea Guo", backup="Maryanne Alhallak",
         note="Hi Anthea, Arsham from SpringBrand. An Oura Ring for skin is such a great pitch. We help brands find the right skincare creators. Would love to connect!",
         dm="Thanks for connecting, Anthea!\n\nSkin tech lives on TikTok and Instagram, and SpringBrand finds skincare and wellness creators with 20K–100K followers, tracks what's trending, and turns a product shot into a 15-second ad. It can also benchmark your pricing against competitors. Most calls cost under a cent.\n\nWant a free list of 20 skincare creators who fit Lumeria, plus three ad ideas?"),
    dict(company="Audora", category="Consumer & creator", contact="Dhanush R", backup="",
         note="Hi Dhanush, Arsham from SpringBrand. Audiobooks with a unique voice per character is a lovely idea. We help with creators and voice content. Would love to connect!",
         dm="Thanks for connecting, Dhanush!\n\nBookTok is made for Audora. SpringBrand finds book creators with 20K–100K followers on TikTok and Instagram, spots trending titles, and can turn a scene into a short video with voiceover for ads. Most calls cost under a cent, with no subscription.\n\nWant a free list of 20 BookTok creators, plus three ad concepts?"),
    dict(company="Tsenta", category="Consumer & creator", contact="Agnay Srivastava", backup="Pulkit Gupta",
         note="Hi Agnay, Arsham from SpringBrand. An AI agent that finds jobs and applies for you will spread fast. We help with the creator side. Would love to connect!",
         dm="Thanks for connecting, Agnay!\n\nCareer content is one of the biggest niches on TikTok and LinkedIn. SpringBrand finds career creators with 20K–100K followers, tracks what job seekers are complaining about on Reddit, and turns that into posts and short ads. Most calls cost under a cent.\n\nWant a free list of 20 career creators who'd be a great fit for Tsenta?"),
]


def main():
    over = [(l["company"], len(l["note"])) for l in LEADS if len(l["note"]) > 200]
    assert not over, f"notes over 200 chars: {over}"
    L = ["# LinkedIn outreach: day 1 (20 companies)", "",
         "Twenty High-fit YC S2026 companies, four or so per category. For each: who to contact, a connection note "
         "(under 200 characters, LinkedIn's limit for personalised invites) and a DM to send once they accept.", "",
         "**How to run it:** send 20 invites today. When someone accepts, send the DM the same day. "
         "If there's no reply after 4–5 days, like or thoughtfully comment on one of their posts, then send one short nudge: "
         "\"Hi {name}, just bumping this. Happy to send the free sample whenever it's useful.\" "
         "Log everything in the tracker CSV.", "",
         "**Finding them:** search LinkedIn for the contact's name plus the company. If they don't turn up, try the backup founder.", ""]
    cat = None
    for i, l in enumerate(LEADS, 1):
        if l["category"] != cat:
            cat = l["category"]; L += [f"## {cat}", ""]
        L += [f"### {i}. {l['company']}", "",
              f"**Contact:** {l['contact']}" + (f" (backup: {l['backup']})" if l["backup"] else ""), "",
              f"**Connection note** ({len(l['note'])} chars):", "", "> " + l["note"], "",
              "**DM after they accept:**", "", "> " + l["dm"].replace("\n\n", "\n>\n> "), ""]
    (ROOT / "docs/linkedin-outreach-day-1.md").write_text("\n".join(L))
    with open(ROOT / "private/linkedin-tracker.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["#", "Company", "Category", "Contact", "Backup contact", "Connection note", "DM after accept",
                    "Invite sent", "Accepted", "DM sent", "Replied", "Next step"])
        for i, l in enumerate(LEADS, 1):
            w.writerow([i, l["company"], l["category"], l["contact"], l["backup"], l["note"], l["dm"], "", "", "", "", ""])
    print(len(LEADS), "leads; longest note", max(len(l["note"]) for l in LEADS), "chars")


if __name__ == "__main__":
    main()
