"""
CS 521 Information Structures with Python
#########################################
Module          - HW 4
Creation Date   - 10/10/2018
Student Name    - Gautam Gowrishankar

"""
from keyword import kwlist #contains all the python keywords
import platform
import pathlib as p
print ("Python version being used for this code - ", platform.python_version(),'\n')

#show an "Open" dialog box and return the path to the selected file
from tkinter import Tk
from tkinter.filedialog import askopenfilename
print("Select the file ")
Tk().withdraw()
file = p.Path(askopenfilename())
temp = []

print("File Location - ",file)

#proceed to process the file
if not file.exists():
    print("File Does Not Exist")
else:
    try:
        infile = open(file, 'r')
        text = infile.read().split()
        print("Searching for Keywords..")
        for word in text:
            if word in kwlist:
                temp.append(word)
        infile.close()
        if bool(temp):
           kwrds = {x:temp.count(x) for x in temp}
           for kwrds,count in kwrds.items():
               print("Keyword '"+kwrds+"' occurs",count,"time(s)")
        else:
            print("No Keywords in file")
    except:
        print("Program Aborted..")

print("\n -End of Program- ")
