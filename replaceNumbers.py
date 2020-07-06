# -*- coding: utf-8 -*-
"""
@author: Emir
"""

x = 10
y = 20


x,y = y,x #Replace two numbers 

print("x = " + str(x))
print("y = " + str(y))


temp = x  #second way of replacing
x = y
y = temp


print("x = " + str(x)) 
print("y = " + str(y))

