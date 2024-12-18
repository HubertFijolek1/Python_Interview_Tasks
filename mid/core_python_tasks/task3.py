# 3. Write a decorator that logs the execution time of a function

# Solution 1 (Using time module):

import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Example:
@time_logger
def slow_function():
    time.sleep(2)

slow_function()

# Solution 2 (Using functools.wraps to preserve metadata):

from functools import wraps

def time_logger2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Solution 3 (Logging to a file):

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        with open("log.txt", "a") as f:
            f.write(f"Function {func.__name__} took {end_time - start_time:.4f} seconds\\n")
        return result
    return wrapper

