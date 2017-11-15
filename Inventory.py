"""

Hannah - I haven't changed your code just yet, but the multiline here is going to be what you'll need to change. Its our merged code.

If you have questions, let me know.

"""


class Item(object):
    def __init__(self, name, attack, armor, price, description):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.price = price
        self.description = description

"""
class Item(object):
    def __init__(self, name, attack, armor, price, description, location):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.used = False
        self.itemacquired = False
        self.price = price
        self.description = description
        self.location = location
"""

class Inventory(object):
    def __init__(self):
        self.stuff = {}

    def add_item(self, item):
        self.stuff[item.name] = [item.attack, item.armor, item.price, item.description]

    def print_items(self):
        for key in self.stuff:
            print(key)
