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
#
# Things I want:
#
#   - Number of Input files read (add counter at file open counter)
#
#   - Total number of lines read (add counter in for loop while reading lines)
#
#   - Max Dist run by a participant (when read new dist, if dist<maxDist: maxDist = dist)
#
#   - Min dist run (same as maxDist but with minimum)
#
#   - Total number of participants
#
#   - Number of participants with multiple records
#
#   - Output file
#       > same format as input files but with output being
#       > name,number of appearances,total distance ran to hundredths place
#
# So have the counters while opening and reading things,
# everything else can be taken from the master list printed in the output file.
# So make the output file as a list, print each item on a line in a file, get all
# stats and such from the list/set/dictionary/whatever (most likely dictionary)
# Read names off of data.txt, then send the names to processFile("fileName")
# which will add the new info to master dictionary
#
#
# What I actually need:
#
#   - Counters for number of files and lines read
#
#   - A dictionary containing: participant's name, number of appearances, total dist ran
#
#   - For nums, ints are 2 chars long xx, dist is 10 including ".", xxxx.xxxxx
#
#
#   Cool trick, to remove duplicates, newDupFreeList = list(set(originalList))
#
#######################################################

# This function gets passed a file name and creates a dictionary with
# the information inside the file, then returns that dicrionary
def makeDict(fileName):
    # initializing variables and opening the file
    file = open(fileName,"r")
    d = {}
    lineNum = 0

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

#
def buildProfile(name, numFiles, fileNames):
    numRecords = 0
    totRan = 0
    for i in range(numFiles):
        dict, lines = makeDict(fileNames[i])
        if(name in dict):
            numRecords += 1
            totRan += dict[name]
        else:() #    Who cares
    return numRecords,totRan
# End buildProfile

def incorporate(nameList, dict):
    newNames = []
    for key in dict:
        newNames.append(key)
    newNameList = list(set(nameList + newNames))
    return newNameList

# End incorporate()

def formatNum(num):
    if(isinstance(num,int)):
        return "{:>3}".format(num)
    elif (isinstance(num, float)):
        return "{:>11.5f}".format(num)
    else:
        print("Something went wrong! AAAHHHHH!\nquitting...")
        quit()
# End formatNum()

# Opens the master file and stores the names of the files to open in fileNames
# Also numFiles will = number of files - 1
def main():
    master = open("f2016_cs8_a3.data.txt","r")
    fileNames = []
    numFiles = 0
    for line in master:
        fileNames.append(line.rstrip("\n"))
        numFiles += 1
    master.close()

    totLines = 0
    names = []
    for i in range(numFiles):
        dict, lines = makeDict(fileNames[i])
        totLines += lines
        names = incorporate(names,dict)
    names.sort()
    totDist = 0
    maxDist = 0
    maxDistName = ""
    minDist = 1000
    minDistName = ""
    # Total participats = len(names)
    partsWMR = 0
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
    print("Number of Input files read   : " + formatNum(numFiles + 1))
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

