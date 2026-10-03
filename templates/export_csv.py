"""Export the categorized company list as CSV.

Writes private/yc-s2026-categorized-companies.csv (with founder contacts,
git-ignored) and data/yc-s2026-categorized.csv (no contact details).
Run after render.py so contacts match the mail-merge file.
"""
import csv, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAY = {
    "Ads and SEO": "Competitor keyword gaps and where rivals get their traffic",
    "Social Media": "Listening on X, Reddit and TikTok; trends into posts; creators",
    "Creative Content": "UGC ad concepts, 15-second video, voiceover",
    "E-commerce": "Pricing vs. competitors, conversion drops, product copy",
    "Sales and CRM": "Target companies and decision-makers into the CRM; stalled-deal follow-ups",
    "Customer Support": "Inbox and DM triage, common replies, weekly complaint summary",
}
FIT_ORDER = {"High": 0, "Medium": 1, "Low": 2}
PRIVATE = ("Contact first name", "Contact email", "Other founders")

companies = json.load(open(ROOT / "private/companies.json"))
merge = {r["CompanyKey"]: r for r in csv.DictReader(open(ROOT / "private/mail-merge.csv"))}
companies.sort(key=lambda o: (o["Segment"] == "Needs review", o["Segment"], FIT_ORDER[o["Fit"]], o["Company"].lower()))

rows = []
for o in companies:
    m = merge.get(o["Company"], {})
    rows.append({
        "Category": o["Segment"], "Company": o["Company"], "What they do": o["Description"],
        "Website": o["URL"], "Location": o["Location"], "Fit": o["Fit"],
        "Partner candidate": "Yes" if o["Partner"] else "",
        "Lead SpringBrand scenario": o["PrimaryScenario"], "Second scenario": o["SecondaryScenario"],
        "SpringBrand play": PLAY.get(o["PrimaryScenario"], "Review manually"),
        "Email template": m.get("Template", ""), "Contact first name": m.get("FirstName", ""),
        "Contact email": m.get("Email", ""), "Other founders": m.get("OtherFounders", ""),
    })

with open(ROOT / "private/yc-s2026-categorized-companies.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
public = [k for k in rows[0] if k not in PRIVATE]
with open(ROOT / "data/yc-s2026-categorized.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=public); w.writeheader(); w.writerows({k: r[k] for k in public} for r in rows)

print(len(rows), "companies")
print(Counter(r["Category"] for r in rows))
