from functions_to_test import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-2, 2), 0)
        self.assertEqual(Calculator.add(-2, -2), -4)
        self.assertRaises(TypeError, Calculator.add, '2', 3)
        self.assertRaises(TypeError, Calculator.add, 2, '3')

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(2, 3), -1)
        self.assertEqual(Calculator.subtract(-2, 3), -5)
        self.assertEqual(Calculator.subtract(-2, -3), 1)
        self.assertRaises(TypeError, Calculator.subtract, '2', 3)
        self.assertRaises(TypeError, Calculator.subtract, 2, '3')
        self.assertRaises(TypeError, Calculator.subtract, '2', '3')

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertEqual(Calculator.multiply(-2, 3), -6)
        self.assertEqual(Calculator.multiply(-2, -3), 6)
        self.assertEqual(Calculator.multiply(0, 3), 0)
        self.assertRaises(TypeError, Calculator.multiply, '2', '3')

    def test_divide(self):
        self.assertEqual(Calculator.divide(6, 3), 2)
        self.assertEqual(Calculator.divide(6, -3), -2)
        self.assertEqual(Calculator.divide(-6, -3), 2)
        self.assertRaises(ValueError, Calculator.divide, 5, 0)
        self.assertRaises(ValueError, Calculator.divide, '5', 0)
        self.assertRaises(TypeError, Calculator.divide, '6', 2)
        self.assertRaises(TypeError, Calculator.divide, 6, '2')
        self.assertRaises(TypeError, Calculator.divide, '6', '2')


if __name__ == '__main__':
    unittest.main()
