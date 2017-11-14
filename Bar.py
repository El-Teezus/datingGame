import Item
import Room
import setpiece


wayward_souls = Room.Bar("bar", "go get drunk")

class BarP:
    BarDates = ["Blond","Burnette","Red-Head"]
    BarAlreadyDated = [0,0,0]
    BarDatesDetails = ["Long blond hair, Five feet 3 inches, likes sailing", "Short burnette", "Red-Head, Four Foot 11"]

    CurrentStatus = 1
    CurrentDate = -1

    def __init__(self):
        self.numberofdates = 3

    def barProcess(self):

        print("In bar process")

        while BarP.CurrentStatus != 0:
            x = 0
            currentSelection = 0
            currentScore = 0
            if BarP.CurrentStatus == 1: # 1 means that they have not yet picked a date
             #   print("2 In bar process")
                for date in BarP.BarDates:
                    x=x+1
              #      print("3 In bar process")
                    print("Date", x, " ", date)
               # print("3A In bar process")
                if BarP.CurrentDate > -1:
                    currentSelection = input("For more details enter Date Number or Enter 'Good' to initiate with " + BarP.BarDates[int(BarP.CurrentDate)-1])
                else:
                    currentSelection = input("For more details enter Date Number")
                if currentSelection == "Good" :
                    print("selected ",BarP.BarDates[int(BarP.CurrentDate)-1])
                    BarP.CurrentStatus = 2
                elif int(currentSelection) < x:
                    BarP.CurrentDate = int(currentSelection)
                    print("Date Details", BarP.CurrentDate, " ", BarP.BarDatesDetails[int(BarP.CurrentDate)-1])
                    print("To find out more about the people to date; enter the date number")
            elif  BarP.CurrentStatus == 2: # Have selected Date
                 print("4 Questions")
                 input("input something - this is only a place holder")
            elif  BarP.CurrentStatus == 3: # Have selected Date
                 print("4 In bar process")
            else:
                print("5 In bar process")
                return BarP.currentlocation
