def test_input_list_raise_error(self):
        with self.assertRaises(TypeError):
            prime_num_gen([4, "yay"])