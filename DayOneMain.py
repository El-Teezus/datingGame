import Main

class event:
    def __init__(self, function, location, day):
        self.hasoccurred = False
        self.function = function
        self.location = location
        self.day = day

def barmain():
    # is going to be turned into an introduction section.
    print('You wake up with a throbbing headache.  Some rando suggested you should visit the Town Square, the Tavern, and the Beach. Where would you like to go?')
    selection = input('--->   ')
    # is in there for the arrival section
    if selection ==  "Tavern":
        print('You walk into the inn and see an empty seat at the bar. You also see a spot near a couple of guys at the fire.')
        print('Sit at Bar ')
        print('Sit by the fire')
        selection = input('--->   ')
        if selection == "Sit at bar":
            print('You grab a seat at the end of the bar. The fire in the hearth smells faintly of smoke even though a fire isn\'t lit. The bartender smiles and hands you a pint of ale.')
        elif selection == "Sit by fire":
            print('They don\'t like you and you have to go home because you\'re bad at making friends.')
        else:
            print('Failure')
    elif selection == "Town Square" or "town square":
        print('The tavern is filled with super drunk people. So pretty much the norm.')
    elif selection == "Beach":
        print('Ah look at that. A dragon. That\'s something.')

def dragonmain():
    print('A horse’s hooves echoed on the cobblestone path. Behind it, a man atop a small carriage whistles softly as the day broke on the horizon. It was a warm summer day, and you could feel the wind blow across your face. You see a small town in the distance, and you’re happy your long journey is almost over. You hear a low rumbling in the distance which you think is strange, but the man before you interrupts your thoughts.\n\n\"You doin\' someth\'n \'ere in Aria? Not many people come to this small town, \'cept for the traders.\n\n You nod your head as the carridge slows to a stop. As you thank the man for the ride, you put a single coin into his hand. He tips his hat at you and spurs his horse forward, continuing on his own journey. You look toward the town and can hear the bustling of people within. You head inside through the main gates and look around.\n\nThe town square is bustling people, with traders advertising their fares, women pulling their children along, and shoppers shuffling about. You hear a loud roar, and look around in confusion. Others around you also stop what they’re doing to look toward the sky. It seems even closer than before, and after a few seconds you head toward one of the guards to ask about it.\n Suddenly, you see a massive shadow cast on the ground. A deafening roar is heard above your head, and the earth shudders as a massive shadow lands in front of you. The force of the landing pushes you to the ground, and you cover your eyes from the blast of wind. You hear shrieks of the townspeople and the soldiers frantically running around you, and you scramble to get up.\n\nAs your vision comes back into focus, you see a massive black dragon, it’s entire body covered in obsidian scales and sharp horns protruding from it’s spine. Smoke poured out of it\'s nostrils and the smell of sulfur filled the air. You could see its fiery eyes staring at you, and you stood paralyzed with fear. The world swam by around you as the sky errupted into clouds around the twisted creature. To your horror, the beast gives another shattering roar and steps toward you.\n ')

