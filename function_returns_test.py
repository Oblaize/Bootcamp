from unittest import TestCase
from prime_numbers import prime_num_gen


class PrimeTestCase(TestCase):

    def test_function_returns_something(self):
        prime = prime_num_gen(5)
        self.assertIsNotNone(prime)
