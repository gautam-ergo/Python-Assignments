"""
CS 521 Information Structures with Python
#########################################
Module          - HW 2
Creation Date   - 09/25/2018
Student Name    - Gautam Gowrishankar

Intent:
    Mathematical Expressions using Python.
"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')

celsius = input("Enter a degree in Celsius: ")
farenheit = ((9/5) * float(celsius))+ 32
print(celsius,"Celsius is ",farenheit,"Farenheit" )
print ("\nEnd of Program\n")
