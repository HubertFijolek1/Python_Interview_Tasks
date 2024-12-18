#9. Function to find and replace a word in a text file

# Solution 1 (Using str.replace):

def find_and_replace(filename, old_word, new_word):
    with open(filename, 'r') as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open(filename, 'w') as file:
        file.write(content)

# Solution 2 (Using line-by-line modification):

def find_and_replace2(filename, old_word, new_word):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line.replace(old_word, new_word))

# Solution 3 (Using re.sub for regex-based replacement):

import re

def find_and_replace3(filename, old_word, new_word):
    with open(filename, 'r') as file:
        content = file.read()
    content = re.sub(rf'\\b{old_word}\\b', new_word, content)
    with open(filename, 'w') as file:
        file.write(content)
