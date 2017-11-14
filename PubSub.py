"""
Data Master will hold an instance for the class

-An instance of the Information Expert GRASP Principle
-Also uses an Interface Pattern
-Interface Pattern uses the Publisher Pattern to Spread it.
-Feeds information to the Initializer, which is a Pattern Instance of Singleton

"""

class Subscriber:
    def __init__(self, name):
        self.name = name

    def check(self):

class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)




class ItemMonitor(Subscriber):
    """
    Monitors the state of the item
    Item monitor checks the inventory.
    Returns result to the Controller
    Controller grabs information from the item like the description
    Passes description to the Player
    """
    def __init__(self, name):
        Subscriber.__init__(self)
        self.name = name
    def checkInv(self):
        ### checkInv needs item from use
        for item in Inventory.InvArray:
            if item in Inventory.InvArray == True:
                Controller.canDo = True
            else:
                Controller.canDo = False


    ### links up to the inventory
    ### if the item is there, then return true

class EventMonitor(Subscriber):
    """
    Monitors the state of the event
    """
    ### on decisions, links up to the event monitor

class LocationMonitor(Subscriber):
    """
    Monitors the state of the location
    """
    ### On decisions, will check if the player is at a certain location.

class DateMonitor(Subscriber):
    """
    Monitors whether dates have occurred.
    """

