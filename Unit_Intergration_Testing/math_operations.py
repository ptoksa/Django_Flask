# math_operations.py

from calculator import Calculator

class MathOperations:
    def __init__(self):
        self.calculator = Calculator()
    
    def calculate_sum_and_product(self, a, b):
        sum_result = self.calculator.add(a, b)
        product_result = self.calculator.multiply(a, b)
        return sum_result, product_result
