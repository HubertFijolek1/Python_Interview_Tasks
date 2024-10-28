### 18. **Function to check if a number is a perfect square**

import math

def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n

def is_perfect_square2(n):
    for i in range(1, n // 2 + 2):
        if i * i == n:
            return True
    return False

def is_perfect_square3(n):
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return True
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1
    return False
