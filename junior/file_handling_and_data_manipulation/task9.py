#9. Function to find and replace a word in a text file

# Solution 1 (Using str.replace):

def find_and_replace(filename, old_word, new_word):
    with open(filename, 'r') as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open(filename, 'w') as file:
        file.write(content)
