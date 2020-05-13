# This is a demo file for organising geographies and controlling demo functions.
# Import useful python packages
# Git reposistory
# https://github.com/CMCD1996/GOCPI.git
# Make more changes from the pull request
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import scipy as sc 
import sklearn as skl 
import csv as csv

# Create python list for geogrpahies, starting with countries
# Create an empty list
countries = []

# Creates a geography set
geography_set = [['AFRICA'],
                ['ASIA'],
                ['EUROPE'],
                ['NORTH AMERICA'],
                ['OCEANIA'],
                ['SOUTH AMERICA']]

continents = ['AFRICA','ASIA','EUROPE','NORTH AMERICA','OCEANIA','SOUTH AMERICA']

# Sets up a for loop to append countries to the continents in the geography set
file = open('Country and Continent.txt','r')
for line in file:
    string = line.split('\n')
    string = string[0].split(',')
    countries.append(string[1].upper())
    for i in range(0,6,1):
        if string[0].upper() == geography_set[i][0]:
            geography_set[i].append(string[1].upper())

# This code block is to inform count 
with open('countries.csv', 'w') as file:
    writer = csv.writer(file, delimiter = ',')
    writer.writerow(countries)
file.close()

# Creates array of world cities
data = pd.read_csv("Cities.csv")

cities_df = pd.concat([data['city'],data['country'],data['population']],axis = 1)
cities_df['continent'] = ""
cities_df.dropna(inplace = True)

# Capitalises country and city names
cities_df['country'] = cities_df['country'].str.upper()
cities_df['city'] = cities_df['city'].str.upper()

# Place the continent required in the row
for index, row in cities_df.iterrows():
    for i in range(0,6,1):
        for j in range(0,len(geography_set[i]),1):
            if geography_set[i][j] == row['country']:
                cities_df.at[index,'continent'] = geography_set[i][0]

# Save dataframe as new CSV
cities_df.to_csv('geography_set.csv',index=False)

# Expand the geography_set to include new files
