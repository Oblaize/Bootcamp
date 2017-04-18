from unittest import TestCase
from prime_numbers import prime_num_gen


class PrimeTestCase(TestCase):

    def test_function_returns_something(self):
        prime = prime_num_gen(5)
        self.assertIsNotNone(prime)

    def test_returns_list(self):
        self.assertIsInstance(prime_num_gen(3), list)

    def test_non_int_returns_type_error(self):
        with self.assertRaises(TypeError):
            prime_num_gen('x')

    def test_input_list_raise_error(self):
        with self.assertRaises(TypeError):
            prime_num_gen([4, "yay"])

    def test_correct_output(self):
        self.assertEqual(prime_num_gen(5), [2,3,5])

    def test_correct_output_input_is_zero(self):
        "should return an empty list"
        self.assertEqual(prime_num_gen(0), [])