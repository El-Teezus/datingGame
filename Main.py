import blond
import redhead
import brunette

class Main:

    #list of Locations
    loclist = ["tavern","woods","castle"]  
    #List of Dates
    datelist = ["Blond","Red-Head","Brunette"]
    #List of Date Atributes
    DatesDetails = ["Long blond hair, Five feet 3 inches, likes sailing", "Short burnette", "Red-Head, Four Foot 11"]

    AlreadyDated = [0,0,0]
    currentdate = -1
    DayNumber = 1

    currentScore = 0

def questions():
    #dfferent set of questions depending on previous answers
    if Main.currentScore > 250:
        questionLevel = 2   # questions 6-9
    elif Main.currentScore > 100:
        questionLevel = 1   # questions 4-6
    else:
        questionLevel = 0   # questions 1-3

    #Load the right set of questions
    if Main.datelist[Main.currentdate] == "Blond":
        listofQuestions = blond.BlondC.Questions[questionLevel]
    elif Main.datelist[Main.currentdate] == "Red-Head":
        listofQuestions = redhead.redheadC.Questions[questionLevel]
    elif Main.datelist[Main.currentdate] == "Brunette":
        listofQuestions = brunette.brunetteC.Questions[questionLevel]

    questionNumber = -1

    for questions in listofQuestions:
        questionNumber = questionNumber + 1
        print("\n", questions)
        ans = "xx"
        #Make sure their answer is A or B or C 
        while "ABCabc".find(ans) == -1:
            ans = input("Enter your answer:\n")
        
        #Make it uppercase
        ans = ans.upper()        
        if ans == "A":
            Main.currentScore = Main.currentScore + 50
        elif ans == "B":
            Main.currentScore = Main.currentScore + 0
        elif ans == "C":
            Main.currentScore = Main.currentScore - 50

    print("Current Score is: ", Main.currentScore)


def chooseDate():
    ix = -1
    numberOfAvailableDates = 0   
    Main.currentdate = -1
    for date in Main.datelist:    
        ix = ix + 1
        if Main.AlreadyDated[ix] == 0:
            numberOfAvailableDates = numberOfAvailableDates + 1
            print("Date", ix + 1, " is a ", date)
            print( "   ", Main.DatesDetails[ix] ," \n")

    while int(Main.currentdate) <  1  or int(Main.currentdate) > 3: 
        Main.currentdate = input("Enter the number of the person you would like to date.\n")
        if not Main.currentdate.isdigit(): #check if numeric
            Main.currentdate = -1 #force to reask question

    Main.currentdate = int(Main.currentdate) - 1  # index is actually 1 less than the input
    print("You are now on a date with the ", Main.datelist[Main.currentdate] )
    Main.AlreadyDated[Main.currentdate] = 1  #Mark Dated
    questions()


def main():

    currentlocation = "start"

    #Loop 3 times... or days
    while Main.DayNumber <= 3:
        print("\nToday is day ", Main.DayNumber)     

        #Loop until they type in a valid location in the Main.LocList
        while currentlocation not in Main.loclist:
            print("\nHere is a list of places to go: ")
            #Print out the List of avaliable places to go that have not already been visited
            for locs in Main.loclist:
                print(locs)
            currentlocation = input("\nSo, where would you like to go today?\n")
            currentlocation = currentlocation.lower()

        #We have a valid location
        if currentlocation.lower() == "tavern":
            print("\nYou are now in the tavern.  Who would you like to date?\n")
            #Start the dating process
            chooseDate()
            #Remove Tavern from the List... Can only visit once
            Main.loclist.remove("tavern")

        elif currentlocation.lower() == "woods":
            print("\nYou are in the Woods. Who would you like to date?\n")
            #Start the dating process
            chooseDate()
            #Remove Woods from the List... Can only visit once
            Main.loclist.remove("woods")
        elif currentlocation.lower() == "castle":
            print("\nYou are in the Castle  Who would you like to date?\n")
            #Start the dating process
            chooseDate()
            #Remove Castle from the List... Can only visit once
            Main.loclist.remove("castle")
        
        #Set the location back to nothing so that the above While loop will work
        currentlocation = ""

        #Add a Day
        Main.DayNumber = Main.DayNumber + 1
          
    #Out of days... All done
    print("\nGame Over")     

main()
