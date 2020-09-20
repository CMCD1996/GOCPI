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
import docplex.mp as dpmp
import tarfile as tf
from ibm_watson_machine_learning import APIClient

###############################################################################
# Processing
###############################################################################
# Initialise Optimisation Class
energy_system_optimisation = GF.Optimisation()
# Use Cplex on the IBM Cloud to create the optimisation techniques.
# Create APIClient to use your cloud platform
# API Key: (Bxhv-kuLYXfle61GiFIbR_uM7n_LA0Ou4X-RrMcgztE0) - IBM Cloud Access
apikey = "Bxhv-kuLYXfle61GiFIbR_uM7n_LA0Ou4X-RrMcgztE0"
url = "https://us-south.ml.cloud.ibm.com"
directory = '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Inputs/GOCPI OseMOSYS/'
data = 'GOCPI_Data.txt'
model = 'GOCPI_Model.txt'
output = 'GOCPI.lp'
payload_input = directory + output
payload_output = directory + "GOCPI.csv"
results = directory + "GOCPI_Output.txt"
tar_file = directory + "GOCPI.tar.gz"
csv = "GOCPI.csv"
csv_file = directory + csv
lp_file = directory + output
space_exists = True
deployment_exists = True
create_data_assets = False
string = 'glpsol -m ' + data + ' -d ' + model + '--wlp ' + output

api_wml_credentials = {
    "apikey": apikey,  # User Account API
    #"instance_id":
    #"2dc64ea2-6be8-43d0-b217-ec2a5743e8c9",  # Watson Machine Learning
    "url": url
}

# Initialises client credentials
client = APIClient(api_wml_credentials)

# Create a deployment space and set it
space_name = 'gocpi_deployment_space'
cos_resource_crn = 'crn:v1:bluemix:public:cloud-object-storage:global:a/09d7320da1734f7e84aaedf597c37111:83e6751a-cefc-49ce-93de-4fbaee7e52af::'
instance_crn = 'crn:v1:bluemix:public:pm-20:us-south:a/09d7320da1734f7e84aaedf597c37111:2dc64ea2-6be8-43d0-b217-ec2a5743e8c9::'

metadata = {
    client.spaces.ConfigurationMetaNames.NAME: space_name,
    client.spaces.ConfigurationMetaNames.DESCRIPTION:
    space_name + ' for Deployment ',
    client.spaces.ConfigurationMetaNames.STORAGE: {
        "type": "bmcos_object_storage",
        "resource_crn": cos_resource_crn
    },
    client.spaces.ConfigurationMetaNames.COMPUTE: {
        "name": "existing_instance_id",
        "crn": instance_crn
    }
}
# Set the default spaces based on the outcomess
if space_exists == True:
    client.spaces.list()
    space_id = input('Please input the Space ID: ')
else:
    space = client.spaces.store(meta_props=metadata)
    space_id = client.spaces.get_id(space)

# Set the client space
client.set.default_space(space_id)

# Create input and output data assets
if create_data_assets == True:
    client.data_assets.create('GOCPI_Energy_System_Lp_File', lp_file)
    client.data_assets.create('GOCPI_Energy_System_CSV_File', csv_file)


# Deploy model files
# Get location of model deployment
# Create  tar file for model deployment
# Reset tarfile function (Source: IBM Watson Machine Learning)
def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    return tarinfo


# Create the tar file
tar = tf.open(tar_file, "w:gz")
tar.add(lp_file, arcname="GOCPI.lp", filter=reset)
tar.close()

# List deployments using python API
print(client.deployments.list())

# Get the list of software available
client.software_specifications.list()
software_name = input("Please Input Software Name: ")
software_spec_uid = client.software_specifications.get_uid_by_name(
    software_name)

# Create the model deployment using the created arc file
energy_system_model_metadata = {
    client.repository.ModelMetaNames.NAME: "Energy System",
    client.repository.ModelMetaNames.DESCRIPTION: "Model for Energy System",
    client.repository.ModelMetaNames.TYPE: "do-cplex_12.10",
    client.repository.ModelMetaNames.RUNTIME_UID: "do_12.10",
    client.repository.ModelMetaNames.SOFTWARE_SPEC_UID: software_spec_uid
}

energy_system_model_details = client.repository.store_model(
    model=tar_file, meta_props=energy_system_model_metadata)

energy_system_model_uid = client.repository.get_model_uid(
    energy_system_model_details)

# Create deployment
n_nodes = 1

meta_props = {
    client.deployments.ConfigurationMetaNames.NAME:
    "Energy System Deployment " + str(n_nodes),
    client.deployments.ConfigurationMetaNames.DESCRIPTION:
    "Energy System",
    # client.deployments.ConfigurationMetaNames.HARDWARE_SPEC:
    client.deployments.ConfigurationMetaNames.BATCH: {},
    client.deployments.ConfigurationMetaNames.COMPUTE: {
        'name': 'S',
        'nodes': n_nodes
    }
}

# Test if deployment already exists
if deployment_exists == True:
    client.deployments.list()
    deployment_uid = input('Please input the Deployment UID: ')
else:
    deployment_details = client.deployments.create(energy_system_model_uid,
                                                   meta_props=meta_props)
    deployment_uid = client.deployments.get_uid(deployment_details)

