from pandas import DataFrame, read_csv
import matplotlib.pyplot as pyplot
import pandas as pd
import sys
import matplotlib
import datetime


# print('Python version ' + sys.version)
# print('Pandas version ' + pd.__version__)
# print('Matplotlib version ' + matplotlib.__version__)

# names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
# births = [968, 155, 77, 578, 973]

# BabyDataSet = list(zip(names, births))
# print(BabyDataSet)

# df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
# print(df)

# df.to_csv('births1880.csv', index=False, header=True)

# Location = r'.\births1880.csv'
# df = pd.read_csv(Location)
# print(df) 

# How to get range of datetime
# Method 1

# Create data frame
# df = pd.DataFrame()

# Create datetimes
# df['date'] = pd.date_range('1/1/2001', periods=100000, freq='H')

# Select observations etween two datetimes
# selected = df[(df['date'] > '2002-1-1 01:00:00') & (df['date'] <= '2002-1-1 04:00:00')]

# print(selected)

# Set index
# df = df.set_index(df['date'])

# Select observations between two datetimes
# selected = df.loc['2002-1-1 01:00:00' : '2002-1-1  04:00:00']

# print(selected)

df = pd.read_csv("randomTimePrice.csv")
print(df)

selected = df[(df['Time']) > '20/08/25 00:00']
print(selected)

currentDate = datetime.datetime.now()
print(currentDate.strftime("%y/%m/%d %H:%M"))