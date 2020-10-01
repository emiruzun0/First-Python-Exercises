# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:14:14 2020

@author: Emirhan UZUN

Formatting String
"""

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name,number))

print("Your lucky number is {number}, {name}".format(name = name, number = len(name)*3))

#-------------------------------

price = 7.5
with_tax = price * 1.09
print(price,with_tax)
print("Base price : ${:.2f}. With Tax : ${:.2f}".format(price,with_tax))


#--------------------------------

