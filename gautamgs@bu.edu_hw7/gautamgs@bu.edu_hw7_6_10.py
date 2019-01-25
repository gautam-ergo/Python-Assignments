"""
CS 521 Information Structures with Python
#########################################
Module          - HW 7
Creation Date   - 11/07/2018
Student Name    - Gautam Gowrishankar

"""
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:#and number != divisor:
            return False
        divisor += 1
    return True # number is prime

count = 0
for x in range (2,10000):
    if isPrime(x):
        count +=1
print("Number of Prime Numbers less than 10,000:",count)
print("\n -End of Program- ")
