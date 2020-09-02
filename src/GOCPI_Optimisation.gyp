###############################################################################
# GOCPI_Optimsation runs the optimsation through docplex
###############################################################################

# Imports the necessary python modules
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

###############################################################################
# Processing
###############################################################################
Processing = GF.Navigation()
directory = '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Inputs/GOCPI OseMOSYS'
data = 'GOCPI_Data.txt'
model = 'GOCPI_Model.txt'
output = 'GOCPI.lp'
string = 'glpsol -m ' + data + ' -d ' + model + '--wlp ' + output
.create_linear_programme_file(directory, data, model, output)
