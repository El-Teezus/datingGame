"""
The person class is going to be the constructor
"""

class Person:
    """
    Person object. People are locked and tied into locations
    """
    def __init__(self, desc, dialog, location, name, formattedname):
        self.desc = desc
        self.dialog = dialog
        self.location = location
        self.name = name
        self.talkedTo = False
        self.formattedname = formattedname

alderman = Person('whats an alderman', 'i dont know what i do', 'village', 'alderman', "the alderman")
Drunkard = Person('the archetype of a father', "I've left the tavern alone. There is no one there. I have abandondeded my post. You should pay the tavern a visit.", 'village', 'drunk', "The Drunk")
Moe = Person('he serves drinks', "Say some gangster is dissing ya fly girl, you just give em one of these", 'bar', 'moe', "Moe")
personList = [alderman, Drunkard, Moe]
#Nahnym = Person("she's kind of odd", )
