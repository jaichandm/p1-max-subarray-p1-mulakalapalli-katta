import unittest
import random

from maxsubarray import max_subarray_brute_force, max_subarray_kadane

class TestMaxSubarray(unittest.TestCase):
    def test_generated_by_hand_1(self):
        A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_brute_force(A), 6)
        self.assertEqual(max_subarray_kadane(A), 6)

    def test_generated_by_hand_2(self):
        A = [-1, -2, -3, -4]
        self.assertEqual(max_subarray_brute_force(A), -1)
        self.assertEqual(max_subarray_kadane(A), -1)
        
    def test_generated_by_hand_3(self):
        A = [2,3,-2,-6, -4,-1,3,8]
        self.assertEqual(max_subarray_brute_force(A), 11)
        self.assertEqual(max_subarray_kadane(A), 11)

if __name__ == '__main__':
    unittest.main()