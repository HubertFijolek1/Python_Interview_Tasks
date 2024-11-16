# 1. Function that takes a string and returns a dictionary with the count of each character

# Solution 1 (Using collections.Counter):
from collections import Counter

def char_count(s):
    return dict(Counter(s))

# Example:
print(char_count("hello"))

# Solution 2 (Using a dictionary with a loop):

def char_count2(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts

print(char_count2("hello"))

# Solution 3 (Using defaultdict):

from collections import defaultdict

def char_count3(s):
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1
    return dict(counts)

print(char_count3("hello"))
