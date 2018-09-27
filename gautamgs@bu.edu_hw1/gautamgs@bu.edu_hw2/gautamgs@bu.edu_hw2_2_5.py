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

bill = input("Enter your bill amount:")
tips = 0.15 * float(bill)
total = float(bill) + tips
print("Gratuity (Tips) = {0:1.2f}".format(tips))
print("Total Amount = {0:1.2f}".format(total))
print ("\nEnd of Program\n")
