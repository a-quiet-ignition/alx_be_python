import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1000, 1), 1001)
        self.assertEqual(self.calc.add(11.33, 2.42), 13.75)
        
    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(100, 0.5), 99.5)
        
    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(5, -1), -5)
        self.assertEqual(self.calc.multiply(5.2, 5), 26)
        self.assertEqual(self.calc.multiply(0, 100), 0)
       

    def test_division(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(5, -1), -5)
        self.assertEqual(self.calc.divide(5.2, 2), 2.6)
        self.assertEqual(self.calc.divide(5, 0), None)
        