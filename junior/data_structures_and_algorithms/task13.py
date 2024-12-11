### 13. **Function to check if a string contains only unique characters**

def has_unique_chars(s):
    return len(s) == len(set(s))

def has_unique_chars2(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            return False
        char_dict[char] = True
    return True

def has_unique_chars3(s):
    seen = []
    for char in s:
        if char in seen:
            return False
        seen.append(char)
    return True
