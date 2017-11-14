class Item(object):
    def __init__(self, name, attack, armor, price, description):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.price = price
        self.description = description

class Inventory(object):
    def __init__(self):
        self.stuff = {}

    def add_item(self, item):
        self.stuff[item.name] = [item.attack, item.armor, item.price, item.description]

    def print_items(self):
        for key in self.stuff:
            print(key)
