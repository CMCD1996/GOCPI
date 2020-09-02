# GOCPI_Inputs is a file processing script. This script prepare the spreadsheets for VEDA processing to
# be feed into the GAMS Optimisation
# This script was adpated into the GOCPI module

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

# Very Important Step: Set directory root for file operations.
source_root = Path(
    '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Inputs'
)
print(source_root)


# Finds a file within a function
def Find_File(target_root, target_file):
    for root, dirs, files in os.walk(target_root):
        for name in files:
            if name == target_file:
                f = os.path.abspath(os.path.join(root, name))
    return f


# Defines custom functions necessary for excel script processing
# Set_Values updates single cell inputs for the VEDA spreadsheet
def Set_Values(source_root, source_file, source_sheet, source_range,
               updated_value, destination_file):
    from openpyxl import load_workbook
    from pathlib import Path
    # Finds the source file from the assign root directory
    f = Find_File(source_root, source_file)
    # Performs the workbook manipulation and updates values
    workbook = load_workbook(filename=f)
    sheet = workbook[source_sheet]
    defined_range = workbook.defined_names[source_range]
    split_string = defined_range.attr_text.split('$')
    address = split_string[1] + split_string[2]
    sheet[str(address)].value = updated_value
    # Finds the destination file
    f = Find_File(source_root, destination_file)
    # Saves the updated file
    workbook.save(filename=f)


# Initialises all variables in the System Settings. These are created in arrays and interated through via for loops.

# Book Region_Maps (Number of Regions Base Sheet Mechanics relate to,
# This will be expanded upon depending on the sets of geographies to be included.
# We will begin with two regions (Based off TIMES Demo Model 12)s
REG1 = 'REG1'  # Ideally two selected Regions (New Zealand)
REG2 = 'REG2'  # (Australia)

# Timeslices
SZN1 = "S"  # Summer
SZN2 = "W"  # Winter
DN1 = "D"  # Day
DN2 = "N"  # Night

# Time Periods
StartYear = 2030

# ActivePDef
# This variable defines how split up the forecast period into smaller time intervals
# Pdef-1 is a two period definition (1 Year then 2 years for a total of 3 years)
# Pdef-5 is a 5 period definition of 1,2,5,5,5 year periods respectively.
# Pdef-11 is an 11 period definition of 1,2,5,5,5,5,5,5,5,5,5 year periods respectively.
# Pdef-1,5 and 11 are the only available options at the moment.
APDEF = "Pdef-11"

#Import Settings have been left unchanged in the SysSettings Sheet. See the import
# settings for a proper definition

# Interpolation and Extrapolation Defaults are unchanged as well. See details in the
# System settings spreadsheet if you want to make changes.

# Constants for the modelling process in the modelling sheet
# (TFM_INS)
GDY = StartYear  # Discount Year
Discount = 0.05  # Discount Rate (This discount rate will change depending on the region in question
# Figure out how to vary dicount rates depending on financial inputs)

# Fraction of year for season and day/night level (Should change depending on the geography)
# Determine how to make these changes after you get a baseline model running
REG_Num_Sum_Days = 175
REG_Num_Days = 365
REG_Num_Win_Days = (REG_Num_Days - REG_Num_Sum_Days)
Frac_REG_Num_Sum_Days = REG_Num_Sum_Days / REG_Num_Days
Frac_REG_Num_Win_Days = REG_Num_Win_Days / REG_Num_Days

Sum_Hours_Per_Day = 12.5
Win_Hours_Per_Day = 11.5
Hours_Per_Day = 24

Frac_Sum_Hours_Per_Day = Sum_Hours_Per_Day / (Hours_Per_Day)
Frac_Win_Hours_Per_Day = Sum_Hours_Per_Day / (Hours_Per_Day)
Frac_Sum_Hours_Per_Night = (1 - Frac_Sum_Hours_Per_Day)
Frac_Win_Hours_Per_Night = (1 - Frac_Win_Hours_Per_Day)

SD_YRFR = Frac_REG_Num_Sum_Days * Frac_Sum_Hours_Per_Day
SN_YRFR = Frac_REG_Num_Sum_Days * Frac_Sum_Hours_Per_Night
WD_YRFR = Frac_REG_Num_Win_Days * Frac_Win_Hours_Per_Day
WN_YRFR = Frac_REG_Num_Win_Days * Frac_Win_Hours_Per_Night

# Currency for investment decisions underpinning the model
CUR = "MEuro05"

# Default Units (Review and come back to this commodity part of the model)
# Explicitly Commodity Groups are not required in the modelling process at this stage.

# Creates a function to update the spreadsheet relative to those feed in to the function
# Inserts the various cells in python as required
# Imports the various functions needed for the file

source_file = "SysSettings.xlsm"
source_sheet = "TimePeriods"
source_range = "StartYear"
updated_value = StartYear
destination_file = "SysSettings.xls"

# Update the StartYear
Set_Values(source_root, source_file, source_sheet, source_range, updated_value,
           destination_file)
