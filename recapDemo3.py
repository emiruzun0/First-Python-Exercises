# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:44:05 2020

@author: Emirhan UZUN

Prime Number
"""

primeNumber = int(input("Enter a number : "))
control = True

for x in range(2,primeNumber):
    if primeNumber % x == 0:
        control = False
        break
    
if control == False :
    print("This is not a prime number ! ")
else:
    print("This is a prime number")