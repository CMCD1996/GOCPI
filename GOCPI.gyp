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
country_code = []

# Creates array from Countrie Data
file = open("Countries.txt","rt")
countries = file.read()
countries = countries.split('\n')
file.close()

# Creates array from Continent Data
file = open("Continents.txt","rt")
continents = file.read()
continents = continents.split(',')
print(continents)
file.close()

# Creates array of world cities
data = pd.read_csv("Cities.csv")
data.dropna(inplace = True)
cities_df = pd.concat([data['city'],data['country']],axis = 1)

# Create continents lists
#print(continents)

# Creates arrays for of cities for relevant countries
cities_countries = list(data['country'])
cities_df['cities_countries'] =  cities_countries
unique_countries = list(dict.fromkeys(cities_countries))

# Create a dictionary to output file
with open('Unique Countries.txt',"w") as file:
    for country in unique_countries:
        file.write("%s \n" % country)

cities = list(data['city'])



# Creates arrays for of cities for relevant countries
cities_countries = list(data['country'])
cities_df['cities_countries'] =  cities_countries
unique_countries = list(dict.fromkeys(cities_countries))



# Create new columns with the cities and Countries
# data.drop(['city_ascii', 'lat','lng','iso2','iso3','admin_name','capital','population'],axis =1)

# Puts each word into an array
# for word in file:
#     word.split('|')
#     #country_code.append(a)
#     #countries.append(b)
# #print(count(word))
# for i in countries:
#     print(i)
#     print("\n")


