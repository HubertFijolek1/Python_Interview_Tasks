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
