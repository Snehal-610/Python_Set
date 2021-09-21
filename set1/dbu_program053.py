#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 53 :

# Define a class named Rectangle which can be
# constructed by a length and width.
# The Rectangle class has a method which can compute the area.

# Hints:
# Use def methodName(self) to define a method.


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def RectangleArea(self):
        return self.length * self.width


newRectangle = Rectangle(12, 10)
print(newRectangle.RectangleArea())
