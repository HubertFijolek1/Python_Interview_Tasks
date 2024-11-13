### 5. Script to extract lines from a log file containing a specific keyword

#Solution 1(Using a loop and ` in `):

def extract_lines_with_keyword(filename, keyword):
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                print(line.strip())
