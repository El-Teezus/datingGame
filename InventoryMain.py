from Inventory import Inventory, Item
from Emma import Emma, Dialog
import Player
import Area
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

def requirements(*args):
    """
    Follows
    :param args: takes in arguments as relating to object arguments so that we can have a more importable code without starting new functions
    :return: A boolean statement, so that we do not have to worry about old code.
    """
    if all([*args]) is True:
        return True
    else:
        return False


def main():
    inventory = load_inventory()
    emma_gifts = load_emma_gifts()
    d = Dialog()
    if requirements(Player.player.location == 'plains', Player.player.day == 'day2') is True:
        print('You see Emma in the plains practicing with her sword. You can tell that she\'s focused, and you can see the sheen of sweat across her brow. Even though she is small, you can see that her blows are resonating against the practice dummy with force. She sees you watching, and waves you over.\n')
        print ('"Hey! Crazy what happened huh? I needed some time to clear my head..."\n\n You nod your head. The village was in shambles, and you almost lost your life. It isn\'t surprising that she\'s a little shaken up.')
        print ('"I\'m still a little upset... Do you think we could just talk for a little bit?"')
        print('1.)Yes')
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
            elif selection == 'Yes' or '1':
                for i in range(3):
                    if emma.relationship > 5:
                        if not d.is_empty('like'):
                            all = d.get_all("like")
                            s = random.choice(all)
                            print(s)
                            if s == 'Do you you like puppies?':
                                print('1.) I do! They\'re amazing')
                                print('2.) No,I hate them.')
                                selection = input('--->   ')
                                if selection == "1":
                                    emma.relationship = emma.relationship + 4
                                    print('Me too! They\'re so fun to play with, and I really like their cute pup faces.')
                                    d.remove(s, "like")
                                elif selection == '2':
                                    emma.relationship = emma.relationship -4
                                    print('Oh...really? That\'s too bad, I think they\'re great...Well, anyway...')
                                    d.remove(s, "like")
                            elif s == 'I think you\'re really cool! Do you like me?':
                                print('1.) I think you\'re incredible.')
                                print('2.)I guess you just don\'t really do it for me.')
                                selection = input('--->   ')
                                if selection == "1":
                                    emma.relationship = emma.relationship + 4
                                    print('Emma blushes. "I\'m really happy that you think so".')
                                    d.remove(s, "like")
                                elif selection == '2':
                                    print('Wow go fuck yourself.')
                                    d.remove(s, "like")
                            elif s == 'Do you want to go watch the sunset?':
                                print('1.)I actually am allergic to the sun, and your company. So no.')
                                print('2.) I think that sounds lovely right now. Should we leave now?')
                                selection = input('--->   ')
                                if selection == "1":
                                    emma.relationship = emma.relationship -5
                                    print('Ughh... I guess we shouldn\'t then...')
                                    d.remove(s, "like")
                                elif selection == '2':
                                    emma.relationship = emma.relationship + 6
                                    print('Yeah, lets go right now!!')
                                    d.remove(s, "like")
                            else:
                                print("Maybe?")
                    if emma.relationship >= -5 and emma.relationship <= 5:
                        if not d.is_empty('neutral'):
                            all = d.get_all("neutral")
                            s = random.choice(all)
                            print(s)
                            if s == 'Are you enjoying the town so far?':
                                print('1.) It\'s a mess and everyone here is poor. I hate it.')
                                print('2.) Everyone her seems very friendly! I\'ve been having a really great time here.')
                                selection = input('--->   ')
                                if selection == "1":
                                    print('How could you think something like that? Everyone here is fantastic, and you\'re just really judgemental.')
                                    emma.relationship = emma.relationship - 6
                                    d.remove(s, "neutral")
                                elif selection == "2":
                                    print('I think so too! I\'ve always felt really at home here.')
                                    emma.relationship = emma.relationship + 4
                                    d.remove(s, "neutral")
                            elif s == 'Were you here during the dragon attack?':
                                print('I was. I helped a couple people into the sewers. We were all beat up, but we made it out okay.')
                                print('Yeah I was. Does this place normally have such crazy stuff happening?')
                                selection = input('--->   ')
                                if selection == "1":
                                    print('That was you? I\'m so glad you were there! Thank you so much!')
                                    emma.relationship = emma.relationship + 10
                                    d.remove(s, "neutral")
                                elif selection == "2":
                                    print('Not normally. It\s a really peaceful town normally.')
                                    emma.relationship = emma.relationship + 1
                                    d.remove(s, "neutral")
                            elif s == 'Are you planning on staying long?':
                                print('1.) Yeah, I think I\'ll stay a little bit longer.')
                                print('2.) I don\'t think I wanna stay in a place like this.')
                                selection = input('--->   ')
                                if selection == "1":
                                    emma.relationship = emma.relationship + 4
                                    print('I\'m glad you like it here!')
                                    d.remove(s, "neutral")
                                elif selection == '2':
                                    emma.relationship = emma.relationship - 4
                                    print('Well, if you feel like that it probably is a good idea to leave.')
                                    d.remove(s, "neutral")
                    if emma.relationship < -10:
                        if not d.is_empty('dislike'):
                            all = d.get_all("dislike")
                            s = random.choice(all)
                            print(s)
                            if s == 'Umm... Are you here just to bother me?':
                                print('1.) I\'m sorry, I didn\'t mean to upset you. It\'s just been a stressful day.')
                                print('2.) Yeah I mean I don\'t have anything better to do.')
                                selection = input('--->   ')
                                if selection == "1":
                                    emma.relationship = emma.relationship + 5
                                    print('It\'s alright, I understand. Everyone here it feeling stressed out too.')
                                    d.remove(s, "dislike")
                                elif selection == '2':
                                    emma.relationship = emma.relationship -5
                                    print('Wow, alright. I actually have things better to do, so maybe you should just leave me alone.')
                                    d.remove(s, "dislike")
                            elif s == 'You didn\'t help Arnold during the dragon attack?':
                                print('1.) Everyone needs to look out for themselves. I could have died trying to save them too.')
                                print('2.) No, I was a coward. I regret it deeply.')
                                selection = input('--->   ')
                                if selection == "1":
                                    emma.relationship = emma.relationship + 7
                                    print('"You don\'t really care about others, huh?"')
                                    d.remove(s, "dislike")
                                elif selection == '2':
                                    print('"I understand, I was really scared too. They both got out okay, so it all worked out."')
                                    d.remove(s, "dislike")
                            elif s == 'Did you mean to annoy me?':
                                print('1.) Only a little bit. It\' kind of cute seeing you worked up.')
                                print('2.) I just don\'t care how you feel, that\'s all.')
                                selection = input('--->   ')
                                if selection == "1":
                                    emma.relationship = emma.relationship -5
                                    print('She laughs, but her face brightens up and she tries to hide her smile.')
                                    d.remove(s, "dislike")
                                elif selection == '2':
                                    emma.relationship = emma.relationship + 6
                                    print('Yeah, lets go right now!!')
                                    d.remove(s, "dislike")
                            else:
                                print("Maybe?")
                if emma.relationship > 15:
                        print('\nEmma sighs.\n\n "I know we can\'t actually do anything right now with the dragon attacking. It\'s not safe... Someone has to do something." Her downcast face is filled with sadness, and you can see she\'s fighting past tears.\n\nIn a spur of the moment decision, you decide that you might as well risk your life for this town you just got to. You don\'t have anything else going on. You tell Emma.\n\n"Really?? You\'re amazing!! I believe in you, I\m sure you can do it. But just in case, I want you to give you my sword." She passes the shortsword to you, and you can see it\s very sharp, but heavily used.\n\n "Good luck!!" She leans over and kisses you on the cheek, and you head towards the town, confused as to why you just agreed to do this.')

                        Player.player.state = 'win'
                        Area.theCave.canAccess = True
                        break


                elif emma.relationship <= 15:
                        print('\nEmma sighs.\n\n "We can\'t actually do anything right now with the dragon attacking. It\'s not safe... Someone has to do something." Her downcast face is filled with sadness, and you can see she\'s fighting past tears.\n\nIn a spur of the moment decision, you decide that you might as well risk your life for this town you just got to. You don\'t have anything else going on. You tell Emma.\n\n"Really? Why would you do that?"\n\n You shrug. You see that she\'s confused, but she doesn\'t try to stop you.\n\n "Umm...Good luck."\n\n.You head towards the town, confused as to why you just agreed to do this.')
                        Player.player.state = 'lose'
                        Area.theCave.canAccess = True
                        break
            else:
                print('Make legal selection')
            selection = input('--->   ')


main()
