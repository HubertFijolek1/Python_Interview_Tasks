### 9. **Function to generate all permutations of a given string**

from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

def string_permutations2(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i, char in enumerate(s):
        for perm in string_permutations2(s[:i] + s[i + 1:]):
            perms.append(char + perm)
    return perms

from heapq import heapify, heappop

def string_permutations3(s):
    heap = list(permutations(s))
    heapify(heap)
    return [''.join(heappop(heap)) for _ in range(len(heap))]
