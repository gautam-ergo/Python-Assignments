"""
CS 521 Information Structures with Python
#########################################
Module          - HW 5
Creation Date   - 10/17/2018
Student Name    - Gautam Gowrishankar

"""
def formPentagon(n):
    return n*(3 * n-1 )/2;
print("Pentagon Numbers - \n")
for x in range(1,101):
    if (x % 10) == 0:
        print('%6d' % (formPentagon(x)))
    else:
        print('%6d' % (formPentagon(x)),end='|')

print("\n -End of Program- ")
