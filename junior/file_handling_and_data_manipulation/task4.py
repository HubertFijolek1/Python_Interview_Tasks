### 4. Function to read a file and count the frequency of each word

#Solution 1 (Using collections.Counter)

from collections import Counter
def count_word_frequency(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return Counter(words)



