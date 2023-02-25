def max_subarray_brute_force(A):
    n = len(A)
    maxsum = A[0]
    for i in range(n):
        for j in range(i, n):
            total = sum(A[i:j+1])
            if total > maxsum:
                maxsum = total
    return maxsum