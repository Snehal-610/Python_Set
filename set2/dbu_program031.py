#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 31 :

# Define a function that can accept two strings as input
# and print the string with maximum length in console.
# If two strings have the same length, then the function
# should print all strings line by line.

# Hints:
# Use len() function to get the length of a string

def MaxString(s1, s2):
    if len(s1) > len(s2):
        print(f"Maximum string is {s1}")
    elif len(s1) < len(s2):
        print(f"Maximum string is {s2}")
    else:
        print(f"Both string {s1} and {s2} has same length.")


InpStr1 = input("Enter First string: ")
InpStr2 = input("Enter Second string: ")
MaxString(InpStr1,InpStr2)


