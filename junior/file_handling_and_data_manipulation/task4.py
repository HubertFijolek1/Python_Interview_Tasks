### 4. Function to read a file and count the frequency of each word

#Solution 1 (Using collections.Counter)

from collections import Counter
def count_word_frequency(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return Counter(words)


#Solution 2 (Using a dictionary)

def count_word_frequency2(filename):
    word_count = {}
    with open(filename, 'r') as file:
        for word in file.read().split():
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

