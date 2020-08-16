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
print(nz_energy_system.emission)

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
# Creates the YearSplit parameter 2D Matrix
nz_energy_system.set_year_split(TIMESLICE, nz_energy_system.year, splits)

# Imports S&P NZX:50 and S&P ASX:200 Indices Arrays to calculate market returns
root = '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Inputs/GOCPI OseMOSYS'
file_root = Path(root)
file_spreadsheet = 'Returns.xls'
location = GF.Navigation(file_root, file_spreadsheet)
market_returns = location.Find_File()
nz_df = pd.read_excel(market_returns, sheet_name='NZ')
aus_df = pd.read_excel(market_returns, sheet_name='AUS')
nz_index = nz_df[["Monthly_Returns"]].to_numpy()
aus_index = aus_df[["Monthly_Returns"]].to_numpy()

# Defines the Dictionaries required for Region. All regions should have the same names
# Creates a dictionary of market indices
market_index = {'NEWZEALAND': nz_index, 'AUSTRALIA': aus_index}
# Tresury Equity Balances as at 2019
# (Australia has negative equity, New Zealand has $139746000000)
# However, Governments do not have market equity so should be zer for both
equity = {'NEWZEALAND': 0, 'AUSTRALIA': 0}
# Tresury Debt Balance as at 2019
debt = {'NEWZEALAND': 110477000000, 'AUSTRALIA': 619219000000}
# Tresury Finance Cost(Interest Expenses on Debt as at 2019
cost_of_debt_pre_tax = {'NEWZEALAND': 4059000000, 'AUSTRALIA': 17088000000}
# Preference Equity (None for governments)
preference_equity = {'NEWZEALAND': 0, 'AUSTRALIA': 0}
market_value_preference_shares = {'NEWZEALAND': 1, 'AUSTRALIA': 1}
# (Set to zero if none otherwise you get an error)
preference_dividends = {'NEWZEALAND': 0, 'AUSTRALIA': 0}
# Calculated from 10 Year Treasury Bonds (10 Year Average)
risk_free_rate = {'NEWZEALAND': 0.0360, 'AUSTRALIA': 0.0335}
# Company Tax Rates
effective_tax_rate = {'NEWZEALAND': 0.28, 'AUSTRALIA': 0.30}
# Beta for region modelled
market_risk_coefficient = {'NEWZEALAND': 0, 'AUSTRALIA': 0}

# Set discount rates
nz_energy_system.set_discount_rate(equity, debt, market_index,
                                   cost_of_debt_pre_tax, risk_free_rate,
                                   effective_tax_rate, preference_equity,
                                   market_value_preference_shares,
                                   preference_dividends,
                                   market_risk_coefficient)
print(np.size(nz_energy_system.DiscountRate))

case = nz_energy_system
system = GF.Energy_Systems(
    nz_energy_system.year, nz_energy_system.region, nz_energy_system.emission,
    nz_energy_system.technology, nz_energy_system.fuel,
    nz_energy_system.timeslice, nz_energy_system.mode_of_operation,
    nz_energy_system.storage, nz_energy_system.daytype,
    nz_energy_system.season, nz_energy_system.dailytimebracket)

load_status = {
    # sets
    "year": 1,
    "region": 1,
    "emission": 1,
    "technology": 1,
    "fuel": 1,
    "timeslice": 1,
    "mode_of+operation": 1,
    "storage": 1,
    "daytype": 1,
    "season": 1,
    "dailtytimebracket": 1,
    # Parameters
    "YearSplit": 1,
    "DiscountRate": 1,
    "DaySplit": 0,
    "Conversionls": 0,
    "Conversionld": 0,
    "Conversionlh": 0,
    "DaysInDayType": 0,
    "TradeRoute": 0,
    "DepreciationMethod": 0,
    "SpecifiedAnnualDemand": 0,
    "SpecifiedDemandProfile": 0,
    "AccumulatedAnnualDemand": 0,
    "CapacityToActivityUnit": 0,
    "CapacityFactor": 0,
    "AvailabilityFactor": 0,
    "OperationalLife": 0,
    "ResidualCapacity": 0,
    "InputActivityRatio": 0,
    "OutputActivityRatio": 0,
    "CapitalCost": 0,
    "VariableCost": 0,
    "FixedCost": 0,
    "TechnologyToStorage": 0,
    "TechnologyFromStorage": 0,
    "StorageLevelStart": 0,
    "StorageMaxChargeRate": 0,
    "StorageMaxDischargeRate": 0,
    "MinStorageCharge": 0,
    "OperationalLifeStorage": 0,
    "CapitalCostStorage": 0,
    "ResidualStorageCapacity": 0,
    "CapacityOfOneTechnologyUnit": 0,
    "TotalAnnualMaxCapacity": 0,
    "TotalAnnualMinCapacity": 0,
    "TotalAnnualMaxCapacityInvestment": 0,
    "TotalAnnualMinCapacityInvestment": 0,
    "TotalTechnologyAnnualActivityLowerLimit": 0,
    "TotalTechnologyAnnualActivityUpperLimit": 0,
    "TotalTechnologyModelPeriodActivityUpperLimit": 0,
    "TotalTechnologyModelPeriodActivityLowerLimit": 0,
    "ReserveMarginTagTechnology": 0,
    "ReserveMarginTagFuel": 0,
    "ReserveMargin": 0,
    "RETagTechnology": 0,
    "RETagFuel": 0,
    "REMinProductionTarget": 0,
    "EmissionActivityRatio": 0,
    "EmissionsPenalty": 0,
    "AnnualExogenousEmission": 0,
    "AnnualEmissionLimit": 0,
    "ModelPeriodExogenousEmission": 0,
    "ModelPeriodEmissionLimit": 0,
}
