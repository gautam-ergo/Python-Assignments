# -*- coding: utf-8 -*-
"""
CS 677 Data Science with Python
#########################################
Module          - HW 2
Creation Date   - 10/03/2018
Student Name    - Gautam Gowrishankar
"""
import csv
import numpy as np
from statistics import stdev,mean
import os

#Declare variables
returns = []
count = 0

ticker='GPS'
input_dir = r'/Users/arun/Downloads/CS677 - PY/'
input_file = os.path.join(input_dir, ticker + '_Mod.csv')

try:

    #Read input file and process it
    with open(input_file) as f:
        lines = f.read().splitlines()
        maxRow = len(lines)
    for row in range(len(lines)):
        lines[row] = lines[row].split(",")

    #Populate returns
    for i in range(1,maxRow):
        returns.append(float(lines[i][10]))

    #Define the tails of ditribution
    leftBound = mean(returns) - (2 * stdev(returns))
    rightBound = mean(returns) + (2 * stdev(returns))

    for i in range(len(returns)):
        if returns[i] < leftBound or returns[i] > rightBound:
            count += 1

    print("\n",str(round(count/(len(lines) - 1), 2)*100),"% of days are beyond two standard deviations from the mean")

    if round((count/(len(lines) - 1)), 2) <= 0.05:
        print("The returns are normally distributed")
    if round((count/(len(lines) - 1)), 2) > 0.05:
        print("The returns are not normally distributed")

except Exception as e:
    print("Error:",str(e))

print("\n -End of Program- ")
