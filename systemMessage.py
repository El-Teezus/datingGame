"""
will help generate messages when things happen
"""
import person
import setpiece
import Player
import Room
class MessageGenerator:
    def actionMessage(action, name):
        """
        generates a message when the player does an action to return a more complete feeling experience.
        The next iterations are going to differentiate for the specific type of action to create a authentic feeling experience

        Will take in the argument from the list and make it a thing from the switcher.
        """

        print('You ' + action + ' the ' + name)
