import os
import numpy as np
class Energy_Systems:
    
    """ 
    Energy Systems are a set of user defined systems which includes 
    all of the sets and parameters necessary.
    
    Attributes:
    
    
    TODO: Populate with energy sets when necessary
            
    """
    def __init__(self, year, region,emission,technology,fuel,timeslice,mode_of_operation,storage,daytype,season,dailytimebracket):
        """ Function to create complete energy system set to prepare datafile, as per the established model.

        Args:
            Sets:
                YEAR = Set of Years
                REGION = Set of Regions
            Parameters:
                ADD
        """
        self.year = year
        self.region = region
        self.emission = emission
        self.technology = technology
        self.fuel = fuel
        self.timeslice = timeslice
        self.mode_of_operation = mode_of_operation
        self.storage = storage
        self.daytype = daytype
        self.season = season
        self.dailytimebracket = dailytimebracket

        ly = len(self.year)
        lr = len(self.region)
        le = len(self.emission) 
        lt = len(self.technology) 
        lf = len(self.fuel) 
        ll = len(self.timeslice)
        lm = len(self.mode_of_operation)
        ls = len(self.storage)
        lld = len(self.daytype)
        lls = len(self.season)
        llh = len(self.dailytimebracket)

        self.ly = ly
        self.lr = lr
        self.le = le
        self.lt = lt
        self.lf = lf
        self.ll = ll
        self.lm = lm
        self.ls = ls
        self.lld = lld 
        self.lls = lls
        self.llh = llh

        self.YearSplit = np.zeros((ll,ly))
        self.DiscountRate = np.zeros((lr))
        self.DaySplit = np.zeros((llh,ly))
        self.Conversionls = np.zeros((ll,ls))
        self.Conversionld = np.zeros((lld,ls))
        self.Conversionlh = np.zeros((llh,ll))
        self.DaysInDayType = np.zeros((lls,lld,ly))
        self.TradeRoute = np.zeros((lr,lr,lf,ly))
        self.DepreciationMethod = np.zeros((lr))
        self.SpecifiedAnnualDemand = np.zeros((lr,lf,ly))
        self.SpecifiedDemandProfile = np.zeros((lr,lf,ll,ly))
        self.AccumulatedAnnualDemand = np.zeros((lr,lf,ly))
        self.CapacityToActivityUnit = np.zeros((lr,lt))
        self.CapacityFactor = np.zeros((lr,lt,ll,ly))
        self.AvailabilityFactor = np.zeros((lr,lt,ly))
        self.OperationalLife = np.zeros((lr,lt))
        self.ResidualCapacity = np.zeros((lr,lt,ly))
        self.InputActivityRatio = np.zeros((lr,lt,lf,lm,ly))
        self.OutputActivityRatio = np.zeros((lr,lt,lf,lm,ly))
        self.CapitalCost = np.zeros((lr,lt,ly))
        self.VariableCost = np.zeros((lr,lt,lm,ly))
        self.FixedCost = np.zeros((lr,lt,ly))
        self.TechnologyToStorage = np.zeros((lr,lt,ls,lm))
        self.TechnologyFromStorage = np.zeros((lr,lt,ls,lm))
        self.StorageLevelStart = np.zeros((lr,ls))
        self.StorageMaxChargeRate = np.zeros((lr,ls))
        self.StorageMaxDischargeRate = np.zeros((lr,ls))
        self.MinStorageCharge = np.zeros((lr,ls,ly))
        self.OperationalLifeStorage = np.zeros((lr,ls))
        self.CapitalCostStorage = np.zeros((lr,ls,ly))
        self.ResidualStorageCapacity = np.zeros((lr,ls,ly))
        self.CapacityOfOneTechnologyUnit = np.zeros((lr,lt,ly))
        self.TotalAnnualMaxCapacity = np.zeros((lr,lt,ly))
        self.TotalAnnualMinCapacity = np.zeros((lr,lt,ly))
        self.TotalAnnualMaxCapacityInvestment = np.zeros((lr,lt,ly))
        self.TotalAnnualMinCapacityInvestment = np.zeros((lr,lt,ly))
        self.TotalTechnologyAnnualActivityLowerLimit= np.zeros((lr,lt,ly))
        self.TotalTechnologyAnnualActivityUpperLimit = np.zeros((lr,lt,ly))
        self.TotalTechnologyModelPeriodActivityUpperLimit = np.zeros((lr,lt))
        self.TotalTechnologyModelPeriodActivityLowerLimit = np.zeros((lr,lt))
        self.ReserveMarginTagTechnology = np.zeros((lr,lt,ly))
        self.ReserveMarginTagFuel = np.zeros((lr,lf,ly))
        self.ReserveMargin = np.zeros((lr,ly))
        self.RETagTechnology = np.zeros((lr,lt,ly))
        self.RETagFuel = np.zeros((lr,lf,ly))
        self.REMinProductionTarget = np.zeros((lr,ly))
        self.EmissionActivityRatio = np.zeros((lr,lt,le,lm,ly))
        self.EmissionsPenalty = np.zeros((lr,le,ly))
        self.AnnualExogenousEmission = np.zeros((lr,le,ly))
        self.AnnualEmissionLimit = np.zeros((lr,le,ly))
        self.ModelPeriodExogenousEmission = np.zeros((lr,le))
        self.ModelPeriodEmissionLimit = np.zeros((lr,le))

    def SetParameters(self):
        """Sets the parameters for the functions
        
        Args: 
            Parameters for the basic problem
        
        Returns: 
            The loaded in parameters and sets
    
        """    
    def CreateDataFile(self,file_location,default_array):
        """Function create the GOCPI OseMOSYS Energy Systems Data File necessary for optimisation
        
        Args: 
            Default: An array of default values for the Energy System parameters
        
        Returns: 
            The GOCPI OseMOSYS file
    
        """
        # Opens the file for write the data
        with open(file_location,'w') as f:
            # Sets up the preamble for the data file
            f.write('# GOCPI OseMOSYS Data File\n')
            f.write('# Insert instructions when the file is running properly\n')
            f.write('#\n')
            # Sets
            f.write('# Sets\n#\n')
            # year
            set_string = ' '.join(self.year)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # region
            set_string = ' '.join(self.region)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # emission
            set_string = ' '.join(self.emission)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # technology
            set_string = ' '.join(self.technology)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # fuel
            set_string = ' '.join(self.fuel)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # timeslice
            set_string = ' '.join(self.timeslice)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # mode_of_operation 
            set_string = ' '.join(self.mode_of_operation)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # storage 
            set_string = ' '.join(self.storage)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # daytype
            set_string = ' '.join(self.daytype)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # season 
            set_string = ' '.join(self.season)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            # dailytimebracket 
            set_string = ' '.join(self.dailytimebracket)
            f.write('set YEAR\t:=\t{0};\n'.format(set_string))
            f.write('#\n')
            # Parameters

            # YearSplit = np.zeros((ll,ly))
            # DiscountRate = np.zeros((lr))
            # DaySplit = np.zeros((llh,ly))
            # Conversionls = np.zeros((ll,ls))
            # Conversionld = np.zeros((lld,ls))
            # Conversionlh = np.zeros((llh,ll))
            # DaysInDayType = np.zeros((lls,lld,ly))
            # TradeRoute = np.zeros((lr,lr,lf,ly))
            # DepreciationMethod = np.zeros((lr))
            # SpecifiedAnnualDemand = np.zeros((lr,lf,ly))
            # SpecifiedDemandProfile = np.zeros((lr,lf,ll,ly))
            # AccumulatedAnnualDemand = np.zeros((lr,lf,ly))
            # CapacityToActivityUnit = np.zeros((lr,lt))
            # CapacityFactor = np.zeros((lr,lt,ll,ly))
            # AvailabilityFactor = np.zeros((lr,lt,ly))
            # OperationalLife = np.zeros((lr,lt))
            # ResidualCapacity = np.zeros((lr,lt,ly))
            # InputActivityRatio = np.zeros((lr,lt,lf,lm,ly))
            # OutputActivityRatio = np.zeros((lr,lt,lf,lm,ly))
            # CapitalCost = np.zeros((lr,lt,ly))
            # VariableCost = np.zeros((lr,lt,lm,ly))
            # FixedCost = np.zeros((lr,lt,ly))
            # TechnologyToStorage = np.zeros((lr,lt,ls,lm))
            # TechnologyFromStorage = np.zeros((lr,lt,ls,lm))
            # StorageLevelStart = np.zeros((lr,ls))
            # StorageMaxChargeRate = np.zeros((lr,ls))
            # StorageMaxDischargeRate = np.zeros((lr,ls))
            # MinStorageCharge = np.zeros((lr,ls,ly))
            # OperationalLifeStorage = np.zeros((lr,ls))
            # CapitalCostStorage = np.zeros((lr,ls,ly))
            # ResidualStorageCapacity = np.zeros((lr,ls,ly))
            # CapacityOfOneTechnologyUnit = np.zeros((lr,lt,ly))
            # TotalAnnualMaxCapacity = np.zeros((lr,lt,ly))
            # TotalAnnualMinCapacity = np.zeros((lr,lt,ly))
            # TotalAnnualMaxCapacityInvestment = np.zeros((lr,lt,ly))
            # TotalAnnualMinCapacityInvestment = np.zeros((lr,lt,ly))
            # TotalTechnologyAnnualActivityLowerLimit= np.zeros((lr,lt,ly))
            # TotalTechnologyAnnualActivityUpperLimit = np.zeros((lr,lt,ly))
            # TotalTechnologyModelPeriodActivityUpperLimit = np.zeros((lr,lt))
            # TotalTechnologyModelPeriodActivityLowerLimit = np.zeros((lr,lt))
            # ReserveMarginTagTechnology = np.zeros((lr,lt,ly))
            # ReserveMarginTagFuel = np.zeros((lr,lf,ly))
            # ReserveMargin = np.zeros((lr,ly))
            # RETagTechnology = np.zeros((lr,lt,ly))
            # RETagFuel = np.zeros((lr,lf,ly))
            # REMinProductionTarget = np.zeros((lr,ly))
            # EmissionActivityRatio = np.zeros((lr,lt,le,lm,ly))
                #Writes new line character at parameter metadata to the text file
            f.write('#\n')
            f.write('param\tEmissionActivityRatio\tdefault\t%s:\n'%default)
            # Writes parameter values to the text files
            for i in range(self.le):
                # Sets index value for format string
                emission = self.emission[i]
                for j in range(self.lm):
                    # Sets index value for format string
                    MOO = self.mode_of_operation[j]
                    for k in range(self.ly):
                        # Sets index value for format string
                        y = self.year[k]
                        # Converts matrix columns to strings columns to strings
                        columns = self.technology
                        column_string = ' '.join(columns)
                        # Converts maxtrix rows to list
                        array = np.array(self.region)
                        array = array.T
                        lt = array.tolist()
                        # Creates 2D matrix for this value
                        mat = self.EmissionActivityRatio[:,:,i,j,k]
                        # Converts combined matrix to list and combines lists
                        matlist = mat.tolist()
                        #Combines the two lists
                        combined_list = list(zip(lt,matlist))
                        # Writes index specific parameter values to the text files 
                        f.write("\t[*,*,{0},{1},{2}]:\t{3}\t:=\n".format(emission,MOO,y,column_string))
                        for line in combined_list:
                            combinedflat = ''.join(str(line))
                            combinedflat = combinedflat.replace('[','')
                            combinedflat = combinedflat.replace(']','')
                            combinedflat = combinedflat.replace("'",'')
                            combinedflat = combinedflat.replace(",",'')
                            combinedflat = combinedflat.replace("(",'')
                            combinedflat = combinedflat.replace(")",'')
                            f.write("{0}\n".format(combinedflat))

                f.write(';\n')
        # EmissionsPenalty = np.zeros((lr,le,ly))
        # AnnualExogenousEmission = np.zeros((lr,le,ly))
        # AnnualEmissionLimit = np.zeros((lr,le,ly))
        # ModelPeriodExogenousEmission = np.zeros((lr,le))
        # ModelPeriodEmissionLimit = np.zeros((lr,le))
        # 
        return 