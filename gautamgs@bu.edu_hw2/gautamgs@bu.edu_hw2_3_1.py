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

radius = input("Enter Center to Vertex length:")
s = (2*float(radius))*(q.sin(q.pi/5))
a = ((3*q.sqrt(3))/2)*(s**2)
print("The area of the pentagon is {0:1.2f}".format(a))
print ("\nEnd of Program\n")
