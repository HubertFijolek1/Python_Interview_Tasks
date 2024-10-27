### 10. **Script to calculate the sum of digits of an integer**

def sum_of_digits(n):
    return sum([int(digit) for digit in str(n)])

def sum_of_digits2(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

def sum_of_digits3(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits3(n // 10)
