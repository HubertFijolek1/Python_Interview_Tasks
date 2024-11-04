### 2. **Function to read a CSV file and print its content row by row**

import csv
def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

import pandas as pd
def read_csv2(filename):
    df = pd.read_csv(filename)
    print(df.to_string(index=False))

def read_csv3(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip().split(','))
