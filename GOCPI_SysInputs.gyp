# This is for setting the core system inputs for GOCPI to feed into the data models

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

# This script is the master inputs script for the display of sheets
# Initialises all variables in the System Settings
# Book Region_Maps (Number of Regions Base Sheet Mechanics relate to, 
# This will be expanded upon depending on the sets of geographies to be included.
# We will begin with two regions
REG1 = 'REG1'
REG2 = 'REG2'

# Timeslices
SZN1 = "S" # Summer
SZN2 = "W" # Winter
DN1 = "D" # Day
DN2 = "N" # Night

# Time Periods
StartYear = 2020

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
GDY = StartYear # Discount Year
Discount = 0.05 # Discount Rate (This discount rate will change depending on the region in question
# Figure out how to vary dicount rates depending on financial inputs)

# Fraction of year for season and day/night level (Should change depending on the geography)
# Determine how to make these changes after you get a baseline model running
REG_Num_Sum_Days = 175
REG_Num_Days = 365
REG_Num_Win_Days = (REG_Num_Days - REG_Num_Sum_Days)
Frac_REG_Num_Sum_Days = REG_Num_Sum_Days/REG_Num_Days
Frac_REG_Num_Win_Days = REG_Num_Win_Days/REG_Num_Days

Sum_Hours_Per_Day = 12.5
Win_Hours_Per_Day = 11.5
Hours_Per_Day = 24

Frac_Sum_Hours_Per_Day = Sum_Hours_Per_Day/ (Hours_Per_Day)
Frac_Win_Hours_Per_Day = Sum_Hours_Per_Day/ (Hours_Per_Day)
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