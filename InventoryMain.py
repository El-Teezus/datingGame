from Inventory import Inventory, Item

def load_inventory():
    inventory = Inventory()
    inventory.add_item(Item('Sword', 5, 1, 15, 'It\'s super sharp!'))
    inventory.add_item(Item('Leather Armor', 0, 10, 25, 'Covers up your shame'))
    inventory.add_item(Item('Rose', 0, 0, 2, 'A symbol of love'))
    inventory.add_item(Item('Ring', 0, 0, 100, 'Give to the lady(or man) of your dreams!'))
    return inventory

def main():
    inventory = load_inventory()
    print('Choose from these options')
    print ('Check Inventory')
    print ('Check Location')
    selection = input('--->   ')
    while selection != "done":
        if selection == "Check Inventory":
            inventory.print_items()
        elif selection == "Check Location":
            print('Where you are (later)')
        else:
            print('Make legal selection')
        selection = input('--->   ')


main()
