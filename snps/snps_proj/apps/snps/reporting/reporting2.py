# snps python file created 20/05/2017 by fshaw

from reportlab.pdfgen import canvas
import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import red

def do_report():
    doc = SimpleDocTemplate("test.pdf", pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle('red_title', parent=styles['title'], textColor=red))

    story = []
    story.append(Paragraph("Case: xx704", styles["Normal"]))
    story.append(Paragraph("Test Report", styles["red_title"]))
    print(styles["Title"])
    story.append(Paragraph("Results of DNA Analysis", styles["red_title"]))
    doc.build(story)