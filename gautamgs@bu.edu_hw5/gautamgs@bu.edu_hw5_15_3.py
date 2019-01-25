"""
CS 521 Information Structures with Python
#########################################
Module          - HW 5
Creation Date   - 10/17/2018
Student Name    - Gautam Gowrishankar

"""
def gcd(x,y):
    if x % y == 0:
        return y
    return (gcd(y, x % y))
print("G.C.D of two numbers:\n")
try:
    a,b = (int(x) for x in input("Enter two numbers (separated by ,): ").split(","))
    print("G.C.D of",a,"and",b,"is %s"%(gcd(a,b)))
except:
    print("Input only integers..")

print("\n -End of Program- ")
