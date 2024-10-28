### 13. **Function that finds the maximum difference between any two elements in a list**

def max_difference(lst):
    return max(lst) - min(lst)

def max_difference2(lst):
    max_diff = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            diff = abs(lst[i] - lst[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def max_difference3(lst):
    lst.sort()
    return lst[-1] - lst[0]

