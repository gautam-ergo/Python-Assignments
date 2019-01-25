
"""
CS 521 Information Structures with Python
#########################################
Module          - HW 3
Creation Date   - 10/01/2018
Student Name    - Gautam Gowrishankar

Intent:
    To illustrate file manipulation.
"""

#Importing all the necessary pkg
import platform
import pathlib as p
print ("Python version being used for this code - ", platform.python_version(),'\n')

#show an "Open" dialog box and return the path to the selected file
from tkinter import Tk
from tkinter.filedialog import askopenfilename
print("Select the file ")
Tk().withdraw()
file = p.Path(askopenfilename())

print("File Location - ",file)
word = input("Enter the string to be removed (Case sensitive): ")
found = 'N'
temp = []

#proceed to process the file
if not file.exists():
    print("File Does Not Exist")
else:
    try:
        fil = open(file, 'r')
        print("File opened..")
        for line in fil:
            if word in line:
                line = line.replace(word, " ")
                found = 'Y'
            temp.append(line)
        fil.close()
        if found == 'Y':
           new = open(file, 'w')
           print("Replacing...")
           for line in temp:
               new.write(line)
           new.close()
           print("Done")
        else:
            print("String not found in file.")
    except IOError:
        print("Something Went Wrong")

print("\n -End of Program- ")
