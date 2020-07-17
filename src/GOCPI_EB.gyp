# GOCPI_EB prepares the energy balance across time for certain geographies

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
import openpyxl as pyxl
import pathlib
import os
import pydrive


# Very Important Step: Sets directory root for file operations.
source_root = pathlib.Path('/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Energy Balances')

# Load in the EnergyBalance.csv file found from the University of Auckland SourceOECD Database.
# This csv contains the energy balances around the world

# Important Step: Sets the Energy Balances Folder ID in my personal google drive
folderID = '1PCUMeT8c9dJE1ES8JDg62w2rKMASOxSW' # Energy Balance

# Loads in appropriate pydrive functions for access
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# # Creates the authorisation to access the google drive
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Gains authorisation using the clients_secrets.json file in the src directory
# # Creates a google drive object to handle files
# drive = GoogleDrive(gauth)

# # Tests the access to the google drive and finds all IEAEnergyBalances.csv File IDs in the EnergyBalances Directory
# file_list = [] 
# title_list = []
# files = drive.ListFile({'q': "'1MD5ewAKAy2McqyCfjivwavj278giRvmR' in parents and trashed=false"}).GetList()
# for filex in files:
#     print(filex['id'])
#     print(filex['title'])
#     file_list.append(filex['id'])  # IEAEnergyBalance.csvs File IDs
#     title_list.append(filex['title']) # IEAEnergyBalance.csvs Titles

# Gets the linksto the two files wanted 
# Links for IEA Energy Balance for 2018 (A-K) and IEA Energy Balance for 2017 (L-Z)
IEAWEBAK = source_root/'IEAWorldEnergyBalances2017A-K.csv'
IEAWEBLZ = source_root/'IEAWorldEnergyBalances2017L-Z.csv'

# Creates dataframes from IEA World Energy Statistics and Balances CSVs from Stats.OECD.org in the OECDiLibrary
# Note the data is from #https:s//stats.oecd.org/ and #https://www-oecd-ilibrary-org.ezproxy.auckland.ac.nz/
column_headers = ['ID','Unit','Geo_Code','Geo_Description','Prod_Code','Prod_Description','Flow_Code','Flow_Description','Year','Value(TJ)']
f1 = open(IEAWEBAK,'r')
df_A = pd.read_csv(f1,header = None)
df_A.columns = column_headers
df_A.info(verbose = True)
f2 = open(IEAWEBLZ,'r')
df_B = pd.read_csv(f2,header = None)
df_B.columns = column_headers
df_B.info(verbose = True)
frames = [df_A,df_B]
df = pd.concat(frames)
df.info(verbose = True)

# Closes the files
f1.close()
f2.close()

# Find the unique items in each list of the energy balance sheets
uv_prod = df.Prod_Description.unique()
uv_geo = df.Geo_Description.unique()
uv_flow = df.Flow_Description.unique()

# Establishes the rows and columns for the EnergyBalance.xlsm spreadsheet
# Note: Most likely in the calculation, Other will be a sink so Total Energy Supply - Conversion Losses = Total Energy Consumed
# Rows (Energy uses)
Primary = ['Domestic Supply','Imports','Exports','Total Primary Supply']
Conversion = ['Energy Sector Consumption','Electricity Plants','Heat Plants','Petroluem Refineries','Total Conversion']
Consumption = ['Residential','Commercial','Industry','Agriculture','Transport','Other','Non Energy','Bunkers','Total Final Consumption']

# Primary (To complete)
DomesticSupply = ['Production']
Imports = ['Imports']
Exports = ['Exports']
TotalPrimarySupply = ['Total primary energy supply']

# Conversion (To complete)
Energy_Sector_Consumption = ['']
Electricity_Plants = ['']
Heat_Plants = ['']
Petroleum_Refineries = ['']
Total_Conversion = ['']

# Consumption (To complete)
Residential = ['']
Commercial = ['']
Industry = ['']
Agriculture = ['']
Transport= ['']
Other = ['Stock changes','Transfers','Statistical differences']
Non_Energy = ['']
Bunkers = ['International marine bunkers', 'International aviation bunkers']
Total_Final_Consumption = ['']

