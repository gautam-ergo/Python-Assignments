# -*- coding: utf-8 -*-
"""
CS 677 Data Science with Python
#########################################
Module          - HW 2
Creation Date   - 10/03/2018
Student Name    - Gautam Gowrishankar
"""
import os
import pandas as pd
import math
import numpy as np
import random
from mlxtend.frequent_patterns import apriori

input_dir = r'/Users/arun/Downloads/CS677 - PY/'
input_file  = os.path.join(input_dir, 'BreadBasket_DMS_output.csv')


def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

def busiest(df,colName):
    print("Busiest",colName,"at the Bakery was",df.groupby(df[colName]).size().idxmax(),
          "when a total of",df.groupby(df[colName]).size().max(),"transactions occured.");
    profitable = df["Item_Price"].groupby(df[colName]).sum().reset_index(name='counts').max()
    print("Profitable ",colName,"at the Bakery was",df["Item_Price"].groupby(df[colName]).sum().idxmax(),
          "when a total of $",round(df["Item_Price"].groupby(df[colName]).sum().max(),3),"transactions occured.");

df = pd.read_csv(input_file)

print("\nFollowing are the inferences from the Bakery Dataset:\n")
for colName in ['Hour','Weekday','Period']:
    busiest(df,colName)
    print("")

#Most popular item
print("\nMost Popular item -",df.groupby(df["Item"]).size().idxmax(),
           "which has been bought",df.groupby(df["Item"]).size().max(),"times");

#Least popular item
leastPopular = df['Item'].value_counts()
leastPopular = leastPopular[leastPopular == leastPopular.min()].dropna()
leastPopular = leastPopular.index.tolist()
print('Least Popular items - ' + ', '.join(leastPopular),
             "which has been bought",df.groupby(df["Item"]).size().min(),"time");


#Most and least popular combination of 2 items
encodedDF = df.groupby(['Transaction', 'Item'])['Item'].count().unstack().reset_index().fillna(0).set_index('Transaction').applymap(encode_units)
boughtTogether = apriori(encodedDF, min_support=0.00001, use_colnames=True, max_len=2)
boughtTogether['length'] = boughtTogether['itemsets'].apply(lambda x: len(x))
boughtTogether = boughtTogether[(boughtTogether['length'] == 2)]
popularCombo = boughtTogether['itemsets'].at[boughtTogether['support'].sort_values(ascending = False).idxmax()]
print('Most popular combination of two items: ', end='')
print([x for x in popularCombo])
print('Least popular combination of two items: ',
     boughtTogether['itemsets'].at[boughtTogether['support'].sort_values(ascending = False).idxmin()],"\n")


#Number of barristas for each day of the week, 1 barrista:60 transactions
trans = df.groupby('Weekday')['Transaction'].nunique()
df["Date"] = df["Year"].map(str) + df["Month"].map(str) + df["Day"].map(str)
days = df.groupby('Weekday')['Date'].nunique()
trans = trans/days
baristas = trans/60
for k,v in dict(baristas).items():
    print(k,"requires",int(np.ceil(v)),"baristas")

#Divide all items into 3 groups - drinks, food, unknown
df['Type'] = 'unknown'
food = ['Bread', 'Jam', 'Cookies', 'Muffin', 'Pastry', 'Medialuna', 'Tartine', 'Basket', 'Farm House', 'Fudge', "Ella's Kitchen Pouches", 'Victorian Sponge', 'Frittata', 'Pick and Mix Bowls', 'Cake', 'Chicken sand', 'Focaccia', 'Sandwich', 'Eggs', 'Brownie', 'Granola', 'Empanadas', 'Bowl Nic Pitt', 'Bread Pudding', 'Truffles', 'Bacon', 'Spread', 'Kids biscuit', 'Caramel bites', 'Jammie Dodgers', 'Tiffin', 'Olum & polenta', 'Polenta', 'Bakewell', 'Toast', 'Scone', 'Crepes', 'Vegan mincepie', 'Bare Popcorn', 'Muesli', 'Crisps', 'Pintxos', 'Panatone', 'Brioche and salami', 'Salad', 'Chicken Stew', 'Spanish Brunch', 'Raspberry shortbread sandwich', 'Extra Salami or Feta', 'Duck egg', 'Baguette', 'Vegan Feast', 'Nomad bag', 'Chocolates', 'Half slice Monster ', 'Cherry me Dried fruit', 'Raw bars', 'Tacos/Fajita']
drink = ['Hot chocolate', 'Coffee', 'Tea', 'Mineral water', 'Juice', 'Soup', 'Smoothies', 'Mighty Protein', 'Coke', 'My-5 Fruit Shoot', 'Dulce de Leche', 'Honey', 'Chimichurri Oil', 'Lemon and coconut', 'Mortimer']
df['Type'] = np.where(df['Item'].isin(food), 'food', df['Type'])
df['Type'] = np.where(df['Item'].isin(drink), 'drink', df['Type'])

#Average price of a drink and Number of drinks per transaction (Group size)
dfCopy = df.copy()
dfCopy = dfCopy[dfCopy['Type'] == 'drink']
drinkCost = dfCopy['Item_Price'].mean()
drinkPrice = dfCopy['Item_Price'].sum()
print('\nAverage price of a drink is $' , str(round(drinkCost, 2)))
print('Average number of drinks per transaction: ',np.ceil(dfCopy.groupby(['Transaction'])['Type'].agg('count').mean()))


#Average price of a food item
dfCopy = df.copy()
dfCopy = dfCopy[dfCopy['Type'] == 'food']
foodCost = dfCopy['Item_Price'].mean()
foodPrice = dfCopy['Item_Price'].sum()
print('Average price of a food item is $',str(round(foodCost, 2)))

#Drinks vs Food items, the more profitable one
print('Food items are more profitable' if foodPrice > drinkPrice else 'Drinks are more profitable')


#Top 5 and Botttom 5 items by popularity
popItems = df['Item'].value_counts().sort_values(ascending = False).head(5)
popItems = popItems.index.tolist()
leastpopItems = df['Item'].value_counts().sort_values(ascending = True).head(5)
leastpopItems = leastpopItems.index.tolist()
print('\nFive most popular items: '+ ', '.join(popItems))
print('Five least popular items: ' + ', '.join(leastpopItems))


#Day of the week, hour, day period at which most popular items are sold
df = df[df['Item'].isin(popItems)]
print('\nWeekday at which most popular items are sold: ', df.groupby(['Weekday'])['Item'].agg('count').idxmax())
print('Hour at which most popular items are sold:',df.groupby(['Hour'])['Item'].agg('count').idxmax(),
      'am' if  df.groupby(['Hour'])['Item'].agg('count').idxmax() < 12 else 'p.m')
print('Period at which most popular items are sold: ',df.groupby(['Period'])['Item'].agg('count').idxmax())
print("\n -End of Program- ")
