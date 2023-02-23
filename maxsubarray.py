def max_subarray_brute_force(A):
    n = len(A)
    maxsum = A[0]
    for i in range(n):
        for j in range(i, n):
            total = sum(A[i:j+1])
            if total > maxsum:
                maxsum = total
    return maxsum

def max_subarray_kadane(A):
    max_end_here = max_far_end = A[0]
    for x in A[1:]:
        max_end_here = max(x, max_end_here + x)
        max_far_end = max(max_far_end, max_end_here)
    return max_far_end

A=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Max sub array using Brute Froce: ",max_subarray_brute_force(A))
print("Max sub array using Kadane Froce: ",max_subarray_kadane(A))