import timeit
import random

from maxsubarray import max_subarray_brute_force, max_subarray_kadane

# Sizes of array list A
sizes = [10, 50, 100, 250, 500]

# Number of iterations for timing
num_iter = 100

# Results dictionary
results = {'brute': {}, 'kadane': {}}

# Iterate over sizes
for size in sizes:
    # Generate random array list A
    A = [random.randint(-100, 100) for _ in range(size)]

    # Time brute force algorithm
    start_time = timeit.default_timer()
    for _ in range(num_iter):
        max_subarray_brute_force(A)
    end_time = timeit.default_timer()
    results['brute'][size] = end_time - start_time

    # Time Kadane's algorithm
    start_time = timeit.default_timer()
    for _ in range(num_iter):
        max_subarray_kadane(A)
    end_time = timeit.default_timer()
    results['kadane'][size] = end_time - start_time

    
# Print results
print("No. of iterations for timing:",num_iter)
print("Results (time in seconds):")
print("Size\tBrute force\tKadane")
for size in sizes:
print("{}\t{:.6f}\t{:.6f}".format(size, results['brute'][size], results['kadane'][size]))
