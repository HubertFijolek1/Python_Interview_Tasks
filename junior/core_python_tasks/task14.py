### 14. **Function that rotates a list to the right by `n` positions**

def rotate_list(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

from collections import deque
def rotate_list2(lst, n):
    d = deque(lst)
    d.rotate(n)
    return list(d)

def rotate_list3(lst, n):
    for _ in range(n):
        lst.insert(0, lst.pop())
    return lst
