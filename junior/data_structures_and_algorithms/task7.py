### 7. **Implement binary search in Python**

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search2(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:ś
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search2(arr, target, mid + 1, high)
    else:
        return binary_search2(arr, target, low, mid - 1)

import bisect
def binary_search3(arr, target):
    idx = bisect.bisect_left(arr, target)
    if idx != len(arr) and arr[idx] == target:
        return idx
    return -1
