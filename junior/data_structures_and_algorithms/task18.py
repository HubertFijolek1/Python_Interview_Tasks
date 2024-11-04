### 18. **Function that merges two dictionaries, combining values for matching keys**

from collections import defaultdict
def merge_dicts(dict1, dict2):
    result = defaultdict(int)
    for d in (dict1, dict2):
        for key, value in d.items():
            result[key] += value
    return dict(result)

def merge_dicts2(dict1, dict2):
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}


