"""Build docs/springbrand-email-templates.pdf from templates.py and private/mail-merge.csv."""
import csv
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from templates import TEMPLATES, PRICE_LINE, SIGNATURE, FOLLOW_UP_2

ROOT = Path(__file__).resolve().parent.parent
D = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', D + 'DejaVuSans.ttf')); pdfmetrics.registerFont(TTFont('DVB', D + 'DejaVuSans-Bold.ttf'))
addMapping('DV', 0, 0, 'DV'); addMapping('DV', 1, 0, 'DVB'); addMapping('DV', 0, 1, 'DV'); addMapping('DV', 1, 1, 'DVB')
GREEN = colors.HexColor('#2F5D50'); INK = colors.HexColor('#1F2328'); MUTED = colors.HexColor('#57606A'); TINT = colors.HexColor('#EEF4F1'); PAPER = colors.HexColor('#F6F8FA'); LINE = colors.HexColor('#D0D7DE')
st = lambda n, **k: ParagraphStyle(n, **{'fontName': 'DV', 'textColor': INK, **k})
H1 = st('h1', fontSize=22, leading=27, fontName='DVB'); H2 = st('h2', fontSize=16, leading=20, fontName='DVB', textColor=GREEN)
H3 = st('h3', fontSize=10.5, leading=13, fontName='DVB', spaceBefore=9, spaceAfter=4); B = st('b', fontSize=9.5, leading=13.5)
EM = st('em', fontSize=9, leading=12.8); SM = st('sm', fontSize=8, leading=10.5, textColor=MUTED)
W = letter[0] - 1.3 * inch

def box(text, fill=PAPER):
    html = escape(text).replace('{', '<font color="#0969DA">{').replace('}', '}</font>').replace('\n', '<br/>')
    return Table([[Paragraph(html, EM)]], colWidths=[W], style=[('BACKGROUND', (0, 0), (-1, -1), fill), ('BOX', (0, 0), (-1, -1), 0.5, LINE),
        ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10), ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)])

def footer(c, d):
    c.saveState(); c.setFont('DV', 7.5); c.setFillColor(MUTED)
    c.drawString(0.65 * inch, 0.4 * inch, 'SpringBrand: outreach email templates'); c.drawRightString(letter[0] - 0.65 * inch, 0.4 * inch, f'Page {d.page}'); c.restoreState()

merge = list(csv.DictReader(open(ROOT / 'private/mail-merge.csv')))
doc = SimpleDocTemplate(str(ROOT / 'docs/springbrand-email-templates.pdf'), pagesize=letter, leftMargin=0.65 * inch, rightMargin=0.65 * inch,
                        topMargin=0.6 * inch, bottomMargin=0.65 * inch, title='SpringBrand Outreach Email Templates', author='SpringBrand')
S = [Paragraph('SpringBrand Outreach Email Templates', H1), Spacer(1, 4),
     Paragraph('One sequence per YC S2026 category, signed by the Marketing Director. Every sequence offers free starter credits plus a sample built for the company\'s needs, and makes the core point: <b>' + PRICE_LINE + '</b>', B), Spacer(1, 8),
     Paragraph('Sequence', H3),
     Paragraph('<b>Day 0:</b> Email 1, the offer. <b>Day 3:</b> Follow-up 1 in the same thread, adding one new use case and repeating the offer. <b>Day 7:</b> Follow-up 2, the break-up email, which asks for a referral if they\'re not the right person.', B),
     Paragraph('Merge fields', H3),
     Paragraph('<font color="#0969DA">{first_name}</font> founder\'s first name · <font color="#0969DA">{company}</font> · <font color="#0969DA">{tagline}</font> the company\'s one-liner from the YC list · <font color="#0969DA">{target}</font> who they sell to (category 4) or the incumbents they compete with (category 5) · <font color="#0969DA">{sender_name}</font>. All fields are already filled for all 262 companies in the companion mail-merge CSV.', B),
     Paragraph('Writing rules', H3)]
for r in ['Under ~120 words. It\'s written to be read on a phone between meetings.',
          'Open with their company, not ours: the YC one-liner shows the email isn\'t a blast.',
          'Name the specific GTM job the category struggles with, then show SpringBrand doing it.',
          'One offer only: a free sample built for them, plus starter credits.',
          'End on a question that can be answered in one word ("Which city?", "Want them?").',
          'No invented customers, numbers or partnerships. Tool names describe capability, not integrations.',
          'Send plain text from a real inbox. Test subject lines A and B on each category.']:
    S.append(Paragraph(r, st('bl', fontSize=9.3, leading=13, leftIndent=10), bulletText='•'))
for t in TEMPLATES:
    ex = next((m for m in merge if m['Template'] == t['key'] and m['Fit'] == 'High'), next((m for m in merge if m['Template'] == t['key']), None))
    S += [PageBreak(), Paragraph(t['category'], H2), Paragraph(escape(t['angle']), SM), Spacer(1, 6),
          Paragraph('<b>Subject lines (A/B/C):</b> ' + ' · '.join(escape(s) for s in t['subjects']), B),
          Paragraph('Email 1 (day 0)', H3), box(t['email_1'].replace('{price}', PRICE_LINE) + '\n\n' + SIGNATURE),
          KeepTogether([Paragraph('Follow-up 1 (day 3, same thread)', H3), box(t['follow_up_1'] + '\n\n' + SIGNATURE)])]
    if ex:
        S.append(KeepTogether([Paragraph(f'Filled-in example: {escape(ex["Company"])}', H3), Paragraph('<b>Subject:</b> ' + escape(ex['Subject']), EM), Spacer(1, 3), box(ex['Email1'], TINT)]))
S += [PageBreak(), Paragraph('Follow-up 2: break-up email (day 7, all categories)', H2), Spacer(1, 6), box(FOLLOW_UP_2 + '\n\n' + SIGNATURE)]
doc.build(S, onFirstPage=footer, onLaterPages=footer)
