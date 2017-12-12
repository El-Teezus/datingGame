"""
Data Master will hold an instance for the class

-An instance of the Information Expert GRASP Principle
-Also uses an Interface Pattern
-Interface Pattern uses the Publisher Pattern to Spread it.
-Feeds information to the Initializer, which is a Pattern Instance of Singleton

-This is circular, need to improve.
"""
import person
import Player
import setpiece

def locationVerifier(arugment):
    """
    Verification to ensure that players are in the same area as their things.
    :param arugment:
    :return:
    """
    if arugment == Player.player.location:
        return True
    else:
        print("You are not in the same area.")



class DataMaster:
    """
    Accesses the items through here, rather than directly.
    """

    item_synonym = ['sword', 'sigil', 'dagger']
    person_object_synonym = person.personList
    setpiece_synonym = setpiece.setPieceList
    object_synonyms = [person_object_synonym, setpiece_synonym]
    # LocationRegistry():
    #
    # ItemRegistry():
    #
    # PlaceRegistry():
    #
    # DateRegistry():