# Designs Payload for deployment
# solve_payload = {
#     client.deployments.DecisionOptimizationMetaNames.SOLVE_PARAMETERS: {
#         'oaas.logAttachmentName': 'log.txt',
#         'oaas.logTailEnabled': 'true',
#         'oaas.resultsFormat': 'JSON'
#     },
#     client.deployments.DecisionOptimizationMetaNames.INPUT_DATA_REFERENCES: [{
#         'id':
#         'GOCPI.lp',
#         'type':
#         's3',
#         'connection': {
#             'endpoint_url':
#             COS_ENDPOINT,
#             'access_key_id':
#             cos_resource_crn['cos_hmac_keys']["access_key_id"],
#             'secret_access_key':
#             cos_resource_crn['cos_hmac_keys']["secret_access_key"]
#         },
#         'location': {
#             'bucket': COS_BUCKET,
#             'path': lp_file
#         }
#     }],
#     client.deployments.DecisionOptimizationMetaNames.OUTPUT_DATA_REFERENCES: [{
#         'id':
#         'solution.json',
#         'type':
#         's3',
#         'connection': {
#             'endpoint_url':
#             url,
#             'access_key_id':
#             cos_resource_crn['cos_hmac_keys']["access_key_id"],
#             'secret_access_key':
#             cos_resource_crn['cos_hmac_keys']["secret_access_key"]
#         },
#         'location': {
#             'bucket': COS_BUCKET,
#             'path': 'solution.json'
#         }
#     }, {
#         'id':
#         'log.txt',
#         'type':
#         's3',
#         'connection': {
#             'endpoint_url':
#             url,
#             'access_key_id':
#             cos_credentials['cos_hmac_keys']["access_key_id"],
#             'secret_access_key':
#             cos_credentials['cos_hmac_keys']["secret_access_key"]
#         },
#         'location': {
#             'bucket': COS_BUCKET,
#             'path': 'log.txt'
#         }
#     }]
# }
energy_system_payload = {
    client.deployments.DecisionOptimizationMetaNames.SOLVE_PARAMETERS: {
        "oaas.logTailEnabled": "true"
    }
    # client.deployments.DecisionOptimizationMetaNames.INPUT_DATA: [{
    #     "id": lp_file
    # }],
    # client.deployments.DecisionOptimizationMetaNames.OUTPUT_DATA: [{
    #     "id":
    #     csv_file
    # }]
}
# job_details = client.deployments.create_job(deployment_uid, solve_payload)
# job_uid = client.deployments.get_job_uid(job_details)

# Create jobs for the deployment
# job_details = client.deployments.create_job(deployment_uid,
#                                             energy_system_payload)
# job_uid = client.deployments.get_job_uid(job_details)

# Run job using deployment

# Deletes deployment

# # Find deployment pace ID
# def guid_from_space_name(client, space_name):
#     instance_details = client.service_instance.get_details()
#     space = client.spaces.get_details()
#     return (next(item for item in space['resources']
#                  if item['entity']["name"] == space_name)['metadata']['guid'])

#

# Set the default client space
# instance_details = client.service_instance.get_instance_id()
# client.set.default_space()
# client.set.default_project()
# print(instance_details)
# client.set.default_space()
# client.set.default_project()
# # Create a data asset to the IBM Cloud

# files = {
#     'Energy Balances 1':
#     '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Energy Balances/IEAWorldEnergyBalances2017A-K.csv',
#     'Energy Balances 2':
#     '/Users/connor/Google Drive/Documents/University/Courses/2020/ENGSCI 700A&B/GOCPI/data/Energy Balances/IEAWorldEnergyBalances2017L-Z.csv'
# }

# data_assets_to_create = ['Energy Balances 1', 'Energy Balances 2']
# created_assets = {}
# for assets in data_assets_to_create:
#     asset_details = client.data_assets.create(name="Energy_System_Test",
#                                               file_path=files[assets])
#     created_assets[assets] = asset_details

# Get information of assets

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

# Solve locally using Cplex
energy_system_cplex = cp.Cplex()
# Read in the model file
output = energy_system_cplex.set_results_stream(None)
output = energy_system_cplex.set_log_stream(None)
# Write the loaded model to the energy system
energy_system_cplex.read(lp_file)
# Solve the model
energy_system_cplex.solve()
# Returns the objective value
objective_value = energy_system_cplex.solution.get_objective_value()
values = energy_system_cplex.solution.get_values()
print(np.size(values))

# Creates a prints model outputs
with cp.Cplex() as c, open(results, "w") as f:
    output = c.set_results_stream(f)
    output.write("GOCPI Example")

# Creates Docplex example
# energy_system_docplex = docplex.cp.model.CpoModel(name="GOCPI_Docplex")
energy_system_docplex_lp = dpmp.model_reader.ModelReader.read(
    lp_file, model_name='GOCPI_Docplex_Lp')

mdl = energy_system_docplex_lp.solve(url=url, api=apikey)
# print('mdl', mdl)
# return_code = sb.call("conda init bash", shell=True)
# return_code = sb.call("conda activate osemosys", shell=True)
# os.system('conda activate osemosys')
# Optimise.create_linear_programme_file(directory, data, model, output)
