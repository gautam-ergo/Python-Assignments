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


#Census Calculation
secnds = (365*24*3600)
birth  = secnds/7
death  = secnds/13
immig  = secnds/45
exist  = 312032486
people  = birth + immig - death
print("Existing Population - ", str(exist))
for x in range(1,6):
    newpop  = people + exist
    print("\n At the End of Year ", x, "-", str(int(newpop)))
    exist = newpop
    
print("\n -End of Program- ")
