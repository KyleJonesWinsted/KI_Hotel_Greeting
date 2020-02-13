import unittest
from data_model.Template import Template
from data_model.Guest import Guest, Reservation
from data_model.Company import Company

class TestTemplate(unittest.TestCase):
    
    def setUp(self):
        self.template = Template(1, 'test template', 'this is a test [firstName] [lastName] [companyName] [roomNumber]')

    def test_render_template_string(self):
        test_reservation = Reservation(123, 12345678, 12345678)
        test_guest = Guest(1, 'first', 'last', test_reservation)
        test_company = Company(1, 'company', 'city', 'timezone')
        test_greeting = self.template.render_template_string(test_guest, test_company)
        self.assertEqual(test_greeting, 'this is a test first last company 123')

    def test_serialize(self):
        serial_template = self.template.serialize()
        self.assertEqual(serial_template, {
            "id": 1,
            "shortName": "test template",
            "templateText": 'this is a test [firstName] [lastName] [companyName] [roomNumber]'
        })

if __name__ == "__main__":
    unittest.main()