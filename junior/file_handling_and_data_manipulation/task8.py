#8. Function to read a JSON file and pretty-print the data

#Solution 1 (Using `json.dumps` with `indent`):

import json
def pretty_print_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    print(json.dumps(data, indent=4))

# Solution 2 (Using pprint for formatted printing):

from pprint import pprint

def pretty_print_json2(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    pprint(data)


#Solution 3 (Manual formatting using loops):

def pretty_print_json3(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    for key, value in data.items():
        print(f"{key}: {json.dumps(value, indent=4)}")
