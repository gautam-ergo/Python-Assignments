
"""
CS 521 Information Structures with Python
#########################################
Module          - HW 3
Creation Date   - 10/01/2018
Student Name    - Gautam Gowrishankar

Intent:
    To illustrate the mathematical functionality.
"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')

a,b,c = input("enter a, b, c: ").split(",")
a = float(a)
b = float(b)
c = float(c)

#checking the discriminant
def real(a, b, c):
    dis = (b**2)-(4*a*c)

    if dis < 0:
        print("The equation has no real roots")
    else:
        return dis


discri = real(a, b, c)

#caculating the roots
def roots(a, b, c, discri):

    x = ((-b)+(discri**0.5))/(2*a)
    y = ((-b)-(discri**0.5))/(2*a)

    if x == y:
        print("The root is {0:1.2f}".format(x))
    else:
        print("The roots are", x, "and", y)

if discri != None:
    roots(a, b, c, discri)

print("\n -End of Program- ")
