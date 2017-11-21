"""
The controller class passes arguments to the Synonym Engine and the Object System, which then push requests to the objects and proper methods themselves.

So far, GoTo is a simple iteration that changes location, but needs to be changed so it goes to the Synonym Engine.

"""

import Room
import Player
import synonym_system
import Actions

inputmessage = ''


def fixString(sentence):
    cutWords = [' the ', ' at ', ' to ', ' with ', ' the ', ' on ', ' like ']
    """
    Fix string allows the System to better understand user arguments.
    ____>>>>Iteration One: Eliminates whitespace.
    Iteration Two: Eliminates punctuation
    Iteration Three:
    :param sentence:
    :return:
    """
    ### The next iteration will remove punctuation.
    sentence = sentence.lower()
    for word in cutWords:
        if word in sentence:
            sentence = sentence.replace(word, " ")
    sentence = sentence.replace(" ", "")
    return sentence


def selector(actionArgument, restofphrase):
    for actionArg in Actions.PlayerActions.action_synonym:
        if actionArgument == Actions.PlayerActions.location_actions_synoym:
            Room.Map.change_room(restofphrase)
            break
        elif actionArgument == Actions.PlayerActions.item_actions_synonym:
            print('hoi')
            break
        elif actionArgument == Actions.PlayerActions.person_actions_synonym:
            Actions.PlayerActions.talk(restofphrase)
            break
        elif actionArgument == Actions.PlayerActions.get_access_itemSynonym:
            print('leskeddit')
            break
        elif actionArgument == Actions.PlayerActions.check_access_synonym:
            Actions.PlayerActions.check(restofphrase)
            break
        elif actionArgument == Actions.PlayerActions.quit_game_synonym:
            print('its, me')
            break

def synonymTest(phrase):
    """
    The Synonym Engine.
    Gives the player extra functionality by allowing them to use
    more options to say the same thing.

    At some point, it would be beneficial to update this to run is and True.

    Also: spaces may be problematic
    _____>> Next step is to integrate the fixString and TestWord from stringPrac into the Program
    """
    changePhrase = fixString(phrase)
    for wordlist in Actions.PlayerActions.action_synonym:
        for word in wordlist:
            if word in changePhrase:
                actionArgument = wordlist
                break
    restofphrase = changePhrase
    print(restofphrase)
    print(actionArgument)
    selector(actionArgument, restofphrase)
    #print(restofphrase)
    #objectAccess(restofphrase)
    # print(wordlist)
    # print(word)
    # print(actionArg)
    # print(restofphrase)


#synonymTest('talk to LT')

# def GoTos(whatstheword):
#     """
#
#     :param whatstheword:
#     :return:
#     """
#     for room in Room.Map.roomArray:
#         if whatstheword == room.name:
#             Player.LT.location = room.name
#             print('you went to ' + room.name)
#             print(Player.LT.location)
#             break
#         elif whatstheword == 'help':
#             print('enter check map to view locations')
#             break

    # elif whatstheword == 'the bar':
    #     print('you went to the bar')
    # elif whatstheword == 'the library':
    #     print('you went to the library')
    # elif whatstheword == 'the coffee house':
    #     print('you went to the coffee house')
    # elif whatstheword == 'the night club':
    #     print('you went to the night club')

# def TheUseIts(whatstheword):
#     if whatstheword == 'the mykyffn':
#         print('in game if you use this at the wrong time, you die')
#     elif whatstheword == 'the sword':
#         print('you give this to the warrior')
#     else:
#         print("i don't know what you're talking about")

# def cheggit(helpWith):
#     if helpWith == 'locations' or 'the map' or 'places' or 'map':


def trymessage(phrase):
    """
    passes off arguments to other things
    :return:
    """
    synonymTest(phrase)
    # if inputmessage[0:5] == 'go to':
    #     ### inputmessage is going to use the synonym system
    #     GoTos(inputmessage[6:])
    # elif inputmessage[0:3] == 'use':
    #     TheUseIts(inputmessage[4:])
    # elif inputmessage[0:5] == 'check' or 'help' or 'help with':
    #     print('check')

# class Controller:
#     global inputmessage
#     def canDo(self):
#         """
#         determines if the thing can be done.
#         :return:
#         """
