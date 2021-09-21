#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 33 :

# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

def SequreDict(n):
    dict ={}
    for i in range(1,n):
        dict[i] = i**2
    return dict


n = int(input("Enter Length of Dict: "))
dict = SequreDict(n+1)
print("Result: ", dict)

