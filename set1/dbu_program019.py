#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 19 :

# You are required to write a program to sort the
# (name, age, height) tuples by ascending order
# where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
# ('Json', '21', '85'), ('Tom', '19', '80')]

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# from operator import itemgetter
#
# lst = []
# n = int(input("How many person information: "))
# for i in range(n):
#     name = input("Enter Name: ")
#     age = int(input("Enter Age: "))
#     score = int(input("Enter Score: "))
#     tup = (name, age, score)
#     lst.append(tup)
#
# print(sorted(lst, key=itemgetter(0, 1, 2)))


# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map((lambda a :a if(a[0] == "A") else None), fruit)
#
# print(list(map_object))
# tables = [lambda x=x: x * 10 for x in range(1, 11)]
#
# for table in tables:
#     print(table())