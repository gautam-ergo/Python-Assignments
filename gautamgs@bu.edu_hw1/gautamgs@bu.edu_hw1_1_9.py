""" 
CS 521 Information Structures with Python
#########################################
Module          - HW 1
Creation Date   - 09/18/2018
Student Name    - Gautam Gowrishankar

Intent:
    Using Python to Perform Mathematical Computations

"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')


#Area and Permiter Calculation
width  = 4.5
height = 7.9
area   = width * height
print ("Area of the Rectangle = {0:10.2f}".format(area))
perimerter = (2 * width)+(2 * height)
print ("Perimeter of the Rectangle = {0:10.2f}".format(perimerter))
print ("\nEnd of Program \n")
