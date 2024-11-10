# 5. Class implementing a simple stack with push and pop operations

# Solution 1 (Using a list):

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

# Solution 2 (Using a linked list for stack):

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack2:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data
