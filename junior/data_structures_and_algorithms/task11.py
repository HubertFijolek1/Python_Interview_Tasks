### 11. **Function to merge two sorted lists into one sorted list without using the built-in sort function**

def merge_sorted_lists(lst1, lst2):
    result = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    return result

def merge_sorted_lists2(lst1, lst2):
    result = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))
    return result + lst1 + lst2

def merge_sorted_lists3(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1
    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge_sorted_lists3(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge_sorted_lists3(lst1, lst2[1:])

