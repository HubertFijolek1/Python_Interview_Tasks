### 2. **Function to check if a string is a palindrome**

def is_palindrome(s):
    return s == s[::-1]

def is_palindrome2(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome3(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome3(s[1:-1])
