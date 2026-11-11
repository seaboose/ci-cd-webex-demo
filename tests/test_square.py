import unittest
from calculator import square

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(6), 36)

if __name__ == "__main__":
    unittest.main()
