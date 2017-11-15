import person
import Item
import setpiece
import Item


class PlayerActions:
    #### a class with all the player actions to interact while in the overworld
    #
    # def check(checkit):
    #     #### check objects before they are interacted with.
    #     if type(checkit) == Item or Person or Setpiece:
    #         return checkit.desc

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

    





mykyffn = Item.Item(553, "The mykyffn", "don't look in the box", "bar")
print(mykyffn.used)
PlayerActions.use(mykyffn)
print('hello')
print(mykyffn.used)

