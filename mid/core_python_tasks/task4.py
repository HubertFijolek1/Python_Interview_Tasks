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
