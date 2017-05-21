# snps python file created 20/05/2017 by fshaw

from reportlab.pdfgen import canvas
import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
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

    story = []
    story.append(Paragraph("Case: xx704", styles["Normal"]))
    story.append(Paragraph("Test Report", styles["red_title"]))
    story.append(Paragraph("Results of DNA Analysis", styles["red_title"]))

    elements = []

    p = Paragraph('Nkaarco<br/> Diagnostic<br/> Testing Services.', styles['Normal'])

    data = [["Case Number", "XX704"],

            ["Company Name", "Nkaarco Diagnostic Testing Services."],
            ["", "Norwich Research Park, Colney Lane, Norwich, Norfolk,"],
            ["", "NR4 7UH"],

            ["Client", "INNA U"],

            ["Test", "Vitimins and Antioxidants Test"],

            ["Date of receipt of items", ""]
    ]
    t = Table(data)
    t.setStyle(
        TableStyle([('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                    ('VALIGN', (0, 0), (1, -0), 'TOP'),])
    )

    # story.append(Paragraph("Case Number", styles["Normal"]))

    # story.append(Spacer(height=0, width=4 * cm))

    # story.append(Paragraph("Case Number", styles["Normal"]))
    story.append(t)
    doc.build(story)
