"""
CS 521 Information Structures with Python
#########################################
Module          - HW 6
Creation Date   - 10/28/2018
Student Name    - Gautam Gowrishankar

"""
import math


class RegularPolygon:

    def __init__(self, n=3, side=1, x=0, y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def getN(self):
        return self.__n

    def getSide(self):
        return self.__side

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setN(self, n):
        self.__n = n

    def setSide(self, side):
        self.__side = side

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getArea(self):
        return (self.__n * pow(self.__side, 2)) / (4 * math.tan(math.pi/self.__n))

    def getPerimeter(self):
        return self.__n * self.__side


polygon = RegularPolygon()
print("\n Polygon 1: \n Area: %.3f"%(polygon.getArea()) +
      " \n Perimeter: ",polygon.getPerimeter())
polygon = RegularPolygon(6, 4)
print("\n Polygon 2: RegularPolygon(6, 4)\n Area: %.3f"%(polygon.getArea()) +
      " \n Perimeter: ",polygon.getPerimeter())
polygon = RegularPolygon(10, 4, 5.6, 7.8)
print("\n Polygon 3: RegularPolygon(10, 4, 5.6, 7.8)\n Area: %.3f"%(polygon.getArea()) +
      " \n Perimeter: ",polygon.getPerimeter())
print("\n -End of Program- ")
