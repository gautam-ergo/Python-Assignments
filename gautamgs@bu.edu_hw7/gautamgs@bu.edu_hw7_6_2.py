"""
CS 521 Information Structures with Python
#########################################
Module          - HW 7
Creation Date   - 11/07/2018
Student Name    - Gautam Gowrishankar

"""
def sumDigits(n):
    inp = list(map(int, str(n)))
    print("Sum of the digits is:",sum(inp))

try:
    inp = input("Enter an integer: ")
    if int(inp):
        sumDigits(inp)
except Exception as e:
    print("Error:",str(e))

print("\n -End of Program- ")
