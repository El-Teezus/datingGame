class Room:
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
wayward_souls = Bar("bar", "go get ")

class Player:
    def __init__(self, location, name):
        self.location = location
        self.name = name


player = Player("plains", "Hiro")

class Map:
    roomArray = [ThePlace, wayward_souls]
    def change_room(request):
        if player.location == request:
            print("you are already there")
        for room in Map.roomArray:
            if request == room.name:
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



Map.change_room("bar")
