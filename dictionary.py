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


#-----------------------------

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}

for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount,ext))
    
    
print(file_counts.keys())
print(file_counts.values())


for value in file_counts.values():
    print(value)
#--------------------------
    
    
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))


#--------------------------------

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
print(wardrobe.update(new_items))