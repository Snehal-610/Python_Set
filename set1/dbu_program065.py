#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 65:

# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=1

# with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program:


# 5

# Then, the output of the program should be:

# 500

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Hints:
# We can define recursive function in Python.

def Rec(n):
    if n != 0:
        return Rec(n - 1) + 100
    return 0


n = int(input("enter a Number:"))
result = Rec(n)
print(f"Your Expected Output is: {result}")

# f = lambda n: f(n - 1) + 100 if n > 0 else n == 0
# print(f(n))
