#
# Name : Ian Hesner
# Email : ith3@pitt.edu
# Date : 11/18/16
# Class : CS0008-f2016
# Instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment 3
#
# Notes:
#
# Alex is lazy.
#
#######################################################

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
        lineNum += 1
        if(line == "name,distance\n"):()  # Do nothing, we don't care about that line
        else:
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
# End processFile()

# This function takes someones name (as well as some other numbers that help
# with finding info, and compliles all of the information about them contained
# in the given files
def buildProfile(name, numFiles, fileNames):

    # Initializing variables
    numRecords = 0
    totRan = 0

    # Finds if the name is contained in any of the files, if so retrieved
    # info under that name and returns how many times they appear and total distance ran
    for i in range(numFiles):
        dict, lines = makeDict(fileNames[i])
        if(name in dict):
            numRecords += 1
            totRan += dict[name]
        else:() #    Who cares
    return numRecords,totRan
# End buildProfile

# This function is for adding new names to a list, without adding names
# already contained in said list
def incorporate(nameList, dict):
    newNames = []
    for key in dict:
        newNames.append(key)
    newNameList = list(set(nameList + newNames))
    return newNameList
# End incorporate()

# This function is for formatting any numbers to be printed
# Gets a number coming in and returns a nice neat string
def formatNum(num):
    if(isinstance(num,int)):
        return "{:>3}".format(num)
    elif (isinstance(num, float)):
        return "{:>11.5f}".format(num)
    else:
        print("Something went wrong! AAAHHHHH!\nquitting...")
        quit()
# End formatNum()


def main():
    # Opens and closes the master file and stores the names of the files to open in fileNames
    master = open("f2016_cs8_a3.data.txt","r")
    fileNames = []
    numFiles = 0
    for line in master:
        fileNames.append(line.rstrip("\n"))
        numFiles += 1
    master.close()

    # This takes every file and compiles a list of all names contained in the
    # files, with no repeats. Also counts "lines read."
    totLines = 0
    names = []
    for i in range(numFiles):
        dict, lines = makeDict(fileNames[i])
        totLines += lines
        names = incorporate(names,dict)
    names.sort()

    # Initializing statistical variables that will be part of the output
    totDist = 0
    maxDist = 0
    maxDistName = ""
    minDist = 1000
    minDistName = ""
    partsWMR = 0

    # Creates and fills the output file, while creating the requested stats
    outputFile = open("Output.txt","w")
    outputFile.writelines("name, number of records, total distance ran\n")
    for name in names:
        numRec, dist = buildProfile(name, numFiles, fileNames)
        outputFile.writelines(name + "," + str(numRec) + "," + str(dist) + "\n") #add this to the output file
        totDist += dist
        if(numRec > 1):
            partsWMR += 1
        else:() # who cares
        if(dist > maxDist):
            maxDist = dist
            maxDistName = name
        elif(dist < minDist):
            minDist = dist
            minDistName = name
        else: () # who cares

    # Output
    print("Number of Input files read   : " + formatNum(numFiles))
    print("Total number of lines read   : " + formatNum(totLines))
    print()
    print("total distance run           : " + formatNum(totDist))
    print()
    print("max distance run             : " + formatNum(maxDist))
    print("  by participant             : " + maxDistName)
    print("min distance run             : " + formatNum(minDist))
    print("  by participant             : " + minDistName)
    print()
    print("Total number of participants : " + formatNum(len(names)))
    print("Number of participants")
    print("witn multiple records        : " + formatNum(partsWMR))
# End main

main()

