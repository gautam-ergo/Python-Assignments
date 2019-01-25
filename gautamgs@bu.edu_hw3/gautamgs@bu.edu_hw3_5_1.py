"""
CS 521 Information Structures with Python
#########################################
Module          - HW 3
Creation Date   - 09/18/2018
Student Name    - Gautam Gowrishankar

Intent:
    To llustrate the loop functionality.
"""

#For Displaying the current version of Python
import platform
print ("Python version being used for this code - ", platform.python_version(),'\n')

#variables
inp = []
pos_cnt = 0
neg_cnt = 0

#Processing inputs
while (True):
    try:
        x = int(input("Enter an integer, the input ends if it is 0: "))
        if(x == 0):
            break
        inp.append(x)
        if (x > 0):
            pos_cnt += 1
        elif (x < 0):
            neg_cnt += 1
    except ValueError:
        print("Not an integer")

if inp != []:
    print("The number of positives is", pos_cnt)
    print("The number of negative is", neg_cnt)
    print("The total is", sum(inp))
    print("The average is", sum(inp)/(pos_cnt + neg_cnt))
else:
    print("You didn't enter any number. No inputs to process..")

print("\n -End of Program- ")
