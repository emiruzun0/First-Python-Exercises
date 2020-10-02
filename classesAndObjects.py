# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:32:28 2020

@author: Emirhan UZUN

Classes and Objects
"""

class Apple:
    color = ""
    flavor = ""
    
jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())


golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"


#------------------------

class Piglet:
    """Represents a piglet that can say their name."""
    name = "piglet"
    years = 0
    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18
    def speak(self):
        """Outputs a message including name of the piglet"""
        print("Oink! I'm {}! Oink!".format(self.name))
        
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()
        
piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())

help(Piglet)  #Docstring



