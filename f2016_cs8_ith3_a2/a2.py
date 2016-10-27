#
# Name : Ian Hesner
# Email : ith3@pitt.edu
# Date : 10/28/16
# Class : CS0008-f2016
# Instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment 2
#
# Notes:
#       I added an extra data file (dataE.csv), which is basically the
#   data1.csv file with lots of errors. I tried to make this program to
#   be able to handle misformatted data files and help the person
#   using this program to find those errors. This would help a lot if
#   these files were millions of lines long instead of 50.
#

#######################################################

def processFile(file):

    # Setting initial values:
    pDis = 0               # Distance
    pLines = 0             # Line Count
    errors = 0             # Error Count
    errlist = []           # Keep track of where errors occur
    lineNum = 0            # Keep track of line number for ^

    # The for loop that scans through the lines
    for lines in file:
        lineNum += 1
        # A try statement is used here to catch misformatted lines
        try:
            # Reads line
            line = lines.rstrip('\n').split(',')
            # What is printed in the if statement explains this step
            if(line[0] == ""):
                print("(Line " + str(lineNum) + " does not have a name but was included in the calculation.)")
            # Adding up partial totals
            pDis += float(line[1])
            pLines += 1

        # If there is an error, record where and add to the error count
        except:
            errlist.append(lineNum)
            errors += 1
    # End for loop

    # Output explaining what errors were found (only printed if there were errrors)
    if(errors != 0):
        print("There were " + str(errors) + " errors in line(s) " + str(errlist) + "\n(These lines were not included in the calculation.)")
    return pDis,pLines
# End processFile


def printKV(dis, lines):
    print("Partial # of lines  : " + formatNum(lines))
    print("Partial distance run: " + formatNum(dis))
# End printKV

# Can be used to format any number into the defined format
def formatNum(num):
    if(isinstance(num, int)):
        return "{:10}".format(num)
    elif(isinstance(num, float)):
        return "{:10.3f}".format(num)
    else:
        print("ERROR")
        quit()
# End formatNum

# I felt like putting the main program into a function, I think it looks more "beautified"
def main():
    # start running total of variables and a boolean for the while loop
    totDis = 0
    totLines = 0
    keepGoing = True
    # This while loop is the main function which asks for a file name and
    # processes the file before closing it, in addition to doing dummy tests
    while(True):
        # Getting file name
        fileName = input("\nFile to be read     : ")

        # Testing if they want to quit
        if(fileName == "" or fileName == "q" or fileName == "quit"):
            keepGoing = False
            continue

        # Attempting to open the file
        # If there is no file, send them back to the start of the loop
        else:
            try:
                file = open(fileName, "r")
            except:
                print("File not found.")
                continue
        # Here we process the file, then close it
        dis,lines = processFile(file)
        file.close()
        # Then print this round of values and adds them to the total
        printKV(dis,lines)
        totDis += dis
        totLines += lines
    # End while loop

    # Printing the final output
    print("\nTotals")
    print("Total # of lines    : " + formatNum(totLines))
    print("Total distance run  : " + formatNum(totDis))
# End Main

# This kicks everything off
main()