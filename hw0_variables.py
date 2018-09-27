""" 
CS 521 Information Structures with Python
#########################################
Module          - HW 0
Creation Date   - 09/10/2018
Student Name    - Gautam Gowrishankar

Intent:
    A basic program to illustrate the different types of Data types
    available in python.
"""

#For Displaying the current version of Python
import platform
print ("Python version being used - ", platform.python_version(),'\n')


#Variable Classifications
print ('Following are the data types in Python: \n')
intA = 1
print ('Variable intA =',intA,'\n Is of type >>', type(intA),'stored at ',id(intA),'\n')
fltF = 3.14
print ('Variable fltF =',fltF,'\n Is of type >>', type(fltF),'stored at ',id(fltF),'\n')
strS = 'Python'
print ('Variable strS =',strS,'\n Is of type >>', type(strS),'stored at ',id(strS),'\n')
cpxC = 1j
print ('Variable cpxC =',cpxC,'\n Is of type >>', type(cpxC),'stored at ',id(cpxC),'\n')
tupT = (1,2,'Py')
print ('Variable tupT =',tupT,'\n Is of type >>', type(tupT),'stored at ',id(tupT),'\n')
lstL = ['Py',1]
print ('Variable lstL =',lstL,'\n Is of type >>', type(lstL),'stored at ',id(lstL),'\n')
bolB = True
print ('Variable bolB =',bolB,'\n Is of type >>', type(bolB),'stored at ',id(bolB),'\n')        
setE = set([1,2])
print ('Variable setE =',setE,'\n Is of type >>', type(setE),'stored at ',id(setE),'\n')
dicD = {"module":"Python"}
print ('Variable dicD =',dicD,'\n Is of type >>', type(dicD),'stored at ',id(dicD),'\n\n End of Program')
