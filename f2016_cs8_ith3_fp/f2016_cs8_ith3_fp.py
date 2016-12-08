#
# Name : Ian Hesner
# Email : ith3@pitt.edu
# Date : 12/15/16
# Class : CS0008-f2016
# Instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Final Project
#
# Notes:
#
#
#
#######################################################

# This class creats a participant object as requested
class participant():
    # Initializing variables
    name = "Unknown"
    runs = 0
    dist = 0

    # Methods (Pretty self explanatory by name)
    def __str__(self):
        return "Name : " + formatItem(self.name) + ". Distance run : " + formatItem(self.dist) + ". Runs : " + formatItem(self.runs)

    def __init__(self, name, dist = 0):
        self.name = name
        self.dist = dist
        if(dist == 0):
            self.runs = 0
        else:
            self.runs = 1

    def getName(self):
        return self.name

    def getDistance(self):
        return self.dist

    def getRuns(self):
        return self.runs

    def addDistance(self,newDist):
        self.dist += newDist
        self.runs += 1

    def addDistances(self, dists):
        for i in len(dists):
            self.dist += dists[i]
            self.runs += 1

    def outputPrint(self):
        return self.name + "," + str(self.runs) + "," + str(self.dist) + "\n"
# End partticipant()


# This function gets passed a file name and creates a dictionary containing
# the information inside the file, then returns that dictionary
def makeDict(fileName):

    # initializing variables and opening the file
    d = {}
    lineNum = 0
    try:
        file = open(fileName,"r")
    except:
        print("File " + fileName + " not found.")
        return d,lineNum

    # This for loop goes through the file and fills the dictionary
    for line in file:
        if(line == "name,distance\n"):()  # Do nothing, we don't care about that line
        else:
            lineNum += 1
            data = line.rstrip('\n').split(',')
            data[0] = data[0].strip()
            try:
                data[1] = float(data[1])
                d[data[0]] = data[1]
            except:
                print("There is an error in line " + str(lineNum) + " of " + fileName + ".")

    # Closing file and returning the dictionary, as well as lines read
    file.close()
    return d, lineNum
# End makeDict()


# This function is for formatting any numbers/str to be printed
def formatItem(itm):
    if(isinstance(itm,int)):
        return "{:>3}".format(itm)
    elif (isinstance(itm, float)):
        return "{:>8.4f}".format(itm)
    elif(isinstance(itm, str)):
        return "{:>20}".format(itm)
    else:
        print("Something went wrong! AAAHHHHH!\nquitting...")
        quit()
# End formatNum()


def main():

    # Opens and closes the master file and stores the names of the files to open in fileNames
    opened = False
    while(not opened):
        # This try statement loops until the user enters a file that is actually there.
        try:
            masterName = input("Master file name:")
            master = open(masterName, "r")
            opened = True
        except:
            print(formatItem("File not found.\n"))
    fileNames = []
    numFiles = 0
    for line in master:
        fileNames.append(line.rstrip("\n"))
        numFiles += 1
    master.close()

    # This runs through all the files and puts the info into a list of
    # participant objects where each object contains all the info for the participant
    totLines = 0
    participants = {}
    for i in range(numFiles):
        dict, lines = makeDict(fileNames[i])
        totLines += lines
        for key in dict:
            if(key in participants):
                participants[key].addDistance(dict[key])
            else:
                participants[key] = participant(key,dict[key])


    # Initializing statistical variables that will be part of the statistical output
    totDist = 0
    maxDist = 0
    maxDistName = ""
    minDist = 1000
    minDistName = ""
    partsWMR = 0


    # Creates and fills the output file, while creating the requested stats
    outputFile = open("f2016_cs8_ith3_fp.data.output.csv","w")
    outputFile.writelines("name, number of records, total distance ran\n")
    for part in participants:
        # Write the line in the output file
        outputFile.writelines(participants[part].outputPrint())
        # Stat stuff
        totDist += participants[part].getDistance()
        if(participants[part].getDistance() > maxDist):
            maxDist = participants[part].getDistance()
            maxDistName = participants[part].getName()
        elif(participants[part].getDistance() < minDist):
            minDist = participants[part].getDistance()
            minDistName = participants[part].getName()
        else: () # Who cares
        if(participants[part].getRuns() > 1):
            partsWMR += 1
        else: () # Who cares
    outputFile.close()

    # Output
    print("Number of Input files read   : " + formatItem(numFiles))
    print("Total number of lines read   : " + formatItem(totLines))
    print()
    print("total distance run           : " + formatItem(totDist))
    print()
    print("max distance run             : " + formatItem(maxDist))
    print("  by participant             : " + maxDistName)
    print("min distance run             : " + formatItem(minDist))
    print("  by participant             : " + minDistName)
    print()
    print("Total number of participants : " + formatItem(len(participants)))
    print("Number of participants")
    print("with multiple records        : " + formatItem(partsWMR))
# End main

main()

