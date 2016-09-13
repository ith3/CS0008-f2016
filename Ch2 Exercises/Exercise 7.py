#
# Name : Ian Hesner
# Email : ith3@pitt.edu
# Date : 09/08/16
# Class : CS0008-f2016
# Instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Chapter 2 Exercise 7
#
# Notes:
# Feedback on formatting is much appreciated

#######################################################

### EXERCISE 7 ###

#Labeling for your convenience
print("Exercise 7:\n")

#Getting imputs for miles and gallons and then saving them as floats
mi = input("How many miles did you drive?\n")
mi = float(mi)
gal = input("How many gallons of fuel did you consume?\n")
gal = float(gal)
#converting mi->km and gal->L
km = mi * 1.60934
L = gal * 0.264172
#Calculaating L/100km
Lp100 = 100 * L / km
#changing and formating numbers to strings to print
km = str("%.2f" %km)
L = str("%.2f" %L)
Lp100 = str("%.2f" %Lp100)
#Output
print("You travelled " + km + "km consuming " + L + " liters of fuel at a rate of " + Lp100 + " L/100km.\n\n")
#Done
