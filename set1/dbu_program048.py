#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 48 :

# Write a program which can filter() to make a list
# whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.
even = filter(lambda a : a % 2 == 0, [i for i in range(1,21)])
print(f"Even Numbers: {list(even)}")



# from functools import reduce
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rs = reduce(lambda x, y: x + y, list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, ls))))
# print(rs)
