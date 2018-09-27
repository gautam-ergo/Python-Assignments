"""
CS 521 Information Structures with Python
#########################################
Module          - HW 2
Creation Date   - 09/25/2018
Student Name    - Gautam Gowrishankar

Intent:
    To llustrate the Mathematical functionality.
"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')

feet = input("Enter a value for Feet:")
meters = 0.305 * float(feet)
print(feet,"feet is", meters,"meters")
print ("\nEnd of Program\n")
