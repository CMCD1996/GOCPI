# GOCPI_EB prepares the energy balance across time for certain geographies

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
import openpyxl as pyxl
import pathlib
import os
import pydrive


# Very Important Step: Sets directory root for file operations.
source_root = pathlib.Path('/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Energy Balances')

# Load in the EnergyBalance.csv file found from the University of Auckland SourceOECD Database.
# This csv contains the energy balances around the world

# Important Step: Sets the Energy Balances Folder ID in my personal google drive
folderID = '1PCUMeT8c9dJE1ES8JDg62w2rKMASOxSW' # Energy Balance

# Loads in appropriate pydrive functions for access
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# # Creates the authorisation to access the google drive
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Gains authorisation using the clients_secrets.json file in the src directory
# # Creates a google drive object to handle files
# drive = GoogleDrive(gauth)

# # Tests the access to the google drive and finds all IEAEnergyBalances.csv File IDs in the EnergyBalances Directory
# file_list = [] 
# title_list = []
# files = drive.ListFile({'q': "'1MD5ewAKAy2McqyCfjivwavj278giRvmR' in parents and trashed=false"}).GetList()
# for filex in files:
#     print(filex['id'])
#     print(filex['title'])
#     file_list.append(filex['id'])  # IEAEnergyBalance.csvs File IDs
#     title_list.append(filex['title']) # IEAEnergyBalance.csvs Titles

# Gets the linksto the two files wanted 
# Links for IEA Energy Balance for 2018 (A-K) and IEA Energy Balance for 2017 (L-Z)
IEAWEBAK = source_root/'IEAWorldEnergyBalances2017A-K.csv'
IEAWEBLZ = source_root/'IEAWorldEnergyBalances2017L-Z.csv'

# Creates dataframes from IEA World Energy Statistics and Balances CSVs from Stats.OECD.org in the OECDiLibrary
# Note the data is from #https:s//stats.oecd.org/ and #https://www-oecd-ilibrary-org.ezproxy.auckland.ac.nz/
column_headers = ['ID','Unit','Geo_Code','Geo_Description','Prod_Code','Prod_Description','Flow_Code','Flow_Description','Year','Value(TJ)']
f1 = open(IEAWEBAK,'r')
df_A = pd.read_csv(f1,header = None)
df_A.columns = column_headers
df_A.info(verbose = True)
f2 = open(IEAWEBLZ,'r')
df_B = pd.read_csv(f2,header = None)
df_B.columns = column_headers
df_B.info(verbose = True)
frames = [df_A,df_B]
df = pd.concat(frames)
df.info(verbose = True)

# Closes the files
f1.close()
f2.close()

# Find the unique items in each list of the energy balance sheets
uv_prod = df.Prod_Description.unique()
uv_geo = df.Geo_Description.unique()
uv_flow = df.Flow_Description.unique()

# Establishes the rows and columns for the EnergyBalance.xlsm spreadsheet
# Note: Most likely in the calculation, Other will be a sink so Total Energy Supply - Conversion Losses = Total Energy Consumed
# Rows (Energy uses)
Primary = ['Domestic Supply','Imports','Exports','Total Primary Supply']
Conversion = ['Energy Sector Consumption','Electricity Plants','Heat Plants','Petroluem Refineries','Total Conversion']
Consumption = ['Residential','Commercial','Industry','Agriculture','Transport','Other','Non Energy','Bunkers','Total Final Consumption']

#  Columns (Energy Types)
Energy = ['Solid Fuels', 'Natural Gas', 'Crude Oil','Diesel Oil','Kerosene','LPG','Motor Spirit','Naphtha','Heavy Fuel Oil','Other Petroleum Products','Nuclear Energy','Biomass','Hydro power','Wind energy','Solar Energy','Industrial Wastes','Derived Heat','Electricity','Total']

# Creates lists of all the sources
# Primary
DomesticSupply = ['Production']
Imports = ['Imports']
Exports = ['Exports']
TotalPrimarySupply = ['Total primary energy supply']

# Conversion (To complete)

# Consumption (To complete)

# Creates a pivot table to display the data in the way similar to the Energy Balance Sheet (cols = Energy Product, rows = Energy Flows)
EBPT = pd.pivot_table(df,index=['Geo_Description','Flow_Description'],values=['Value(TJ)'],columns=['Prod_Description'],aggfunc=[np.sum],fill_value=0)
# Filters to the geography the user has selected
Selected_Geo = uv_geo[0] # Update once turned into a custom function
Input_String = 'Geo_Description == ["'+ Selected_Geo +'"]'
EBPTG = EBPT.query(Input_String)
print(EBPTG)
# Write the filtered pivot table to an excel file
writer = pd.ExcelWriter(source_root/"Geo EB.xlsx")
EBPTG.to_excel(writer,Selected_Geo) 
writer.save()