# Energy Flows
Energy_Flows = ['Production', 'Imports', 'Exports', 'International marine bunkers',
 'International aviation bunkers', 'Stock changes',
 'Total primary energy supply', 'Transfers', 'Statistical differences',
 'Transformation processes', 'Main activity producer electricity plants',
 'Autoproducer electricity plants', 'Main activity producer CHP plants',
 'Autoproducer CHP plants', 'Main activity producer heat plants',
 'Autoproducer heat plants', 'Heat pumps', 'Electric boilers',
 'Chemical heat for electricity production', 'Blast furnaces', 'Gas works',
 'Coke ovens', 'Patent fuel plants', 'BKB/peat briquette plants',
 'Oil refineries','Petrochemical plants', 'Coal liquefaction plants',
 'Gas-to-liquids (GTL) plants', 'For blended natural gas',
 'Charcoal production plants', 'Non-specified (transformation)',
 'Energy industry own use', 'Coal mines', 'Oil and gas extraction',
 'Gasification plants for biogases',
 'Liquefaction (LNG) / regasification plants',
 '"Own use in electricity, CHP and heat plants"', 'Pumped storage plants',
 'Nuclear industry', 'Non-specified (energy)', 'Losses',
 'Total final consumption', 'Industry', 'Mining and quarrying',
 'Construction', 'Manufacturing', 'Iron and steel',
 'Chemical and petrochemical', 'Non-ferrous metals', 'Non-metallic minerals',
 'Transport equipment', 'Machinery', 'Food and tobacco',
 '"Paper, pulp and printing"', 'Wood and wood products',
 'Textile and leather', 'Industry not elsewhere specified', 'Transport',
 'World aviation bunkers', 'Domestic aviation', 'Road', 'Rail',
 'Pipeline transport', 'World marine bunkers', 'Domestic navigation',
 'Non-specified (transport)', 'Residential',
 'Commercial and public services', 'Agriculture/forestry', 'Fishing',
 'Final consumption not elsewhere specified', 'Non-energy use',
 'Non-energy use industry/transformation/energy',
 'Memo: Non-energy use in industry', 'Memo: Non-energy use in construction',
 'Memo: Non-energy use in mining and quarrying',
 'Memo: Non-energy use in iron and steel',
 'Memo: Non-energy use in chemical/petrochemical',
 'Memo: Non-energy use in non-ferrous metals',
 'Memo: Non-energy use in non-metallic minerals',
 'Memo: Non-energy use in transport equipment',
 'Memo: Non-energy use in machinery',
 'Memo: Non-energy use in food/beverages/tobacco',
 'Memo: Non-energy use in paper/pulp and printing',
 'Memo: Non-energy use in wood and wood products',
 'Memo: Non-energy use in textiles and leather',
 'Memo: Non-energy use in industry not elsewhere specified',
 'Non-energy use in transport', 'Non-energy use in other',
 'Electricity output (GWh)',
 'Electricity output (GWh)-main activity producer electricity plants',
 'Electricity output (GWh)-autoproducer electricity plants',
 'Electricity output (GWh)-main activity producer CHP plants',
 'Electricity output (GWh)-autoproducer CHP plants' 'Heat output',
 'Heat output-main activity producer CHP plants',
 'Heat output-autoproducer CHP plants',
 'Heat output-main activity producer heat plants',
 'Heat output-autoproducer heat plants']

#  Columns (Energy Types)
Energy = ['Solid Fuels', 'Natural Gas', 'Crude Oil','Diesel Oil','Kerosene','LPG','Motor Spirit','Naphtha','Heavy Fuel Oil','Other Petroleum Products','Nuclear Energy','Biomass','Hydro power','Wind energy','Solar Energy','Industrial Wastes','Derived Heat','Electricity','Total']

Solid_Fuels = ['']
Natural_Gas = ['']
Crude_Oil = ['']
Diesel_Oil = ['']
Kerosene = ['']
LPG = ['']
Motor_Spirit = ['']
Naphtha = ['']
Heavy_Fuel_Oil = ['']
Other_Petroleum_Products = ['']
Nuclear_Energy = ['']
Biomass = ['']
Hydro_power = ['']
Wind_Energy = ['']
Solar_Energy = ['']
Industrial_Wastes = ['']
Derived_Heat = ['']
Electricity = ['']
Total = ['']


Enery_Types = ['Hard coal (if no detail)', 'Brown coal (if no detail)', 'Anthracite',
 'Coking coal', 'Other bituminous coal', 'Sub-bituminous coal', 'Lignite',
 'Patent fuel', 'Coke oven coke', 'Gas coke', 'Coal tar' 'BKB',
 'Gas works gas', 'Coke oven gas', 'Blast furnace gas',
 'Other recovered gases', 'Peat', 'Peat products', 'Oil shale and oil sands',
 'Natural gas', 'Crude/NGL/feedstocks (if no detail)', 'Crude oil',
 'Natural gas liquids', 'Refinery feedstocks',
 'Additives/blending components', 'Other hydrocarbons', 'Refinery gas',
 'Ethane', 'Liquefied petroleum gases (LPG)',
 'Motor gasoline excl. biofuels', 'Aviation gasoline',
 'Gasoline type jet fuel', 'Kerosene type jet fuel excl. biofuels',
 'Other kerosene', 'Gas/diesel oil excl. biofuels', 'Fuel oil', 'Naphtha',
 'White spirit & SBP', 'Lubricants', 'Bitumen', 'Paraffin waxes',
 'Petroleum coke', 'Other oil products', 'Industrial waste',
 'Municipal waste (renewable)', 'Municipal waste (non-renewable)',
 'Primary solid biofuels', 'Biogases' 'Biogasoline' 'Biodiesels',
 'Bio jet kerosene', 'Other liquid biofuels',
 'Non-specified primary biofuels and waste', 'Charcoal',
 'Elec/heat output from non-specified manufactured gases',
 'Heat output from non-specified combustible fuels', 'Nuclear', 'Hydro',
 'Geothermal', 'Solar photovoltaics', 'Solar thermal',
 '"Tide, wave and ocean"', 'Wind', 'Other sources', 'Electricity', 'Heat',
 'Total', 'Memo: Renewables']

# Creates a pivot table to display the data in the way similar to the Energy Balance Sheet (cols = Energy Product, rows = Energy Flows)
EBPT = pd.pivot_table(df,index=['Geo_Description','Flow_Description'],values=['Value(TJ)'],columns=['Prod_Description'],aggfunc=[np.sum],fill_value=0)
# Filters to the geography the user has selected
Selected_Geo = uv_geo[0] # Update once turned into a custom function
Input_String = 'Geo_Description == ["'+ Selected_Geo +'"]'
EBPTG = EBPT.query(Input_String)

# Write the filtered pivot table to an excel file
writer = pd.ExcelWriter(source_root/"Geo EB.xlsx")
EBPTG.to_excel(writer,Selected_Geo) 
writer.save()












