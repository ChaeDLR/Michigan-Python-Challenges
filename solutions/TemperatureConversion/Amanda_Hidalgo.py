# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:04:21 2022

@author: Amanda

Module 1 Python Exercise 
Farenheit to Celsius Converter

References: 
_name_ == "_main_": - https://stackoverflow.com/questions/419163/what-does-if-name-main-do
Typing - https://docs.python.org/3/library/typing.html
Defining Functions - https://docs.python.org/3/tutorial/controlflow.html#defining-functions
Multiple Funcitons - https://stackoverflow.com/questions/29075601/how-to-run-multiple-functions-in-order
"""

#Defining a function that converts farenheit to celsius
def celsius_converter(ftemp: float): # Convert to Celsius
    ctemp = (ftemp - 32) * (5/9)
    return ctemp

#Defining a function that converts celsius to farenheit
def farenheit_converter(ctemp: float): #Convert to Farenheit
    ftemp = (ctemp * (9/5)) + 32
    return ftemp

#Defining a function that takes in user input and produces a calculated result for choice A
def choice_A():      
    try:
        user_input = float(input("Please enter the Farenheit temperature: "))
        ftemp = float(user_input)
        celsius_result: float = celsius_converter(ftemp)
        print("The Celsius temperature is: ", str(round(celsius_result, 2)))
    
    except ValueError:
        print("Invalid user input, please enter the temperature only.")
        
#Defining a function that takes in user input and produces a calculated result for choice B
def choice_B():
    try:
        user_input = float(input("Please enter the Celsius temperature: "))
        ctemp = float(user_input)
        farenheit_result: float = farenheit_converter(ctemp)
        print("The Farenheit temperature is: ", str(round(farenheit_result, 2)))
                
    except ValueError:
        print("Invalid user input, please enter the temperature only.")

#Defining a function that asks users if they'd like to continue
def continue_input():
    question = input("Would you like to return to the menu (Y/N)?")
    if question == "Y" or question == "y":
        main()
    elif question == "N" or question == "n":
        pass
    else:
        print("Invalid entry, please enter a 'Y' or 'N'")

#Defining a function that produces a menu startup screen         
def menu():
    print("**********Welcome to the Temperature Converter**********")
    print()
    
    choice = input("""
                   A: Convert Farenheit to Celsius
                   B: Convert Celsius to Farenheit
                   
                   Please enter your choice: """)
    if choice == "A" or choice == "a":
        choice_A()
        continue_input()
    elif choice == "B" or choice == "b":
        choice_B()
        continue_input()
    else:
        print("Invalid entry, please try again.")

#Defining a function to initialize the main program    
def  main():      
# If this file is the program's entry point
    if __name__ == '__main__':
        menu()
 
main()