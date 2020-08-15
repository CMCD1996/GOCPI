# GOCPI_NZ_Example.gyp is an exemplar script in how to build a
# data case for the Model

# Import all necessary python packages
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

# Sets sets (All must be one word)
# Creates a New Zealand Energy System Scenario using the CreateCases Module
nz_energy_system = GF.CreateCases()

# Creates the set for all the sets

# Defines the forecast period
nz_energy_system.set_year(2020, 2030, 1)
print(nz_energy_system.year)

# Defines the regions
REGION = ['NEWZEALAND', 'AUSTRALIA']
nz_energy_system.set_region(REGION)
print(nz_energy_system.region)

# Defines the Emissions
EMISSION = ['CO2', 'NOX', 'CO', 'METHANE']
nz_energy_system.set_emission(EMISSION)
print(nz_energy_system.emissions)

# Defines the technology set
TECHNOLOGY = [
    'E01', 'E21', 'E31', 'E51', 'E70', 'IMPDSL1', 'IMPGSL1', 'IMPHCO1',
    'IMPOIL1', 'IMPURN1', 'RHE', 'RHO', 'RL1', 'SRE', 'TXD', 'TXE', 'TXG',
    'RIV', 'RHu', 'RLu', 'TXu'
]
nz_energy_system.set_technology(TECHNOLOGY)
print(nz_energy_system.technology)

# Defines the fuels set
FUEL = [
    'CSV', 'DSL', 'ELC', 'GSL', 'HCO', 'HYD', 'LTH', 'OIL', 'URN', 'RH', 'RL',
    'TX'
]
nz_energy_system.set_fuel(FUEL)
print(nz_energy_system.fuel)

# Defines timeslices
TIMESLICE = [
    'DAY_SUMMER', 'NIGHT_SUMMER', 'DAY_WINTER', 'NIGHT_WINTER',
    'DAY_INTERMEDIATE', 'NIGHT_INTERMEIATE'
]
nz_energy_system.set_timeslice(TIMESLICE)
print(nz_energy_system.timeslice)

# Defines Modes of Operation
nz_energy_system.set_mode_of_operation(2)
print(nz_energy_system.mode_of_operation)

# Defines the storage set
STORAGE = ['DAM']
nz_energy_system.set_storage(STORAGE)
print(nz_energy_system.storage)

# Defines the daytype (numbers represent different daytypes)
nz_energy_system.set_daytype(3)
print(nz_energy_system.daytype)

# Defines the seasons
nz_energy_system.set_season(4)
print(nz_energy_system.season)

# Defines the dailytimebracket
nz_energy_system.set_daily_time_bracket(3)
print(nz_energy_system.dailytimebracket)

# Defines the YearSplit parameter
# Creates Dictionary for number of days
days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

# Combines summer, winter and intermediate nights
days_summer = days['January'] + days['February'] + days['December']
days_winter = days['June'] + days['July'] + days['August']
days_intermediate = days['April'] + days['May'] + days['March'] + days[
    'September'] + days['October'] + days['November']
days_total = days_summer + days_winter + days_intermediate

# Creates fractions and stores values in a dictionary
day_summer = (0.5 * days_summer / days_total)
night_summer = (0.5 * days_summer / days_total)
day_winter = (0.5 * days_winter / days_total)
night_winter = (0.5 * days_winter / days_total)
day_intermediate = (0.5 * days_intermediate / days_total)
night_intermediate = (0.5 * days_intermediate / days_total)

# Dictionaries
splits = {
    'DAY_SUMMER': day_summer,
    'NIGHT_SUMMER': night_summer,
    'DAY_WINTER': day_winter,
    'NIGHT_WINTER': night_winter,
    'DAY_INTERMEDIATE': day_intermediate,
    'NIGHT_INTERMEIATE': night_intermediate
}

# Imports S&P NZX:50 and S&P ASX:200 Indices Arrays to calculate market returns

# Defines the Dictionaries required for country profiles
equity = {'NEWZEALAND': 1, 'AUSTRALIA': 1}
debt = {'NEWZEALAND': 110477000000, 'AUSTRALIA': 1}
cost_of_equity = {'NEWZEALAND': 1, 'AUSTRALIA': 1}
cost_of_debt = {'NEWZEALAND': 1, 'AUSTRALIA': 1}
risk_free_rates = {'NEWZEALAND': 1, 'AUSTRALIA': 1}
market_returns = {'NEWZEALAND': 1, 'AUSTRALIA': 1}
effective_tax_rate = {'NEWZEALAND': 0.28, 'AUSTRALIA': 0.30}

# Creates the YearSplit parameter 2D Matrix (make sure order is preserved when passing in functions)
