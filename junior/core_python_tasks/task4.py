### 4. **Function to remove duplicates from a list while preserving order**

def remove_duplicates2(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

def remove_duplicates3(lst):
    return list(dict.fromkeys(lst))
