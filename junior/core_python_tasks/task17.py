### 17. **Function that reverses a string without using built-in reverse functions**

def reverse_string(s):
    return s[::-1]

def reverse_string2(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def reverse_string3(s):
    if len(s) == 0:
        return s
    return reverse_string3(s[1:]) + s[0]
