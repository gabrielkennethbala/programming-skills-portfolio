# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:36:11 2024

@author: xplod
"""


#these are the variables for the correct password, the max number of attempts and the current number of attempths
password = "12345"
max_attempts = 5
attempts = 0

#this is the code for how much attempts are allowed to be made, aswell as the results for the right and wrong passwords
while attempts < max_attempts:
    user_password = input("Enter your password: ")
    if user_password == password:
        print("Access granted.")
    else:
        attempts += 1
        remaining_tries = max_attempts - attempts
        if remaining_tries > 0:
            print(f"Incorrect password. You have {remaining_tries} attempts left.")
        else:
            print("Maximum attempts reached. Authorities have been alerted, youre cooked brmo.")