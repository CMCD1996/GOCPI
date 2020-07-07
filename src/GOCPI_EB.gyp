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
folderID = '1MD5ewAKAy2McqyCfjivwavj278giRvmR' # Energy Balance

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

#Gets link to the two file wanted
link = '1dHSJuPkgqTHhZtiD-iKSTEsMWkecbnC-' # File IDs for IEA Energy Balances for 2017

fileID = 'https://drive.google.com/file/d/' + link
source_file = source_root/'IEAEnergyBalance2017.xlsm'
# Links for IEA Energy Balance for 2018 (A-K) and IEA Energy Balance for 2017 (L-Z)

# Imports Pandas process IEA World Energy Statistics and Balances CSVs from Stats.OECD.org in the OECDiLibrary
# Note the data is from #https://stats.oecd.org/ and #https://www-oecd-ilibrary-org.ezproxy.auckland.ac.nz/
print(fileID)
df_A = pd.read_excel(source_file,sheet_name = 'A',index_col = 0,header = 0)


