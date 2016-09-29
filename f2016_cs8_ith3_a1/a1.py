#
# Name : Ian Hesner
# Email : ith3@pitt.edu
# Date : 09/27/16
# Class : CS0008-f2016
# Instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment 1
#
# Notes:
#

#######################################################

#Useful conversions
kpm = 1.60934
Lpg = 3.78541

#Getting unit system
units = input("What unit system would you like to use?\n(Enter 1 for metric and 0 for USC)\n")
units = int(units)
#Dummy test for unit system
if(units != 0 and units != 1):
    print("Please enter a 1 or 0.")
    quit()
else:()

#Gathering inputs and getting values in both units
if(units == 1):
    #inputs
    dis = input("How far did you drive? (In km)\n")
    dis = float(dis)
    gas = input("How much gas did you use? (In L)\n")
    gas = float(gas)
    #Getting value in both units
    dism = dis
    disUS = dis/kpm
    gasm = gas
    gasUS = gas/Lpg
elif(units == 0):
    # inputs
    dis = input("How far did you drive? (In miles)\n")
    dis = float(dis)
    gas = input("How much gas did you use? (In gallons)\n")
    gas = float(gas)
    # Getting value in both units
    dism = dis*kpm
    disUS = dis
    gasm = gas*Lpg
    gasUS = gas
else: #Weirdness insurance
    print("Error")
    quit()

#Calculating consumption rates
consm = 100*gasm/dism
consUS = disUS/gasUS

#Determining Consumption Category
if(consm > 20):
    consCat = "Extremely Poor"
elif(consm > 15 and consm <= 20):
    consCat = "Poor"
elif(consm > 10 and consm <= 15):
    consCat = "Average"
elif(consm > 8 and consm <= 10):
    consCat = "Good"
elif(consm > 0 and consm <= 8):
    consCat = "Excellent"
else: #Weirdness insurance
    print("Error")
    quit()

#Making all the numbers into beautiful strings
dism = str("{:9.3f}".format(dism))
disUS = str("{:9.3f}".format(disUS))
gasm = str("{:9.3f}".format(gasm))
gasUS = str("{:9.3f}".format(gasUS))
consm = str("{:9.3f}".format(consm))
consUS = str("{:9.3f}".format(consUS))

#Output
print("                     USC            Metric")
print("Distance_____: "+disUS+"\bmiles   "+dism+"\bkm")
print("Gas__________: "+gasUS+"\bgallons "+gasm+"\bLiters")
print("Consumption__: "+consUS+"\bmpg     "+consm+"\bL/100km\n")
print("Gas Consumption Rating : "+consCat)

#Done