from data_model.UserInterface import UserInterface
from data_model.Guest import Guest, Reservation
from data_model.Company import Company
from data_model.Template import Template
import unittest
from unittest import mock

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        test_reservation = Reservation(123, 1234, 1234)
        guests = [Guest(1, 'first', 'last', test_reservation)]
        companies = [Company(1, 'company', 'city', 'timezone')]
        templates = [Template(1, 'test', 'test text')]
        self.ui = UserInterface(guests, companies, templates)
    
    def test_get_user_input(self):
        with mock.patch('builtins.input', return_value = "2"):
            self.assertEqual(2, self.ui._get_user_int_input("", None, 3))
        with self.assertRaises(Exception):
            with mock.patch('builtins.input', return_value = "5"):
                self.ui._get_user_int_input("", None, 3)


if __name__ == "__main__":
    unittest.main()