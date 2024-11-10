### 3. Class hierarchy with a base class `Animal` and derived classes `Dog` and `Cat`

# Solution 1 ( Simple inheritance):

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Solution 2 (Using __init__ for shared attributes):

class Animal2:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog2(Animal2):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat2(Animal2):
    def speak(self):
        return f"{self.name} says Meow!"


