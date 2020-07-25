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

    def Parameters(self):
        """Function to return energy system examples for a particular scenario
        
        Args: 
            None
        
        Returns: 
            sets and parameters relating to that energy scenario
    
        """    
    def PrintToFile(self):
        """Function to return energy system examples for a particular scenario
        
        Args: 
            None
        
        Returns: 
            sets and parameters relating to that energy scenario
    
        """  
        return 