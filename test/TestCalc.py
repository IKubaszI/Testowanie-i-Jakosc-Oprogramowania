import unittest
from src.Myoperation import Calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        print("* setUp")
        self.calc = Calc()

    def test_add(self):
        print("** test_add()")
        # Arrange
        a, b = 3, 2
        # Act
        result = self.calc.add(a, b)
        # Assert
        self.assertEqual(result, 5)

    def test_subtract(self):
        print("** test_subtract()")
        # Arrange
        a, b = 5, 3
        # Act
        result = self.calc.subtract(a, b)
        # Assert
        self.assertEqual(result, 2)

    def test_multiply(self):
        print("** test_multiply()")
        # Arrange
        a, b = 4, 3
        # Act
        result = self.calc.multiply(a, b)
        # Assert
        self.assertEqual(result, 12)

    def test_divide(self):
        print("** test_divide()")
        # Arrange
        a, b = 10, 2
        # Act
        result = self.calc.divide(a, b)
        # Assert
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        print("** test_divide_by_zero()")
        # Arrange
        a, b = 10, 0
        # Act & Assert
        with self.assertRaises(ValueError):
            self.calc.divide(a, b)

    def tearDown(self):
        print("*** tearDown()")
        self.calc = None

if __name__ == "__main__":
    unittest.main()