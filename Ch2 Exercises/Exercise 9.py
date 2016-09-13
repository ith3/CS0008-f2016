#
# Name : Ian Hesner
# Email : ith3@pitt.edu
# Date : 09/08/16
# Class : CS0008-f2016
# Instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Chapter 2 Exercise 9
#
# Notes:
# Feedback on formatting is much appreciated

#######################################################

### EXERCISE 9 ###

#Labeling for your convenience
print("Exercise 9:\n")

#Get Fahrenheit value and converts to float
f = input("How many degrees Fahrenheit?\n")
f = float(f)
#Conversion and formatting
c = 5/9*(f - 32)
#changing and formating c to a str to print
c = str("%.2f" %c)
#Output
print("That is " + c + "°C.\n\n")
#Done
