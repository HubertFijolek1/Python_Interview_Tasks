### 14. **Function to remove the nth element from a list**

def remove_nth_element(lst, n):
    del lst[n]
    return lst

def remove_nth_element2(lst, n):
    return lst[:n] + lst[n + 1:]

def remove_nth_element3(lst, n):
    lst.pop(n)
    return lst