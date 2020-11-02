# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:06:08 2020

@author: Emir
"""

import os

print(os.getcwd())  #check which current directory
os.mkdir("new_dir")  #create a directory
os.chdir("new_dir")  #change the directory
print(os.getcwd())



os.mkdir("newer_dir")  
os.rmdir("newer_dir")    #remove the directory if it is empty

print(os.getcwd())

os.listdir("website")   #returns a list of all the files and sub-directories in a given directory


# os.path.join(dir,name)   add a slash between two name (split)
# os.path.isdir(name)   check is a file or directory

