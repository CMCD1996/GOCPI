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

# Defines the technology set
TECHNOLOGY = [
    'E01', 'E21', 'E31', 'E51', 'E70', 'IMPDSL1', 'IMPGSL1', 'IMPHCO1',
    'IMPOIL1', 'IMPURN1', 'RHE', 'RHO', 'RL1', 'SRE', 'TXD', 'TXE', 'TXG',
    'RIV', 'RHu', 'RLu', 'TXu'
]
nz_energy_system.set_technology(TECHNOLOGY)

# Defines the fuels set
FUEL = [
    'CSV', 'DSL', 'ELC', 'GSL', 'HCO', 'HYD', 'LTH', 'OIL', 'URN', 'RH', 'RL',
    'TX'
]
nz_energy_system.set_fuel(FUEL)

# Defines timeslices
TIMESLICE = [
    'DAY_SUMMER', 'NIGHT_SUMMER', 'DAY_WINTER', 'NIGHT_WINTER',
    'DAY_INTERMEDIATE', 'NIGHT_INTERMEDIATE'
]
nz_energy_system.set_timeslice(TIMESLICE)

# Defines Modes of Operation
nz_energy_system.set_mode_of_operation(2)

# Defines the storage set
STORAGE = ['DAM']
nz_energy_system.set_storage(STORAGE)

# Defines the daytype (numbers represent different daytypes)
# 1 = Weekday (Mon - Fri), 2 = Weekend (Sat & Sun)
nz_energy_system.set_daytype(2)

# Defines the seasons
# (Three seasons (Summer (1), Winter (2) and Intermediate (3)))
nz_energy_system.set_season(3)

# Defines the dailytimebracket (Number of distinct periods in a day)
# 4 = Morning (6hrs), Afternoon (6hrs), Evening (6hrs), Night (6hrs)
nz_energy_system.set_daily_time_bracket(4)

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
    'NIGHT_INTERMEDIATE': night_intermediate
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

# Sets the discount rates
nz_energy_system.set_discount_rate(equity, debt, market_index,
                                   cost_of_debt_pre_tax, risk_free_rate,
                                   effective_tax_rate, preference_equity,
                                   market_value_preference_shares,
                                   preference_dividends,
                                   market_risk_coefficient)

# Creates Dictionary of day splits (assumes constant accross years)
# Preserve the order of the split.
hour_split = {"1": 6, "2": 6, "3": 6, "4": 6}
num_days = 365
num_hours = 24
nz_energy_system.set_day_split(nz_energy_system.dailytimebracket,
                               nz_energy_system.year, hour_split, num_days,
                               num_hours)
print(nz_energy_system.DaySplit)

# Sets a dictionary to match the timeslice with season
link_ls = {
    "DAY_SUMMER": "1",
    "NIGHT_SUMMER": "1",
    "DAY_WINTER": "2",
    "NIGHT_WINTER": "2",
    "DAY_INTERMEDIATE": "3",
    "NIGHT_INTERMEDIATE": "3"
}
nz_energy_system.set_conversion_ls(nz_energy_system.timeslice,
                                   nz_energy_system.season, link_ls)
# Sets a dictionary to match the timeslice with daytype
# Daytypes: 1 = Weekday (Mon - Fri), 2 = Weekend (Sat & Sun)
# Order must be preserved
link_ld = {
    "DAY_SUMMER": np.ones((1, 2)),
    "NIGHT_SUMMER": np.ones((1, 2)),
    "DAY_WINTER": np.ones((1, 2)),
    "NIGHT_WINTER": np.ones((1, 2)),
    "DAY_INTERMEDIATE": np.ones((1, 2)),
    "NIGHT_INTERMEDIATE": np.ones((1, 2))
}
nz_energy_system.set_conversion_ld(nz_energy_system.timeslice,
                                   nz_energy_system.daytype, link_ld)
# Sets a dictionary to match the timeslice with daytype
# 1). Morning (6hrs), 2).Afternoon (6hrs), 3).Evening (6hrs), 4).Night (6hrs)
# Order must be preserved in the arrays
link_lh = {
    "DAY_SUMMER": np.array([1, 1, 0, 0]),
    "NIGHT_SUMMER": np.array([0, 0, 1, 1]),
    "DAY_WINTER": np.array([1, 1, 0, 0]),
    "NIGHT_WINTER": np.array([0, 0, 1, 1]),
    "DAY_INTERMEDIATE": np.array([1, 1, 0, 0]),
    "NIGHT_INTERMEDIATE": np.array([0, 0, 1, 1])
}
override_conversionlh = None
# Sets the Conversionlh parameter

nz_energy_system.set_conversion_lh(nz_energy_system.timeslice,
                                   nz_energy_system.dailytimebracket, link_lh,
                                   override_conversionlh)
# Creates season dictionary for daytypes (Assumed to be the same each year)
link_dtdt = {
    "1": np.array([5, 2]),
    "2": np.array([5, 2]),
    "3": np.array([5, 2])
}
override_dtdt = None
# Sets the DaysInDayType parameter
nz_energy_system.set_days_in_day_type(nz_energy_system.season,
                                      nz_energy_system.daytype,
                                      nz_energy_system.year, link_dtdt,
                                      override_dtdt)

# Creates trade relationships using an 2D numpy array
# Must [NEWZEALAND, AUSTRALIA],[NEWZEALAND, AUSTRALIA]
trade = np.array([[0, 1], [1, 0]])
nz_energy_system.set_trade_route(trade)

# Creates depreciation methods dictionary
depreciation_methods = {"NEWZEALAND": 2, "AUSTRALIA": 2}
override_depreciation = None
nz_energy_system.set_depreciation_method(nz_energy_system.region,
                                         depreciation_methods,
                                         override_depreciation)

