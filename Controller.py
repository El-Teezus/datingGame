"""
The controller class passes arguments to the Publisher and Subscribers

"""

inputmessage = ''


def trymessage():
    if inputmessage[0:5] == 'go to':
        ### inputmessage is going to use the synonym system
        if inputmessage[6:] == 'the beach':
            print('you went to the beach')
        if inputmessage[6:] == 'the bar':
            print('you went to the bar')
        if inputmessage[6:] == 'the library':
            print('you went to the library')
        if inputmessage[6:] == 'the coffee house':
            print('you went to the coffee house')
        if inputmessage[6:] == 'the night club':
            print('you went to the night club')
    if inputmessage[0:3] == 'use':
        if inputmessage[4:] == 'the mykyffn':
            print('in game if you use this at the wrong time, you die')
    else:
        print("i don't know what you're talking about")

# class Controller:
#     global inputmessage
#     def canDo(self):
#         """
#         determines if the thing can be done.
#         :return:
#         """
