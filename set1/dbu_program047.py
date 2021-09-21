#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 47 :

# Write a program which can map() and filter() to make
# a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, [i for i in range(1,11)]))
print(f"Expected Output: ", list(result))
