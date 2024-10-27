### 8. **Program to generate the first `n` Fibonacci numbers**

def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq[:n]

def fibonacci_recursive(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    return fibonacci_recursive(n - 1) + [fibonacci_recursive(n - 1)[-1] + fibonacci_recursive(n - 2)[-1]]

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

