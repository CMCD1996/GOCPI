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
import pathlib as pl
import os
import pydrive

# Load in the EnergyBalance.csv file found from the University of Auckland SourceOECD Database.
# This csv contains the energy balances around the world

# Loads in appropriate pydrive functions for access
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Creates the authorisation to access the google drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Gains authorisation using the clients_secrets.json file in the src directory
# Creates a google drive object to handle files
drive = GoogleDrive(gauth)

# Tests the access to the google drive
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'],file1['id']))

#EB_df = pd.read_csv(f)
#EB_df.head()
