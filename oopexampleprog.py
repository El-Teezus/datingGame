import Bar
import Beach
import Location
inBar = Bar.BarP()
inBeach = Beach.BeachP()
loc = Location.Location()


def main():

    currentlocation = ""

    while currentlocation != "quit":
        if currentlocation in loc.loclist:
            print('Currently at the location "{}"'.format(currentlocation))
            if currentlocation == "Bar":
                currentlocation = inBar.barProcess()
            elif currentlocation == "Beach":
                currentlocation = inBeach.beachProcess()
        else:
            print('Unknown Location enter something else')
            currentlocation = input("Enter valid location: ")


main()
