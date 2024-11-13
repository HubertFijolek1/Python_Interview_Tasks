# 6. Script to list all files and subdirectories in a directory

# Solution 1 (Using `os.listdir`):

import os

def list_files_and_subdirectories(directory):
    for item in os.listdir(directory):
        print(item)
