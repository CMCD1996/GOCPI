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
import subprocess as sb
import docplex as dp
from watson_machine_learning_client import WatsonMachineLearningAPIClient

###############################################################################
# Processing
###############################################################################
# Create WatsonMachineLearningAPIClient to use your cloud platform
# API Key: (Bxhv-kuLYXfle61GiFIbR_uM7n_LA0Ou4X-RrMcgztE0) - IBM Cloud Access
# Instance ID: (0194934c-fdaf-4cac-a086-1a66c30325bb) - Specific Service from Resource List (IBM Watson)
api_wml_credentials = {
    "apikey":
    "Bxhv-kuLYXfle61GiFIbR_uM7n_LA0Ou4X-RrMcgztE0",  # User Account API
    "instance_id":
    "2dc64ea2-6be8-43d0-b217-ec2a5743e8c9",  # Watson Machine Learning
    "url": "https://us-south.ml.cloud.ibm.com"
}
# client = WatsonMachineLearningAPIClient(api_wml_credentials)

Optimise = GF.Optimisation()
directory = '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Inputs/GOCPI OseMOSYS/'
data = 'GOCPI_Data.txt'
model = 'GOCPI_Model.txt'
output = 'GOCPI.lp'
results = directory + "GOCPI_Output.txt"
string = 'glpsol -m ' + data + ' -d ' + model + '--wlp ' + output
# os.chdir(directory)
# os.system('conda init bash')
# os.system('conda activate osemosys')

# Test the local use of cplex
energy_system_cplex = cp.Cplex()
# Read in the model file
lp_file = directory + output
output = energy_system_cplex.set_results_stream(None)
output = energy_system_cplex.set_log_stream(None)
# Write the loaded model to the energy system
energy_system_cplex.read(lp_file)
# Solve the model
energy_system_cplex.solve()
# Returns the objective value
objective_value = energy_system_cplex.solution.get_objective_value()
values = energy_system_cplex.solution.get_values([0])
print(values)

# Creates a prints model outputs
with cp.Cplex() as c, open(results, "w") as f:
    output = c.set_results_stream(f)
    output.write("GOCPI Example")

# return_code = sb.call("conda init bash", shell=True)
# return_code = sb.call("conda activate osemosys", shell=True)
# os.system('conda activate osemosys')
# Optimise.create_linear_programme_file(directory, data, model, output)
