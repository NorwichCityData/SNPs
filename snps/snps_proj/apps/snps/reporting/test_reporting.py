# snps python file created 30/04/2017 by fshaw

import unittest
from fpdf import Template
from .reporting import get_template, add_fields
import os
from .reporting2 import do_report


class TestReportingMethods(unittest.TestCase):
    '''
    def test_template(self):
        t = get_template()
        template = t['template']
        print(t['meta'])
        f = template.render('test.pdf')
        self.assertEquals(type(f), type(str()))

        with open('test.pdf') as pdf_file:
            self.assertTrue(pdf_file)
        #os.remove('test.pdf')
    

    def test_pdf_fields(self):
        t = get_template()
        pdf = add_fields(t['template'], dict())
        f = pdf.render('test.pdf')
        with open('test.pdf') as pdf_file:
            self.assertTrue(pdf_file)
    '''

    def test_reportlab(self):
        r = do_report()

if __name__ == '__main__':
    unittest.main()
