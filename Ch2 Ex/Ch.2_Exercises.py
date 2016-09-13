#
# name : Ian Hesner
# email : ith3@pitt.edu
# date : 09/08/16
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Chapter 2 Exercises
#
# Notes:
# Feedback on formatting is much appreciated

#######################################################

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

#######################################################

### EXERCISE 5 ###

#Labeling for your convenience
print("Exercise 5:\n")

#Define speed for equation work
v = 90
#Finding the distance traveled after a given time (x4)
d6 = v * 6
d10 = v * 10
d15 = v * 15
d225 = v * 29/12
#converting numbers to strings to print in the output (x4)
d6 = str(d6)
d10 = str(d10)
d15 = str(d15)
d225 = str(d225)
#Output (x4)
print("The car will travel " + d6 + "km in 6 hours going 90 km/hr")
print("The car will travel " + d10 + "km in 10 hours going 90 km/hr")
print("The car will travel " + d15 + "km in 15 hours going 90 km/hr")
print("The car will travel " + d225 + "km in 2 hours and 25 minutes going 90 km/hr\n\n")
#Done

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




