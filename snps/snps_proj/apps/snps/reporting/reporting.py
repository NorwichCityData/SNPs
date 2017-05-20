# snps python file created 30/04/2017 by fshaw
from fpdf import Template
from fpdf import FPDF

elements = [

    {'field_description': 'case_id, top left', 'name': 'case_id', 'type': 'T', 'x1': 20, 'y1': 10, 'x2': 20, 'y2': 20,
     'font': 'Arial',
     'size': 8.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0xbebebe, 'background': 0, 'align': 'I', 'text': '',
     'priority': 2, },
    {'field_description': 'Main Title', 'name': 'title_1', 'type': 'T', 'x1': 96, 'y1': 30, 'x2': 106, 'y2': 30,
     'font': 'Arial',
     'size': 14.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0xff0000, 'background': 0, 'align': 'I',
     'text': '',
     'priority': 2, },
    {'field_description': 'Sub Title', 'name': 'title_2', 'type': 'T', 'x1': 77, 'y1': 52, 'x2': 90, 'y2': 70,
     'font': 'Arial',
     'size': 14.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0xff0000, 'background': 0, 'align': 'I',
     'text': '',
     'priority': 2, },
    {'field_description': 'case_number_label', 'name': 'case_number_label', 'type': 'T', 'x1': 20, 'y1': 50, 'x2': 40, 'y2': 70,
     'font': 'Arial',
     'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
     'text': '',
     'priority': 2, },
    {'field_description': 'case_number', 'name': 'case_number', 'type': 'T', 'x1': 100, 'y1': 100, 'x2': 20,
     'y2': 20,
     'font': 'Arial',
     'size': 10.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
     'text': '',
     'priority': 2, },
    {'field_description': 'company_label', 'name': 'company_label', 'type': 'T', 'x1': 20, 'y1': 120, 'x2': 40,
     'y2': 130,
     'font': 'Arial',
     'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
     'text': '',
     'priority': 2, },
    {'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 25.0, 'x2': 100.0, 'y2': 57.0, 'font': 'Arial', 'size': 0,
     'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '',
     'priority': 3, },
    ]


def get_template():
    f = Template(format="A4", elements=elements,
                 title="Sample Invoice")
    f.add_page()
    els = list()
    for e in elements:
        els.append({'name': e['name'], 'type': e['type']})
    # return both the template and the fields to be used to fetch from the backend
    return {'template': f, 'meta': els}


def add_fields(template, fields):
    template['case_id'] = 'Case: xx17'
    template['title_1'] = 'Test Report'
    template['title_2'] = 'Results of DNA Analysis'
    template['case_number_label'] = 'Case Number:'
    template['case_number'] = 'xx17'  # autofill
    template['company_label'] = 'Company:'  # autofill
    template['line1'] = 'Nkaarco Diagnostic Testing Services. Norwich Research Park, Colney Lane, Norwich, Norfolk, NR4 7UH'
    return template
