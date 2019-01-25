"""
CS 521 Information Structures with Python
#########################################
Module          - HW 5
Creation Date   - 10/17/2018
Student Name    - Gautam Gowrishankar

"""
def sum( num ):
    if num == 0:
        return 0
    return (num % 10 + sum(int(num / 10)))

try:
    inp = int(input("Enter an integer:"))
    print("Sum of the digits in",inp,"is %s"%(sum(inp)))
except:
    print("Input only integers..")

print("\n -End of Program- ")
