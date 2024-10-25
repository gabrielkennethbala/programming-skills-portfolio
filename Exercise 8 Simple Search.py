# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:59:18 2024

@author: xplod
"""
#remember that all strings are case sensitive
#these are the variables with the names inserted
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#this is for the name they are trying to search for, with an input to determin which name the user is trying to search
search_name = input("Search for your name")

#this is the if and else control flow statements, and they provide the user with an answer for wether or not their name is on the list
if search_name in names:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found.")