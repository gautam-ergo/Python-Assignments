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
    num = [int(x) for x in input("Enter Integer between 1 and 100 (separated by space):  ").split(" ")]

    a = dict((x,num.count(x)) for x in set(num))
    for num,occur in a.items():
        if occur == 1:
           print(num,"occurs",occur,"time")
        else:
           print(num,"occurs",occur,"times")
except:
    print("Please Enter Valid Integers")

print("\n -End of Program- ")
