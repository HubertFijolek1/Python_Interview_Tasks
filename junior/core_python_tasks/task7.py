### 7. **Function to find the factorial of a number

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

from functools import reduce
def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

