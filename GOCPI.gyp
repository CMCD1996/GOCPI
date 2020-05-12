# This is a demo file for organising geographies and controlling demo functions.
# Import useful python packages
# Git reposistory
# https://github.com/CMCD1996/GOCPI.git
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import scipy as sc 
import sklearn as skl 

# This script should be updated
# Create an array of numbers as make a plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]

plt.scatter(x, y, label="stars", color="green",
            marker="1", s=30)

plt.xlabel('x axis')
plt.ylabel('y axis')

# Check we can submit file properly to the github
plt.title('Plot')
plt.legend()

plt.show()

# End of script