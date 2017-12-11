import blonde
import redhead
import brunette

class Main:

    #list of Locations
    loclist = ["tavern","woods","castle"]  
    #List of Dates
    datelist = ["Blonde","Brunette","Red-Head"]
    #List of Date Atributes
    DatesDetails = ["Long blonde hair, Five feet 3 inches, likes metal art", "Short burnette", "Red-Head, Four Foot 11"]
    AlreadyDated = [0,0,0]
    currentdate = -1
    
    #List of Gifts
    Giftlist = ["Gift 1","Gift 2","Gift 3"]
    #List of Date Atributes
    GiftPoints = [10,0,-10]
    AlreadyGifted = [0,0,0]
    currentGift = -1

    
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
    if Main.datelist[Main.currentdate] == "blonde":
        listofQuestions = blonde.blondeC.Questions[questionLevel]
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

def chooseGift():
    ix = -1
    numberOfAvailableGifts = 0   
    Main.currentGift = -1
    print("\nYou can choose a gift if you want to give or enter a 0 to not give a gift." )
    for Gift in Main.Giftlist:    
        ix = ix + 1
        if Main.AlreadyGifted[ix] == 0:
            numberOfAvailableGifts = numberOfAvailableGifts + 1
            print("Gift", ix + 1, " is a ", Gift)

    while int(Main.currentGift) <  0  or int(Main.currentGift) > 3: 
        Main.currentGift = input("\nEnter the number of the Gift you would like to Give.\n")
        if not Main.currentGift.isdigit(): #check if numeric
            Main.currentGift = -1 #force to reask question

    if int(Main.currentGift) == 0:
        print("Cheapskate!")
    else:
        Main.currentGift = int(Main.currentGift) - 1  # index is actually 1 less than the input
        if Main.GiftPoints[Main.currentGift] > 0:
            print("She loved your gift and you just earned a bonus of ", Main.GiftPoints[Main.currentGift], " points!" )        
            Main.currentScore = Main.currentScore + Main.GiftPoints[Main.currentGift]
        elif GiftPoints[Main.currentGift] < 0:
            print("She hated your gift and you just lost ", Main.GiftPoints[Main.currentGift], " points!" )
            Main.currentScore = Main.currentScore + Main.GiftPoints[Main.currentGift]
        else:        
            print("She didn't like or hate your gift... Pretty Lame\n" )
        Main.AlreadyGifted[Main.currentGift] = 1  #Mark Gifted

    questions()

def chooseDate():
    ix = -1
    numberOfAvailableDates = 0   
    Main.currentdate = -1
    for date in Main.datelist:    
        ix = ix + 1
        if Main.AlreadyDated[ix] == 0:
            numberOfAvailableDates = numberOfAvailableDates + 1
            print("Date", ix + 1, " is a ", date)
            print( "   ", Main.DatesDetails[ix] )

    while int(Main.currentdate) <  1  or int(Main.currentdate) > 3: 
        Main.currentdate = input("Enter the number of the person you would like to date.\n")
        if not Main.currentdate.isdigit(): #check if numeric
            Main.currentdate = -1 #force to reask question

    Main.currentdate = int(Main.currentdate) - 1  # index is actually 1 less than the input
    print("You are now on a date with the ", Main.datelist[Main.currentdate] )
    Main.AlreadyDated[Main.currentdate] = 1  #Mark Dated
    chooseGift()




def main():

    currentlocation = "start"

    from pathlib import Path
    contents = Path("intro.txt").read_text()
    print(contents)

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
