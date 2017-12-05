from Inventory import Inventory, Item
from Emma import Emma, Dialog

import random

def load_inventory():
    inventory = Inventory()
    inventory.add_item(Item('Sword', 5, 1, 15, 'It\'s super sharp!'))
    inventory.add_item(Item('Leather Armor', 0, 10, 25, 'Covers up your shame'))
    inventory.add_item(Item('Rose', 0, 0, 2, 'A symbol of love'))
    inventory.add_item(Item('Ring', 0, 0, 100, 'Give to the lady(or man) of your dreams!'))
    return inventory

def load_emma_gifts():
    d={'Likes': ['Sword', 'Leather Armor'], 'Dislikes': ['Ring'], 'Neutral': ['Rose']}
    return d


def brunette():
    inventory = load_inventory()
    emma_gifts = load_emma_gifts()
    d = Dialog()
    # print('Choose from these options')
    # print ('Check Inventory')
    # print ('Check Location')
    print ('Give gift to Emma?')
    print('Talk to Emma?')
    emma = Emma("likes", "dislikes", "neutral")
    selection = input('--->   ')
    while selection != "done":
        if selection == "Check Inventory":
            inventory.print_items()
        elif selection == "Check Location":
            print('Where you are (later)')

        elif selection == ('Give gift to Emma'):
            print('Which Item?')
            inventory.print_items()
            gift = input('--->')
            e = Emma(emma_gifts['Likes'], emma_gifts['Dislikes'], emma_gifts['Neutral'])
            e.checkgift(gift)
            print('Current Relationship Level:')
            print(e.get_relationship())



        elif selection == 'Talk to Emma':
            for i in range(3):
                if emma.relationship > 5:
                    if not d.is_empty('like'):
                        all = d.get_all("like")
                        s = random.choice(all)
                        print(s)
                        print(all)
                        print("Current Relationship: ")
                        print(emma.relationship)
                        if s == 'Do you you like puppies?':
                            print('1.) I do! They\'re amazing')
                            print('2.) No,I hate them.')
                            selection = input('--->   ')
                            if selection == "1":
                                d.remove(s, "like")
                                emma.relationship = emma.relationship + 4
                                print('\nMe too! They\'re so fun to play with, and I really like their cute pup faces.(Hannah is lonely')
                            elif selection == '2':
                                d.remove(s, "like")
                                emma.relationship = emma.relationship -4
                                print('\nOh...really? That\'s too bad, I think they\'re great...Well, anyway...')
                        elif s == 'I think you\'re really cool! Do you like me?':
                            print('1.) I think you\'re incredible.')
                            print('2.)I guess you just don\'t really do it for me.')
                            selection = input('--->   ')
                            if selection == "1":
                                d.remove(s, "like")
                                emma.relationship = emma.relationship + 4
                                print('\nEmma blushes. "I\'m really happy that you think so".')
                            elif selection == '2':
                                d.remove(s, "like")
                                emma.relationship = emma.relationship - 10
                                print('Wow go fuck yourself.')
                        elif s == 'Do you want to go watch the sunset?':
                            print('1.)I actually am allergic to the sun, and your company. So no.')
                            print('2.) I think that sounds lovely right now. Should we leave now?')
                            selection = input('--->   ')
                            if selection == "1":
                                d.remove(s, "like")
                                emma.relationship = emma.relationship -5
                                print('\nUghh... I guess we shouldn\'t then...')
                            elif selection == '2':
                                d.remove(s, "like")
                                emma.relationship = emma.relationship + 6
                                print('\nYeah, lets go right now!!')
                        else:
                            print("Maybe?")
                        # d.remove(s, "like")
                        # emma.relationship = emma.relationship + 2
                        print(emma.relationship)
                if emma.relationship >= -5 and emma.relationship <= 5:
                    if not d.is_empty('neutral'):
                        all = d.get_all("neutral")
                        s = random.choice(all)
                        print(s)
                        print(all)
                        print("Current Relationship: ")
                        print(emma.relationship)
                        if s == 'Are you enjoying the town so far?':
                            print('1.) It\'s a mess and everyone here is poor. I hate it.')
                            print('2.) Everyone her seems very friendly! I\'ve been having a really great time here.')
                            selection = input('--->   ')
                            if selection == "1":
                                d.remove(s, "neutral")
                                print('\nHow could you think something like that? Everyone here is fantastic, and you\'re just really judgemental.')
                                emma.relationship = emma.relationship - 6
                            elif selection == "2":
                                d.remove(s, "neutral")
                                print('\nI think so too! I\'ve always felt really at home here.')
                                emma.relationship = emma.relationship + 4
                        elif s == 'Were you here during the dragon attack?':
                            print('1.) I was. I helped a couple people into the sewers. We were all beat up, but we made it out okay.')
                            print('2.) Yeah I was. Does this place normally have such crazy stuff happening?')
                            selection = input('--->   ')
                            if selection == "1":
                                d.remove(s, "neutral")
                                print('\nThat was you? I\'m so glad you were there! Thank you so much!')
                                emma.relationship = emma.relationship + 10
                            elif selection == "2":
                                d.remove(s, "neutral")
                                print('\nNot normally. It\s a really peaceful town normally.')
                                emma.relationship = emma.relationship + 1
                        elif s == 'Are you planning on staying long?':
                            print('1.) Yeah, I think I\'ll stay a little bit longer.')
                            print('2.) I don\'t think I wanna stay in a place like this.')
                            selection = input('--->   ')
                            if selection == "1":
                                d.remove(s, "neutral")
                                emma.relationship = emma.relationship + 4
                                print('\nI\'m glad you like it here!')
                            elif selection == '2':
                                d.remove(s, "neutral")
                                emma.relationship = emma.relationship - 4
                                print('\nWell, if you feel like that it probably is a good idea to leave.')
                if emma.relationship < -10:
                    if not d.is_empty('dislike'):
                        all = d.get_all("dislike")
                        s = random.choice(all)
                        print(s)
                        print(all)
                        print("Current Relationship: ")
                        print(emma.relationship)
                        if s == 'Umm... Are you here just to bother me?':
                            print('1.) I\'m sorry, I didn\'t mean to upset you. It\'s just been a stressful day.')
                            print('2.) Yeah I mean I don\'t have anything better to do.')
                            selection = input('--->   ')
                            if selection == "1":
                                d.remove(s, "dislike")
                                emma.relationship = emma.relationship + 5
                                print('\nIt\'s alright, I understand. Everyone here it feeling stressed out too.')
                            elif selection == '2':
                                d.remove(s, "dislike")
                                emma.relationship = emma.relationship -5
                                print('\nWow, alright. I actually have things better to do, so maybe you should just leave me alone.')
                        elif s == 'You didn\'t help Arnold during the dragon attack?':
                            print('1.) Everyone needs to look out for themselves. I could have died trying to save them too.')
                            print('2.) No, I was a coward. I regret it deeply.')
                            selection = input('--->   ')
                            if selection == "1":
                                d.remove(s, "dislike")
                                emma.relationship = emma.relationship - 7
                                print('\n"You don\'t really care about others, huh?"')
                            elif selection == '2':
                                d.remove(s, "dislike")
                                emma.relationship = emma.relationship + 2
                                print('\n"I understand, I was really scared too. They both got out okay, so it all worked out."')
                        elif s == 'Did you mean to annoy me?':
                            print('1.) Only a little bit. It\' kind of cute seeing you worked up.')
                            print('2.) I just don\'t care how you feel, that\'s all.')
                            selection = input('--->   ')
                            if selection == "1":
                                d.remove(s, "dislike")
                                emma.relationship = emma.relationship -5
                                print('\nShe laughs, but her face brightens up and she tries to hide her smile.')
                            elif selection == '2':
                                d.remove(s, "dislike")
                                emma.relationship = emma.relationship + 6
                                print('\nYeah, lets go right now!!')
                        else:
                            print("Maybe?")
                        print(emma.relationship)

        else:
            print('Make legal selection')
        selection = input('--->   ')


brunette()
