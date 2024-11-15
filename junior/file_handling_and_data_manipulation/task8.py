#8. Function to read a JSON file and pretty-print the data

#Solution 1 (Using `json.dumps` with `indent`):

import json
def pretty_print_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    print(json.dumps(data, indent=4))

