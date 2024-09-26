import unittest
from app import load_data

class TestApp(unittest.TestCase):
    def test_load_data(self):
        data = load_data()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

if __name__ == "__main__":
    unittest.main()
