"""
main is where we have the initiated commands and probably the constructors. More on that later.
"""

import Controller
import person
import Item
import Room
import Player

gameDesc = "The Bad Thing is doing Things We Don't Like. We Need to Find a Way to Kill THE BAD THING. "



def main():
    itsrunning = "true"
    print(gameDesc)
    while itsrunning == "true":
        Controller.inputmessage = input('what are you going to do?')
        Controller.trymessage()

main()


classroom = Room.Room('P132', 'COMP830: Object Oriented Software Development')
untitled_not_really_mastered = Item.Item(47, 'dating game', 'probably the G.O.A.T', 'in our hearts')
fellow_kids = person.Person('fellow kids', 'how do you do', 'the hallway', 'fellow kids')


# def test():
#     print('This is ' + LT.name + " and I'm " + LT.location)
#     print('We are in ' + classroom.name + ', for ' + classroom.desc)
#     print('You are going to be able to talk to the average person. ' + fellow_kids.dialog + " " + fellow_kids.name)
#
#
# test()
