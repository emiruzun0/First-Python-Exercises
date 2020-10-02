# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:00:58 2020

@author: Emirhan UZUN

Composition
"""


class Repository:
    def __init__(self):
        self.packages = {} 
    def add_package(self,package):
        self.packages[package.name] = package
        
    def total_size(self):
        result = 0
        for package in self.package.values():
            result += package.size
        return result

