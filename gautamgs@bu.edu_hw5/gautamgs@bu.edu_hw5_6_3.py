"""
CS 521 Information Structures with Python
#########################################
Module          - HW 5
Creation Date   - 10/17/2018
Student Name    - Gautam Gowrishankar

"""
def isPalindrome(*args):
    if str(org) == str(rev):
        return True;

def reverse(number):
    rev = number[::-1]
    return rev

try:
    inp = input("Enter an integer: ")
    if int(inp):
        org = list(map(int, str(inp)))
        rev = reverse(org)
        if isPalindrome(org,rev):
            print("Palindrome indeed..")
        else:
            print("Not a Palindrome..")
except:
    print("Input only integers..")

print("\n -End of Program- ")
