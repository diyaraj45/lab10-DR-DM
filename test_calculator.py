import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(8, 5), 3)
        self.assertEqual(subtract(5, 0), 5)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        pass

    def test_divide(self): # 3 assertions
        pass
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertEqual(div(5, 0), 0)
        self.assertRaises(ZeroDivisionError, div, 0, 0)
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(math.log(4, 4), 1)
        self.assertEqual(math.log(8, 2), 3)
        self.assertEqual(math.log(100, 10), 2)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, math.log ,2, 0)
        # use same technique from test_divide_by_zero
    ##########################

    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        pass

    def test_hypotenuse(self): # 3 assertions
        pass

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        pass
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()