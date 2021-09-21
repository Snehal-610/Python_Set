#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 44 :

# Write a program which accepts a string as input to print "Yes"
# if the string is "yes" or "YES" or "Yes", otherwise print "No".

# Hints:
# Use if statement to judge condition.
answer = input("Enter your answer Yes or No: ")
if answer.lower() == 'yes':
    print("YES! Great")
else:
    print("No")