"""
main is where we have the initiated commands and probably the constructors. More on that later.
"""

import Controller
import event


gameDesc = "                         ~******************************************************************************************~\n" \
           "                         ~##########################################################################################~\n" \
           "                         ~###########LawrenceThompson#########################################DanielRubin###########~\n" \
           "                         ~##################################### TBD: the Game ######################################~\n" \
           "                         ~******************************************************************************************~\n" \
           "                         +-------------------------------TEXT BASED DATING the GAME!!!------------------------------+\n" \
           "                         ~******************************************************************************************~\n" \
           "                         ~####################### El-Teezy and the Beautiful Indigo Children #######################~\n" \
           "                         ~##########################################################################################~\n" \
           "                         ~######################################HannahYudkin########################################~\n" \
           "                         ~##########################################################################################~\n" \
           "                         ~******************************************************************************************~\n"



def main():
    itsrunning = "true"
    print(gameDesc)
    event.intro()
    while itsrunning == "true":
        Controller.inputmessage = input('what are you going to do? \n')
        Controller.trymessage(Controller.inputmessage)

main()

