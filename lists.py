# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:31:19 2020
List Data Structure
@author: Emir
"""

student1 = "Joseph"
student2 = "Michael"
student3 = "Miley"

students = ["Joseph","Michael","Lincoln"]
print(students[1]) # Print index 1 of list
print(students) # Print all elements

students.append("Sarah") # Add new element to list
students.remove("Joseph") # Remove element from list
print(students)

students[1] = "Amy" # Replace the list element
print(students)

#List Constructor
cities = list(("New York","Chicago"))
print(cities)
print(len(cities)) # Number of elements

#other functions
# print(cities.clear()) // Clear the list
cities.append("New York")
print("Number of New York element : " + str(cities.count("New York"))) # Number of occurence of value

print("Chicago index : " + str(cities.index("Chicago")))

cities.pop(2) # Remove element of that index
cities.insert(0,"Istanbul") # Insert element to given index
print(cities)
cities.reverse() # Reverse elements
print(cities) 
      
cities3 = cities.copy() # Copy elements
cities2 = cities # Reference to same adress
cities2[0] = "Cleveland"
print(cities) # We change cities2 but also cities was changed
print(cities2)
print(cities3)

cities.extend(cities3) # Extend the list with given parameter
print(cities)

cities.sort() # Alphabectically sorting
print(cities)



