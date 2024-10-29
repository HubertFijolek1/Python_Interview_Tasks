### 2. **Function to return a list of even numbers**

def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def even_numbers2(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

def even_numbers3(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result
