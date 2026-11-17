"""Render the large-type Wholechain cover letter with the CV's bundled fonts."""
from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, PageBreak

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parents[1] / 'output/pdf/Chiko_Mukwenha_Cover_Letter_Wholechain.pdf'
for name, filename in [('Manrope', 'Manrope-Regular.ttf'), ('Manrope-Semibold', 'Manrope-Semibold.ttf'),
                       ('Newsreader', 'Newsreader-Regular.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(HERE / 'fonts' / filename)))
pdfmetrics.registerFontFamily('Manrope', normal='Manrope', bold='Manrope-Semibold')
INK = colors.HexColor('#202832')
MUTED = colors.HexColor('#596573')
STYLES = {
    'name': ParagraphStyle('name', fontName='Newsreader', fontSize=32, leading=36, textColor=INK, spaceAfter=8),
    'role': ParagraphStyle('role', fontName='Manrope-Semibold', fontSize=10, leading=14, textColor=INK, spaceAfter=8),
    'contact': ParagraphStyle('contact', fontName='Manrope', fontSize=9, leading=13, textColor=MUTED, spaceAfter=22),
    'body': ParagraphStyle('body', fontName='Manrope', fontSize=14, leading=20.5, textColor=INK, spaceAfter=15),
}


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Manrope', 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(48, 28, 'CHIKO MUKWENHA / WHOLECHAIN')
    canvas.drawRightString(A4[0] - 48, 28, str(doc.page))
    if doc.page > 1:
        canvas.setFont('Newsreader', 16)
        canvas.setFillColor(INK)
        canvas.drawString(48, A4[1] - 32, 'Chiko Mukwenha')
    canvas.restoreState()


def build():
    blocks = (HERE / 'cover-letter.md').read_text().strip().split('\n\n')
    story = []
    for i, block in enumerate(blocks):
        if block == '<!-- pagebreak -->':
            story.append(PageBreak())
            continue
        if i == 0:
            story.append(Paragraph(escape(block[2:]), STYLES['name']))
        elif i == 1:
            story.append(Paragraph(escape(block), STYLES['role']))
            story.append(Paragraph(
                '<link href="mailto:hi@chikomukwenha.co">hi@chikomukwenha.co</link> / '
                '<link href="https://chikomukwenha.co">chikomukwenha.co</link>', STYLES['contact']))
        else:
            text = escape(block).replace('\n', '<br/>')
            # Keep emphasis in the same font family to retain the quiet design.
            text = re.sub(r'\*(.*?)\*', r'<b>\1</b>', text)
            story.append(Paragraph(text, STYLES['body']))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(str(OUTPUT), pagesize=A4, title='Chiko Mukwenha | Wholechain cover letter',
                          author='Chiko Mukwenha')
    frame = Frame(48, 54, A4[0] - 96, A4[1] - 48 - 54,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id='Letter', frames=[frame], onPage=footer))
    doc.build(story)
    print(OUTPUT)


if __name__ == '__main__':
    build()
