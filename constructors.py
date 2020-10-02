# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:17:13 2020

@author: Emirhan UZUN

Constructors
"""

class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color,self.flavor)
        
jonagold = Apple("red","sweet")
print(jonagold.color)
print(jonagold)

