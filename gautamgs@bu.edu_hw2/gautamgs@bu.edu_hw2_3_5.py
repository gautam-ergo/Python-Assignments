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
import math as q

n = input("Enter the number of sides:")
s = input("Enter the side:")
area = ((float(n)*float(s)**2)/(4*q.tan(q.pi/float(n))))

print("The area of the polygon is ",area)
print ("\nEnd of Program\n")
