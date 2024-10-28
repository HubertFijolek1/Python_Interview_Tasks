### 20. **Function that counts how many times a character appears in a string**

def count_char(s, char):
    return s.count(char)

def count_char2(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

from collections import Counter
def count_char3(s, char):
    counter = Counter(s)
    return counter[char]

