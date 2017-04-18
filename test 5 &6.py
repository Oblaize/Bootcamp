def test_correct_output(self):
        self.assertEqual(prime_num_gen(5), [2,3,5])

def test_correct_output_input_is_zero(self):
        "should return an empty list"
        self.assertEqual(prime_num_gen(0), [])
