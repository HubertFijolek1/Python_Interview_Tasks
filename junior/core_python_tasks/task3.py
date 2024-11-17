### 3. **Script to count lines, words, and characters in a file**

def count_file_content2(filename):
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        return len(lines), len(words), len(content)
