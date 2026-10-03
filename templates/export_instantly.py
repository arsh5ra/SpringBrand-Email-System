"""Export leads and sequences for Instantly.

Writes (git-ignored, contains contacts):
  private/instantly/all-leads.csv           every lead, with a campaign column
  private/instantly/<campaign>.csv          one lead file per campaign
Writes (safe to commit):
  docs/instantly-sequences.md               sequence copy using Instantly variables

Instantly maps Email / First Name / Last Name / Company Name / Website /
Location / Personalization to its built-in fields; every other column
becomes a custom variable ({{tagline}}, {{target}}, {{subject_a}}, ...).
Run after render.py.
"""
import csv, json, re
from collections import Counter
from pathlib import Path
from templates import TEMPLATES, SIGNATURE, FOLLOW_UP_2
from render import TARGET, AGENT_NEED, CREATOR_NICHE, tagline

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "private/instantly"
FIT_ORDER = {"High": 0, "Medium": 1, "Low": 2}
CAMPAIGN = {
    "gtm": "01-gtm-growth-builders", "dev": "02-ai-infra-devtools", "b2b": "03-b2b-enterprise-saas",
    "smb": "04-vertical-ai-smb", "svc": "05-ai-native-services", "con": "06-consumer-health-creator",
    "deep": "07-deep-tech-hardware-bio", "partner": "08-partner-candidates",
}
# Our merge fields -> Instantly variables.
VARS = {"{first_name}": "{{firstName}}", "{company}": "{{companyName}}", "{tagline}": "{{tagline}}", "{target}": "{{target}}",
        "{agent_need}": "{{agent_need}}", "{creator_niche}": "{{creator_niche}}"}


def to_instantly(text):
    for a, b in VARS.items():
        text = text.replace(a, b)
    return text


def main():
    companies = {o["Company"].split(" (")[0]: o for o in json.load(open(ROOT / "private/companies.json"))}
    merge = list(csv.DictReader(open(ROOT / "private/mail-merge.csv")))
    OUT.mkdir(parents=True, exist_ok=True)

    leads, seen = [], set()
    for m in merge:
        email = m["Email"].strip().lower()
        if not email or email in seen:
            continue
        seen.add(email)
        o = companies[m["Company"]]
        founders = [g.groups() for g in re.finditer(r"([^;<]+?) <([^>]*)>", o["Founders"])]
        full = next((n.strip() for n, e in founders if e.lower() == email), None) or \
            next((n.strip() for n, _ in founders if n.split()[0] == m["FirstName"]), m["FirstName"])
        last = " ".join(full.split()[1:])
        leads.append({
            "Email": email, "First Name": m["FirstName"], "Last Name": last, "Company Name": m["Company"],
            "Website": o["URL"], "Location": o["Location"],
            "Personalization": f'I came across {m["Company"]} in the S26 batch ("{tagline(o["Description"])}").',
            "campaign": CAMPAIGN[m["Template"]], "category": m["Category"], "fit": m["Fit"],
            "tagline": tagline(o["Description"]), "target": TARGET.get(m["Company"], "your customers"),
            "agent_need": AGENT_NEED.get(m["Company"], ""),
            "creator_niche": CREATOR_NICHE.get(m["Company"], ""),
            "subject_a": m["Subject"], "subject_b": m["SubjectB"],
            "lead_scenario": o["PrimaryScenario"], "second_scenario": o["SecondaryScenario"],
            "other_founders": m["OtherFounders"],
        })
    leads.sort(key=lambda r: (r["campaign"], FIT_ORDER[r["fit"]], r["Company Name"].lower()))
    cols = list(leads[0])

    def write(path, rows):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)

    write(OUT / "all-leads.csv", leads)
    for key, name in CAMPAIGN.items():
        write(OUT / f"{name}.csv", [r for r in leads if r["campaign"] == name])

    # Sequence copy to paste into each Instantly campaign.
    L = ["# Instantly sequences", "",
         "One Instantly campaign per lead file in `private/instantly/`. Paste each step below into the campaign's sequence.",
         "Variables: `{{firstName}}`, `{{companyName}}` (built in), `{{tagline}}`, `{{target}}`, `{{agent_need}}`, `{{creator_niche}}`, `{{subject_a}}`, `{{subject_b}}` (custom columns in the lead file).",
         "Use subject A and B as two variants of step 1 to A/B test. Steps 2 and 3 are sent as replies in the same thread (leave their subject blank).", ""]
    for t in TEMPLATES:
        L += [f"## {CAMPAIGN[t['key']]} ({t['category']})", "",
              "**Step 1 (day 0)**, subject variant A: `{{subject_a}}`, variant B: `{{subject_b}}`", "",
              "```", to_instantly(t["email_1"]), "", SIGNATURE, "```", "",
              "**Step 2 (wait 3 days, same thread)**", "", "```", to_instantly(t["follow_up_1"]), "", SIGNATURE, "```", "",
              "**Step 3 (wait 4 more days, same thread)**", "", "```", to_instantly(t.get("follow_up_2", FOLLOW_UP_2)), "", SIGNATURE, "```", ""]
    (ROOT / "docs/instantly-sequences.md").write_text("\n".join(L))

    print(len(leads), "leads;", len(merge) - len(leads), "duplicates skipped")
    print(Counter(r["campaign"] for r in leads))


if __name__ == "__main__":
    main()
