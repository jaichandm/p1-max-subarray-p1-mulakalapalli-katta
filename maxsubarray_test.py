import unittest
import random


class TestMaxSubarray(unittest.TestCase):
    def generated_hand_test_1(self):
        A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_brute_force(A), 6)
        self.assertEqual(max_subarray_kadane(A), 6)

    def generated_hand_test_2(self):
        A = [-1, -2, -3, -4]
        self.assertEqual(max_subarray_brute_force(A), -1)
        self.assertEqual(max_subarray_kadane(A), -1)

    def test_randomized(self):
        A = [random.randint(-100, 100) for _ in range(100)]
        self.assertEqual(max_subarray_brute_force(A), max_subarray_kadane(A))

if _name_ == '_main_':
    unittest.main()
