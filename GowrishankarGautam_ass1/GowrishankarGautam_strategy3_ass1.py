# -*- coding: utf-8 -*-
"""
CS 677 Data Science with Python
#########################################
Module          - HW 1
Creation Date   - 02/03/2018
Student Name    - Gautam Gowrishankar

Intent:
    To try and create a profitable strategy using Adjusted Closing price of a ticker.
Note:Using the pandas modified version of source file 'GPS_MOD'
"""
import datetime
import os
import csv
from statistics import median,mean

#Logic: after W consecutive declines, buy on day W ($150) and sell on W+1 day.
def performTrading(window):
    dayCount = 0
    numberOfShares = 0

    for i in range(1, maxRow):
        if window < maxRow - i:
            if float(lines[i][10]) < 0:
                dayCount += 1
            else:
                dayCount = 0
            if window == dayCount:
                numberOfShares = 150//float(lines[i][9])
                revenue = (numberOfShares*float(lines[i+1][9])) - (numberOfShares*float(lines[i][9]))
                if revenue > 0:
                    profit.append(float(revenue))
                else:
                    loss.append(float(revenue))
        else:
            break


ticker='GPS'
input_dir = r'/Users/arun/Downloads/CS677 - PY/'
input_file = os.path.join(input_dir, ticker + '_Mod.csv')

#List of +ve and -ve trades
profit = []
loss = []

#Read input file and process it
with open(input_file) as f:
    lines = f.read().splitlines()
    maxRow = len(lines)
for row in range(len(lines)):
    lines[row] = lines[row].split(",")


print("\nWith an Investment of $150, arrived at the following figures:\n")
print("Window   Trades   Profit Trades   Average Profit   Losing Trades  Average Loss")
try:
    for day in range(1, 6):
        performTrading(day)
        print(day,"day\t",len(profit)+len(loss),"\t ",len(profit), "\t\t ",round(mean(profit),4),"\t\t",len(loss),"\t ", round(mean(loss),3))
        profit *= 0
        loss *= 0

except Exception as e:
    print("Error:",str(e))

print("\n -End of Program- ")
