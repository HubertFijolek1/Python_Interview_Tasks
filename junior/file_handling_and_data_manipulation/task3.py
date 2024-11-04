### 3. **Function to rename all files in a directory by adding a suffix**

def rename_files(directory, suffix):
    for filename in os.listdir(directory):
        new_name = f"{filename}{suffix}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

import glob
import os

def rename_files2(directory, suffix):
    for filepath in glob.glob(os.path.join(directory, '*')):
        base = os.path.basename(filepath)
        new_name = f"{base}{suffix}"
        os.rename(filepath, os.path.join(directory, new_name))

from pathlib import Path
def rename_files3(directory, suffix):
    path = Path(directory)
    for file in path.iterdir():
        file.rename(file.with_name(file.name + suffix))

