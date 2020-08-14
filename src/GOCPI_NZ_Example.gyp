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

# Defines the regions
REGION = ['NEWZEALAND', 'AUSTRALIA']
nz_energy_system.set_region(REGION)

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
    'INTERMEDIATE_DAY', 'INTERMEDIATE_NIGHT', 'SUMMER_DAY', 'SUMMER_NIGHT',
    'WINTER_DAY', 'WINTER_NIGHT'
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