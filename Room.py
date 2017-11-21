"""
The Room class uses the names of the rooms as a common link for locations and interaction objects.
Interaction Objects - People, Items, Events.
It is helpful because rooms have people in them.


We have created the rooms, the rooms go into a map.

We need to switch change locations to be the map.

"""

class Room:
    """
    constructor for a room - the common link with most items in the game insofar as interactivity.
    rooms will later get descriptions added on to them as well.
    """
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def describeme(self):
        print("You are in the " + self.name + " which is known as " + self.desc + ".")

    def describeit(self):
        return (self.describeme(), "it works")

    def presentItems(self):
        return ("Bro you can win")


class Plains(Room):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Bar(Room):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


ThePlace = Plains("plains", "It's the plains")
wayward_souls = Bar("bar", "to alcohol. the cause and solution to all of lifes problems")

class Player:
    def __init__(self, location, name):
        self.location = location
        self.name = name

def locationLoader():
    """
    loads the objects in the location into their respective spots so the player is able to easily access array's. Objects will be loaded according to type. This is to save resources.
    :return:
    """



player = Player("plains", "Hiro")

class Map:
    """
    consults the roomArray so that we can change rooms and have interactivity.
    """
    roomArray = [ThePlace, wayward_souls]
    location_synonym = [wayward_souls.name, ThePlace.name]
    def change_room(request):
        for room in Map.roomArray:
            if player.location in request:
                print("you are already there")
                break
            if room.name in request:
                print(player.location)
                player.location = room.name
                print("TEST: you are now in " + room.name + " which should be the " + player.location)





class Description:
    def __init__(self , desc):
        self.desc = desc

    def describeit(self):
        return (self.describeme(), "it works")

    def presentItems(self):
        return ("Bro you can win")



#Map.change_room("bar")
