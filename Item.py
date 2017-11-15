"""
Items is somewhat iffy at this point. More expansion is going to be needed.
"""
class Description:
    """
    may use description to have more interactivity. Not currently implemented, but maybe in the future it will be justified.
    """
    def __init__(self , desc):
        self.desc = desc
    def describeme(self):
        return self.desc

class Item(object):
    """
    inventory still has the same item in it. once you figure out how attack works, let me know.
    """
    def __init__(self, name, attack, armor, price, description, location):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.used = False
        self.itemacquired = False
        self.price = price
        self.description = description
        self.location = location

# class Item:
# pre merge item instance
#
#     def __init__(self, id, name, desc, location):
#         self.id = id
#         self.name = name
#         self.used = False
#         self.itemacquired = False
#         self.desc = desc
#         self.location = location


mykyffn = Item("the mykyffn", 50, 40, 39, "don't look in the box", "bar")
