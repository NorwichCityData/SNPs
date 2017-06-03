# snps python file created 20/05/2017 by fshaw

from reportlab.pdfgen import canvas
import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors


def do_report():
    doc = SimpleDocTemplate("test.pdf", pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    global styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle('red_title', parent=styles['title'], textColor=colors.red))
    styles.add(ParagraphStyle('red_subtitle', parent=styles['title'], textColor=colors.red, alignment=TA_LEFT))

    global story
    story = []
    story.append(Paragraph("Case: xx704", styles["Normal"]))
    story.append(Paragraph("Test Report", styles["red_title"]))
    story.append(Paragraph("Results of DNA Analysis", styles["red_title"]))

    do_frontpage()
    story.append(PageBreak())

    do_vitamins()

    do_antioxidants()
    story.append(PageBreak())

    story.append(get_title_block("Overview - Modifications to introduce"))

    story.append(get_spacer())

    do_mods_block("increase",
                  ["Folic Acid", "Vitamin B6", "Vitamin e", "Vitamin B12", "Vitamin D", "Calcium", "Omega 3", "Fiber"])

    doc.build(story)


def do_frontpage():
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


def do_vitamins():
    # Do copy paragraph on Vitamins
    stitle = "Vitamins and Antioxidants"
    story.append(Paragraph(stitle, styles['red_subtitle']))

    para = "There are genetic markers associated with being predisposed to lower levels of certain nutrients, " \
           "which means you may want to make certain your diet has enough of the foods that contain these nutrients. " \
           "Ensuring you consume the right amount of vitamins and nutrients fro m your diet is an important part of " \
           "your health plan."

    story.append(Paragraph(para, styles['Normal']))

    story.append(get_spacer())

    t = get_title_block()
    story.append(t)
    story.append(get_spacer())

    # Do table for Vitamins and Antioxidants
    data = [['Vitamin', 'Gene', 'Variant Tested', 'Result', 'Recommended Action'],
            ['Vitamin B2', 'MTHFR', 'rs1801133', 'CT', Paragraph(
                'With your genotype, increase in homocysteine level will cause heart disease since the riboflavin level has very small effect on the homocysteine level. Healthy diet should be maintained. (1)',
                style=styles['Normal'])],
            ['Vitamin B6', 'NBPF3', 'rs4654748', 'CC', Paragraph(
                'With your genotype, the vitamin B6 level is more likely lower in blood. Maintain healthy diet and eat vitamin B6 enriched foods. (2)',
                style=styles['Normal']),
             ],
            ['...', '...', '...', '...']

            ]
    t = Table(data, colWidths=[3 * cm, 2 * cm, 3 * cm, 2 * cm, 7 * cm])
    t.setStyle(
        TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.blue),
                    ('BACKGROUND', (0, 0), (4, 0), colors.red),
                    ('TEXTCOLOR', (0, 0), (4, 0), colors.white),
                    ('TEXTCOLOR', (1, 1), (1, len(data) - 1), colors.blue),
                    ('VALIGN', (0, 0), (4, len(data) - 1), 'MIDDLE'),
                    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                    ]),

    )
    story.append(t)


def do_antioxidants():
    story.append(get_spacer())
    data = [
        ["Antioxidants", "Gene", "Variant Tested", "Result", "Recommended Action"],
        [Paragraph("WANKGA", styles['Normal']), 'GSTT1', 'indel', 'DD',
         Paragraph(
             "You have significantly reduced protection from environmental toxin. Avoid environmental pollutants such as automobile emissions and cigarette smoke which could cause skin aging and slacking.",
             styles['Normal'])],
        ['', 'GSTM1', 'indel', 'DI',
         Paragraph("Your body can sufficiently defend against substances that accelerate the skin aging.",
                   styles["Normal"])]
    ]
    t = Table(data, colWidths=[3 * cm, 2 * cm, 3 * cm, 2 * cm, 7 * cm])
    t.setStyle(
        TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.blue),
                    ('BACKGROUND', (0, 0), (4, 0), colors.red),
                    ('TEXTCOLOR', (0, 0), (4, 0), colors.white),
                    ('TEXTCOLOR', (1, 1), (1, len(data) - 1), colors.blue),
                    ('VALIGN', (0, 0), (4, len(data) - 1), 'MIDDLE'),
                    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                    ('SPAN', (0, 1), (0, -1))
                    ]),

    )

    story.append(t)


def get_title_block(header_text="Results"):
    # do results title block
    data = [["", header_text]]

    t = Table(data, [3 * cm, 13 * cm], 1 * cm, hAlign='LEFT')
    t.setStyle(
        TableStyle([
            ('BOX', (0, 0), (-1, -1), 0.25, colors.blue),
            ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
            ('TEXTCOLOR', (1, 0), (1, 0), colors.red),
            ('BACKGROUND', (0, 0), (0, 0), colors.red)
        ])
    )
    return t


def do_mods_block(left_text="increase", right_text=[]):
    # do results title block
    els = []
    for el in right_text:
        els.append(Paragraph(el, styles["Normal"]))

    lst = ListFlowable(els)

    data = [[left_text, lst]]

    t = Table(data, [3 * cm, 13 * cm], hAlign='LEFT')
    t.setStyle(
        TableStyle([
            ('BOX', (0, 0), (-1, -1), 0.25, colors.blue),
            ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
            ('TEXTCOLOR', (0, 0), (0, 0), colors.white),
            ('BACKGROUND', (0, 0), (0, 0), colors.red)
        ])
    )
    story.append(t)


def get_spacer():
    return Spacer(width=0, height=0.33 * cm)
