### 17. **Function that checks whether a string has balanced brackets**

def is_balanced(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def is_balanced2(s):
    counter = 0
    for char in s:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
            if counter < 0:
                return False
    return counter == 0

def is_balanced3(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in pairs:
            stack.append(pairs[char])
        elif not stack or char != stack.pop():
            return False
    return not stack