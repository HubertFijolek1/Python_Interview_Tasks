# 4. Function to flatten a nested list


# Solution 1 (Using recursion):
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

# Example:
print(flatten([[1, 2, [3]], 4]))

# Solution 2 (Using a stack):

def flatten2(lst):
    flat_list = []
    stack = list(lst)
    while stack:
        item = stack.pop(0)
        if isinstance(item, list):
            stack = item + stack
        else:
            flat_list.append(item)
    return flat_list
