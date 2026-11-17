"""Render cv.md with bundled Newsreader and Manrope fonts (requires ReportLab)."""
from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, PageBreak, Table, TableStyle, Spacer,
    HRFlowable,
)

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('cv.md')
OUTPUT = ROOT / 'output/pdf/Chiko_Mukwenha_CV_Wholechain.pdf'
FONT_DIR = Path(__file__).with_name('fonts')
for name, filename in [
    ('Manrope', 'Manrope-Regular.ttf'),
    ('Manrope-Semibold', 'Manrope-Semibold.ttf'),
    ('Newsreader', 'Newsreader-Regular.ttf'),
    ('Newsreader-Semibold', 'Newsreader-Semibold.ttf'),
]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
pdfmetrics.registerFontFamily('Manrope', normal='Manrope', bold='Manrope-Semibold')
pdfmetrics.registerFontFamily('Newsreader', normal='Newsreader', bold='Newsreader-Semibold')
INK = colors.HexColor('#202832')
MUTED = colors.HexColor('#596573')
RULE = colors.HexColor('#D7DCE1')
WIDTH = A4[0] - 96
RAIL = 77
styles = {
    'name': ParagraphStyle('name', fontName='Newsreader', fontSize=37, leading=41, textColor=INK, spaceAfter=9),
    'tagline': ParagraphStyle('tagline', fontName='Manrope-Semibold', fontSize=10, leading=14, textColor=INK, spaceAfter=8),
    'contact': ParagraphStyle('contact', fontName='Manrope', fontSize=8, leading=12, textColor=MUTED),
    'section': ParagraphStyle('section', fontName='Manrope-Semibold', fontSize=8, leading=11, textColor=MUTED, spaceAfter=9, keepWithNext=True),
    'company': ParagraphStyle('company', fontName='Manrope-Semibold', fontSize=11.5, leading=16, textColor=INK),
    'title': ParagraphStyle('title', fontName='Manrope', fontSize=9, leading=13, textColor=MUTED),
    'date': ParagraphStyle('date', fontName='Manrope', fontSize=8, leading=12, textColor=MUTED),
    'body': ParagraphStyle('body', fontName='Manrope', fontSize=9, leading=13, textColor=INK, spaceAfter=6),
    'note': ParagraphStyle('note', fontName='Manrope', fontSize=8.5, leading=12, textColor=MUTED, leftIndent=RAIL, spaceAfter=5),
    'bullet': ParagraphStyle('bullet', fontName='Manrope', fontSize=9, leading=13, textColor=INK, leftIndent=RAIL+9, firstLineIndent=-9, spaceAfter=4),
}
CONTACTS = {
    'hi@chikomukwenha.co': 'mailto:hi@chikomukwenha.co',
    'github.com/chikomukwenha': 'https://github.com/chikomukwenha',
    'linkedin.com/in/chikomukwenha': 'https://linkedin.com/in/chikomukwenha',
    'chikomukwenha.co': 'https://chikomukwenha.co',
}


def markup(text):
    text = escape(text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    return ' | '.join(
        f'<link href="{CONTACTS[field]}">{field}</link>' if field in CONTACTS else field
        for field in text.split(' | ')
    )


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.5)
    canvas.line(48, 40, A4[0] - 48, 40)
    canvas.setFont('Manrope', 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(48, 26, 'CHIKO MUKWENHA  /  FRONTEND & PRODUCT ENGINEERING')
    canvas.drawRightString(A4[0] - 48, 26, f'{doc.page} / 2')
    if doc.page > 1:
        canvas.setFont('Newsreader', 14)
        canvas.setFillColor(INK)
        canvas.drawString(48, A4[1] - 31, 'Chiko Mukwenha')
    canvas.restoreState()


def header(lines):
    left = [Paragraph(markup(lines[0][2:]), styles['name']),
            Paragraph(markup(lines[1]), styles['tagline']),
            Paragraph(markup(lines[2]), styles['contact'])]
    right = [Paragraph(markup(field), styles['contact'])
             for line in lines[3:] for field in line.split(' | ')]
    table = Table([[left, right]], colWidths=[WIDTH-180, 180], hAlign='LEFT')
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (1, 0), (1, 0), 15),
        ('TOPPADDING', (1, 0), (1, 0), 5),
    ]))
    return table


def role(line, compact=False):
    company, title, date = [part.strip() for part in line[4:].split('|')]
    table = Table([[
        Paragraph(markup(date), styles['date']),
        ([Paragraph(markup(company), styles['company']),
          Paragraph(markup(title), styles['title'])] if not compact else
         Paragraph(f'<b>{markup(company)}</b> / {markup(title)}', styles['body'])),
    ]], colWidths=[RAIL, WIDTH-RAIL], hAlign='LEFT')
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (0, 0), 2),
    ]))
    table.keepWithNext = True
    table.spaceBefore = 7
    return table


def build():
    lines = [line for line in SOURCE.read_text().splitlines() if line.strip()]
    first_section = next(i for i, line in enumerate(lines) if line.startswith('## '))
    story = [header(lines[:first_section]), Spacer(1, 13)]
    in_role = False
    compact = False
    for line in lines[first_section:]:
        if line == '<!-- pagebreak -->':
            story.append(PageBreak())
            in_role = False
        elif line.startswith('## '):
            compact = line == '## Earlier engineering experience'
            story.extend([
                Spacer(1, 10),
                HRFlowable(width='100%', thickness=0.5, color=RULE, spaceAfter=8),
                Paragraph(markup(line[3:]).upper(), styles['section']),
            ])
            in_role = False
        elif line.startswith('### '):
            story.append(role(line, compact))
            in_role = True
        elif line.startswith('- '):
            style = styles['bullet'] if in_role else styles['body']
            story.append(Paragraph('&#8226; ' + markup(line[2:]), style))
        else:
            story.append(Paragraph(markup(line), styles['note' if in_role else 'body']))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=48, leftMargin=48,
                           topMargin=48, bottomMargin=54,
                           title='Chiko Mukwenha | React & Product Engineering', author='Chiko Mukwenha')
    # A single zero-padding frame keeps paragraphs, rules, and tables on the
    # same 48-point left edge. SimpleDocTemplate's default frame padding made
    # full-width tables protrude six points past the surrounding paragraphs.
    frame = Frame(48, 54, WIDTH, A4[1] - 48 - 54,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id='CV', frames=[frame], onPage=footer))
    doc.build(story)
    print(OUTPUT)


if __name__ == '__main__':
    build()
