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


def tagline(desc):
    t = re.sub(r"[^\u0000-￿]", "", desc or "").strip().rstrip(".")
    t = t.split(". ")[0]  # long descriptions: first sentence only
    return t


def fill(text, **kw):
    return text.format(price=PRICE_LINE, **kw)


def render_md():
    L = ["# SpringBrand outreach email templates", "",
         "One sequence per YC S2026 category: first email, follow-up on day 3, break-up email on day 7.",
         "Sent by Arsham, Marketing Director, with a short personal intro. Offer: free starter credits plus a sample built around the company's needs.",
         "Merge fields: `{first_name}`, `{company}`, `{tagline}` (the company's one-liner from the YC list), "
         "`{target}` (categories 4 and 5).", "",
         "**Writing rules used:** under ~110 words per email, a warm one-line intro, one specific offer, one question as the call to action. "
         "Every first email makes the price point (under a cent per call, no subscription); \"one bill\" appears only where "
         "consolidating tools is the pitch (GTM builders, B2B SaaS, partners).", ""]
    for t in TEMPLATES:
        L += [f"## {t['category']}", "", f"**Angle:** {t['angle']}", "",
              "**Subject lines (A/B):** " + " · ".join(f"`{s}`" for s in t["subjects"]), "",
              "### Email 1 (day 0)", "", "```", fill(t["email_1"], first_name="{first_name}", company="{company}",
              tagline="{tagline}", target="{target}"), "", SIGNATURE, "```", "",
              "### Follow-up 1 (day 3, reply in the same thread)", "", "```", t["follow_up_1"], "", SIGNATURE, "```", ""]
    L += ["## Follow-up 2: break-up email (day 7, all categories)", "", "```", FOLLOW_UP_2, "", SIGNATURE, "```", ""]
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
            name = next((n for n, _ in founders if n.split()[0].lower() == local), founders[0][0] if founders else "")
        kw = dict(first_name=name.split()[0] if name else "there", company=o["Company"].split(" (")[0],
                  tagline=tagline(o["Description"]), target=TARGET.get(o["Company"], "your customers"),
                  sender_name=sender)
        sig = SIGNATURE.format(**kw)
        out.append({
            "Company": kw["company"], "Category": o["Segment"], "Template": key, "Fit": o["Fit"],
            "FirstName": kw["first_name"], "Email": email, "OtherFounders": "; ".join(o["Founders"].split(";")[1:]).strip(),
            "Subject": t["subjects"][0].format(**kw),
            "SubjectB": t["subjects"][1].format(**kw),
            "Email1": fill(t["email_1"], **kw) + "\n\n" + sig,
            "FollowUp1": t["follow_up_1"].format(**kw) + "\n\n" + sig,
            "FollowUp2": FOLLOW_UP_2.format(**kw) + "\n\n" + sig,
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
