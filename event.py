import person
import Player

class event:
    """
    Creates the event constructor for the events
    """
    def __init__(self, location, day):
        self.occurred = False
        self.location = location
        self.day = day

class eventLogic:
    """
    Singleton Instance of the __eventClass.
    Will hold the events to see if they are applicable.
    """

    def ckLocation(location):
        if Player.player.location == location:
            return True

    def ckDate(date):
        if Player.player.day == date:
            return True

    def ckEvent(checkevent):
        if checkevent.occurred == False:
            return True

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

introParam = event('village', 'day1')

# print(requirements(eventLogic.ckLocation('village'), eventLogic.ckDate('day1'), eventLogic.ckEvent(introParam)))

def intro():
    if requirements(Player.player.location == 'village', introParam.occurred == False) is True:
        print('\n A horse’s hooves echoed on the cobblestone path. Behind it, a man atop a small carriage whistles softly as the day broke on the horizon. It was a warm summer day, and you could feel the wind blow across your face. You see a small town in the distance, and you’re happy your long journey is almost over. You hear a low rumbling in the distance which you think is strange, but the man before you interrupts your thoughts.')
        print()
        print('\"You doin\' someth\'n \'ere in Aria? Not many people come to this small town, \'cept for the traders.')
        print()
        print('You thank the man for the ride and put a single coin into his hand. He tips his hat at you and spurs his horse forward, continuing on his own journey. You look toward the town and can hear the bustling of people within. You head inside through the main gates and look around. ')

def wakeup():
    print("You have awoken in the Tavern to searing pain. Once awake. You realize that you need to find a way to defeat this dragon before it further terrorizes the lives of the people in this town. But first, you need to find out where it is, and how you can defeat it.")

def dragonmain():
    """
    Once this happens, the event needs to return True whenever the player reaches the end of the event.
    :return:
    """
    if requirements(Player.player.location == 'townsquare', Player.player.day == 'day1', DragonAttack.occurred == False) is True:
            print('The town square is bustling people, with... You hear a loud roar, and look around in confusion. Others around you also stop what they’re doing to look toward the sky. It seems even closer than before, and after a few seconds you head toward one of the guards to ask about it.')
            print()
            print('Suddenly, you see a massive shadow cast on the ground. A deafening roar is heard above your head, and the earth shudders as a massive shadow lands in front of you. The force of the landing pushes you to the ground, and you cover your eyes from the blast of wind. You hear shrieks of the townspeople and the soldiers frantically running around you, and you scramble to get up.')
            print()
            print('As your vision comes back into focus, you see a massive black dragon, it’s entire body covered in obsidian scales and sharp horns protruding from it’s spine. Smoke poured out of it\'s nostrils and the smell of sulfur filled the air. You could see its fiery eyes staring at you, and you stood paralyzed with fear. The world swam by around you as clouds swarmed around the twisted creature. To your horror, the beast gives another shattering roar and steps toward you.')
            print()
            print('“Run you idiot!”, you hear someone cry out.')
            print('1.) Run')
            print('2.) Stay and fight')
            selection = input('--->   ')
            # if selection == "Fight" or "2" or "Stay and fight" or "Stay and fight":
            if selection == "2" or selection == "Stay and fight":
                print('You grab the dagger from your waistband and charge toward the beast, raising your weapon in triumph. You look towards the dragon who seems to smirk at your insolence, and suddenly your entire body is consumed in fire. ')
                print('You died. Why did you think that would work?')
                print('Restart?')
            # elif selection == "Run" or "run" or "1":
            elif selection == "1" or selection == "Run":
                print('The call broke your trance. You bolt towards the direction of the voice as you narrowly miss the dragon breathing hot flames in your direction. Debris falls from the sky as buildings crumble around you and you can feel yourself shaking with adrenaline and fear.')
                print()
                print('You run blindly through the town, flinching at a distant crash and the screams that followed. You still felt the blazing of heat on your skin, and even with your vision blurred you could see the smoke and destruction.')
                print()
                print('You turn a corner and run toward a tower at the end of town when you hear a loud crash and a little girl scream. A ways ahead, you see a man with a beam of lumber covering his chest next to a building with a roof that had just collapsed. A little girl struggled to pull off bits of wood and rocks. The man was red in the face, and it was clear that he could not lift the lumber by himself. The small girl looked around for help, and when she saw you she jumped up. You could see tears streaming down her face as she ran towards you.')
                print()
                print('\"Please!\", she sobbed. \"Save my Papa! He\'s stuck and he can\'t lift up the wood! The dragon is gonna get him, please help!\", she sniffled. She grabbed your hand and pulled you closer to her father. Behind you, you feel faint rumbling of foot steps coming closer.')
                print('1.) Continue towards the tower')
                print('2.) Help them')
                selection = input('--->   ')
                if selection == "Continue towards the tower" or selection == "1":
                    print('You shake her off, and continue on your way. "Wait!” she screams and grabs you again. You yank back your wrist and she falls backwards.')
                    print('“Abigail!!”, the man huffs from under the rubble. He glares at you as you turn and run, and you hear another roar. As you get closer to the castle, you hear her sobs getting quieter and quieter.')
                elif selection == "Help them" or selection == "2":
                    print("As you help them, your vision becomes increasingly blurry, until you are knocked out. You aren't sure if you're going to learn the answer to the Great Question. Ultimately, you are feeling a sense of finality. Will anyone sing about you?")
                    Player.player.location = 'tavern'
                    DragonAttack.occurred = True
                    Player.player.day = 'day2'
                    wakeup()
                else:
                    print('Make legal selection')
            else:
                print('Make legal selection')

DragonAttack = event('townsquare', 'day1')

def barmain():
    # change the area to barif selection ==  "Tavern":
        print('The tavern is filled with super drunk people. So pretty much the norm. You walk into the inn and see an empty seat at the bar. You also see a spot near a couple of guys at the fire.')
        print('Sit at Bar ')
        print('Sit by the fire')
        selection = input('--->   ')
        if selection == "Sit at bar":
            print('You grab a seat at the end of the bar. The fire in the hearth smells faintly of smoke even though a fire isn\'t lit. The bartender smiles and hands you a pint of ale.')
        elif selection == "Sit by fire":
            print('They don\'t like you and you have to go home because you\'re bad at making friends.')
        else:
            print('Failure')



def winState():
    if requirements(Player.player.day == 'day2', Player.player.state == 'win', Player.player.location == 'cave'):
        print("The dragon is now defeated. You teleported behind it and stabbed it. If it could understand English, it would have heard you say 'nothing personal kid'.")




def loseState():
    if requirements(Player.player.day == 'day2', Player.player.location == 'cave', Player.player.state == 'lose'):
        print('You got gored by the dragon and will now enjoy the sweet sweet release of death.')
