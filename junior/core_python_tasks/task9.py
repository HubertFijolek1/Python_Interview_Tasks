### 9. **Function to convert a string to title case**

def to_title_case(s):
    return s.title()

def to_title_case2(s):
    return ' '.join([word.capitalize() for word in s.split()])

def to_title_case3(s):
    return ' '.join(map(str.capitalize, s.split()))

