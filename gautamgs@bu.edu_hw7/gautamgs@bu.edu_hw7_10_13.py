"""
CS 521 Information Structures with Python
#########################################
Module          - HW 7
Creation Date   - 11/07/2018
Student Name    - Gautam Gowrishankar

"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')

def eliminateDuplicates(lst):
    print ("The distinct numbers are:",*(set(lst)),sep = ' ')

try:
    num = [int(x) for x in input("Enter ten numbers (separated by space):  ").split(" ")]
    eliminateDuplicates(num)
except Exception as e:
    print("Error:",str(e))

print("\n -End of Program- ")
