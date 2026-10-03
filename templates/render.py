"""Render the outreach templates into docs, a PDF and a per-company mail-merge CSV.

Usage: python3 templates/render.py [--sender "Full Name"]
Reads private/companies.json (git-ignored: founder contacts) and writes
docs/email-templates.md, docs/springbrand-email-templates.pdf and
private/mail-merge.csv.
"""
import argparse, csv, json, re
from pathlib import Path
from templates import TEMPLATES, PRICE_LINE, SIGNATURE, FOLLOW_UP_2

ROOT = Path(__file__).resolve().parent.parent
SEGMENT_KEY = {t["category"]: t["key"] for t in TEMPLATES}

# Category 4: who each company sells to. Category 5: the incumbents it competes with.
TARGET = {
    "Alloovium": "construction contractors", "Asteria": "online retailers", "Async": "small business owners",
    "Bernard": "appliance repair companies", "Bizmark": "consumer goods brands", "CarSignal": "auto repair shops",
    "FlowManual": "construction companies", "Luca IQ": "CPA firms", "Marble": "restaurants",
    "Pango": "e-commerce brands", "Perceptron ML": "law firms", "Rational": "accounting firms",
    "RealPact": "real estate brokerages", "Sidekick": "frontline service businesses",
    "Vestris": "title and escrow companies", "Whitespace": "wholesale distributors", "Zaplar": "hotels",
    "Axelrod": "boutique hotels", "Dream": "rental and fleet operators", "HERA": "machine shops",
    "Torus": "engineering firms",
    "Billow AI Labs": "Big-4 firms", "Donkey": "traditional sourcing agents",
    "Erinys": "traditional law firms", "Last Accounting Company": "traditional accounting firms",
    "Marker": "traditional consultancies", "Peer": "traditional freight brokers",
    "Wingman Law": "established personal injury firms", "Allia Health": "traditional behavioral health practices",
    "Atlia": "traditional property managers", "Audun": "traditional collection agencies",
    "Callbook AI": "traditional collection agencies", "Cova": "traditional home care agencies",
    "Denta": "traditional dental insurers", "Florin": "traditional insurance carriers",
    "PRINCEPS": "traditional insurers", "Radley": "traditional radiology practices", "Rex": "traditional BPOs",
    "Risklytics": "traditional insurers", "Standard Medical": "traditional primary care clinics",
    "Prescience, Inc.": "traditional healthcare providers",
}

# Partner campaign: the moment an agent would reach for each company's product.
AGENT_NEED = {
    "Agentcard": "needs to pay for something", "Amorphic Labs": "needs to buy or sell software",
    "Click": "needs deep research done", "Context.dev": "needs live web context",
    "Executor": "needs a new integration", "Financial Datasets": "needs live market data",
    "Inkbox": "needs to email, text or call someone", "Magma": "needs high-quality trace data",
    "Praxis Robotics": "needs company data", "Rindler": "needs to act on a website",
    "Speko": "needs speech or a voice model",
}

# Category 6: the creator niche each consumer company should work with.
CREATOR_NICHE = {
    "Audora": "BookTok", "Gutgutgoose": "gut-health", "Illume Labs": "longevity and health", "Instaplay": "gaming",
    "Lumeria": "skincare", "MOCHI.TV": "anime", "OpenTrade": "investing", "PokerClubHub": "poker",
    "RonanRx Inc.": "biohacking", "Roster": "prediction-market", "Snap Poker": "poker", "Sunflower": "sobriety",
    "tash": "trading-card", "Touchy": "AI and tech", "Tsenta": "career", "Wondering": "education",
    "Aponic": "productivity", "Arbital": "trading", "Bloomy": "parenting and education", "Egoist Machines": "AI and tech",
    "Kandor": "personal-finance", "Omanta": "health and science", "Palette": "creator-economy",
    "Paperboy Products, Inc.": "productivity",
}

# Category 2: the topic developers discuss around each devtools company.
DEV_TOPIC = {
    "Agent FM": "running multiple coding agents", "Agnost AI": "AI agent analytics", "Archal": "agent evals",
    "Buildbox": "AI agent user experience", "Bullet": "coding agents", "Conifer": "LLM token costs",
    "Dialogus": "voice agents", "Experiential Labs": "fine-tuning your own models", "GitCafe": "Git hosting for AI-written code",
    "Glen": "agent memory", "Hoplite": "autonomous software factories", "HyperProbe": "AI debugging in production",
    "Indexable": "agent sandboxes", "Jcode": "parallel coding agents", "machine0": "cloud computers for agents",
    "Mentlio": "AI coding spend", "OneCLI": "agent identity and auth", "Prized": "internal tool builders",
    "screenpipe": "screen-aware AI", "Supapool": "parallel coding agents", "Tibero": "agent optimization",
    "Understudy Labs": "moving to open-weight models", "Vendo": "letting users extend your product",
    "Akon Labs": "AI agent infrastructure", "Amulet": "agent file systems", "Belvedir": "private AI models",
    "Caution": "secure hosting", "Coasty": "computer-use agent evals", "Codag": "agent logging",
    "Computable": "GPU compute pricing", "Datoric": "secure training data", "Fabraix": "AI agent security",
    "hiloop": "recursive self-improvement", "Inner": "supply chain attacks", "Lamb Labs": "fast AI inference",
    "Markov": "computer-use training data", "Mireye": "physical-world AI agents", "Nebula Security": "AI-powered security",
    "Ooak Data": "RL environments", "OpenRelay": "distributed AI inference", "Osseus": "robotics development",
    "Paraloft": "autonomous AI agents", "SpaceFlow Technologies, Inc.": "running AI agents in production",
    "Traceforce": "on-device AI security", "Tracer": "combining open-source models",
}

