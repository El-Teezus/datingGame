import person
import setpiece
import Item
import Player
import Room
#import synonym_system
import DataMaster
import systemMessage

class PlayerActions:
    # a class with all the player actions to interact while in the overworld

    # def check(checkit):
    #     #### check objects before they are interacted with.
    #     if type(checkit) == Item or Person or Setpiece:
    #         return checkit.desc

    location_actions_synoym = ['go', 'location', 'arrive', 'move']

    item_actions_synonym = ['use', 'apply', 'implement', 'deploy']

    person_actions_synonym = ['talk', 'speak', 'conversate', 'roundtable']

    get_access_itemSynonym = ['take', 'grab', 'acquire']

    check_access_synonym = ['look', 'check', 'examine', 'view', 'look']

    quit_game_synonym = ['stop', 'end', 'quit', 'die', 'anhero']

    help_game_synonym = ['help', 'assist', 'commands', 'actions']

    action_synonym = [location_actions_synoym, item_actions_synonym, person_actions_synonym, get_access_itemSynonym, check_access_synonym, help_game_synonym, quit_game_synonym]

    def use(item):
        # use item has some issues with keeping the item's effect
        if type(item) == Item.Item:
            item.used = True
            return item.used
    # alternate dialogues according to what you're trying to talk to
    #   > person: are you a sociopath? you can't just use people like that.
    #   > setpiece: Everyone uses that. Stop being entitled
    #   > location: I think you're looking for the toilet.

    def talk(livingThing):
        # talk to a person, return key dialog
        # if the class of object is a person
        # this gets triggered when the synonym for talk is returned
        for synonymObjs in DataMaster.DataMaster.object_synonyms:
            for objs in synonymObjs:
                if objs.name in livingThing:
                    systemMessage.MessageGenerator.actionMessage('talked to', objs.name)
                    print(objs.dialog)
                    # if type(livingThing) == person.Person:
                    #     print(livingThing)
    # alternate dialogues according to what you're trying to talk to
    #   > item: holding the item.name, and trying to talk to it, nothing happened
    #   > setpiece: I recommend not doing that. someone could have you taken away to be studied.
    #   > location: Trying to write a story I see?

    def check(thing):
        setpiece_synonym = [setpiece.theDragon, setpiece.computerSetPiece, setpiece.barSetPiece]
        location_synonym = []
        item_synonym = []
        people_synonym = []
        objectSynonyms = [setpiece_synonym, location_synonym, item_synonym, people_synonym]
        print(thing)
    # resolves the name of the item - objectSynonyms will be used
        for synonymList in objectSynonyms:
            for syonymItem in synonymList:
                if syonymItem.name in thing:
                    # returns the check description item.
                    # next the player location and the thing location needs to be verified.
                    systemMessage.MessageGenerator.actionMessage('checked', syonymItem.name)
                    print(syonymItem.desc)

    # confirmTypeArray = [Item.Item, Player.Player, setpiece.SetPiece, Room.Room, person.Person]
    # # examine an item, person, setpiece, or location
    # for confirmItem in confirmTypeArray:
    #     # the boilerplate for checking the item
    #     if type(thing) == confirmItem:
    #         # next, enter the loop of name synonyms
    #         # example is going to pertain to setpieces, so it is going to be the name checked first, then the type confirmed.
    #         thing.examined = 'true'
    #         print(thing.desc)

    def help():
        print('You can do the following things: \n' +
              '    Talk to people \n' +
              '    Check things out \n' +
              '    Go to different locations \n' +
              '    Use items \n' + '    Good Luck!\n')

    def quitgame():
        print('Thanks for Playing!')
        quit()

LT = person.Person('hi', 'its me', 'here', 'LT')

#mykyffn = Item.Item(553, "The mykyffn", "don't look in the box", "bar")
#print(mykyffn.used)
#PlayerActions.use(mykyffn)
#print('hello')
#print(mykyffn.used)

