
class Description:
    def __init__(self , desc):
        self.desc = desc
    def describeme(self):
        return self.desc

class Item:

    def __init__(self, id, name, desc, location):
        self.id = id
        self.name = name
        self.used = False
        self.itemacquired = False
        self.desc = desc
        self.location = location


mykyffn = Item(553, "The mykyffn", "don't look in the box", "bar")
