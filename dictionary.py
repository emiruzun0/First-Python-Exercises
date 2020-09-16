# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:21:31 2020

@author: Emirhan UZUN
"""

myDictionary = {
    "book" : "kitap",
    "table" : "masa" 
    }   #Key - value

myDictionary2 = dict(kitap = "book",masa = "table")  #Define


print(myDictionary)
print(myDictionary["book"])  #Find value

myDictionary["pencil"] = "kalem"
myDictionary["book"] = "kitap 1"  #change value
print(myDictionary)


del(myDictionary["book"])
print(myDictionary)
