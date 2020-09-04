#################################################################
# Optimisation contains the Optimisation Class to use CPLEX
#################################################################

# Import python modules
import os
import cplex as cp
import docplex as dp
import subprocess as sp


# Begin class breakdown
class Optimisation:
    """ Prepare and runs optimisation with IBM ILOG CPLEX Optimisation Studio
    """
    def __init__(self):
        """ Initialise the optimisation class
        """

    def use_bash_shell(self, command):
        """ Execute bash commands in python scripts

        Args:
            command (str): Command to execute
        """
        # Execute the demand
        sp.Popen([['/bin/bash', '-c', command]])

    def create_linear_programme_file(self, directory, data_file, model_file,
                                     output_file):
        """ Creates the model file through executing model system commands

            Args:
                directory (str): Name of directory to put data into
                data_file (str): Name of energy system data file
                model_file (str): Name of energy system model file
                output_file (str): Name of output linear programme
            """
        # Change the working directory
        os.chdir(directory)
        # Load the custom anaconda environment
        # This assumes the conda environment has already been initialised.
        os.system('conda activate osemosys')
        # Execute the file structure to create the linear programming file
        # (glpsol -m GOCPI_Model.txt -d GOCPI_Data.txt --wlp GOCPI.lp)
        command = 'glpsol -m ' + data_file + ' -d ' + model_file + '--wlp ' + output_file
        os.system(command)

    def run_cplex_cloud(self):
        """ This functions runs the cplex module to create the docplex
        """

    def run_cplex_local(self):
        """ This function runs cplex on the local device if the energy system is capable 
            of solving a model of that size
        """
        # Creates the model structure
        model = cp.Cplex()
        # Set the