# Initialises yet to be written parameters to check progress / load Parameters (Delete later)
ly = len(nz_energy_system.year)
lr = len(nz_energy_system.region)
le = len(nz_energy_system.emission)
lt = len(nz_energy_system.technology)
lf = len(nz_energy_system.fuel)
ll = len(nz_energy_system.timeslice)
lm = len(nz_energy_system.mode_of_operation)
ls = len(nz_energy_system.storage)
lld = len(nz_energy_system.daytype)
lls = len(nz_energy_system.season)
llh = len(nz_energy_system.dailytimebracket)

#nz_energy_system.YearSplit = np.ones((ll, ly))
#nz_energy_system.DiscountRate = np.ones((lr))
#nz_energy_system.DaySplit = np.ones((llh, ly))
#nz_energy_system.Conversionls = np.ones((ll, lls))
#nz_energy_system.Conversionld = np.ones((ll, lld))
#nz_energy_system.Conversionlh = np.ones((ll, llh))
#nz_energy_system.DaysInDayType = np.ones((lls, lld, ly))
#nz_energy_system.TradeRoute = np.ones((lr, lr, lf, ly))
#nz_energy_system.DepreciationMethod = np.ones((lr))
nz_energy_system.SpecifiedAnnualDemand = np.ones((lr, lf, ly))
nz_energy_system.SpecifiedDemandProfile = np.ones((lr, lf, ll, ly))
nz_energy_system.AccumulatedAnnualDemand = np.ones((lr, lf, ly))
nz_energy_system.CapacityToActivityUnit = np.ones((lr, lt))
nz_energy_system.CapacityFactor = np.ones((lr, lt, ll, ly))
nz_energy_system.AvailabilityFactor = np.ones((lr, lt, ly))
nz_energy_system.OperationalLife = np.ones((lr, lt))
nz_energy_system.ResidualCapacity = np.ones((lr, lt, ly))
nz_energy_system.InputActivityRatio = np.ones((lr, lt, lf, lm, ly))
nz_energy_system.OutputActivityRatio = np.ones((lr, lt, lf, lm, ly))
nz_energy_system.CapitalCost = np.ones((lr, lt, ly))
nz_energy_system.VariableCost = np.ones((lr, lt, lm, ly))
nz_energy_system.FixedCost = np.ones((lr, lt, ly))
nz_energy_system.TechnologyToStorage = np.ones((lr, lt, ls, lm))
nz_energy_system.TechnologyFromStorage = np.ones((lr, lt, ls, lm))
nz_energy_system.StorageLevelStart = np.ones((lr, ls))
nz_energy_system.StorageMaxChargeRate = np.ones((lr, ls))
nz_energy_system.StorageMaxDischargeRate = np.ones((lr, ls))
nz_energy_system.MinStorageCharge = np.ones((lr, ls, ly))
nz_energy_system.OperationalLifeStorage = np.ones((lr, ls))
nz_energy_system.CapitalCostStorage = np.ones((lr, ls, ly))
nz_energy_system.ResidualStorageCapacity = np.ones((lr, ls, ly))
nz_energy_system.CapacityOfOneTechnologyUnit = np.ones((lr, lt, ly))
nz_energy_system.TotalAnnualMaxCapacity = np.ones((lr, lt, ly))
nz_energy_system.TotalAnnualMinCapacity = np.ones((lr, lt, ly))
nz_energy_system.TotalAnnualMaxCapacityInvestment = np.ones((lr, lt, ly))
nz_energy_system.TotalAnnualMinCapacityInvestment = np.ones((lr, lt, ly))
nz_energy_system.TotalTechnologyAnnualActivityLowerLimit = np.ones(
    (lr, lt, ly))
nz_energy_system.TotalTechnologyAnnualActivityUpperLimit = np.ones(
    (lr, lt, ly))
nz_energy_system.TotalTechnologyModelPeriodActivityUpperLimit = np.ones(
    (lr, lt))
nz_energy_system.TotalTechnologyModelPeriodActivityLowerLimit = np.ones(
    (lr, lt))
nz_energy_system.ReserveMarginTagTechnology = np.ones((lr, lt, ly))
nz_energy_system.ReserveMarginTagFuel = np.ones((lr, lf, ly))
nz_energy_system.ReserveMargin = np.ones((lr, ly))
nz_energy_system.RETagTechnology = np.ones((lr, lt, ly))
nz_energy_system.RETagFuel = np.ones((lr, lf, ly))
nz_energy_system.REMinProductionTarget = np.ones((lr, ly))
nz_energy_system.EmissionActivityRatio = np.ones((lr, lt, le, lm, ly))
nz_energy_system.EmissionsPenalty = np.ones((lr, le, ly))
nz_energy_system.AnnualExogenousEmission = np.ones((lr, le, ly))
nz_energy_system.AnnualEmissionLimit = np.ones((lr, le, ly))
nz_energy_system.ModelPeriodExogenousEmission = np.ones((lr, le))
nz_energy_system.ModelPeriodEmissionLimit = np.ones((lr, le))

# Sets the case (Toggle depending on the data set you choose to use)
case = nz_energy_system

# Initialises the energy system
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

# Loads the datacase to the system
system.load_datacase(case, system, load_status)

# Sets up location information
data_txt = 'GOCPI_NZ_Example_Data.txt'
model_source_file = 'GOCPI_OseMOSYS_Structure.xlsx'
root = '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Inputs/GOCPI OseMOSYS'
data_roots = Path(root)
data_location_1 = os.path.join(data_roots, data_txt)

# Sets the default parameters
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
system.create_data_file(data_location_1, default_parameters)

# Cereate the Model File
system.create_model_file(root, model_source_file)
