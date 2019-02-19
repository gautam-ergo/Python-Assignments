# -*- coding: utf-8 -*-
"""
CS 677 Data Science with Python
#########################################
Module          - HW 1
Creation Date   - 02/03/2018
Student Name    - Gautam Gowrishankar

Intent:
    To try and create a profitable strategy using Adjusted Closing price of a ticker.
"""
import datetime
import os
import csv
from statistics import median,mean

#Logic:
#If adj close > s_ma then buy
#Else sell
def performTrading(lines):
    stockBought = False
    records = []
    for i in range(1, maxRow):
        if stockBought == False: #Buy it!!
            if lines[i][adjClose] > lines[i][shortMA]:
                stockCost = float(lines[i][adjClose])
                numberOfShares = 150 // stockCost
                stockBought = True
        else:#sell stock
            if lines[i][adjClose] <= lines[i][shortMA]:
                revenue = (float(lines[i][adjClose]) * float(numberOfShares)) - (float(stockCost) * float(numberOfShares))
                if revenue > 0:
                    profit.append(float(revenue))
                else:
                    loss.append(float(revenue))
                stockBought = False

ticker='GPS'
input_dir = r'/Users/arun/Downloads/CS677 - PY/'
input_file = os.path.join(input_dir, ticker + '_Mod.csv')

#List of +ve and -ve trades
profit = []
loss = []
try:
#Read input file and process it
    with open(input_file) as f:
        lines = f.read().splitlines()
        maxRow = len(lines)
    for row in range(len(lines)):
        lines[row] = lines[row].split(",")

    #identify indexes
    adjClose = lines[0].index("Adj Close")
    shortMA = lines[0].index("Short_MA")

    #Processing
    print("\nWith an Investment of $150, arrived at the following figures:\n")
    print("Trades   Profit Trades    Average Profit   Losing Trades  Average Loss")
    performTrading(lines)
    print(len(profit)+len(loss),"\t",len(profit), "\t\t ",round(mean(profit),3),"\t\t",len(loss),"\t", round(mean(loss),3))
    profit *= 0
    loss *= 0

except Exception as e:
    print("Error:",str(e))

print("\n -End of Program- ")
