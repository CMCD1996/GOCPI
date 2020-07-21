import os

class Navigation():
    """ Navigation is a class for navigating, manipulating and editing data in the GOCPI model.
    
    Attributes:
        Find_File(string) representing a string to the file path
    
    
    TODO: Fill out all functions below
            
    """
    def __init__(self):
                
        def Find_File(self,target_root,target_file):
            """
            Find_File searches for a target file, from a base directory, to construct
            a target directory.

            Inputs: 
            target_root = The base directory to search from (string).
            target_file = The name of the target file (string).

            Outputs: 
            f = Combinated target file location (string).
            """

            for root, dirs, files in os.walk(target_root):
                for name in files:
                    if name == target_file:
                        f = os.path.abspath(os.path.join(root, name))
            return f