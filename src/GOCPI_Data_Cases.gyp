# GOCPI_Data_Cases is a methodology to import scenario data
# across multiple files. These are the
# sets and parameters for the Energy System Optimisation Model.
# A python script was chosen over other storage methods (e.g. excel)
# as values can be stored in matrices and many values are configured differently

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
import GOCPI as GF

# Sets sets
YEAR = ['1990','1991','1992','1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']
REGION = ['UTOPIA','TOPIA','DYSTOPIA','NEW ZEALAND', 'AUSTRALIA','CANADA']
EMISSION = ['CO2','NOX','CO','METHANE']
TECHNOLOGY = ['E01','E21','E31','E51','E70','IMPDSL1','IMPGSL1','IMPHCO1','IMPOIL1','IMPURN1', 'RHE','RHO','RL1','SRE','TXD','TXE','TXG','RIV','RHu','RLu','TXu']
FUEL = ['CSV','DSL','ELC','GSL','HCO','HYD','LTH','OIL','URN','RH','RL','TX']
TIMESLICE = ['ID','IN','SD','SN','WD','WN']
MODE_OF_OPERATION = ['1','2']
STORAGE = ['DAM']
DAYTYPE = ['Dummy']
SEASON = ['Dummy']
DAILYTIMEBRACKET = ['Dummy']

# Sets 
sets = [YEAR,REGION, EMISSION, TECHNOLOGY, FUEL, TIMESLICE, MODE_OF_OPERATION, STORAGE,DAYTYPE,SEASON,DAILYTIMEBRACKET]

# Create the energy system with sets and initialised parameters. The parameter have the necessary parameters
Demo = GF.Energy_Systems(YEAR,REGION, EMISSION, TECHNOLOGY, FUEL, TIMESLICE, MODE_OF_OPERATION, STORAGE,DAYTYPE,SEASON,DAILYTIMEBRACKET)

# This user must now initialise the parameters as they choose to configure the energy system for the optimisation model.
# This is incredibly important. The user must understand the configuration of the energy system to do this! Consult the
# User manual to build this optimisation.

# End of user defined inputs in this script

# Sets the textfile saved locations
data_txt = 'GOCPI_OseMOSYS_Data.txt'
root = '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Inputs/GOCPI OseMOSYS'
data_roots = Path(root)
data_location = os.path.join(data_roots,data_txt)

Demo.EmissionActivityRatio = np.ones(Demo.EmissionActivityRatio.shape)
default_parameters = {'YearSplit':0, 'DiscountRate':0, 'DaySplit':0, 'Conversionls':0, 'Conversionld':0, 'Conversionlh':0, 'DaysInDayType':0,
        'TradeRoute':0, 'DepreciationMethod':0, 'SpecifiedAnnualDemand':0, 'SpecifiedDemandProfile':0, 'AccumulatedAnnualDemand':0,
        'CapacityToActivityUnit':0, 'CapacityFactor':0, 'AvailabilityFactor':0, 'OperationalLife':0, 'ResidualCapacity':0, 'InputActivityRatio':0,
        'OutputActivityRatio':0, 'CapitalCost':0, 'VariableCost':0, 'FixedCost':0 , 'TechnologyToStorage':0 , 'TechnologyFromStorage':0, 'StorageLevelStart':0,
        'StorageMaxChargeRate':0, 'StorageMaxDischargeRate':0, 'MinStorageCharge':0, 'OperationalLifeStorage':0, 'CapitalCostStorage':0, 
        'ResidualStorageCapacity':0, 'CapacityOfOneTechnologyUnit':0, 'TotalAnnualMaxCapacity':0, 'TotalAnnualMinCapacity':0, 'TotalAnnualMaxCapacityInvestment':0,
        'TotalAnnualMinCapacityInvestment':0, 'TotalTechnologyAnnualActivityLowerLimit':0, 'TotalTechnologyAnnualActivityUpperLimit':0, 
        'TotalTechnologyModelPeriodActivityUpperLimit':0, 'TotalTechnologyModelPeriodActivityLowerLimit':0, 'ReserveMarginTagTechnology':0,
        'ReserveMarginTagFuel':0, 'ReserveMargin':0, 'RETagTechnology':0, 'RETagFuel':0, 'REMinProductionTarget':0, 'EmissionActivityRatio':0,
        'EmissionsPenalty':0, 'AnnualExogenousEmission':0, 'AnnualEmissionLimit':0, 'ModelPeriodExogenousEmission':0,'ModelPeriodEmissionLimit':0}

# default_parameters

Demo.CreateDataFile(data_location,default_parameters)


# # EmissionActivityRatio = np.zeros((lr,lt,le,lm,ly))
# # Sets default for the function
# default  = 0
# with open(data_location,'w') as f:
#     #Writes new line character at parameter metadata to the text file
#     f.write('#\n')
#     f.write('param\tEmissionActivityRatio\tdefault\t%s:\n'%default)
#     # Writes parameter values to the text files
#     for i in range(Demo.le):
#         # Sets index value for format string
#         emission = Demo.emission[i]
#         for j in range(Demo.lm):
#             # Sets index value for format string
#             MOO = Demo.mode_of_operation[j]
#             for k in range(Demo.ly):
#                 # Sets index value for format string
#                 y = Demo.year[k]
#                 # Converts matrix columns to strings columns to strings
#                 columns = Demo.technology
#                 column_string = ' '.join(columns)
#                 # Converts maxtrix rows to list
#                 array = np.array(Demo.region)
#                 array = array.T
#                 lt = array.tolist()
#                 # Creates 2D matrix for this value
#                 mat = Demo.EmissionActivityRatio[:,:,i,j,k]
#                 # Converts combined matrix to list and combines lists
#                 matlist = mat.tolist()
#                 #Combines the two lists
#                 combined_list = list(zip(lt,matlist))
#                 # Writes index specific parameter values to the text files 
#                 f.write("\t[*,*,{0},{1},{2}]:\t{3}\t:=\n".format(emission,MOO,y,column_string))
#                 for line in combined_list:
#                     combinedflat = ''.join(str(line))
#                     combinedflat = combinedflat.replace('[','')
#                     combinedflat = combinedflat.replace(']','')
#                     combinedflat = combinedflat.replace("'",'')
#                     combinedflat = combinedflat.replace(",",'')
#                     combinedflat = combinedflat.replace("(",'')
#                     combinedflat = combinedflat.replace(")",'')
#                     f.write("{0}\n".format(combinedflat))

#     f.write(';\n')
            


 

