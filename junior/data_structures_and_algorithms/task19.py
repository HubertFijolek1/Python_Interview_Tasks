### 19. **Function to find the middle element of a linked list**

def find_middle(lst):
    slow, fast = 0, 0
    while fast < len(lst) - 1:
        fast += 2
        slow += 1
    return lst[slow]

def find_middle2(lst):
    return lst[len(lst) // 2]

def find_middle3(lst):
    middle = 0
    for i in range(len(lst) // 2):
        middle += 1
    return lst[middle]
