### 15. **Function that returns the number of vowels in a string**

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_vowels2(s):
    vowels = "aeiouAEIOU"
    return sum([1 for char in s if char in vowels])

def count_vowels3(s):
    vowels = set("aeiouAEIOU")
    return len(list(filter(lambda char: char in vowels, s)))

