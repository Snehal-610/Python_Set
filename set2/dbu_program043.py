#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 43 :

# Write a program to generate and print another
# tuple whose values are even numbers
# in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
l1 = []
for i in t1:
    if i%2 == 0:
        l1.append(i)
t2 = tuple(l1)
print(f"Original Tuple: {t1}\nEven Tuple: {t2}")
