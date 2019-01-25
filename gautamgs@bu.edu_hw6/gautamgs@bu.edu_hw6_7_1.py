"""
CS 521 Information Structures with Python
#########################################
Module          - HW 6
Creation Date   - 10/28/2018
Student Name    - Gautam Gowrishankar

"""
class Rectangle:
    def __init__(self, w=1, h=2):
        self.width = w
        self.height = h

    def getArea(self):
        return self.width*self.height

    def getPerimeter(self):
        return 2*(self.width+self.height)


width = 4
height = 40
print("\nHeight - ",str(height))
print("Width - ",str(width))
rect = Rectangle(width, height)
print('The area of the rectangle is', rect.getArea())
print('The perimeter of the rectangle is', rect.getPerimeter())

width = 3.5
height = 35.7
print("\nHeight - ",str(height))
print("Width - ",str(width))
rect = Rectangle(width, height)
print('The area of the rectangle is %.2f'%(rect.getArea()))
print('The perimeter of the rectangle is', rect.getPerimeter())
print("\n -End of Program- ")
