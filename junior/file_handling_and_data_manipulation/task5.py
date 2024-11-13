### 5. Script to extract lines from a log file containing a specific keyword

#Solution 1(Using a loop and ` in `):

def extract_lines_with_keyword(filename, keyword):
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                print(line.strip())


#Solution 2(Using list comprehension):

def extract_lines_with_keyword2(filename, keyword):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if keyword in line]
    return lines


# Solution 3(Using `re` for keyword search):

import re

def extract_lines_with_keyword3(filename, keyword):
    with open(filename, 'r') as file:
        for line in file:
            if re.search(keyword, line):
                print(line.strip())

