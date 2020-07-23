import os
class Energy_Systems:
    
    """ 
    Energy Systems are a set of user defined systems which includes 
    all of the sets and parameters necessary.
    
    Attributes:
    
    
    TODO: Populate with energy sets when necessary
            
    """
    def __init__(self, year, region):
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

    def Year(self):
        """Function to return energy system examples for a particular scenario
        
        Args: 
            None
        
        Returns: 
            sets and parameters relating to that energy scenario
    
        """    
        return 