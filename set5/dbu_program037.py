#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 37 :

# Define a function which can generate and print a list
# where the values are square of
# numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.


def SequreDict(n):
    lst = []
    for i in range(1,n+1):
        lst.append(i**2)
    print("Result: ", lst)


n = int(input("Enter Length of Dict: "))
SequreDict(n)