#10. Function to concatenate multiple text files into a single file

# Solution 1 (Using a loop and read/write):

def concatenate_files(output_file, *input_files):
    with open(output_file, 'w') as outfile:
        for fname in input_files:
            with open(fname, 'r') as infile:
                outfile.write(infile.read())

# Solution 2 (Using fileinput):

import fileinput

def concatenate_files2(output_file, *input_files):
    with open(output_file, 'w') as outfile:
        for line in fileinput.input(files=input_files):
            outfile.write(line)

