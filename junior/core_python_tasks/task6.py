### 6. **Function to find the intersection of two lists**

def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def list_intersection2(lst1, lst2):
    return [x for x in lst1 if x in lst2]

def list_intersection3(lst1, lst2):
    return list(filter(lambda x: x in lst2, lst1))
