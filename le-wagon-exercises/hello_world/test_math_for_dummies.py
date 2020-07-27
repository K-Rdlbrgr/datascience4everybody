import unittest
from math_for_dummies import summify, multiply

class TestMathForDummies(unittest.TestCase):

    def test_summify_0_0(self):
        self.assertEqual(summify(0, 0), 0)
    
    def test_summify_2_2(self):
        self.assertEqual(summify(2, 2), 4)

    def test_summify_minus_1_2(self):
        self.assertEqual(summify(-1, 2), 1)

    def test_multiply_0_0(self):
        self.assertEqual(multiply(0, 0), 0)
    
    def test_multiply_2_2(self):
        self.assertEqual(multiply(2, 2), 4)

    def test_multiply_minus_1_2(self):
        self.assertEqual(multiply(-1, 2), -2)

if __name__ == '__main__':
    unittest.main()