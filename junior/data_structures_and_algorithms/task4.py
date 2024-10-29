### 4. **Function to find the second largest number in a list**

def second_largest(lst):
    return sorted(set(lst))[-2]

def second_largest2(lst):
    largest = second = float('-inf')
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

import heapq
def second_largest3(lst):
    return heapq.nlargest(2, set(lst))[1]
