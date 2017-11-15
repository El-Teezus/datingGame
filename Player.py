class Player:
    """
    player is going to be the protagonist. I named this me. Deal with it.
    """
   def __init__(self, location, name):
       ### location is going to be where we are starting
       ### name is going to be the protagonists name
       ### inventory is going to be the initialized inventory
        self.location = location
        self.name = name
        self.inventory = 'inventory'

LT = Player('here','LT')
