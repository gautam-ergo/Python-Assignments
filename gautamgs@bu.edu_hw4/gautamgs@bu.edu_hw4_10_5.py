"""
CS 521 Information Structures with Python
#########################################
Module          - HW 4
Creation Date   - 10/10/2018
Student Name    - Gautam Gowrishankar

"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')
try:
    num = [int(x) for x in input("Enter ten numbers (separated by space):  ").split(" ")]
    distinct = str(set(num))
    print ("The distinct numbers are:",distinct[1:-1])
except:
    print("Please Enter Valid Integers")

print("\n -End of Program- ")
