# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 01:06:16 2020

@author: Emir

Workshop for conditions
"""


number1 = int(input("Enter number 1 : "))
number2 = int(input("Enter number 2 : "))
number3 = int(input("Enter number 3 : "))


if (number1 > number2) and (number1 >= number3):
    maxNum = number1
elif (number2 >= number1) and (number2 >= number3):
    maxNum = number2
else:
    maxNum = number3

print("Max number is ",maxNum)