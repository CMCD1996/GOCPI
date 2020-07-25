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
import GOCPI_CMCD as GF


# Sets sets
YEAR = [1990,1991,1992,1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
REGION = ['UTOPIA']
EMISSION = ['CO2','NOX']
TECHNOLOGY = ['E01','E21','E31','E51','E70','IMPDSL1','IMPGSL1','IMPHCO1','IMPOIL1','IMPURN1', 'RHE','RHO','RL1','SRE','TXD','TXE','TXG','RIV','RHu','RLu','TXu']
FUEL = ['CSV','DSL','ELC','GSL','HCO','HYD','LTH','OIL','URN','RH','RL','TX']
TIMESLICE = ['ID', 'IN','SD','SN','WD','WN']
MODE_OF_OPERATION = [1,2]
STORAGE = ['DAM']
DAYTYPE = ['Dummy']
SEASON = ['Dummy']
DAILYTIMEBRACKET = ['Dummy']

# Sets Additional Sets
BOUNDARY_INSTANCES = ['endc1']

# Sets 
sets = [YEAR,REGION, EMISSION, TECHNOLOGY, FUEL, TIMESLICE, MODE_OF_OPERATION, STORAGE,DAYTYPE,SEASON,DAILYTIMEBRACKET]

# Create the energy system with sets and initialised parameters. The parameter have the necessary parameters
Demo = GF.Energy_Systems(YEAR,REGION, EMISSION, TECHNOLOGY, FUEL, TIMESLICE, MODE_OF_OPERATION, STORAGE,DAYTYPE,SEASON,DAILYTIMEBRACKET)

# This user must now initialise the parameters as they choose to configure the energy system for the optimisation model.
# This is incredibly important. The user must understand the configuration of the energy system to do this! Consult the
# User manual to build this optimisation





