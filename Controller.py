"""
The controller class passes arguments to the Synonym Engine and the Object System, which then push requests to the objects and proper methods themselves.

So far, GoTo is a simple iteration that changes location, but needs to be changed so it goes to the Synonym Engine.

"""

import Room
import Player
import synonym_system
import Actions
import DayOneMain

inputmessage = ''



def fixString(sentence):
    cutWords = [' the ', ' at ', ' to ', ' with ', ' the ', ' on ', ' like ']
    """
    Fix string allows the System to better understand user arguments.
    Eliminates whitespace, and irrelevant words from what is passed into the console.
    """
    ### The next iteration will remove punctuation.
    sentence = sentence.lower()
    for word in cutWords:
        if word in sentence:
            sentence = sentence.replace(word, " ")
    sentence = sentence.replace(" ", "")
    return sentence


def selector(actionArgument, restofphrase):
    """
    The selector works to route the pattern
    :param actionArgument:
    :param restofphrase:
    :return:
    """
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
            Actions.PlayerActions.quitgame()
            break
        elif actionArgument == Actions.PlayerActions.help_game_synonym:
            Actions.PlayerActions.help()
            break

def synonyms(phrase):
    """
    The Synonym Engine.
    Gives the player extra functionality by allowing them to use
    more options to say the same thing.

    At some point, it would be beneficial to update this to run is and True.

    Also: spaces may be problematic
    _____>> Next step is to integrate the fixString and TestWord from stringPrac into the Program
    """
    changePhrase = fixString(phrase)
    try:
        for wordlist in Actions.PlayerActions.action_synonym:
            for word in wordlist:
                if word in changePhrase:
                    actionArgument = wordlist
                    break
        restofphrase = changePhrase
        selector(actionArgument, restofphrase)
    except UnboundLocalError:
        print("didn't work")


def trymessage(phrase):
    """
    passes off arguments to other things
    :return:
    """
    synonyms(phrase)
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
