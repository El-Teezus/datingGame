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
            if currentlocation == "bar":
                currentlocation = inBar.barProcess()
            elif currentlocation.lower() == "Beach":
                currentlocation = inBeach.beachProcess()
        else:
            print('Unknown Location enter something else')
            currentlocation = input("Enter valid location: ")
            currentlocation = currentlocation.lower()

main()
