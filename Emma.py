import Inventory
import random

class Emma:
    """
    person object. we use this so that we can have people who talk to other people and so that things can happen.
    """
    def __init__(self, likes, dislikes, neutral):
        self.likes = likes
        self.neutral = neutral
        self.dislikes = dislikes
        self.relationship = 5

    def checkgift(self, gift):
        if gift in self.likes:
            print("Wow, thank you! I really like this!")
            self.relationship = self.relationship +10
        elif gift in self.neutral:
            print('I guess this is okay?')
        elif gift in self.dislikes:
            print('We just met! I hate this!')
            self.relationship = self.relationship -10
        else:
            print('...What?')
            self.relationship = self.relationship - 2

    def get_relationship(self):
        return self.relationship

    def checkdialog(self, dialog):
        if dialog in self.postive_talk:
            print("")
            self.relationship = self.relationship +5

class Dialog: ##function or subclass of person##
    def __init__(self):
        self.day1like = ['Do you you like puppies?',
                     'I think you\'re really cool! Do you like me?',
                     'Do you want to go watch the sunset?']
        self.day1neutral = ['Are you enjoying the town so far?',
                 'Were you here during the dragon attack?',
                 'Are you planning on staying long?']
        self.day1dislike = ['Umm... Are you here just to bother me?',
                 'You didn\'t help Arnold during the dragon attack?'
                 'Did you mean to annoy me?']

    def get_all(self, what):
        if  what == 'like':
            return self.day1like
        elif what == 'neutral':
            return self.day1neutral
        else:
            return self.day1dislike

    def remove(self, sentence, what):
        if what == "like":
            self.day1like.remove(sentence)
        elif what == "neutral":
            self.day1neutral.remove(sentence)
        else:
            self.day1dislike.remove(sentence)

    def is_empty(self, what):
        if what == 'like':
            return self.day1like == [ ]
        if what == 'dislike':
            return self.day1dislike == [ ]
        else:
            return self.day1neutral == [ ]


