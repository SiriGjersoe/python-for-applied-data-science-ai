# Handling exceptions

# Exceptions are alerts when something unexcpeted happens when running a code. They differ from errors
# Pyhton has built-in exceptions that are raised when errors occur:
# Try and Except blocks are used to handle exceptions in Python

'''Important to understand: You cannot design a function where except triggers the error condition.
except can only handle errors, not detect them.
If you want the check to happen before except, you must:
either check inside try and raise
or use a function that naturally errors (like math.sqrt)
'''

'''Exercise 1: Handling ZeroDivisionErro 
Create a Python function safe_divide that takes two numbers from user input: 
a numerator and a denominator. The function should return the result of dividing them.
 If the denominator is zero, it must catch the error, print "Error: Cannot divide by zero",
   and return None instead of crashing'''

import math


def safe_divide(numerator, denominator):
    try:
        a = numerator/denominator
        return a
    except ZeroDivisionError:
        print('Error because you tried to divide by zero')
        return None 

safe_divide(5,2)

# Quiz 2:
def square_root(number1):
    try:
        if number1 >= 0:
            result = (number1**0.5)
        return result
    except ValueError:
        print('Error: Cannot compute square root of negative number')
        return None
    

# Exercise 2: Handling ValueError
'''The function should generate the square root value if 
you provide a positive integer or float value as input. 
However, the function should be clever enough to detect the mistake if you enter a negative value.''' 
import math

def square_root(number1):
    try:
        math.sqrt(number1)
        return number1 ** 0.5 
    except ValueError:
        print("Invalid input! Please enter a positive integer or float value.")
        return None
square_root(3)

#Exercise 3: Handling Generic Exceptions
'''Define a function that divides num by (num - 5) and stores the result in result.
Use a try-except block to catch any errors.
If an exception occurs, catch Exception as e and print "An error occurred during calculation.'''

def divide_by_difference(num):
    try:
        result = num/(num-5)
        return result
    except:
        print('An error occurred during calculation.')

divide_by_difference(5)

