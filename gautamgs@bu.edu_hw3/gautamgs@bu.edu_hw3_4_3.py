"""
CS 521 Information Structures with Python
#########################################
Module          - HW 3
Creation Date   - 10/01/2018
Student Name    - Gautam Gowrishankar

Intent:
    To illustrate the math functionality.
"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')

#input
try:
    a, b, c, d, e, f = [float(x) for x in input("Enter a, b, c, d, e, f here: ").split(",")]
except:
    print("Correct the input values. Expecting only numbers as input.")

#check if the denominator is zero
def ifZero(a, b, c, d):
    x = (a * d)-(b * c)

    if x == 0:
        print("The equation has no solution")
    else:
        return x

#cramers rule form
def calculate(a, b, c, d, e, f, denominator):
    x = (((e * d)-(b * f))/denominator)
    y = (((a * f)-(e * c))/denominator)
    print("x is", x, "and y =", y)


denominator = ifZero(a, b, c, d)
if denominator != None:
    calculate(a, b, c, d, e, f, denominator)

print("\n -End of Program- ")
