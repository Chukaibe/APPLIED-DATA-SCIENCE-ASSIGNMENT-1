# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 15:05:55 2023

@author: MUSTANG
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file into a DataFrame
cs = pd.read_csv("Crime_Statistics.csv")
print(cs)
print()

# Create a pivot table to get separate columns for each type of crime
crime = cs.pivot(index='Year', columns='Type of Crime', 
                       values='Number of Crimes')

# Create a line chart
plt.plot(crime.index, crime['Assault'], label='Assault')
plt.plot(crime.index, crime['Burglary'], label='Burglary')
plt.plot(crime.index, crime['Robbery'], label='Robbery')
plt.plot(crime.index, crime['Vehicle Theft'], label='Vehicle Theft')
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.legend()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file into a DataFrame
cs = pd.read_csv("Crime_Statistics.csv")

# Group the data by type of crime and sum the number of crimes for each type
crime = cs.groupby('Type of Crime')['Number of Crimes'].sum()

# Create a bar chart
plt.bar(crime.index, crime)
plt.xlabel('Type of Crime')
plt.ylabel('Number of Crimes')
plt.title('Total Number of Crimes by Type')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file into a DataFrame
cs = pd.read_csv("Crime_Statistics.csv")


# Create a dataframe with the crime data
crime_df = pd.read_csv('Crime_Statistics.csv')

# Group the dataframe by Type of Crime and sum the Number of Crimes for each group
crime_sum = cs.groupby('Type of Crime')['Number of Crimes'].sum()

# Print the crime sums for each type
print(crime_sum)

crime = ["Assault", "Burglary", "Robbery", "Vehicle Theft"]
# summary of total crime
cap = np.array([43964, 44139, 21766, 29407])
# pie chart for the four crimes
plt.figure()
plt.pie(cap, labels=crime, autopct='%1.1f%%')
plt.show()