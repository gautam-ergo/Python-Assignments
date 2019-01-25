"""
CS 521 Information Structures with Python
#########################################
Module          - HW 3
Creation Date   - 10/01/2018
Student Name    - Gautam Gowrishankar

Intent:
    To illustrate the math functionality.
"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')

pounds = 2.2
print("Kilograms   Pounds")
for value in range(1, 200, 2):
    temp = value * pounds
    print(value, "         %.1f" %temp)

print("\n -End of Program- ")
