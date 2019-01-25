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

def add(m, j):
    sum = 0
    for i in range(len(m)):
        sum = sum + m[i][j]
    return sum

#processing input
inp = []
for f in range(3):
    rows = [float(x) for x in input("Enter a 3-by-4 matrix for row " + str(f)+" (separated by space):").split(" ")]
    inp.append(rows)

#loop through the inputs
count = len(inp) + 1
for x in range(count):
    print("Sum of Elements in column ",str(x)," is", add(inp, x))

print("\n -End of Program- ")
