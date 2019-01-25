"""
CS 521 Information Structures with Python
#########################################
Module          - HW 7
Creation Date   - 11/07/2018
Student Name    - Gautam Gowrishankar

"""
def isSorted(lst):
    if sorted(lst) == lst:
       print ("List is already Sorted..")
    else:
        print ("List is not Sorted..")

try:
    inp = [int(x) for x in input("Enter list of numbers (separated by ,):").split(",")]
    isSorted(inp)
except Exception as e:
    print("Error:",str(e))

print("\n -End of Program- ")
