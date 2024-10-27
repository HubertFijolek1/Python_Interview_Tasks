### 1. **Function to return the largest number in a list**
def largest_number(lst):
    return max(lst)

### Solution 2
def largest_number2(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

###Solution 3
from functools import reduce

def largest_number3(lst):
    return reduce(lambda a, b: a if a > b else b, lst)