import person
import setpiece
import Item
import Player
import Room

class PlayerActions:
    ### a class with all the player actions to interact while in the overworld

    # def check(checkit):
    #     #### check objects before they are interacted with.
    #     if type(checkit) == Item or Person or Setpiece:
    #         return checkit.desc

    location_actions_synoym = ['go', 'location', 'arrive', 'move']

    item_actions_synonym = ['use', 'apply', 'implement', 'deploy']

    person_actions_synonym = ['talk', 'speak with', 'conversate with', 'roundtable with']

    get_access_itemSynonym = ['take', 'grab', 'acquire']

    check_access_synonym = ['look', 'check', 'examine', 'view', 'look']

    quit_game_synonym = ['stop playing', 'end game', 'quit process', 'die', 'an hero']

    action_synonym = [location_actions_synoym, item_actions_synonym, person_actions_synonym, get_access_itemSynonym, check_access_synonym]


    def use(item):
        ##use item has some issues with keeping the item's effect
        if type(item) == Item.Item:
            item.used = True
            return item.used

    def talk(person):
    #     #### talk to a person, return key dialog
    #     #### if the class of object is a person
        if type(person) == person.Person:
            print (person.Person.dialog)



    def check(thing):
        setpiece_synonym = [setpiece.theDragon]
        location_synonym = []
        item_synonym = []
        people_synonym = []
        objectSynonyms = [setpiece_synonym, location_synonym, item_synonym, people_synonym]
    # resolves the name of the item - objectSynonyms will be used
        for synonymList in objectSynonyms:
            for syonymItem in synonymList:
                if thing == syonymItem.name:
                    # returns the check description item.
                    # next the player location and the thing location needs to be verified.
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


    check('dragon')


#mykyffn = Item.Item(553, "The mykyffn", "don't look in the box", "bar")
#print(mykyffn.used)
#PlayerActions.use(mykyffn)
#print('hello')
#print(mykyffn.used)

