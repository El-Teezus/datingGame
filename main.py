import Controller
import person
import Item
import Room
import Player

bardesc = ['you are now in the bar. bro there are some babes over there']



def main():
    itsrunning = "true"
    while itsrunning == "true":
        print(bardesc)
        Controller.inputmessage = input('what are you going to do?')
        Controller.trymessage()

main()


classroom = Room.Room('P132', 'COMP830: Object Oriented Software Development')
untitled_not_really_mastered = Item.Item(47, 'dating game', 'probably the G.O.A.T', 'in our hearts')
LT = Player.Player('here','LT')
fellow_kids = person.Person('fellow kids', 'how do you do', 'the hallway', 'fellow kids')


# def test():
#     print('This is ' + LT.name + " and I'm " + LT.location)
#     print('We are in ' + classroom.name + ', for ' + classroom.desc)
#     print('You are going to be able to talk to the average person. ' + fellow_kids.dialog + " " + fellow_kids.name)
#
#
# test()
