### 11. **Function that returns the sum of all even numbers in a list**

def sum_even_numbers(lst):
    return sum([num for num in lst if num % 2 == 0])

def sum_even_numbers2(lst):
    return sum(filter(lambda x: x % 2 == 0, lst))

def sum_even_numbers3(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total