def dragonmain2():
    print('“Run you idiot!”, you hear someone cry out.')
    print('1.) Run')
    print('2.) Stay and fight')

    selection = input('--->   ')
    # if selection == "Fight" or "2" or "Stay and fight" or "Stay and fight":
    if selection == "2" or selection == "Stay and fight":
        print(
            'You grab the dagger from your waistband and charge toward the beast, raising your weapon in triumph. You look towards the dragon who seems to smirk at your insolence, and suddenly your entire body is consumed in fire. ')
        print('You died. Why did you think that would work?')
        print('Restart?')
        selection = input('--->   ')
        if selection == "Yes":
            dragonmain()
            dragonmain2()
        else:
            print()
            print('Loser')
    # elif selection == "Run" or "run" or "1":
    elif selection == "1" or selection == "Run":
        print(
            'The call broke your trance. You bolt towards the direction of the voice as you narrowly miss the dragon breathing hot flames in your direction. Debris falls from the sky as buildings crumble around you and you can feel yourself shaking with adrenaline and fear.')
        print()
        print(
            'You run blindly through the town, flinching at a distant crash and the screams that followed. You still felt the blazing of heat on your skin, and even with your vision blurred you could see the smoke and destruction.')
        print()
        print(
            'You turn a corner and run toward a tower at the end of town when you hear a loud crash and a little girl scream. A ways ahead, you see a man with a beam of lumber covering his chest next to a building with a roof that had just collapsed. A little girl struggled to pull off bits of wood and rocks. The man was red in the face, and it was clear that he could not lift the lumber by himself. The small girl looked around for help, and when she saw you she jumped up. You could see tears streaming down her face as she ran towards you.')
        print()
        print(
            '\"Please!\", she sobbed. \"Save my Papa! He\'s stuck and he can\'t lift up the wood! The dragon is gonna get him, please help!\", she sniffled. She grabbed your hand and pulled you closer to her father. Behind you, you feel faint rumbling of foot steps coming closer.')
        print('1.) Continue towards the tower')
        print('2.) Help them')
        selection = input('--->   ')
        if selection == "Continue towards the tower" or selection == "1":
            print(
                'You shake her off, and continue on your way. "Wait!” she screams and grabs you again. You yank back your wrist and she falls backwards.')
            print(
                '“Abigail!!”, the man huffs from under the rubble. He glares at you as you turn and run, and you hear another roar. As you get closer to the castle, you hear her sobs getting quieter and quieter.')
        elif selection == "Help them" or selection == "2":
            print(
                'You bend down next to the girl and wrap your hands around the lumber. As you try to stand, you realize it\'s much heavier than you expected. The man tries again to push the heavy weight off his chest, and you can see perspiration dripping down his face. Behind you, you hear the small girl gasp.')
            print()
            print(
                'You whip your head backwards. The dragon\'s horns peak over the edge of a tall building, breathing fire across the path. Knowing you have little time, your push harder. Your muscles strain from the effort but the beam does not budge.')
            print()
            print('"Papa, he see\'s us!"')
            print()
            print('The ground starts to rumble behind you. You\'re muscles flex and you feel the strength seeping from your limbs. A high pitched screech sounds and the girl beside starts to tremble. You can hear the monster\'s claws dragging along the ground, and know you only have a few seconds left. The tigthness you felt in your arms turned into a sharp pain, and your arms begin to shake due to the effort.')
            print()
            print('Finally, the column gives way and you push it off the man\'s body. You grab his arm and pull him to his feet as he wheezed, his strength having not yet returned. The girl grabs yanks on your sleeve once again, and you look up to see the dragon\'s fangs dripping with blood and only half a courtyard away, each lumbering step causing destruction in his wake. You feel a similar sense of fear as he starts to charge toward the three of you.')
            print()
            print('You quickly throw your arm around the man from under his shoulder, and push the both of you around the building. His heavy weight impedes your speed significantly, but the small girl\'s cries push you forward. The dragon is right behind you as you stumble down the road. In the distance you hear men shouting orders, and pray that you\'ll make it away in time.')
            print()
            print('Where do you go?')
            print('1.) Hide in the closest building')
            print('2.) Take the next alley ')
            selection = input('--->   ')
            if selection == "1":
                print('The three of you scramble into the next building. However, the dragon was too close by and sees you enter. His harsh screeches can be heard from inside the walls, and as the girl huddles against her father, the roof falls above your heads and wreckage falls on top of the three of you. You don\'t survive.')
                print()
                print('Sorry, you tried! But you weren\'t fast enough to escape the dragon. Play again?')
                selection = input('--->   ')
                if selection == "Yes":
                    dragonmain()
                    dragonmain2()
                else:
                    print()
                    print('Loser')
            if selection == "2":
                print('The three of you surge forward and turn down a nearby alley, dodging the rubble falling from above. The man seemed to regain some of his stamina and is able to walk without your support, so the three of you wove around the surrounding barrels and discarded trash littering the passageway. You see an slight opening, shining light into the darkened alley, and the man pushes through the exit blocked by wood and rubble.')
                print()
                print('"Toward the sewers", the man huffed. "The dragon won\'t be able to get us down there". Up ahead you see the edge of a river, with stairs leading to a tunnel.')
                print()
                print('You continue to follow the older man before a loud crash sounds behind you. You look back, but there\'s dust everywhere and you can barely see. You think you can make out little girl on the ground still in the alley, but shes not moving and the dragon is forcing his way between the buildings. One of his wings iss caught, and the dragon turns to grab the tiles keeping him in place with his jaws. The walls have collapsed around Abigail and you\'re not sure if you can get her out in time.')
                print()
                print('ABIGAIL!!')
                print()
                print('1.) Turn Back')
                print('2.) Keep going')
                selection = input('--->   ')
                if selection == "1":
                    print('Realizing the man does not have the strenght to carry the girl and run back it time, you turn back and run back towards the alley. "I\'ll get her, just get to the sewer!", you scream at the man. "I\'ll pass her to you!".')
                    print()
                    print('Flinging planks of wood and rock out of the way, you try to dig a path inward. The dragon howls in frustration, and spits hot fire on what\'s left of the buildings. Ash fills the air and the smoke constricts your lungs. You cough through the pain and finally clear enough to grab Abigail. You scoop her into your arms and head back to the sewer.')
                    print()
                    print('You feel the ground shake as the dragon sets himself free, and as he spreads his wings wind howls around you. As he steps forward, the force of his gait throws fragments of broken glass and rock around you. The man waits close by at the bottom of the stairs, terror stricken with worry clear on his face. It looks grim and you\'re not sure that you\'ll both make it. In a split second decision, you scream.')
                    print('"Catch her!"')
                    print('The man outstretches his arms right as you toss the girl toward him. You glance back, but a large piece of broken wall hits you straight across the head. \n\nEverything goes black.')
                    print()
                    print('...')
                    print()
                    Main.main()
                else:
                    print('You ignore it and think that it\'s too late to save her so you keep going. The man pushes back against you to get by, but you try to force him toward the alley anyway. \n \n "I need go go back!" he belts out. The dragon pushes forward and more dust fills the air, and you keep pushing the man forward. \n\nHe keeps pushing back, as you struggle the dragon fills the air with an inferno. \n\nNone of you make it out alive.\n\nSorry! Wanna play again?')
                    print('Yes')
                    print('No')
                    selection = input('--->   ')
                    if selection == "Yes":
                        dragonmain()
                        dragonmain2()
                    print('Loser')
        else:
            print('Make legal selection')
    else:
        print()
        print('Make legal selection')
        print()
        dragonmain2()


dragonmain()
dragonmain2()
barmain()

