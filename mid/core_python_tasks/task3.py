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
