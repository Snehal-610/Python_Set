#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 13 :

# Write a program that accepts a sentence and
# calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
s = "hello world! 123"
l, d = 0,0
s = list(s)
for i in s:
    if i.isalpha():
        l += 1
    elif i.isdigit():
        d += 1
print(f"Letter: {l} and Digit: {d}")
