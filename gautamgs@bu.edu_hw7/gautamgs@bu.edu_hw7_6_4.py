"""
CS 521 Information Structures with Python
#########################################
Module          - HW 7
Creation Date   - 11/07/2018
Student Name    - Gautam Gowrishankar

"""
def reverse(number):
    rev = number[::-1]
    print("Reversed integer: ",*rev, sep='')

try:
    inp = input("Enter an integer: ")
    if int(inp):
        inp = list(map(int, str(inp)))
        reverse(inp)
except Exception as e:
    print("Error:",str(e))

print("\n -End of Program- ")
