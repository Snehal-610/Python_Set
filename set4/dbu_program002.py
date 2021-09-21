#!/user/bin/python
# -*- coding: utf-8 -*-

# program002 :

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# For example we are going to find factorial of some random numbers

def factorial(n):
    answer = []
    for num in n:
        if num == 0 or num == 1:
            answer.append(1)
        elif num < 0:
            answer.append(f"Invalid Input for {num}")
        else:
            fact = 1
            for i in range(1, num):
                fact += fact * i
            answer.append(fact)
    return answer


Random_list = [5, 3, 4, 12, 6, 8, 9, 2, 0, 1, -55]
result = factorial(Random_list)
print(result)
