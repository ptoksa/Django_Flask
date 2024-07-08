# test_math_operations.py

import unittest
from math_operations import MathOperations

class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.math_ops = MathOperations()
    
    def test_calculate_sum_and_product(self):
        sum_result, product_result = self.math_ops.calculate_sum_and_product(3, 4)
        self.assertEqual(sum_result, 7)
        self.assertEqual(product_result, 12)
    
    def test_calculate_sum_and_product_negative(self):
        sum_result, product_result = self.math_ops.calculate_sum_and_product(-3, 4)
        self.assertEqual(sum_result, 1)
        self.assertEqual(product_result, -12)

if __name__ == '__main__':
    unittest.main()
