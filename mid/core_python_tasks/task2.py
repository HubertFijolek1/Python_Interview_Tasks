#Class-based context manager for opening and closing a file

#Solution 1 (Using __enter__ and __exit__):

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Example:
with FileManager("test.txt", "w") as file:
    file.write("Hello, world!")

# Solution 2 (Using contextlib.contextmanager):

from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Solution 3 (With error handling in __exit__):

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Error occurred: {exc_value}")
        self.file.close()


