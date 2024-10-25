# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:25:33 2024

@author: xplod
"""
#this was hard and i searched for references from stack overflow
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#this is to account and define for the leap year (searched in google for the formula)

def days_of_the_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        return None and print("plesae enter a valid month")
#this is to define the values of 31,30, and 28(otherwise 29 if leap year) to its corresponding months, and invalid if input is unavailable



month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year (e.g., 2023): "))
if 1<= month <= 12:
    days = days_of_the_month(month , year)
    if days is not None:
        print("there are " , days , "in the month of " , month , "of the year" , year )
    else:
        print("invalid")
else:
    print("please enter a valid month")

#this is for user input, wherein they put the number of the month they need, and the year they need
















