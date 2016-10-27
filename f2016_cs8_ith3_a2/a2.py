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
#

#######################################################

#  Whats left:
#      - process file
#      - string formatting
#      - testing


def processFile(file):
    pDis = 0
    pLines = 0




    return pDis,pLines

def printKV(lines, dis):
    print("Partial # of lines   : " + formatNum(lines))
    print("Partial distance run : " + formatNum(lines))
    #check string formating (20 chars??)

# Can be used to format any number into the defined format
def formatNum(num):
    if(isinstance(num, int)):
        return "{:10}".format(num)
    elif(isinstance(num, float)):
        return "{:10.3f}".format(num)
    else:
        print("ERROR")
        quit()

### Main Program Stars Here ###

# start running total of variables and a boolean for the while loop
totDis = 0
totLines = 0
# This while loop is the main function which asks for a file name and
# processes the file before closing it, in addition to doing dummy tests
while(True):
    # Getting file name
    fileName = input("File to be read     : ")

    # Testing if they want to quit
    if(fileName == "" or fileName == "q" or fileName == "quit"):
        break

    # Attempting to open the file
    # If there is no file, send them back to the start of the loop
    else:
        try:
            file = open(fileName, "r")
        except:
            print("File not found.\n")
            continue
    # Here we process the file, then close it
    dis,lines = processFile(file)
    file.close()
    # Then print this round of values and adds them to the total
    printKV(dis,lines)
    totDis += dis
    totLines += lines

# Printing the final output
print("Totals")
print("Total # of lines    : " + formatNum(totLines))
print("Total distance run  : " + formatNum(totDis))