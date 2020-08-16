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
import cplex as cp
import docplex as dp

# Creates sets for the demo model
YEAR = [
    '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998',
    '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
    '2008', '2009', '2010'
]
REGION = ['NEWZEALAND', 'AUSTRALIA']
EMISSION = ['CO2', 'NOX', 'CO', 'METHANE']
TECHNOLOGY = [
    'E01', 'E21', 'E31', 'E51', 'E70', 'IMPDSL1', 'IMPGSL1', 'IMPHCO1',
    'IMPOIL1', 'IMPURN1', 'RHE', 'RHO', 'RL1', 'SRE', 'TXD', 'TXE', 'TXG',
    'RIV', 'RHu', 'RLu', 'TXu'
]
FUEL = [
    'CSV', 'DSL', 'ELC', 'GSL', 'HCO', 'HYD', 'LTH', 'OIL', 'URN', 'RH', 'RL',
    'TX'
]
TIMESLICE = [
    'INTERMEDIATE_DAY', 'INTERMEDIATE_NIGHT', 'SUMMER_DAY', 'SUMMER_NIGHT',
    'WINTER_DAY', 'WINTER_NIGHT'
]
MODE_OF_OPERATION = ['1', '2']
STORAGE = ['DAM']
DAYTYPE = ['1', '2', '3']
SEASON = [
    '1', '2', '3', '4'
]  # Must be denoted in numbers to match constraints in model (1: Summer, 2: Autumn, 3: Winter, 4): Spring)
DAILYTIMEBRACKET = ['1', '2', '3']

# Sets
sets = [
    YEAR, REGION, EMISSION, TECHNOLOGY, FUEL, TIMESLICE, MODE_OF_OPERATION,
    STORAGE, DAYTYPE, SEASON, DAILYTIMEBRACKET
]

# Create the energy system with sets and initialised parameters. The parameter have the necessary parameters
Demo = GF.Energy_Systems(YEAR, REGION, EMISSION, TECHNOLOGY, FUEL, TIMESLICE,
                         MODE_OF_OPERATION, STORAGE, DAYTYPE, SEASON,
                         DAILYTIMEBRACKET)

# This user must now initialise the parameters as they choose to configure the energy system for the optimisation model.
# This is incredibly important. The user must understand the configuration of the energy system to do this! Consult the
# User manual to build this optimisation.

# End of user defined inputs in this script

# Sets the textfile saved locations
data_txt = 'GOCPI_OseMOSYS_Data.txt'
model_source_file = 'GOCPI_OseMOSYS_Structure.xlsx'
root = '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Inputs/GOCPI OseMOSYS'
data_roots = Path(root)
data_location_1 = os.path.join(data_roots, data_txt)

# Dictionary of default parameters for creating a model file
default_parameters = {
    'YearSplit': 1,
    'DiscountRate': 1,
    'DaySplit': 1,
    'Conversionls': 1,
    'Conversionld': 1,
    'Conversionlh': 1,
    'DaysInDayType': 1,
    'TradeRoute': 1,
    'DepreciationMethod': 1,
    'SpecifiedAnnualDemand': 1,
    'SpecifiedDemandProfile': 1,
    'AccumulatedAnnualDemand': 1,
    'CapacityToActivityUnit': 1,
    'CapacityFactor': 1,
    'AvailabilityFactor': 1,
    'OperationalLife': 1,
    'ResidualCapacity': 1,
    'InputActivityRatio': 1,
    'OutputActivityRatio': 1,
    'CapitalCost': 1,
    'VariableCost': 1,
    'FixedCost': 1,
    'TechnologyToStorage': 1,
    'TechnologyFromStorage': 1,
    'StorageLevelStart': 1,
    'StorageMaxChargeRate': 1,
    'StorageMaxDischargeRate': 1,
    'MinStorageCharge': 1,
    'OperationalLifeStorage': 1,
    'CapitalCostStorage': 1,
    'ResidualStorageCapacity': 1,
    'CapacityOfOneTechnologyUnit': 1,
    'TotalAnnualMaxCapacity': 1,
    'TotalAnnualMinCapacity': 1,
    'TotalAnnualMaxCapacityInvestment': 1,
    'TotalAnnualMinCapacityInvestment': 1,
    'TotalTechnologyAnnualActivityLowerLimit': 1,
    'TotalTechnologyAnnualActivityUpperLimit': 1,
    'TotalTechnologyModelPeriodActivityUpperLimit': 1,
    'TotalTechnologyModelPeriodActivityLowerLimit': 1,
    'ReserveMarginTagTechnology': 1,
    'ReserveMarginTagFuel': 1,
    'ReserveMargin': 1,
    'RETagTechnology': 1,
    'RETagFuel': 1,
    'REMinProductionTarget': 1,
    'EmissionActivityRatio': 1,
    'EmissionsPenalty': 1,
    'AnnualExogenousEmission': 1,
    'AnnualEmissionLimit': 1,
    'ModelPeriodExogenousEmission': 1,
    'ModelPeriodEmissionLimit': 1
}

# Create the Data File
Demo.create_data_file(data_location_1, default_parameters)

# Cereate the Model File
Demo.create_model_file(root, model_source_file)

# Convert created model and data files into a Linear Problem file (lp)
# Test the formatting
