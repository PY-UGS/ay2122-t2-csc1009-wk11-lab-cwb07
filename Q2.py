class clockTime:
    #attributes of clockTime object
    hours = 0
    minutes = 0
    seconds = 0

    #set hour's value
    def setHours(self, hours):
        self.hours = hours

    #set minutes's value
    def setMinutes(self, minutes):
        self.minutes = minutes

    #set seconds's value
    def setSeconds(self, seconds):
        self.seconds = seconds

    #set all 3 hours, minutes and seconds value
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    #set full time hours:minutes:seconds
    def showTime(self):
        print(str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))

#create clocktime object
c = clockTime()

#get user input for hours, minutes, seconds
hours = input("Enter your hours: ")
minutes = input("Enter your minutes: ")
seconds = input("Enter your seconds: ")

#set object time
c.setTime(hours, minutes, seconds)

#print and display the time in hours:minutes:seconds format
c.showTime()