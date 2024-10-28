### 12. **Function that converts a list of integers to a list of their squares**

def square_numbers(lst):
    return [x ** 2 for x in lst]

def square_numbers2(lst):
    return list(map(lambda x: x ** 2, lst))

def square_numbers3(lst):
    result = []
    for num in lst:
        result.append(num ** 2)
    return result

