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
print(df.columns)
# Creates a new dataframe based on the variables on the Include column values
df_Include = df[df.Include == 'Yes']
df_model = df_Include[['Name']].copy()

# Creates a file location and write the model to a text file
model_txt = 'GOCPI_OseMOSYS_Model.txt'
model_location = os.path.join(model_roots,model_txt)

# Saves the user defined model to a text file
np.savetxt(model_location,df_model.values,fmt = '%s')

# Creates array of parameters from select sets and functions
df_Include = df[df.Include == 'Yes']
df_target_sets = df_Include[df.Type == "Sets"]
df_sets = df_target_sets[['Name']].copy()
df_target_parameters = df_Include[df.Type == "Parameters"]
df_parameters = df_target_parameters[['Name']].copy()

# Reviews what sets and parameters must the user input for the optimisation model
print(df.head())
print(df_sets.head())
print(df_parameters.head())

# Creates the relevent input ranges for the various models
