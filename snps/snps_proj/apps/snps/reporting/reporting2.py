# snps python file created 20/05/2017 by fshaw

from reportlab.pdfgen import canvas
import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors


def do_report():
    doc = SimpleDocTemplate("test.pdf", pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle('red_title', parent=styles['title'], textColor=colors.red))
    styles.add(ParagraphStyle('red_subtitle', parent=styles['title'], textColor=colors.red, alignment=TA_LEFT))

    story = []
    story.append(Paragraph("Case: xx704", styles["Normal"]))
    story.append(Paragraph("Test Report", styles["red_title"]))
    story.append(Paragraph("Results of DNA Analysis", styles["red_title"]))

    elements = []

    # do table on front page of report
    data = [["Case Number", "XX704"],

            ["Company Name", "Nkaarco Diagnostic Testing Services."],
            ["", "Norwich Research Park, Colney Lane, Norwich, Norfolk,"],
            ["", "NR4 7UH"],

            ["Client", "INNA U"],

            ["Test", "Vitimins and Antioxidants Test"],

            ["Date of receipt of items", "BLANK"],
            ["Items Description", "BLANK"],
            ["Reference Sample", "BLANK"],
            ["Type of Sample", "BLANK"],
            ["Identification", "BLANK"],
            ["Data Analysis Started", "BLANK"]
            ]
    t = Table(data)
    t.setStyle(
        TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                    ('VALIGN', (0, 0), (1, -0), 'TOP'), ])
    )
    story.append(t)
    story.append(PageBreak())

    # Do copy paragraph on second page
    stitle = "Vitamins and Antioxidants"
    story.append(Paragraph(stitle, styles['red_subtitle']))

    para = "There are genetic markers associated with being predisposed to lower levels of certain nutrients, " \
           "which means you may want to make certain your diet has enough of the foods that contain these nutrients. " \
           "Ensuring you consume the right amount of vitamins and nutrients fro m your diet is an important part of " \
           "your health plan."

    story.append(Paragraph(para, styles['Normal']))

    story.append(Spacer(width=0, height=1 * cm))

    t = get_title_block()

    story.append(t)

    doc.build(story)


def get_title_block():

    # do results title block
    data = [["", "Results"]]

    t = Table(data, [2 * cm, 12 * cm], 1 * cm, hAlign='LEFT')
    t.setStyle(
        TableStyle([
            ('BOX', (0, 0), (-1, -1), 0.25, colors.blue),
            ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
            ('TEXTCOLOR', (1, 0), (1, 0), colors.red),
            ('BACKGROUND', (0, 0), (0, 0), colors.red)
        ])
    )
    return t