# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:44:05 2024

@author: xplod
"""

user_dict = {}

num_entries = int(input("Enter the number of entries you want to add:"))

for i in range(num_entries):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict.update({key: value})

print("Dictionary after adding user input:", user_dict)