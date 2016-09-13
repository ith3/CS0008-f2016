#
# Name : Ian Hesner
# Email : ith3@pitt.edu
# Date : 09/08/16
# Class : CS0008-f2016
# Instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Chapter 2 Exercise 10
#
# Notes:
# Feedback on formatting is much appreciated

#######################################################

### EXERCISE 10 ###

#Labeling for your convenience
print("Exercise 10:\n")

#Asks and stores how many cookies they want to make
Cs = input("How many cookies would you like to make?\n")
#Converts c to a float
Cs = float(Cs)
#Calculates how much of each ingredient
sug = Cs * 6.25
but = Cs * 5
flo = Cs * 6.875
#converts numbers to neat strings
Cs = str(Cs)
sug = str(sug)
but = str(but)
flo = str(flo)
#Output
print("To make " + Cs + " cookies, you will need:")
print(sug + "g of sugar")
print(but + "g of butter ")
print(flo + "g of flour")
#Done
