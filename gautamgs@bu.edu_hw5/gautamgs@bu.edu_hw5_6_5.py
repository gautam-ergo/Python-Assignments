"""
CS 521 Information Structures with Python
#########################################
Module          - HW 5
Creation Date   - 10/17/2018
Student Name    - Gautam Gowrishankar

"""
def displaySortedNumbers(num1, num2, num3):
    inp=[]
    inp.extend((num1, num2, num3))
    inp.sort()
    print ("Sorted Numbers - ",inp)
try:
    x,y,z = [float(x) for x in input("Enter three numbers (separated by ,):").split(",")]
    displaySortedNumbers(x,y,z)
except:
    print("Input only Integers")

print("\n -End of Program- ")
