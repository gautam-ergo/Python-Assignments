"""
CS 521 Information Structures with Python
#########################################
Module          - HW 6
Creation Date   - 10/28/2018
Student Name    - Gautam Gowrishankar

"""
class LinearEquation(object):
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def isSolvable(self):
        return ((self.a * self.d) - (self.b * self.c)) != 0

    def getX(self):
        return ((self.e * self.d) - (self.b * self.f)) / ((self.a * self.d) - (self.b * self.c))

    def getY(self):
        return ((self.a * self.f) - (self.e * self.c)) / ((self.a * self.d) - (self.b * self.c))


def main():
    try:
        a, b, c, d, e, f = [float(x) for x in input("Enter a, b, c, d, e, f (separated by comma): ").split(",")]
        eqn = LinearEquation(a, b, c, d, e, f)
        if eqn.isSolvable():
            print("The Roots are %.3f"%(eqn.getX()), "and %.3f"%(eqn.getY()))
        else:
            print('The equation has no solution.')

    except Exception as e:
        print("Please Enter an Integer,",e)


main()
print("\n -End of Program- ")
