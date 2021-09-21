#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 45 :

# Write a program which can filter even numbers in
# a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.

even = filter(lambda x: (x % 2 != 0), [i for i in range(1, 11)])
print(f"Even Numbers: {list(even)}")
