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



