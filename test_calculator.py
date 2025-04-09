import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        pass

    def test_subtract(self): # 3 assertions
        pass
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(-4, 2), 0)
        self.assertNotEqual(divide(4, 0), 0)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        pass

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        self.assertRaises(ValueError, logarithm, 0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertNotEqual(hypotenuse(5, 4), 5)
        self.assertNotEqual(hypotenuse(-4, 5), 5)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)
        self.assertRaises(ValueError, square_root, -3)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()