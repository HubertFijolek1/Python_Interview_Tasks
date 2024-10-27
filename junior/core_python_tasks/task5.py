### 5. **Function to reverse words in a given sentence**

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def reverse_words2(sentence):
    return ' '.join(reversed(sentence.split()))

def reverse_words3(sentence):
    words = sentence.split()
    reversed_sentence = ''
    for word in reversed(words):
        reversed_sentence += word + ' '
    return reversed_sentence.strip()
