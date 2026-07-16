import unittest
from lesson_12.homework_12 import *

class FuncUnitTests(unittest.TestCase):
    def test_multiplication_five(self):
        expected_result = ['5x1=5', '5x2=10', '5x3=15', '5x4=20', '5x5=25']
        actual_result = multiplication_table(5)
        self.assertEqual(expected_result, actual_result)

    def test_multiplication_more_25(self):
        expected_result = []
        actual_result = multiplication_table(30)
        self.assertEqual(expected_result, actual_result)

    def test_multiplication_negative_number(self):
        expected_error_message = "Number must be greater than 0"
        # expected_error_message = "Number must be positive"
        with self.assertRaises(ValueError) as context:
            multiplication_table(-5)
        exception = context.exception
        actual_error_message = exception.args[0]
        self.assertEqual(expected_error_message, actual_error_message, "Unexpected error")

    def test_average_of_numbers_success(self):
        expected_result = 3.0
        actual_result = average_of_numbers([1,2,3,4,5])
        self.assertEqual(expected_result, actual_result)

    def test_average_of_numbers_zero(self):
        expected_error_message = "List is empty"
        with self.assertRaises(ValueError) as context:
            average_of_numbers([])
        exception = context.exception
        actual_error_message = exception.args[0]
        self.assertEqual(expected_error_message, actual_error_message, "Unexpected error")

    def test_func_computer_price_positive_numbers(self):
        self.assertEqual(func_computer_price(1000, 12), 12000)

    def test_func_computer_price_zero_payment(self):
        self.assertEqual(func_computer_price(0, 12), 0)

    def test_func_computer_price_zero_months(self):
        self.assertEqual(func_computer_price(1000, 0), 0)

    def test_func_computer_price_float_values(self):
        self.assertAlmostEqual(func_computer_price(99.99, 12), 1199.88, places=2)

    def test_func_sum_array_numbers_success(self):
        array_list = [
            ("1,2,3,4", 10),
            ("1,2,3,4,50", 60),
            ("1,2,3", 6)
        ]

        for input_data, expected_result in array_list:
            self.assertEqual(func_sum_array_numbers(input_data), expected_result)

    def test_func_sum_array_numbers_failed(self):
        array_list_negative = ["1,2,3,4abc", "1,2,abc,4,50", "qwerty1,2,3"]

        for input_data in array_list_negative:
                self.assertEqual(func_sum_array_numbers(input_data), "Can't do this - not only numbers here!")


if __name__ == '__main__':
    unittest.main(verbosity=2)

