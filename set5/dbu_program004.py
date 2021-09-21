#!/user/bin/python
# -*- coding: utf-8 -*-

# program004:

# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.

# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98

# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# tuple() method can convert list to tuple
n = int(input("How many Data do you want to enter: "))
l = []
for i in range(n):
	k = input(f"Enter {i+1} Data: ")
	l.append(k)
print(f"Output in List: ", l)
t = tuple(l)
print(f"Output in Tuple: ", t)
