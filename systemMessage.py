

import random
"""
The systemMessage class generates custom messages according to what is passed to it. 
This iteration only does the name of the class, but further iterations will take advantage of the type of class that is being checked and potentially make for some funny situations.
"""

class MessageGenerator:
    talkedToArray = ['Knowing it would be important, you talked to ', 'Due to their presence, you talked to ', 'Because they commanded a strong presence, you talked to ', 'Initiating the conversation, you talked to ']
    talkRandom = random.randint(0, len(talkedToArray) - 1)
    wentToArray = ['You decided to visit the ', 'You decided to make a trip to ', ]
    wentToRandom = random.randint(0, len(wentToArray) - 1)
    checkedArray = ['Taking another look, you checked the ', 'Thinking it was important, you checked the ', 'Deciding it important, you checked ', 'Because it caught your eye, you checked ' ]
    checkRandom = random.randint(0, len(checkedArray) - 1)
    def actionMessage(action, subject):
        """
        generates a message when the player does an action to return a more complete feeling experience.
        The next iterations are going to differentiate for the specific type of action to create a authentic feeling experience

        Will take in the argument from the list and make it a thing from the switcher.

        To get rid of redundancy, we're going to use arrays within arrays to get things going.
        """
        if action == 'talked to':
            print(MessageGenerator.talkedToArray[MessageGenerator.talkRandom] + subject + '.')
        if action is 'checked':
            print(MessageGenerator.checkedArray[MessageGenerator.checkRandom] + subject + '.')
        if action is 'went to':
            print(MessageGenerator.wentToArray[MessageGenerator.wentToRandom] + subject + '.')
        #if action is:

        #if action is

#MessageGenerator.actionMessage('checked', ' the bartender')