# Category 1: the data each GTM product runs on (keyed by full company name).
DATA_NEED = {
    "Chromie": "contractor and company data", "Grocalo": "creator and trend data",
    "LemonLime": "lead and competitor data", "Nex": "company and contact data",
    "Osmaura": "search and traffic data on law firms", "Palisade (sales agents)": "buyer and seller lead data",
    "TryNearby": "local creator data", "Pluto": "professional and company data",
}


def start_city(location):
    """Category 4: suggest the company's own HQ city as the first free list."""
    city = (location or "").split(",")[0].replace(" QLD", "").strip()
    return {"New York City": "New York"}.get(city, city) or "your home city"


def tagline(desc):
    t = re.sub(r"[^\u0000-￿]", "", desc or "").strip().rstrip(".")
    t = t.split(". ")[0]  # long descriptions: first sentence only
    return t


def fill(text, **kw):
    return text.format(price=PRICE_LINE, **kw)


def render_md():
    L = ["# SpringBrand outreach email templates", "",
         "One sequence per YC S2026 category: first email, follow-up on day 3, break-up email on day 7.",
         "Sent by Arsham, Growth Marketing Manager, with a short personal intro. Offer: free starter credits plus a sample built around the company's needs.",
         "Merge fields: `{first_name}`, `{company}`, `{tagline}` (the company's one-liner from the YC list), "
         "`{target}` (categories 4 and 5), `{agent_need}` (partner campaign), `{creator_niche}` (category 6), `{dev_topic}` (category 2), `{data_need}` (category 1), `{start_city}` (category 4).", "",
         "**Writing rules used:** under ~110 words per email, a warm one-line intro, one specific offer, one question as the call to action. "
         "Every first email makes the price point (under a cent per call, no subscription); \"one bill\" appears only where "
         "consolidating tools is the pitch (GTM builders, B2B SaaS, partners).", ""]
    for t in TEMPLATES:
        L += [f"## {t['category']}", "", f"**Angle:** {t['angle']}", "",
              "**Subject lines (A/B):** " + " · ".join(f"`{s}`" for s in t["subjects"]), "",
              "### Email 1 (day 0)", "", "```", fill(t["email_1"], first_name="{first_name}", company="{company}",
              tagline="{tagline}", target="{target}", agent_need="{agent_need}", creator_niche="{creator_niche}", dev_topic="{dev_topic}", data_need="{data_need}", start_city="{start_city}"), "", SIGNATURE, "```", "",
              "### Follow-up 1 (day 3, reply in the same thread)", "", "```", t["follow_up_1"], "", SIGNATURE, "```", ""]
        if "follow_up_2" in t:
            L += ["### Follow-up 2 (day 7, same thread)", "", "```", t["follow_up_2"], "", SIGNATURE, "```", ""]
    L += ["## Follow-up 2: break-up email (day 7, all customer categories)", "", "```", FOLLOW_UP_2, "", SIGNATURE, "```", ""]
    (ROOT / "docs/email-templates.md").write_text("\n".join(L))


def render_csv(sender):
    rows = json.load(open(ROOT / "private/companies.json"))
    out = []
    for o in rows:
        key = "partner" if o["Partner"] else SEGMENT_KEY.get(o["Segment"])
        if not key:
            continue  # "Needs review": no description to personalise from
        t = next(x for x in TEMPLATES if x["key"] == key)
        # Prefer the company's listed contact address, greeting the founder who owns it.
        founders = [m.groups() for m in re.finditer(r"([^;<]+?) <([^>]*)>", o["Founders"])]
        email = o["CompanyEmail"].split(",")[0].strip() or (founders[0][1] if founders else "")
        name = next((n for n, e in founders if e.lower() == email.lower()), None)
        if name is None:
            local = email.split("@")[0].lower()
            name = next((n for n, _ in founders if local in [t.lower() for t in n.split()]), founders[0][0] if founders else "")
        parts = name.split()
        if parts and parts[0].lower() == "fnu" and len(parts) > 1:  # "first name unknown" placeholder
            name = " ".join(parts[1:])
        kw = dict(first_name=name.split()[0] if name else "there", company=o["Company"].split(" (")[0],
                  tagline=tagline(o["Description"]), target=TARGET.get(o["Company"], "your customers"),
                  agent_need=AGENT_NEED.get(o["Company"], "needs what you build"),
                  creator_niche=CREATOR_NICHE.get(o["Company"], "niche"),
                  dev_topic=DEV_TOPIC.get(o["Company"], "your category"),
                  data_need=DATA_NEED.get(o["Company"], "good data"),
                  start_city=start_city(o["Location"]),
                  sender_name=sender)
        sig = SIGNATURE.format(**kw)
        out.append({
            "Company": kw["company"], "CompanyKey": o["Company"], "Category": o["Segment"], "Template": key, "Fit": o["Fit"],
            "FirstName": kw["first_name"], "Email": email, "OtherFounders": "; ".join(o["Founders"].split(";")[1:]).strip(),
            "Subject": t["subjects"][0].format(**kw),
            "SubjectB": t["subjects"][1].format(**kw),
            "Email1": fill(t["email_1"], **kw) + "\n\n" + sig,
            "FollowUp1": t["follow_up_1"].format(**kw) + "\n\n" + sig,
            "FollowUp2": t.get("follow_up_2", FOLLOW_UP_2).format(**kw) + "\n\n" + sig,
        })
    order = {"High": 0, "Medium": 1, "Low": 2}
    out.sort(key=lambda r: (order[r["Fit"]], r["Category"], r["Company"].lower()))
    with open(ROOT / "private/mail-merge.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--sender", default="Arsham")
    a = ap.parse_args()
    render_md()
    rows = render_csv(a.sender)
    print(f"{len(rows)} personalised sequences written")
