# 5. Class implementing a simple stack with push and pop operations

# Solution 1 (Using a list):

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None
