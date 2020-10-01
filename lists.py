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


#--------------------
animals = ["Lion","Zebra","Dolphin","Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
    
print("Total characters : {}, Average length: {}".format(chars,chars/len(animals)))

#------------------------------

winners = ["Ashley","Dylan","Reese"]
for index,person in enumerate(winners):
    print("{} - {}".format(index+1,person))
    
    
#----------------------------------
    
def full_email(people):
    result = []
    for email,name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_email([("alex@example.com","Alex Diego"),("shay@example.com","Shay Brandt")]))

#-------------------------------

multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

multiples = [x*7 for x in range(1,11)]
print(multiples)

#---------------------------------

languages = ["Python","Perl","Ruby","Go","Java","C"]
lengths = [len(language) for language in languages]
print(lengths)

#---------------------------------

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

#-------------------------------

