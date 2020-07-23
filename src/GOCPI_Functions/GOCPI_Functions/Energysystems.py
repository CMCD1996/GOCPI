import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Energy_Systems:
    """ Energy Systems are a set of user defined systems which includes 
    all of the sets and parameters necessary.
    
    Attributes:
    
    
    TODO: Populate with energy sets when necessary
            
    """
    
    
    def __init__(self):
        """ Empty to set energy systems datasets
        """
    def Utopia(self):
        """Function to return energy system examples for a particular scenario
        
        Args: 
            None
        
        Returns: 
            sets and parameters relating to that energy scenario
    
        """
        self.YEAR = [1990,1991,1992,1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
        self.REGION = ['Utopia']
            
        return self