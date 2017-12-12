"""
The Room class uses the names of the rooms as a common link for locations and interaction objects.
Interaction Objects - People, Items, Events.
It is helpful because rooms have people in them.


We have created the rooms, the rooms go into a map.

We need to switch change locations to be the map.

"""

import Player
import DataMaster
import person
import setpiece

class Area:
    """
    constructor for a room - the common link with most items in the game insofar as interactivity.
    rooms will later get descriptions added on to them as well.
    """
    def __init__(self, name, desc, location, formattedtext, canAccess):
        self.name = name
        self.desc = desc
        self.location = location
        self.formattedtext = formattedtext
        self.canAccess = canAccess

    def describeme(self):
        print("You are in the " + self.name + " which is known as " + self.desc + ".")

    def describeit(self):
        return (self.describeme(), "it works")



plains = Area("plains", "It's the plains", 'plains', " plains", True)
wayward_souls = Area("tavern", "to alcohol. the cause and solution to all of lifes problems", 'tavern', "tavern", True)
theVillage = Area('village', 'the village', 'village', 'village', True)
townSquare = Area('townsquare', 'important stuff happens here', 'townsquare', "town square", True)
theCastle = Area('castle', 'The King lives here.', 'castle', 'the castle', False)
theCave = Area('cave', 'I bet a dragon is in there. And maybe a really pedantic metaphor', 'cave', 'the cave', False)

def personBuilder():
    personList = []
    personString = " "
    for synonymList in DataMaster.DataMaster.object_synonyms:
            for obj in synonymList:
                if obj.location == Player.player.location:
                    if type(obj) == person.Person:
                        personList.append(obj.formattedname)
    if len(personList) == 0:
        personString = "no one was around."
    elif len(personList) == 1:
        personString = personList[0] + " was there alone."
    elif len(personList) == 2:
            personString = personList[0] + " and " + personList[1] + " were in the area."
    else:
        lastStatement = "and " + personList[-1] + " were in the area."
        del personList[-1]
        for human in personList:
            personString += human + ", "
        personString += lastStatement
    return personString

def setpieceBuilder():
    setpieceList = []
    setpieceResultString = ""
    for synonymList in DataMaster.DataMaster.object_synonyms:
        for obj in synonymList:
            if obj.location == Player.player.location:
                if type(obj) == setpiece.SetPiece:
                    setpieceList.append(obj.formattedname)
    if len(setpieceList) == 0:
            setpieceResultString = "nothing of note nearby"
    elif len(setpieceList) == 1:
            setpieceResultString = setpieceList[0] + " was the only thing of note"
    if len(setpieceList) > 2:
        endSet = " and " + setpieceList[-1] + " were nearby"
        del setpieceList[-1]
        for items in setpieceList:
            setpieceResultString += items + ", "
        setpieceResultString += endSet
    return setpieceResultString

def worldBuilder():
    """
    Linked to the check function. When the player checks the location that they are in, they are given a bit of information about what can be checked.
    :return: a string with all the things linked to a location.

    Changed to reflect the items type.
    Person. You also noticed that " " were around
    Setpiece. You saw the
    """
    peopleHere = personBuilder()
    thingsHere = setpieceBuilder()
    print("Looking around the " + Player.player.location + ", you noticed that " + peopleHere + " You also noticed that " + thingsHere + ".")







def locationLoader():
    """
    loads the objects in the location into their respective spots so the player is able to easily access array's. Objects will be loaded according to type. This is to save resources.
    :return:
    """
    # explores the objects

    # pushes to an array

    # iterates through an array

class Map:
    """
    consults the roomArray so that we can change rooms and have interactivity.
    """
    roomArray = [plains, wayward_souls, theVillage, townSquare, theCastle, theCave]
    location_synonym = [wayward_souls.name, plains.name, townSquare.name, theVillage.name, theCastle.name, theCave.name]
