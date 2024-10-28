### 19. **Function that takes a sentence and removes all punctuation**

import string
def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

def remove_punctuation2(s):
    punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    result = ""
    for char in s:
        if char not in punctuation:
            result += char
    return result

import re
def remove_punctuation3(s):
        return re.sub(r'[^\\w\\s]', '', s)
