# -*- coding: utf-8 -*-
"""
CS 677 Data Science with Python
#########################################
Module          - HW 2
Creation Date   - 10/03/2018
Student Name    - Gautam Gowrishankar
"""
import csv
import os
import numpy as np
import sklearn.metrics
import math
from statistics import stdev,mean,median

#Declare Variables
actual = []
predicted = []

ticker='GPS'
input_dir = r'/Users/arun/Downloads/CS677 - PY/'
input_file = os.path.join(input_dir, ticker + '_digit_analysis.csv')


#Read input file and process it
with open(input_file) as f:
    lines = f.read().splitlines()
    maxRow = len(lines)
for row in range(len(lines)):
    lines[row] = lines[row].split(",")

for i in range(1,len(lines)):
    actual.append(float(lines[i][2]))
    predicted.append(float(lines[i][3]))

#Max absolute error
absError = np.abs(np.subtract((np.array(actual)), (np.array(predicted))))
print('\nMaximum absolute error:',str(round(max(absError), 4)))
#Median absolute error
print('Median absolute error:',str(round(median(absError), 4)))
#Root mean squared error
print('Root mean squared error:',str(round(math.sqrt(sklearn.metrics.mean_squared_error(actual, predicted)), 4)))
#Mean absolute error
print('Mean absolute error:' ,str(round(sklearn.metrics.mean_absolute_error(actual, predicted), 4)))
print("\n -End of Program- ")
