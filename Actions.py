
import person
import setpiece
import Item
import Player
import Area
import DataMaster
import systemMessage
import event
import InventoryMain
import _Main

class PlayerActions:
    location_actions_synoym = ['go', 'location', 'arrive', 'move']

    item_actions_synonym = ['use', 'apply', 'implement', 'deploy']

    person_actions_synonym = ['talk', 'speak', 'conversate', 'roundtable']

    get_access_itemSynonym = ['take', 'grab', 'acquire']

    check_access_synonym = ['look', 'check', 'examine', 'view', 'look']

    quit_game_synonym = ['stop', 'end ', 'quit', 'die', 'anhero']

    help_game_synonym = ['help', 'assist', 'commands', 'actions']

    action_synonym = [location_actions_synoym, item_actions_synonym, person_actions_synonym, get_access_itemSynonym, check_access_synonym, help_game_synonym, quit_game_synonym]

    def use(item):
        if type(item) == Item.Item:
            item.used = True
            return item.used

    def talk(livingThing):
        for synonymObjs in DataMaster.DataMaster.object_synonyms:
            for objs in synonymObjs:
                if objs.name in livingThing:
                    if DataMaster.locationVerifier(objs.location) is True:
                        systemMessage.MessageGenerator.actionMessage('talked to', objs.formattedname)
                        print(objs.dialog)

    def check(thing):
        setpiece_synonym = setpiece.setPieceList
        location_synonym = Area.Map.roomArray
        item_synonym = []
        people_synonym = []
        objectSynonyms = [setpiece_synonym, location_synonym, item_synonym, people_synonym]
        for synonymList in objectSynonyms:
            for syonymItem in synonymList:
                if syonymItem.name in thing:
                    if type(syonymItem) == Area.Area:
                        Area.worldBuilder()
                        break
                    if DataMaster.locationVerifier(syonymItem.location) is True:
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

    def move(request):
        """
        Formerly changeRoom.
        :return:
        """
        oldLocation = Player.player.location
        for areaName in Area.Map.roomArray:
            if oldLocation == areaName.name:
                oldLocation = areaName.formattedtext
        if Player.player.location in request:
            print("You are already there.")
        elif Player.player.location not in request:
            for room in Area.Map.roomArray:
                if room.name in request:
                    if room.canAccess == True:
                        Player.player.location = room.name
                        print("You left the " + oldLocation + ", and went to the " + room.formattedtext)
                        InventoryMain.brunette()
                        event.dragonmain()
                        _Main.main()
                    else:
                        print("You can't go there right now.")


