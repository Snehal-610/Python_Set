#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 20 :

# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield
class Gen():
    def __init__(self, n):
        self.n = n

    def series(self):
        i = 0
        while i < self.n:
            j = i
            i += 1
            if j % 7 == 0:
                yield j


result = Gen(71)
print(f"The series using Generator Yield: \n")
for i in result.series():
    print(i, end=", ")