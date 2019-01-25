"""
CS 521 Information Structures with Python
#########################################
Module          - HW 3
Creation Date   - 10/01/2018
Student Name    - Gautam Gowrishankar

Intent:
    To illustrate the try/catch functionality.
"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')

#Check if the input is valid.
try:
    inp = [int(x) for x in input("Enter SSN in the format ddd-dd-dddd: ").split("-")]
    if len(str(inp[0])) != 3 or len(str(inp[1])) != 2 or len(str(inp[2])) != 4:
            print("Invalid SSN. Correct the format.")
    else:
            print("Valid SSN")
except:
    print("Invalid SSN. Enter only Digits.")

print("\n -End of Program- ")
