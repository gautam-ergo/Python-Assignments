# -*- coding: utf-8 -*-
"""
CS 677 Data Science with Python
#########################################
Module          - HW 1
Creation Date   - 02/03/2018
Student Name    - Gautam Gowrishankar

Intent:
    To try and create a profitable strategy using Adjusted Closing price of a ticker.
Note: Did not modify the source stock file using pandas.
"""
import os
import csv
import datetime
from statistics import median,mean

ticker='GPS' # GAP retail Inc
#input_dir = r'/Users/arun/Downloads/CS677 - PY/'
input_dir = '/Users/arun/Downloads/CS677 - PY/Python-Assignments/GowrishankarGautam_ass1/'
input_file = os.path.join(input_dir, ticker + '.csv')

# Calculating the percent change based on Adj Close.
# Range of input list starts from 1 rather than 0,
# Output in the format - [('Monday',0.3456),('Tuesday',-2.1111)]
def calPercentChange(lis):
    outList = list((lis[i][0],float((((lis[i][1]- lis[i-1][1])/lis[i-1][1])*100))) for i in range(1,len(lis)))
    outList.append((lis[0][0],0))   # making sure we include the first value in the series as well
    return outList

try:
    with open(input_file) as f:
        inpFile = csv.DictReader(f, delimiter=',')

        #Now that we have the input file, Creating a list of tuples in the format
        #[('Monday',12.3456),('Tuesday',21.1111)]
        adjClose_daywise = list((datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%a'),y) for x,y in
                                        (list((val["Date"],float(val["Adj Close"])) for val in inpFile)))

        returns = calPercentChange(adjClose_daywise)

        #Calculating min,max,median,mean based on daily returns
        minDaywise = dict((days, min([v for (k,v) in returns if k == days])) for days in dict(returns).keys())
        maxDaywise = dict((days, max([v for (k,v) in returns if k == days])) for days in dict(returns).keys())
        medianDaywise = dict((days, median([v for (k,v) in returns if k == days])) for days in dict(returns).keys())
        meanDaywise = dict((days, mean([v for (k,v) in returns if k == days])) for days in dict(returns).keys())

        #Do the honors
        print("\nDay\tMin(Returns)\tMax(Returns)\tAverage(Returns)\tMedian(Returns)")
        for day,value in dict(returns).items():
            print(day,"\t%1.2f\t\t%1.2f\t\t%1.2f\t\t\t%1.2f" %(minDaywise[day],maxDaywise[day],meanDaywise[day],medianDaywise[day]))


except Exception as e:
    print("Error:",str(e))

print("\n -End of Program- ")
