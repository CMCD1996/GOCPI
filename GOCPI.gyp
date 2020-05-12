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
countries = file.readlines()
file.close()

# Creates array from Continent Data
file = open("Continents.txt","rt")
continents = file.readlines()
file.close()

# Creates array of world cities
data = pd.read_csv("Cities.csv")
data.dropna(inplace = True)
cities = list(data['city'])
#print(cities)

# Creates arrays for of cities for relevant countries
cities_countries = list(data['country'])
unique_countries = list(dict.fromkeys(cities_countries))

print(unique_countries)

for i in unique_countries:
    i = list()
    for j in cities_countries:
        if i == j:
            i.append(cities[countries.index(j)])
            print(cities[countries.index(j)])


            
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


