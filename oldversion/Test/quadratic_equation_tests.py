import unittest
from src.quadratic_equation import QuadraticEquation

class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        #arrange
        a,b,c = 0,2,4
        #act & assert
        self.assertRaises(ValueError,QuadraticEquation,a,b,c)
    def test_raise_when_delta_larger_0(self):
        a, b, c = 1, -3, 2
        equation = QuadraticEquation(a,b,c)
        result = equation.solve()
        self.assertEqual(result,(2.0,1.0))
    def test_raise_when_delta_equal_0(self):
        a,b,c = 1, -2 ,1
        equation = QuadraticEquation(a,b,c)
        result = equation.solve()
        self.assertEqual(result, (1.0,))
    def test_raise_when_delta_less_0(self):
        a,b,c = 1, 2, 5
        equation = QuadraticEquation(a,b,c)
        result = equation.solve()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()