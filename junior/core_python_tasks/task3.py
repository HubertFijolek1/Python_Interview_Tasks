### 3. **Script to count lines, words, and characters in a file**

def count_file_content(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        words = sum(len(line.split()) for line in lines)
        characters = sum(len(line) for line in lines)
    return len(lines), words, characters

def count_file_content2(filename):
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        return len(lines), len(words), len(content)

from collections import Counter
def count_file_content3(filename):
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        word_count = Counter(content.split())
    return len(lines), len(word_count), len(content)

