This text file describes the Global Optimisation Carbon Pricing Initiative (GOCPI) project directory structure

The 'data' folder contains all raw data gathered for the project
The 'doc' folder contains any text documents/resources/reports related to the project
The 'bin' folder contains external scripts and compiled programs related to the project
The 'src' folder contains all source code related to the project
The 'results' folder contains all files generated from cleanup and analysis

The following information pertains to processes required to run the models.

Updating the GOCPI_Functions Package, uploading to PyPI, then upgrading the remotes.
To upload new versions 
    1) cd to GOCPI
    2) python setup.py sdist 
    3) twine upload dist/*'

Download new versions 
    1) pip install --upgrade GOCPI'

Resources
    Make your own python package: https://towardsdatascience.com/make-your-own-python-package-6d08a400fc2d'
    PyPi https://pypi.org/manage/project/gocpi-functions/releases/#modal-close'

Running the Energy System Model with glpk solver
    1) Install either miniconda or the full version of Anaconda on your device.
    2) Change to the working directory where both text files are present (Model and Data)
    2) In your directory, create a new conda environment using the command 'conda create -n osemosys glpk
    3) Load the conda environment ''(Do this every time you load a new terminal) using conda activate osemosys
    4) Run the model in the terminal using the command 'glpsol -m Model.txt -d Data.txt -o Results.txt
    5) Write LP File for CPLEX using:  glpsol -m GOCPI_OSeMOSYS_Model.txt -d GOCPI_OSeMOSYS_Data.txt --wlp GOCPI.lp

Running the Energy System Model with CPLEX solver
    1) Use academic/student credentials to join the IBM Academic Initiative
    2) Download IBM ILOG CPLEX Optimizer from IBM Academic Software Terminal
    3) Follow installation instructions to install the CPLEX optimizer for your device
    4) Install Python APIs on the Device using the following line in the directory
       python [File Path]]/setup.py install in bash at terminal route
       e.g. python /Applications/CPLEX_Studio1210/python/setup.py install
       Information relating to the package is found here:
       https://www.ibm.com/analytics/cplex-optimizer
       https://github.com/IBMDecisionOptimization/docplex-doc
       Information relating to examples is here:
       https://github.com/IBMDecisionOptimization/docplex-examples
    5) 

