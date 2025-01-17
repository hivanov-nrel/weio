""" 
Input/output class for the fileformat XXX
"""
import numpy as np
import pandas as pd
import os

try:
    from .file import File, WrongFormatError, BrokenFormatError
except:
    EmptyFileError    = type('EmptyFileError', (Exception,),{})
    WrongFormatError  = type('WrongFormatError', (Exception,),{})
    BrokenFormatError = type('BrokenFormatError', (Exception,),{})
    File=dict

class XXXFile(File):
    """ 
    Read/write a XXX file. The object behaves as a dictionary.
    
    Main methods
    ------------
    - read, write, toDataFrame, keys
    
    Examples
    --------
        f = XXXXFile('file.xxx')
        print(f.keys())
        print(f.toDataFrame().columns)  
    
    """

    @staticmethod
    def defaultExtensions():
        """ List of file extensions expected for this fileformat"""
        return ['.XXX']

    @staticmethod
    def formatName():
        """ Short string (~100 char) identifying the file format"""
        return 'XXX file'

    def __init__(self, filename=None, **kwargs):
        """ Class constructor. If a `filename` is given, the file is read. """
        self.filename = filename
        if filename:
            self.read(**kwargs)

    def read(self, filename=None, **kwargs):
        """ Reads the file self.filename, or `filename` if provided """
        
        # --- Standard tests and exceptions (generic code)
        if filename:
            self.filename = filename
        if not self.filename:
            raise Exception('No filename provided')
        if not os.path.isfile(self.filename):
            raise OSError(2,'File not found:',self.filename)
        if os.stat(self.filename).st_size == 0:
            raise EmptyFileError('File is empty:',self.filename)
        # --- Calling (children) function to read
        self._read(**kwargs)

    def write(self, filename=None):
        """ Rewrite object to file, or write object to `filename` if provided """
        if filename:
            self.filename = filename
        if not self.filename:
            raise Exception('No filename provided')
        # Calling (children) function to write
        self._write()

    def _read(self):
        """ Reads self.filename and stores data into self. Self is (or behaves like) a dictionary"""
        # --- Example: 
        #self['data']=[]
        #with open(self.filename, 'r', errors="surrogateescape") as f:
        #    for i, line in enumerate(f):
        #        self['data'].append(line)
        raise NotImplementedError()

    def _write(self):
        """ Writes to self.filename"""
        # --- Example:
        #with open(self.filename,'w') as f:
        #    f.write(self.toString)
        raise NotImplementedError()

    def toDataFrame(self):
        """ Returns object into one DataFrame, or a dictionary of DataFrames"""
        # --- Example (returning one DataFrame):
        #  return pd.DataFrame(data=np.zeros((10,2)),columns=['Col1','Col2'])
        # --- Example (returning dict of DataFrames):
        #cols=['Alpha_[deg]','Cl_[-]','Cd_[-]','Cm_[-]']
        #dfs['Polar1'] = pd.DataFrame(data=..., columns=cols)
        #dfs['Polar1'] = pd.DataFrame(data=..., columns=cols)
        # return dfs
        raise NotImplementedError()

    # --- Optional functions
    def __repr__(self):
        """ String that is written to screen when the user calls `print()` on the object. 
        Provide short and relevant information to save time for the user. 
        """
        s='<{} object>:\n'.format(type(self).__name__)
        s+='|Main attributes:\n'
        s+='| - filename: {}\n'.format(self.filename)
        # --- Example printing some relevant information for user
        #s+='|Main keys:\n'
        #s+='| - ID: {}\n'.format(self['ID'])
        #s+='| - data : shape {}\n'.format(self['data'].shape)
        s+='|Main methods:\n'
        s+='| - read, write, toDataFrame, keys'
        return s
    
    def toString(self):
        """ """
        s=''
        return s



