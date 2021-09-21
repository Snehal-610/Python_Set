#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 21 :

# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. Please write a program
# to compute the distance from current position after a sequence
# of movement and original point. If the distance
# is a float, then just print the nearest integer.

# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

import math

pos = [0, 0]
while True:
    s = input('''Enter a Input for UP/DOWN/LEFT/RIGHT:
First Input for UP = UP 5, Second Input for DOWN = DOWN 3, 
Third Input for LEFT = LEFT 3, Fourth Input for RIGHT = RIGHT 2:-\n''')
    if not s:  # Keep s blank After All 4 Input
        break
    movement = s.split(" ")

    direction = movement[0]  # UP/DOWN/LEFT/RIGHT
    steps = int(movement[1])  # Corresponding Value
    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps
    else:
        pass
print(pos[0], pos[1])
print(int(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2))))
