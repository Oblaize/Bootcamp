def test_returns_list(self):
        self.assertIsInstance(prime_num_gen(3), list)

    def test_non_int_returns_type_error(self):
        with self.assertRaises(TypeError):
            prime_num_gen('x')