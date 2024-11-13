# 6. Script to list all files and subdirectories in a directory

# Solution 1 (Using `os.listdir`):

import os

def list_files_and_subdirectories(directory):
    for item in os.listdir(directory):
        print(item)


#Solution 2 ( Using `os.walk`):

def list_files_and_subdirectories2(directory):
    for root, dirs, files in os.walk(directory):
        for dir_ in dirs:
            print(f"Directory: {os.path.join(root, dir_)}")
        for file in files:
            print(f"File: {os.path.join(root, file)}")


#Solution 3(Using `Path` from `pathlib`):

from pathlib import Path

def list_files_and_subdirectories3(directory):
    path = Path(directory)
    for item in path.iterdir():
        print(item)

