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


#Pi approximation
x = 4 * (1-(1/3)+(1/5)-(1/7)+(1/9)-(1/11))
print ("Pi approximation \n First Result is %.3f" %x)

y = x + 4 * ((1/13)-(1/15))
print ("\n Second Result is %.3f" %y)
print("\n-End of Program-\n")
