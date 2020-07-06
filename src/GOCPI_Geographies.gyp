# GOCPI_Geographies Structures the data in a way
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
import pathlib
import os

# Very Important Step: Sets directory root for file operations.
source_root = pathlib.Path('/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Geographies')

# Finds the relevant files needed to create csvs with the relationships between cities, countries and continents
# Finds a file within a function
def Find_File(target_root,target_file):
    for root, dirs, files in os.walk(target_root):
        for name in files:
            if name == target_file:
                f = os.path.abspath(os.path.join(root, name))
    return f

# Find the necessary files for the geography conversions
f1 = Find_File(source_root,"Country and Continent.txt")
f2 = Find_File(source_root,"countries.csv")
f3 = Find_File(source_root,"Cities.csv")
f4 = Find_File(source_root,"geography_set.csv")

# Creates python list for geographies, starting with countries
# Creates an empty list
countries = []

# Creates a geography set
geography_set = [['AFRICA'],
                ['ASIA'],
                ['EUROPE'],
                ['NORTH AMERICA'],
                ['OCEANIA'],
                ['SOUTH AMERICA']]
continents = ['AFRICA','ASIA','EUROPE','NORTH AMERICA','OCEANIA','SOUTH AMERICA']

# Sets up a for loop to append countries to the continents in the geography sets
file = open(f1,'r')
for line in file:
    string = line.split('\n')
    string = string[0].split(',')
    countries.append(string[1].upper())
    for i in range(0,6,1):
        if string[0].upper() == geography_set[i][0]:
            geography_set[i].append(string[1].upper())

# This code block is to inform count 
with open(f2, 'w') as file:
    writer = csv.writer(file, delimiter = ',')
    writer.writerow(countries)
file.close()

# Creates array of world cities
data = pd.read_csv(f3)
cities_df = pd.concat([data['city'],data['country'],data['population']],axis = 1)
cities_df['continent'] = ""
cities_df.dropna(inplace = True)

# Capitalises country and city names
cities_df['country'] = cities_df['country'].str.upper()
cities_df['city'] = cities_df['city'].str.upper()

# Places the continent required in the row
for index, row in cities_df.iterrows():
    for i in range(0,6,1):
        for j in range(0,len(geography_set[i]),1):
            if geography_set[i][j] == row['country']:
                cities_df.at[index,'continent'] = geography_set[i][0]

# Saves dataframe as new CSV
cities_df.to_csv(f4,index=False)

