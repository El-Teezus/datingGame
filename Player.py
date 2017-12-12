class Protagonist:
    """
    player is going to be the protagonist. Has lots of changing locations.
    """

    def __init__(self, location, name):
       ### location is going to be where we are starting
       ### name is going to be the protagonists name
       ### inventory is going to be the initialized inventory
        self.location = location
        self.name = name
        self.inventory = 'inventory'
        self.day = 'day1'
        self.state = 'undecided'

player = Protagonist("village", "Hiro")
