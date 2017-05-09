# snps python file created 30/04/2017 by fshaw
from fpdf import Template
from fpdf import FPDF

elements = [

    {'name': 'case_id', 'type': 'T', 'x1': 10, 'y1': 10, 'x2': 20, 'y2': 20, 'font': 'Arial',
     'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '',
     'priority': 2, },
    {'name': 'box', 'type': 'B', 'x1': 15.0, 'y1': 15.0, 'x2': 185.0, 'y2': 260.0, 'font': 'Arial', 'size': 0.0,
     'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None,
     'priority': 0, },
    {'name': 'box_x', 'type': 'B', 'x1': 95.0, 'y1': 15.0, 'x2': 105.0, 'y2': 25.0, 'font': 'Arial', 'size': 0.0,
     'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None,
     'priority': 2, },
    {'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 25.0, 'x2': 100.0, 'y2': 57.0, 'font': 'Arial', 'size': 0,
     'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None,
     'priority': 3, },
    {'name': 'barcode', 'type': 'BC', 'x1': 20.0, 'y1': 246.5, 'x2': 140.0, 'y2': 254.0, 'font': 'Interleaved 2of5 NT',
     'size': 0.75, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
     'text': '200000000001000159053338016581200810081', 'priority': 3, },
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

    return template
