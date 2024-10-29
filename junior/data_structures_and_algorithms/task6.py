### 6. **Function to find the GCD (Greatest Common Divisor) using recursion**

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

import math
def gcd2(a, b):
    return math.gcd(a, b)

def gcd3(a, b):
    while b:
        a, b = b, a % b
    return a

