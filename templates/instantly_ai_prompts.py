"""Write docs/instantly-ai-prompts.md: one prompt per campaign for Instantly's AI assistant.

Each prompt carries the exact sequence copy, the per-company values for any
new custom variable (with a generic fallback), and a pre-launch checklist.
"""
import csv
from pathlib import Path
from templates import TEMPLATES, SIGNATURE, FOLLOW_UP_2
from export_instantly import CAMPAIGN, to_instantly

ROOT = Path(__file__).resolve().parent.parent
# New variable per campaign -> generic fallback wording if a value can't be set.
NEW_VAR = {
    "gtm": ("data_need", "fresh lead, traffic and social data"),
    "dev": ("dev_topic", "your space"),
    "smb": ("start_city", "your home city"),
    "con": ("creator_niche", None),
    "partner": ("dev_topic", "your space"),
}
CON_FALLBACK = [('20 {{creator_niche}} creators', '20 creators in your niche'),
                ("this week's {{creator_niche}} trends", "this week's trends in your space"),
                ('{{creator_niche}} creators with', 'creators with')]


def main():
    leads = list(csv.DictReader(open(ROOT / "private/instantly/all-leads.csv")))
    L = ["# Instantly AI prompts", "",
         "Paste one prompt per campaign into Instantly's AI assistant, inside that campaign. "
         "Each prompt is self-contained. None of them launch anything.", ""]
    for t in TEMPLATES:
        name = CAMPAIGN[t["key"]]
        rows = [r for r in leads if r["campaign"] == name]
        subj = [to_instantly(s) for s in t["subjects"][:2]]
        p = [f"You are helping me get my Instantly campaign \"{name}\" ready to launch. Do not launch or schedule it; stop when everything is ready and give me a short report of what you changed and anything you couldn't do.",
             "",
             "## 1. Sequence",
             "Replace the campaign's sequence with exactly these 3 steps. Keep the wording, line breaks and {{variables}} exactly as written. Use plain text, no images or links in step 1.",
             "",
             f"Step 1 (day 0). Subject variant A: {subj[0]} | Subject variant B: {subj[1]}",
             "Body:", "```", to_instantly(t["email_1"]), "", SIGNATURE, "```", "",
             "Step 2 (wait 3 days). Leave the subject EMPTY so it sends as a reply in the same thread.",
             "Body:", "```", to_instantly(t["follow_up_1"]), "", SIGNATURE, "```", "",
             "Step 3 (wait 4 days after step 2). Leave the subject EMPTY so it sends as a reply in the same thread.",
             "Body:", "```", to_instantly(t.get("follow_up_2", FOLLOW_UP_2)), "", SIGNATURE, "```", ""]
        used = ["firstName", "companyName"] + [v for v in ("tagline", "target", "data_need", "dev_topic", "start_city", "creator_niche", "agent_need")
                                              if "{{%s}}" % v in to_instantly(t["email_1"] + t["follow_up_1"] + t.get("follow_up_2", "") + " ".join(t["subjects"]))]
        p += ["## 2. Variables",
              "The sequence uses these variables: " + ", ".join("{{%s}}" % v for v in used) + ". "
              "firstName and companyName are built-in lead fields. The others are custom variables on each lead."]
        if t["key"] in NEW_VAR:
            var, fb = NEW_VAR[t["key"]]
            p += ["", f"The custom variable `{var}` is new, so my leads may not have it yet. Set `{var}` on each lead to the value below, matching by company name:", ""]
            p += [f"- {r['Company Name']}: {r[var]}" for r in rows]
            p += [""]
            if fb:
                p += [f"If you cannot set custom variables on leads, replace every {{{{{var}}}}} in the subjects and bodies with \"{fb}\" instead, so no email has a blank."]
            else:
                p += ["If you cannot set custom variables on leads, make these replacements in the subjects and bodies instead, so no email has a blank:"]
                p += [f"- \"{a}\" -> \"{b}\"" for a, b in CON_FALLBACK]
        p += ["", "Check every lead: if any variable used above is empty for a lead, tell me which leads and which variable. "
              "Do not send to leads with an empty tagline or target; list them for me instead.", "",
              "## 3. Settings",
              "- Open tracking: off. Link tracking: off.",
              "- Stop the sequence for a lead when they reply: on.",
              "- Sending days: Monday to Friday. Sending window: 8:00 to 11:00 in the lead's time zone if supported, otherwise 8:00 to 11:00 US Pacific.",
              "- Daily limit: no more than 30 new leads per sending inbox per day.",
              "- Text only (no HTML formatting, images or unsubscribe banners added to the body).", "",
              "## 4. Final check",
              "Preview the full sequence (all 3 steps and both subject variants) for three different leads. Confirm there are no blanks, no leftover {{...}}, and no doubled spaces. Then report back."]
        L += [f"## {name} ({t['category']}, {len(rows)} leads)", "", "````", *p, "````", ""]
    (ROOT / "docs/instantly-ai-prompts.md").write_text("\n".join(L))
    print("written")


if __name__ == "__main__":
    main()
