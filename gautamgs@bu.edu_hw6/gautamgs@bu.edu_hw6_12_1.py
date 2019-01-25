"""
CS 521 Information Structures with Python
#########################################
Module          - HW 6
Creation Date   - 10/28/2018
Student Name    - Gautam Gowrishankar

"""
import math


class GeometricObject:
    def __init__(self):
        self.color = 'black'
        self.filled = 0

    def getColor(self):
        return self.color

    def getFilled(self):
        return self.filled

    def setColor(self, color):
        self.color = color

    def setFilled(self, filled):
        self.filled = filled

class Triangle(GeometricObject):
    def __init__(self):
        super().__init__()
        self.side1 = 1.0
        self.side2 = 1.0
        self.side3 = 1.0

    def setSides(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getArea(self):
        s = (self.side1+self.side2+self.side3)/2
        area = math.sqrt(s * (s-self.side1) * (s-self.side2) * (s-self.side3))
        return area

    def getPerimeter(self):
        return (self.side1+self.side2+self.side3)

    def __str__(self):
        output = ("Triangle:\nside1 = " + str(self.side1) + "\nside2 = " + str(self.side2)
                  + "\nside3 = " + str(self.side3)+"\ncolor = "+self.color)
        output = output+"\tFilled = "

        if(self.filled == 0):
            output = output + "No"
        else:
            output = output+"Yes"
        return output

try:
  a,b,c = [float(x) for (x) in input("Enter 3 sides(separated by comma) of the triangle - ").split(",")]
  color = str(input("Enter the desired color - "))
  fill = int(input("Filled/Not Filled: Choose 1 for Filled and 0 for Non filled - "))
  tri = Triangle()
  tri.setSides(a, b, c)
  tri.setColor(color)
  tri.setFilled(fill)
  print(tri, "\nArea  = %.3f"%(tri.getArea()), "   Perimeter = %.3f"%(tri.getPerimeter()))
except Exception as e:
    print ("Error:",str(e))
finally:
    print("\n-End of Program-")
