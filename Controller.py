"""
The controller class passes arguments to the Synonym Engine and the Object System, which then push requests to the objects and proper methods themselves.

So far, GoTo is a simple iteration that changes location, but needs to be changed so it goes to the Synonym Engine.

"""

import Room
import Player

inputmessage = ''

#gotothebeach = print('you went to the beach')

def GoTos(whatstheword):
    """

    :param whatstheword:
    :return:
    """
    for room in Room.Map.roomArray:
        if whatstheword == room.name:
            Player.LT.location = room.name
            print('you went to ' + room.name)
            print(Player.LT.location)
            break
        elif whatstheword == 'help':
            print('enter check map to view locations')
            break

    # elif whatstheword == 'the bar':
    #     print('you went to the bar')
    # elif whatstheword == 'the library':
    #     print('you went to the library')
    # elif whatstheword == 'the coffee house':
    #     print('you went to the coffee house')
    # elif whatstheword == 'the night club':
    #     print('you went to the night club')

def TheUseIts(whatstheword):
    if whatstheword == 'the mykyffn':
        print('in game if you use this at the wrong time, you die')
    elif whatstheword == 'the sword':
        print('you give this to the warrior')
    else:
        print("i don't know what you're talking about")

# def cheggit(helpWith):
#     if helpWith == 'locations' or 'the map' or 'places' or 'map':


def trymessage():
    if inputmessage[0:5] == 'go to':
        ### inputmessage is going to use the synonym system
        GoTos(inputmessage[6:])
    elif inputmessage[0:3] == 'use':
        TheUseIts(inputmessage[4:])
    elif inputmessage[0:5] == 'check' or 'help' or 'help with':
        print('check')

# class Controller:
#     global inputmessage
#     def canDo(self):
#         """
#         determines if the thing can be done.
#         :return:
#         """
