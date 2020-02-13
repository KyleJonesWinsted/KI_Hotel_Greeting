import unittest
from data_model.DataController import DataController, FileException

class TestDataController(unittest.TestCase):
    
    def setUp(self):
        self.db = DataController()

    def test_set_file_path(self):
        self.db.set_file_path('test', './test')
        self.assertEqual(self.db.file_paths['test'], './test')

    def test_get_file_path(self):
        self.db.set_file_path('test', './test')
        self.assertEqual(self.db._get_file_path('test'), './test')
        with self.assertRaises(FileException):
            self.db._get_file_path('test2')

if __name__ == "__main__":
    unittest.main()