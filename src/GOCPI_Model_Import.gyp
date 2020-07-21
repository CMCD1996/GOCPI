# GOCPI_Model_Import is a file processing script. This script prepares the text files from an Excel spreadsheet
# for the user defined energy systems model.

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
import openpyxl
import pathlib
import os
from pathlib import Path
from openpyxl import load_workbook
import GOCPI_Functions as GF

# Custom functions necessary for this step
# Finds a file within a function
def Find_File(target_root,target_file):
    for root, dirs, files in os.walk(target_root):
        for name in files:
            if name == target_file:
                f = os.path.abspath(os.path.join(root, name))
    return f
# End of custom functions

# Beginning of scripting
# Very Important Step: Set directory root for file operations.
model_roots = Path('/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Inputs/GOCPI OseMOSYS')

# sets strings as excel file names for the model and parameter data.
model_file = 'GOCPI_OseMOSYS_Structure.xlsx'
data_file = 'GOCPI_OseMOSYS_Structure.xlsx'

# Finds the files necessary to create pandas dataframes.
# model = Find_File(model_roots,model_file)
Location = GF.Navigation(model_roots,model_file)
model = Location.Find_File()

# data = Find_File(data_file,model_file)
df = pd.read_excel(model,sheet_name = 'Model')

# Creates a new dataframe based on the variables on the Include column values
df_Include = df[df.Include == 'Yes']
df_model = df_Include[['Name']].copy()

# Creates a file location and write the model to a text file
model_txt = 'GOCPI_OseMOSYS_Model.txt'
model_location = os.path.join(model_roots,model_txt)

# Saves the user defined model to a text file
np.savetxt(model_location,df_model.values,fmt = '%s')

'/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI'
'/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/src/GOCPI_Functions'
