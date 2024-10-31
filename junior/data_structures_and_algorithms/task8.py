### 8. **Function to return the first non-repeating character in a string**

def first_non_repeating_char(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in s:
        if count[char] == 1:
            return char
    return None

from collections import Counter
def first_non_repeating_char2(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

def first_non_repeating_char3(s):
    unique = []
    repeating = set()
    for char in s:
        if char in repeating:
            continue
        if char in unique:
            unique.remove(char)
            repeating.add(char)
        else:
            unique.append(char)
    return unique[0] if unique else None
