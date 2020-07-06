# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:52:27 2020
Tuple Data Structure
@author: Emir
"""

tupleList = (2,4,6,"Istanbul",(2,3,4),[])
listStructure = [2,4,6,"Istanbul",[3,4,5],()]


print(tupleList)
print(listStructure)

print(len(tupleList))
print(len(listStructure))


listStructure[0] = 6
#tupleList[0] = 6 //Tuple elements cannot be changed ! 
print(tupleList)   
print(listStructure)

print(listStructure[-2]) # S econd element from the right
print(tupleList[-2]) # Second element from the right (Start from 1)

tupleValue = ("Emir")  
print(type(tupleValue)) # Print 'str'
tupleValue2 = ("Emir",)
print(type(tupleValue2)) # Print tuple

