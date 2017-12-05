class BeachP:
    BeachQuestion = ["", ""]

    def __init__(self):
        self.__numberofdates = 0

    def beachProcess(self):
        self.__numberofdates = 1
        print("In beach process")
        self.currentlocation = input("Enter a location: ")
        return self.currentlocation