import unittest
import random

from maxsubarray import max_subarray_brute_force

class TestMaxSubarray(unittest.TestCase):
    def generated_hand_test_1(self):
        A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_brute_force(A), 6)

    def generated_hand_test_2(self):
        A = [-1, -2, -3, -4]
        self.assertEqual(max_subarray_brute_force(A), -1)

if __name__ == '__main__':
    unittest.main()