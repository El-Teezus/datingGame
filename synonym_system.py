""""
11/15/17

The synonym engine will give the player more options so that they can be more natural in typing.

Arrays are used to access the item's within.


"""

import Item
import setpiece
import person
import Room


location_actions_synoym = ['go to', 'change location to', 'arrive at', 'I will move to', 'move to', 'go to the']

item_actions_synonym = ['use', 'apply', 'implement', 'deploy']

person_actions_synonym = ['talk to', 'speak with', 'conversate with', 'roundtable with']

get_access_itemSynonym = ['take', 'grab', 'acquire']

check_access_synonym = ['look at','check', 'examine', 'view', 'look']

quit_game_synonym = ['stop playing', 'end game', 'quit process', 'die', 'an hero']

action_synonym = [location_actions_synoym, item_actions_synonym, person_actions_synonym, get_access_itemSynonym, check_access_synonym]

item_synonym = []
person_object_synonym = []
setpiece_synonym = []
location_synonym = [Room.wayward_souls.name, Room.ThePlace.name]
object_synonym = []

# def access_words():
#     for wordlist in master_synonym:
#         for words in wordlist:
#             print('i got this word: ' + words)
#
# access_words()

def objectAccess(word):
    """
    will access the objects. objects are defined as being something the player interacts with each object has a name so that is the way
    they will be linked. objectAccess will flow directly into the synonym system.

    currently, objectAccess proves that the logic works from the initial section.
    the next step is to solve the issue of strings needing to be recognized.


    """
    for query in location_synonym:
        if word == query:
            print('it works dumbnuts')

def synonyms(phrase):
    """
    The Synonym Engine.
    Gives the player extra functionality by allowing them to use
    more options to say the same thing.

    At some point, it would be beneficial to update this to run is and True.

    Also: spaces may be problematic
    """
    for wordlist in action_synonym:
        for word in wordlist:
            if phrase[0:len(word)] == word:
                print('its true')
                break
    restofphrase = phrase[len(word) + 2:]
    print(restofphrase)
    objectAccess(restofphrase)


synonyms('go to the plains')

def Test(synonymWord):
    """
    a test environment to make sure the synonyms are actually doing things.
    """
    new_word = inputmessage[0:len(synonymWord)]
    inputmessage = 'examine statue'
    print(len(synonymWord))
    print(new_word == synonymWord)
    print(new_word)
    print(inputmessage[len(synonymWord)])
    print(inputmessage[len(synonymWord) + 1:])

#Test('examine statue')
