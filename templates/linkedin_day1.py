"""LinkedIn outreach, day 1: 20 high-fit YC S2026 companies.

One message per contact, at most 300 characters so it fits a LinkedIn
connection note (Premium limit; free accounts allow 200) and also works as
a DM. Run to validate lengths and write docs/linkedin-outreach-day-1.md and
private/linkedin-tracker.csv.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIMIT = 300

# LinkedIn profiles found via web search (September 2026). "Verified": the
# profile headline names the company. "Check": matched from a post URL or the
# headline differs, so glance at the profile before sending.
LEADS = [
    # --- GTM & growth builders ---
    dict(company="LemonLime", subject="A data layer for LemonLime's agents", category="GTM & growth builders", contact="Daniela Muñoz", backup="Jordan Zietz",
         linkedin="https://www.linkedin.com/in/danielamunoz12/", status="Verified",
         message="Hi Daniela, Arsham from SpringBrand. Congrats on S26! LemonLime runs on GTM data, and we give AI agents lead, traffic, social and content tools at under a cent per call, no subscription. Happy to load free credits and build a sample for one of your workflows. Worth a look?"),
    dict(company="Nex", subject="The GTM data under Nex", category="GTM & growth builders", contact="Nazz Mohammad", backup="Francisco Dias",
         linkedin="https://www.linkedin.com/in/najmuzzaman/", status="Verified",
         message="Hi Nazz, Arsham from SpringBrand. Claude Cowork for GTM is a great wedge. We give agents GTM tools (leads, competitor traffic, social, content) at under a cent per call, no subscription. Could be the data layer under Nex. Want free credits to test it in a workflow?"),
    dict(company="TryNearby", subject="Local creators for your next city", category="GTM & growth builders", contact="Obaida Albaroudi", backup="Ahmad Ibrahim",
         linkedin="https://www.linkedin.com/in/obaida-albaroudi-b7b366279/", status="Check: taken from one of Obaida's TryNearby posts",
         message="Hi Obaida, Arsham from SpringBrand. Local creators for local businesses is such a smart market. Our AI tools find creators on TikTok, Instagram and YouTube at under a cent per call. Want a free list of local creators in a city you're launching in? Just name it."),
    dict(company="Osmaura", subject="Where your law firms' rivals get clients", category="GTM & growth builders", contact="Jity Woldemichael", backup="Kali Abeje",
         linkedin="https://www.linkedin.com/in/tselote/", status="Verified",
         message="Hi Jity, Arsham from SpringBrand. Congrats on S26! Law firm growth lives on search, and our AI tools show where rival firms get their traffic and which keywords they miss, at under a cent per call. Want a free keyword breakdown for one of your client markets?"),
    # --- AI agent infra & devtools ---
    dict(company="HyperProbe", subject="Who's talking about prod debugging this week", category="AI agent infra & devtools", contact="Shailendra Singh", backup="Karan Raina",
         linkedin="https://www.linkedin.com/in/shailendra-singh-6540b8b/", status="Verified",
         message="Hi Shailendra, Arsham from SpringBrand. \"Let your coding agent fix prod too\" is a great line. We put GTM tools inside coding agents: who's talking about your space on X and Reddit, plus competitor traffic, at under a cent per call. Can I send you a free snapshot?"),
    dict(company="Agnost AI", subject="Who's discussing agent analytics right now", category="AI agent infra & devtools", contact="Parth Ajmera", backup="Shubham Palriwala",
         linkedin="https://www.linkedin.com/in/parthajmera/", status="Verified",
         message="Hi Parth, Arsham from SpringBrand. Product analytics for AI agents is overdue. We build GTM tools agents call per use, right from Claude Code or Cursor. Happy to send a free breakdown of who's discussing agent analytics on X and Reddit, plus competitor traffic. Interested?"),
    dict(company="Mentlio", subject="25 AI coding teams that fit Mentlio", category="AI agent infra & devtools", contact="Ashank Shah", backup="Ahmet Demirbas",
         linkedin="https://www.linkedin.com/in/ashank-shah/", status="Verified",
         message="Hi Ashank, Arsham from SpringBrand. Token optimization for AI coding teams is a real pain point. Our AI tools find engineering leaders who fit your ideal customer, at under a cent per call with no subscription. Want a free list of 25 teams that match?"),
    dict(company="Conifer", subject="This week's token-bill complaints, free", category="AI agent infra & devtools", contact="Michael Jeffords", backup="Charles Muehlberger",
         linkedin="https://www.linkedin.com/in/michael-bryan-jeffords/", status="Verified",
         message="Hi Michael, Arsham from SpringBrand. We're pay per call too, so Conifer's cost story resonates. Our tools run inside your coding agent and find the Reddit and X threads where devs complain about token bills. Want me to pull this week's for you, free?"),
    # --- B2B / enterprise AI SaaS ---
    dict(company="Litmus", subject="25 companies hiring engineers right now", category="B2B / enterprise AI SaaS", contact="Elena Zhao", backup="Shaivi Rau",
         linkedin="https://www.linkedin.com/in/elena-zhao-015353217/", status="Verified",
         message="Hi Elena, Arsham from SpringBrand. Async work trials for every engineer is a great hiring unlock. Our AI tools find companies hiring engineers right now, with the right decision-makers, at under a cent per call. Want a free list of 25 to start?"),
    dict(company="Rence", subject="25 field sales teams for Rence", category="B2B / enterprise AI SaaS", contact="Frans Paborn", backup="Jonas Rosengren",
         linkedin="https://www.linkedin.com/in/frans-paborn-990120305/", status="Verified",
         message="Hi Frans, Arsham from SpringBrand. An AI coach that rides along every sales visit is a great idea. Our AI tools find companies with field sales teams and their sales leaders, at under a cent per call. Want a free sample of 25 in Europe or the US?"),
    # --- Vertical AI for SMBs ---
    dict(company="CarSignal", subject="Every auto shop in one city", category="Vertical AI for SMBs", contact="Michael Muzzin", backup="Junaid Popalzai",
         linkedin="https://www.linkedin.com/in/mmuzzin/", status="Verified",
         message="Hi Michael, Arsham from SpringBrand. An OS for auto shops is a huge market. Our AI tools build lists of auto repair shops in any city with owner contacts, at under a cent per call. Pick a city and I'll send you a free list. Where should I start?"),
    dict(company="Marble", subject="50 NYC restaurants for Marble", category="Vertical AI for SMBs", contact="Aakar Khanna", backup="Arjun Chaliha",
         linkedin="https://www.linkedin.com/in/aakarkhanna/", status="Check: headline says Truffle (YC S26), possibly Marble's new name",
         message="Hi Aakar, Arsham from SpringBrand. An autonomous back-of-house for restaurants is a big idea. Our AI tools find restaurants by city and cuisine with owner contacts, at under a cent per call. Want a free list of 50 independent NYC restaurants to test with?"),
    dict(company="RealPact", subject="Every brokerage in one metro", category="Vertical AI for SMBs", contact="Erik Peterson", backup="Ranvir Deshmukh",
         linkedin="https://www.linkedin.com/in/erik-peterson-mn/", status="Verified",
         message="Hi Erik, Arsham from SpringBrand. An AI-native OS for brokerages is a smart wedge. Our AI tools build lists of brokerages in any metro with broker-owner contacts, at under a cent per call. Pick a metro and I'll send you a free list. Which one?"),
    dict(company="Zaplar", subject="Independent hotels, one city at a time", category="Vertical AI for SMBs", contact="Douglas Solberg", backup="Axel Andersson Lingbert",
         linkedin="https://www.linkedin.com/in/douglas-solberg/", status="Verified",
         message="Hi Douglas, Arsham from SpringBrand. An agentic hotel OS is a great bet. Our AI tools find independent hotels by city with GM and owner contacts, at under a cent per call. Want a free list for Stockholm, or any city you're targeting?"),
    # --- AI-native service firms ---
    dict(company="Wingman Law", subject="Where PI firms get their clients", category="AI-native service firms", contact="Sunwoo Lee", backup="Mohini Tangri",
         linkedin="https://www.linkedin.com/in/lsunwoo/", status="Verified",
         message="Hi Sunwoo, Arsham from SpringBrand. An AI-native PI firm is bold, and PI lives on search. Our AI tools show where established PI firms get their traffic and which keywords you can win, at under a cent per call. Want a free breakdown of three in your market?"),
    dict(company="Billow AI Labs", subject="The keywords the Big-4 own", category="AI-native service firms", contact="Philip Moniaga", backup="Joanathan McIntosh",
         linkedin="https://www.linkedin.com/in/philipmon/", status="Check: taken from Philip's Billow post; an older profile is at /in/philipmoniaga",
         message="Hi Philip, Arsham from SpringBrand. Taking on the Big-4 comes down to being found. Our AI tools show where traditional accounting firms get their traffic and which keywords you can win, at under a cent per call. Want a free breakdown of three firms you compete with?"),
    # --- Consumer, health & creator ---
    dict(company="Snap Poker", subject="20 poker creators for Snap Poker", category="Consumer & creator", contact="Neel Gadde", backup="Dillon Mehta",
         linkedin="https://www.linkedin.com/in/neel-gadde-491880377/", status="Check: matches Neel's YC post, but the headline doesn't name Snap Poker",
         message="Hi Neel, Arsham from SpringBrand. A social network for online poker is so fun. Our AI tools find poker creators with 20K–100K followers on TikTok, YouTube and X, at under a cent per call. Want a free list of 20 who'd be a great fit for Snap Poker?"),
    dict(company="Lumeria", subject="20 skincare creators for Lumeria", category="Consumer & creator", contact="Anthea Guo", backup="Maryanne Alhallak",
         linkedin="https://www.linkedin.com/in/anthea-guo/", status="Verified",
         message="Hi Anthea, Arsham from SpringBrand. An Oura Ring for skin is such a great pitch. Our AI tools find skincare creators with 20K–100K followers and turn product shots into short ads, at under a cent per call. Want a free list of 20 creators who fit Lumeria?"),
    dict(company="Audora", subject="BookTok, meet Audora", category="Consumer & creator", contact="Dhanush R.", backup="",
         linkedin="https://www.linkedin.com/in/dhanushrv/", status="Verified",
         message="Hi Dhanush, Arsham from SpringBrand. A unique voice per character is a lovely idea, and BookTok is made for it. Our AI tools find book creators and make short video ads with voiceover, at under a cent per call. Want a free list of 20 BookTok creators?"),
    dict(company="Tsenta", subject="20 career creators for Tsenta", category="Consumer & creator", contact="Agnay Srivastava", backup="Pulkit Gupta",
         linkedin="https://www.linkedin.com/in/agnay/", status="Verified",
         message="Hi Agnay, Arsham from SpringBrand. An agent that finds jobs and applies for you will spread fast. Our AI tools find career creators with 20K–100K followers on TikTok and LinkedIn, at under a cent per call. Want a free list of 20 who'd be a great fit for Tsenta?"),
]


def main():
    over = [(l["company"], len(l["message"])) for l in LEADS if len(l["message"]) > LIMIT]
    assert all(len(l["subject"]) <= 60 for l in LEADS), "subject too long"
    assert not over, f"messages over {LIMIT} chars: {over}"
    L = ["# LinkedIn outreach: day 1 (20 companies)", "",
         f"One message per contact, each at most {LIMIT} characters. Send it as the connection note "
         "(fits LinkedIn Premium's 300-character limit), or as a DM if you're already connected. "
         "Free accounts are limited to 200 characters per note, so on a free account send a blank invite "
         "and paste the message as a DM once they accept.", "",
         "**Subjects** show only where LinkedIn has a subject field: InMail and Sales Navigator messages. "
         "Connection notes and regular DMs have none, so there you can open the message with the subject line instead.", "",
         "**How to run it:** send the 20 today. If there's no reply after 4–5 days, like or comment on one of their posts, "
         "then send one short nudge: \"Hi {name}, just bumping this. Happy to send the free sample whenever it's useful.\" "
         "Log everything in the tracker CSV.", "",
         "**Profiles:** ones marked *Check* were matched indirectly, so glance at the profile before sending. "
         "If a link is wrong, search LinkedIn for the name plus the company, or try the backup founder.", ""]
    cat = None
    for i, l in enumerate(LEADS, 1):
        if l["category"] != cat:
            cat = l["category"]; L += [f"## {cat}", ""]
        L += [f"### {i}. {l['company']}: {l['contact']}", "",
              f"**LinkedIn:** {l['linkedin']} ({l['status']})" + (f" · backup: {l['backup']}" if l["backup"] else ""), "",
              f"**Subject:** {l['subject']}", "",
              f"**Message** ({len(l['message'])} chars):", "", "> " + l["message"], ""]
    (ROOT / "docs/linkedin-outreach-day-1.md").write_text("\n".join(L))
    with open(ROOT / "private/linkedin-tracker.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["#", "Company", "Category", "Contact", "LinkedIn profile", "Profile status", "Backup contact",
                    "Subject", "Message", "Characters", "Sent", "Accepted", "Replied", "Next step"])
        for i, l in enumerate(LEADS, 1):
            w.writerow([i, l["company"], l["category"], l["contact"], l["linkedin"], l["status"], l["backup"],
                        l["subject"], l["message"], len(l["message"]), "", "", "", ""])
    lens = sorted(len(l["message"]) for l in LEADS)
    print(len(LEADS), f"messages; {lens[0]}-{lens[-1]} chars")


if __name__ == "__main__":
    main()
