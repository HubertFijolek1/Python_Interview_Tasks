### 7. Function to write a list of dictionaries to a CSV file

#Solution 1 (Using `csv.DictWriter`):

import csv

def write_dict_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
