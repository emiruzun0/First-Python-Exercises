# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:56:08 2020

@author: Emir
"""

import os
import os.path

print(os.path.getsize("file.txt")) #gives the size of file
print(os.path.getmtime("file.txt")) #to check when the file was last modified (Unix timestamp)
  

import datetime

timestamp = os.path.getmtime("file.txt")    #make it easier for us humans to read, like this.
print(datetime.datetime(2020, 1,6,7,2,3,899999))


print(os.path.abspath("file.txt"))  # takes a filename and turns it into an absolute path