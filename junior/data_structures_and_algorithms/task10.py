### 10. **Function to calculate the sum of all elements in a nested list**

def sum_nested_list(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += sum_nested_list(item)
        else:
            total += item
    return total

def sum_nested_list2(nested_list):
    return sum(sum_nested_list(item) if isinstance(item, list) else item for item in nested_list)

def sum_nested_list3(nested_list):
    stack = list(nested_list)
    total = 0
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            total += item
    return total
