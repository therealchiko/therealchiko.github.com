"""Render the editable CV to a two-page, text-selectable PDF.

Run with a Python environment containing reportlab:
    python3 career/wholechain/render_cv.py
"""
from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('cv.md')
OUTPUT = ROOT / 'output/pdf/Chiko_Mukwenha_CV_Wholechain.pdf'
FONT_DIR = Path('/System/Library/Fonts/Supplemental')
for name, filename in [('Arial', 'Arial.ttf'), ('Arial-Bold', 'Arial Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='Arial-Bold')
ink = colors.HexColor('#202B29')
muted = colors.HexColor('#4A5753')
accent = colors.HexColor('#176354')
styles = {
    'name': ParagraphStyle('name', fontName='Arial-Bold', fontSize=27, leading=32, textColor=ink, spaceAfter=7),
    'tagline': ParagraphStyle('tagline', fontName='Arial-Bold', fontSize=11, leading=15, textColor=accent, spaceAfter=8),
    'contact': ParagraphStyle('contact', fontName='Arial', fontSize=9, leading=13, textColor=muted),
    'section': ParagraphStyle('section', fontName='Arial-Bold', fontSize=9, leading=13, textColor=accent, spaceBefore=15, spaceAfter=7, keepWithNext=True),
    'role': ParagraphStyle('role', fontName='Arial-Bold', fontSize=10.3, leading=14, textColor=ink, spaceBefore=8, spaceAfter=5, keepWithNext=True),
    'body': ParagraphStyle('body', fontName='Arial', fontSize=9.5, leading=13.5, textColor=ink, spaceAfter=5, alignment=TA_LEFT),
    'bullet': ParagraphStyle('bullet', fontName='Arial', fontSize=9.5, leading=13.5, textColor=ink, leftIndent=10, firstLineIndent=-8, spaceAfter=4),
}

def markup(text):
    text = escape(text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    contacts = {
        'hi@chikomukwenha.co': 'mailto:hi@chikomukwenha.co',
        'github.com/chikomukwenha': 'https://github.com/chikomukwenha',
        'linkedin.com/in/chikomukwenha': 'https://linkedin.com/in/chikomukwenha',
        'chikomukwenha.co': 'https://chikomukwenha.co',
    }
    return ' | '.join(
        f'<link href="{contacts[field]}">{field}</link>' if field in contacts else field
        for field in text.split(' | ')
    )


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#D8DFDC'))
    canvas.line(48, 42, A4[0] - 48, 42)
    canvas.setFont('Arial', 8)
    canvas.setFillColor(muted)
    canvas.drawString(48, 28, 'CHIKO MUKWENHA')
    canvas.drawRightString(A4[0] - 48, 28, str(doc.page))
    if doc.page > 1:
        canvas.setFont('Arial-Bold', 10)
        canvas.drawString(48, A4[1] - 35, 'Chiko Mukwenha')
    canvas.restoreState()


def build():
    lines = SOURCE.read_text().splitlines()
    story = []
    in_header = True
    header_count = 0
    for line in lines:
        if not line.strip():
            continue
        if line == '<!-- pagebreak -->':
            story.append(PageBreak())
        elif line.startswith('# '):
            story.append(Paragraph(markup(line[2:]), styles['name']))
        elif line.startswith('## '):
            in_header = False
            story.append(Paragraph(markup(line[3:]).upper(), styles['section']))
        elif line.startswith('### '):
            story.append(Paragraph(markup(line[4:]), styles['role']))
        elif line.startswith('- '):
            story.append(Paragraph('&#8226; ' + markup(line[2:]), styles['bullet']))
        elif in_header:
            style = 'tagline' if header_count == 0 else 'contact'
            story.append(Paragraph(markup(line), styles[style]))
            header_count += 1
        else:
            story.append(Paragraph(markup(line), styles['body']))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=48, leftMargin=48,
                           topMargin=48, bottomMargin=57, title='Chiko Mukwenha | React & Product Engineering',
                           author='Chiko Mukwenha')
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)

if __name__ == '__main__':
    build()
