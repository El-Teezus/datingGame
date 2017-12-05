class BarP:
    BarDates = ["Blond","Burnette","Red-Head"]    
    BarDatesDetails = ["Long blond hair, Five feet 3 inches, likes sailing", "Short burnette", "Red-Head, Four Foot 11"]
    BarDateQuestions = [["Do you like sailing?\nA) Yes\nB) Maybe\nC) No ",
                         "Q2 \nA) Yes\nB) Maybe\nC) No ",
                         "Q3 \nA) Yes\nB) Maybe\nC) No "],
                        ["2 Q1 \nA) Yes\nB) Maybe\nC) No ",
                         "2 Q2 \nA) Yes\nB) Maybe\nC) No ",
                         "2 Q3 \nA) Yes\nB) Maybe\nC) No "],
                        ["3 Q1 \nA) Yes\nB) Maybe\nC) No ",
                         "3 Q2 \nA) Yes\nB) Maybe\nC) No ",
                         "3 Q3 \nA) Yes\nB) Maybe\nC) No "],]
    BarDateQuestionValues = [[1,0,-1],[-1,1,0],[1,-1,0]]
    BarAlreadyDated = [0,0,0]
    BonusPoints = 0 
    numberOfAvailableDates = 3

    CurrentStatus = 1
    CurrentDate = -1
    
    def __init__(self):
        self.numberofdates = 3

    def barProcess(self):        
        cont = "x"
        print("In bar process")
        currentSelection = 0
        currentSelectionIndex = 0
        currentScore = 0                        
        while BarP.CurrentStatus != 0:
            if BarP.CurrentStatus == 1: # 1 means that they have not yet picked a date
             #   print("2 In bar process")
                ix = -1
                BarP.numberOfAvailableDates = 0                   
                for date in BarP.BarDates:                    
              #      print("3 In bar process")
                    ix = ix + 1
                    if BarP.BarAlreadyDated[ix] == 0:
                        BarP.numberOfAvailableDates = BarP.numberOfAvailableDates + 1
                        print("Date", ix + 1, " ", date)
                if BarP.numberOfAvailableDates == 0:
                    print("\nNo one left to meet... Sorry\n")
                    BarP.CurrentStatus = 4
               # print("3A In bar process")
                if BarP.CurrentDate > -1: 
                    currentSelection = input("\nFor more details enter Date Number \nor Say 'Hello' to initiate the date with " + BarP.BarDates[int(BarP.CurrentDate)-1] + ": ")
                else:
                    currentSelection = input("\nFor more details enter Date Number: ")
                if currentSelection.lower() == "hello".lower() :
                    print("\nselected ",BarP.BarDates[int(BarP.CurrentDate)-1])
                    BarP.CurrentStatus = 2                    
                #elif int(currentSelection) <= BarP.numberOfAvailableDates: # Currently using a elif so that more can be added later
                elif BarP.BarAlreadyDated[int(currentSelection)-1] == 0: # Currently using a elif so that more can be added later
                    currentSelectionIndex = int(currentSelection)
                    BarP.CurrentDate = int(currentSelection)
                    print("\nDate Details", BarP.CurrentDate, " ", BarP.BarDatesDetails[int(BarP.CurrentDate)-1], "\n")    
                    #print("\nTo find out more about the people to date; enter the Date Number: ")  
            elif  BarP.CurrentStatus == 2: # Have selected Date
                 print("3 Questions")
                 BarP.BarAlreadyDated[currentSelectionIndex-1] = 1
                 currentScore = 0
                 question = -1
                 for questions in BarP.BarDateQuestions[currentSelectionIndex-1]:
              #      print("4 In bar questions")
                    question = question + 1
                    print("\nQuestion\n", questions)
                    ans = "xx"
                    while "ABCabc".find(ans) == -1:
                        ans = input("Enter your answer: ")
                    ans = ans.upper()
                    ansi = ord(ans) 
                    answer = int(ansi) - 65
                    currentScore = currentScore + int(BarP.BarDateQuestionValues[currentSelectionIndex-1][answer])                 
                 if currentScore <= 5:
                    BarP.CurrentStatus = 3
                 else:
                   #Reset                   
                    print("\nThat date did not go well.... You do not feel very confident. \n(You now have " + str(BarP.BonusPoints) + " bonus points)")
                    input("\nHit Enter to continue")
                    BarP.CurrentStatus = 1
                    BarP.CurrentDate = -1
                    BarP.CurrentStatus = 4
            elif  BarP.CurrentStatus == 3: # Have selected Date
                BarP.BonusPoints = BarP.BonusPoints + 1 
                print("\nThe date with ", BarP.BarDates[currentSelectionIndex-1], " was fabulous. You feel very confident.\n(You now have " + str(BarP.BonusPoints) + " bonus points)")
                input("\nHit Enter to continue")
                BarP.CurrentDate = -1                  
                BarP.CurrentStatus = 4
            elif  BarP.CurrentStatus == 4: # Have selected Date
                 BarP.numberOfAvailableDates = BarP.numberOfAvailableDates - 1
                 if BarP.numberOfAvailableDates > 0:
                        BarP.CurrentStatus = 1      
                 else:
                    print("\nTotal Bonus Points = " + str(BarP.BonusPoints))
                    input("\nHit Enter to continue")
                    return("quit")
            else:
                print("5 In bar process")
                return BarP.currentlocation