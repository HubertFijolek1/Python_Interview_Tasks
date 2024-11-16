# 1. Function that takes a string and returns a dictionary with the count of each character

# Solution 1 (Using collections.Counter):
from collections import Counter

def char_count(s):
    return dict(Counter(s))

# Example:
print(char_count("hello"))
