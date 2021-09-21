#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 38 :

# Define a function which can generate a list
# where the values are square of
# numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

def SequreDict(n):
    lst = []
    for i in range(1,n+1):
        lst.append(i**2)
    print("Result: ", lst[:5])


n = int(input("Enter Length of Dict: "))
SequreDict(n)

