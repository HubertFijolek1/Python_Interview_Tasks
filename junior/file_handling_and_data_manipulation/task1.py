### 1. **Script to copy the contents of one file to another**

import shutil
def copy_file(source, destination):
    shutil.copyfile(source, destination)

def copy_file2(source, destination):
    with open(source, 'r') as src_file:
        content = src_file.read()
    with open(destination, 'w') as dest_file:
        dest_file.write(content)

def copy_file3(source, destination):
    with open(source, 'r') as src_file, open(destination, 'w') as dest_file:
        for line in src_file:
            dest_file.write(line)