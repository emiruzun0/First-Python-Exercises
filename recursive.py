# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 00:47:50 2020

@author: Emirhan UZUN


#Recursive
"""

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)


print(factorial(5))

#--------------------


