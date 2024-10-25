# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:47:21 2024

@author: xplod
"""

#this will check if the number the user will input is even or odd
def even_odd(number):
    if number % 2 == 0:
        return (f"The number {number} is even.")
    else:
        return (f"The number {number} is odd.")

def main():
    try:
        user_input = int(input("enter your number: "))
        answer = even_odd(user_input)
        print(answer)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
#this is for checking the user input, comparing it to the even_odd definition, and therefore deciding if it is an even or odd number
#it also checks whether or not the input is a number in the first place, and will give an error if a number or a symbol is placed

if __name__ == "__main__":
    main()
#calls the function
