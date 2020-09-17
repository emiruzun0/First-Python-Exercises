# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 01:21:15 2020

@author: Emirhan UZUN

Break and Continue
"""

cities = ["Ankara","Istanbul","Izmir"]

for city in cities:
    if city == "Istanbul":
        break           #break the loop
    print("Code for " + city + " : " + city[0:3])  #prints the first 3 characters of cities
    print("********")


print("--------------")
for city2 in cities:
    if city2 == "Istanbul":
        continue        #break the loop just this time
    print("Code for " + city2 + " : " + city2[0:3])  #prints the first 3 characters of cities

print("----------------")

 
for x in range(100):
    print(x+1)

print("---------------")


for x in range(1,10):    #include start point, not included last point
    print(x)
    
print("---------------")

#%%
for x in range(2,100,2):   #From 2 to 100, increases 2
    print(x)
    