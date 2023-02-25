import timeit
import random

from maxsubarray import max_subarray_brute_force, max_subarray_kadane

# Sizes of array list A
sizes = [10, 50, 100, 250, 500]

# Number of iterations for timing
num_iter = 100

# Results dictionary
results = {'brute': {}, 'kadane': {}}
