# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 01:00:27 2020

@author: Emir
"""


lights = ["red","yellow","pink"]

currentLight = lights[2]  
#currentLight = lights[1]
#currentLight = lights[2]

print(currentLight)

if currentLight == "red":
    print("STOP!")
elif currentLight == "yellow":
    print("READY!") 
else:       #if the ligts is not red or yellow, just go 
    print("GO!") 

