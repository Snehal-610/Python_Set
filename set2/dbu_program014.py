#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 14 :

# Write a program that accepts a sentence and
# calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
InputString = input("Enter a String: ")
CountLower = 0
CountUpper = 0
for i in InputString:
    if i.islower():
        CountLower += 1
    elif i.isupper():
        CountUpper += 1
print(f"Total Lower Case in String is: {CountLower}, Total Upper Case in String is: {CountUpper}")