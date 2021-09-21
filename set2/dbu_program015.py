#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 15 :

# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# a = int(input("Enter a Single Digit: "))
# b = int(str(a)+str(a))
# c = int(str(a)+str(a)+str(a))
# d = int(str(a)+str(a)+str(a)+str(a))
# result = f"Expected Output: {a + b + c + d}"
# print(result)

a = int(input("Enter a Single Digit: "))
b = int(input("Enter a range for addition: "))
result = 0
for i in range(1,b+1):
    result = result + int(str(a)*i)
print(result)