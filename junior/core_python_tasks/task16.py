### 16. **Function that takes a list of strings and returns the longest string**

def longest_string(lst):
    return max(lst, key=len)

def longest_string2(lst):
    longest = ""
    for s in lst:
        if len(s) > len(longest):
            longest = s
    return longest

from functools import reduce
def longest_string3(lst):
    return reduce(lambda a, b: a if len(a) > len(b) else b, lst)
