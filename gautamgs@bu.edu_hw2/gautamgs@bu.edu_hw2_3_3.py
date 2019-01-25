"""
CS 521 Information Structures with Python
#########################################
Module          - HW 2
Creation Date   - 09/25/2018
Student Name    - Gautam Gowrishankar

Intent:
    To llustrate the Mathematical functionality.
"""

#For Displaying the current version of Python
import platform
import math as M

print ("Python version being used for this code - ", platform.python_version(),'\n')


#Input variables
EARTH_RADIUS = 6371.01
atlantaY =  M.radians(-84.3879824)
atlantaX = M.radians( 33.7489954)
orlandoY = M.radians( -81.3792364999)
orlandoX = M.radians( 28.5383355)
SavannahY = M.radians( -81.09983419999998)
SavannahX = M.radians( 32.0835407)
charlotteY = M.radians( -80.84312669999997)
charlotteX = M.radians( 35.2270869)

#function to calculate distance
def distance( x1,  y1,  x2,  y2):
    return (EARTH_RADIUS * M.acos(M.sin(x1) * M.sin(x2) + M.cos(x1) * M.cos(x2) * M.cos(y1 - y2)))


#Triangle 1
a2s = distance(atlantaX, atlantaY, SavannahX, SavannahY)
s2c = distance(SavannahX, SavannahY, charlotteX, charlotteY)
c2a = distance(charlotteX, charlotteY, atlantaX, atlantaY)
#Triangle 2
a2o = distance(atlantaX, atlantaY, orlandoX, orlandoY)
o2s = distance(orlandoX, orlandoY, SavannahX, SavannahY)
s2a = distance(SavannahX, SavannahY, atlantaX, atlantaY)
#Area
s1 = (a2s + s2c + c2a) / 2
s2 = (a2o + o2s + s2a) / 2
area1 = M.sqrt(s1 * (s1 - a2s) * (s1 - s2c) * (s1 - c2a))
area2 = M.sqrt(s2 * (s2 - a2o) * (s2 - o2s) * (s2 - s2a))

print("Triangle formed by Atlanta,Savannah,Orlando - %.3f" %area2)
print("Triangle formed by Atlanta,Savannah,Charlotte - %.3f" %area1)
print ("Combined area of 4 cities - %.3f" %(area1+area2))
print ("\nEnd of Program\n")
