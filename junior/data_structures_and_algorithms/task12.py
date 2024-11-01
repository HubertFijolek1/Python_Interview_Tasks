### 12. **Implement the selection sort algorithm**

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def selection_sort_recursive2(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    max_idx = n - 1
    for i in range(n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    arr[max_idx], arr[n - 1] = arr[n - 1], arr[max_idx]
    selection_sort_recursive2(arr, n - 1)
    return arr


def selection_sort_inplace3(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

