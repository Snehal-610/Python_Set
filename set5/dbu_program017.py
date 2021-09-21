#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 17 :

# Write a program that computes the net amount of
# a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.
# M means Main Balance D means deposit while W means withdrawal.

MainBalance = 0


def Main():
    global MainBalance
    inp = int(input("Enter 1 or 2:\n1. Deposit\n2. Withdraw\n"))
    if inp == 1:
        def Deposit(M):
            DepositAmount = int(input("Enter Amount for Deposit: "))
            M += DepositAmount
            global MainBalance
            MainBalance = M
            print("Your Main Balance is: ", M)
        Deposit(MainBalance)
    if inp == 2:
        def Withdraw(M):
            WithdrawAmount = int(input("Enter Amount for Withdraw: "))
            if WithdrawAmount > M:
                print("Insufficient Balance")
            else:
                M -= WithdrawAmount
                global MainBalance
                MainBalance = M
                print("Your Main Balance is: ", M)
        Withdraw(MainBalance)


while True:
    ask = input("Do you Want to continue Deposit or Withdraw?[Y/N]\n")
    if ask.upper() == 'Y':
        Main()
    else:
        break


