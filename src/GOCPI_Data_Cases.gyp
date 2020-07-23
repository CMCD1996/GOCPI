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
import GOCPI_Functions as GF

# Beginning of scripting
# Set the appropriate scripting details

YEAR = [1990,1991,1992,1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
REGION = ['Utopia']

Utopia = GF.Energy_Systems(YEAR,REGION)




