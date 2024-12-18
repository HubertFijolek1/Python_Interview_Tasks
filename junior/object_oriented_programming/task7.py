# Class ShoppingCart for adding, removing, viewing items, and calculating the total price

# Solution 1 (Using a list for items):

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def view_cart(self):
        return self.items

    def total_price(self):
        return sum(item['price'] for item in self.items)


#Solution 2(Using a dictionary with quantities) :

class ShoppingCart2:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def view_cart(self):
        return self.items

    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())

