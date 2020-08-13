import os
import numpy as np
import pandas as pd


class CreateCases:
    """ A class of methods to create user-defined data cases
    """
    def __unit__(self):
        """ Sets the parameters and sets for the datacase
        """
        # Sets (Placeholders for setting values)
        self.year = []
        self.region = []
        self.emission = []
        self.technology = []
        self.fuel = []
        self.timeslice = []
        self.mode_of_operation = []
        self.storage = []
        self.daytype = []
        self.season = []
        self.dailytimebracket = []

        # Parameters
        self.YearSplit = np.ones(1, 1)
        self.DiscountRate = np.ones(1, 1)
        self.DaySplit = np.ones(1, 1)
        self.Conversionls = np.ones(1, 1)
        self.Conversionld = np.ones(1, 1)
        self.Conversionlh = np.ones(1, 1)
        self.DaysInDayType = np.ones(1, 1)
        self.TradeRoute = np.ones(1, 1)
        self.DepreciationMethod = np.ones(1, 1)
        self.SpecifiedAnnualDemand = np.ones(1, 1)
        self.SpecifiedDemandProfile = np.ones(1, 1)
        self.AccumulatedAnnualDemand = np.ones(1, 1)
        self.CapacityToActivityUnit = np.ones(1, 1)
        self.CapacityFactor = np.ones(1, 1)
        self.AvailabilityFactor = np.ones(1, 1)
        self.OperationalLife = np.ones(1, 1)
        self.ResidualCapacity = np.ones(1, 1)
        self.InputActivityRatio = np.ones(1, 1)
        self.OutputActivityRatio = np.ones(1, 1)
        self.CapitalCost = np.ones(1, 1)
        self.VariableCost = np.ones(1, 1)
        self.FixedCost = np.ones(1, 1)
        self.TechnologyToStorage = np.ones(1, 1)
        self.TechnologyFromStorage = np.ones(1, 1)
        self.StorageLevelStart = np.ones(1, 1)
        self.StorageMaxChargeRate = np.ones(1, 1)
        self.StorageMaxDischargeRate = np.ones(1, 1)
        self.MinStorageCharge = np.ones(1, 1)
        self.OperationalLifeStorage = np.ones(1, 1)
        self.CapitalCostStorage = np.ones(1, 1)
        self.ResidualStorageCapacity = np.ones(1, 1)
        self.CapacityOfOneTechnologyUnit = np.ones(1, 1)
        self.TotalAnnualMaxCapacity = np.ones(1, 1)
        self.TotalAnnualMinCapacity = np.ones(1, 1)
        self.TotalAnnualMaxCapacityInvestment = np.ones(1, 1)
        self.TotalAnnualMinCapacityInvestment = np.ones(1, 1)
        self.TotalTechnologyAnnualActivityLowerLimit = np.ones(1, 1)
        self.TotalTechnologyAnnualActivityUpperLimit = np.ones(1, 1)
        self.TotalTechnologyModelPeriodActivityUpperLimit = np.ones(1, 1)
        self.TotalTechnologyModelPeriodActivityLowerLimit = np.ones(1, 1)
        self.ReserveMarginTagTechnology = np.ones(1, 1)
        self.ReserveMarginTagFuel = np.ones(1, 1)
        self.ReserveMargin = np.ones(1, 1)
        self.RETagTechnology = np.ones(1, 1)
        self.RETagFuel = np.ones(1, 1)
        self.REMinProductionTarget = np.ones(1, 1)
        self.EmissionActivityRatio = np.ones(1, 1)
        self.EmissionsPenalty = np.ones(1, 1)
        self.AnnualExogenousEmission = np.ones(1, 1)
        self.AnnualEmissionLimit = np.ones(1, 1)
        self.ModelPeriodExogenousEmission = np.ones(1, 1)
        self.ModelPeriodEmissionLimit = np.ones(1, 1)

    def set_year(self, start_year, end_year):
        """ Creates the list of forecast years

        Args:
            start_year (int): Starting year for forecasting
            end_year (int): Ending year for forecasting
        """

    def set_region(self, regions):
        """ Sets the datacases regions of analysis

        Args:
            regions (list): list
        """