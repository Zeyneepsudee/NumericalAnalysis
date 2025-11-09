import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError("m cannot be greater than n.")
    if d <= 0:
        raise ValueError("d must be positive.")
    if n <= 0:
        raise ValueError("n must be positive.")
    if m < 0:
        raise ValueError("m cannot be negative.")

    low, high = 10**(d - 1), 10**d   # tam d basamak
    arr = np.random.randint(low, high, size=(n, n))

    start = (n - m) // 2
    end = start + m
    if m > 0:
        arr[start:end, start:end] = -1

    return arr
