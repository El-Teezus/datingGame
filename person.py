
class Person:
    """
    person object. we use this so that we can have people who talk to other people and so that shit can happen.
    """
    def __init__(self, desc, dialog, location, name):
        self.desc = desc
        self.dialog = dialog
        self.location = location
        self.name = name
        self.talkedTo = False

