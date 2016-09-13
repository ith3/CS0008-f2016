#
# Name : Ian Hesner
# Email : ith3@pitt.edu
# Date : 09/08/16
# Class : CS0008-f2016
# Instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Chapter 2 Exercise 3
#
# Notes:
# Feedback on formatting is much appreciated

########################################################

### EXERCISE 3 ###

# Labeling for your convenience
print("Exercise 3:\n")

#Get how many square meters
m = input("How many square meters in the tract?\n")
#Change the imput to a number instead of a string
m = float(m)
#convert from m^2 to acres
acres = m/4046.8564224
#Change acres to a string to print it
acres = str("%.2f" %acres)
#Output
print("You Have " + acres + " acres in the tract.\n\n")
#Done