#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 22 :

# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and
# Python 3? Read Python 2 or Python 3.

# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

string = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

# from collections import OrderedDict
#
# ans = {}
#
# words = string.split()
# unique_words = set(words)
#
# for item in unique_words:
#     ans[item] = words.count(item)
# z = ans.items()
# od = OrderedDict(sorted(ans.items(), key=lambda e: e[0]))
#
# for item in od.items():
#     print(item[0], item[1])


text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
# text = text.split()
# countDict = dict()
#
# for i in text:
#     if i not in countDict:
#         countDict[i] = text.count(i)
#
# countDict = dict(sorted(countDict.items()))
#
# for k, v in countDict.items():
#     print(k, ":", v)