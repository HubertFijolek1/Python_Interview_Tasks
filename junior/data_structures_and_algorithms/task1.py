#1. Functions to check if two strings are anagrams

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

from collections import Counter
def are_anagrams2(s1, s2):
    return Counter(s1) == Counter(s2)

def are_anagrams3(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
    for char in s2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return all(v == 0 for v in count.values())
