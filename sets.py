# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 20:17:08 2020

@author: Emirhan UZUN
"""

mySet = {"Emir","Ali","Elif"}
mySet2 = set(["Aa","Bb","Cc"])  #Other definiton
print(mySet)

for names in mySet:
    print(names)  #Set elements are not ordered and indexed
    
print("Ali" in mySet)  #Search in set

if "Ali" in mySet:
    print("Ali is in the set")
    
mySet.add("Sena") #Add element
print(mySet)

mySet.update(["Mert","Yagmur","Derin"]) #Add elements more than one
print(mySet)

print(len(mySet))  #Length of set

mySet.remove("Mert")  #Remove element
print(len(mySet))

mySet.discard("Mert") #If the element exist, remove it. Otherwise, don't give an error
print(len(mySet))

x = mySet.pop()  #Remove random element
print(len(mySet))
print(mySet)

x = mySet.clear() #Removes all elements in set
print(mySet)

del(mySet) #deletes set