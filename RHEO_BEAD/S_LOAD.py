import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.integrate as integrate
from scipy import interpolate
from numpy import nan
from scipy.special import gamma, factorial
import openpyxl
import matplotlib.pylab as pl



class SINGLE_LOAD():
    
    def __init__(self):
        """Initialize ROIs
        
        Parameters
        ----------
        Filename: complete filename of the CI file
        
        
        """
        
        
        
        #self.Input_101 =[]
    def __repr__(self): 
        return '<ROI: fn%s>' % (self.path)
    
    def __str__(self):
        str_res  = '\n|---------------|'
        str_res += '\n| CIts class: '
        str_res += '\n|--------------------+--------------------|'
        str_res += '\n| objects: '
        str_res += '\n|--------------------+--------------------|'
        str_res += '\n| Normal Force       : ' + str(self.folderin)
        str_res += '\n| time               : ' + str(self.folderout)
        str_res += '\n| distance           : ' 
        str_res += '\n| contact point      : ' + str(len(self.tau_seconds))
        str_res += '\n| nROI            : ' + str(self.nROI)
        str_res += '\n| Dispx_list      : ' 
        str_res += '\n| Dispy_list      : ' 
        str_res += '\n|--------------------+--------------------|'
        str_res += '\n| methods: '
        str_res += '\n|--------------------+--------------------|'
        str_res += '\n| prepare_folder : creates a folder if not existing'
        str_res += '\n| get_delays     : get delay list from CI'
        str_res += '\n| cI_to_cI_ts    : load and transform in CI_ts'
        str_res += '\n|--------------------+--------------------|'
        return str_res


    def load_data_from_rhometer_single_Load(self,path):
        a = []
        
        n_raw = pd.read_csv(path, index_col=None,skiprows=5,nrows=1,usecols=[2],sep='\t', decimal=",",encoding='UTF-16 LE')
     
        
        a.append(pd.read_csv(path, index_col=None,skiprows=10,nrows=n_raw.iat[0, 0],names= ['Normal Force','time','Distance'],usecols=[2,4,5],sep='\t', decimal=",",encoding='UTF-16 LE'))
        
        self.F_N = np.asarray(a[0]['Normal Force'])
        self.time  = np.asarray(a[0]['time'])
        self.d  = np.asarray(a[0]['Distance'])
        
        return 