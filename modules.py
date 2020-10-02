# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 00:00:36 2020

@author: Emirhan UZUN

Modules
"""

import random   #Generate random numbers
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10)) 

#-------------------------------------

import datetime
now = datetime.datetime.now()
print(type(now))
print(now)
print(now.year)
print(now + datetime.timedelta(days=28 ))