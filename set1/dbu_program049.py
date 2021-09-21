#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 49 :

# Write a program which can map() to make a list whose
# elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.

result = map(lambda a : a**2,[i for i in range(1,21)])
print(f"Square of list element: {list(result)}")

