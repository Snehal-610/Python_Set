#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 46 :

# Write a program which can map() to make a list whose elements
# are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.
result = map(lambda a : a**2,[i for i in range(1,11)])
print(f"sequre of list element: {list(result)}")