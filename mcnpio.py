# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:56:29 2020

@author: mauricio

Functions to create and read MCNP io files
"""

import numpy as np
import pandas as pd

def read_output(file, tally=8, n=1):
    ''' Read non-pulsed standard MCNP ouput file.
    

    Parameters
    ----------
    file : Path object.
        MCNP output file in plain text format
    tally: integer.
        tally type based on MCNP manual. Default is 8: pule-height tally
    n: integer.
        tally number to output. Defaul is the first one found.
        

    Returns
    -------
    df : pandas dataframe.
        dataframe with columns: energy, cts, err

    '''
    lidx = []
    endbin = [] 
    en = []
    print('Reading output file...')
    with open(file, 'r') as myfile:
        for i,l in enumerate(myfile):
            tmp = l.split()
            if 'tally' in tmp and 'type' in tmp and str(tally) in tmp:
                lidx.append(i)
            if 'energy' in tmp:
                en.append(i)
            if ('      total      ') in l:
                endbin.append(i)     
    print(f'Found {len(lidx)} tallies')
    print(f'Output tally {n}') 
    start = [x for x in en if x > lidx[n-1]][0] # begining of data
    end = [x for x in endbin if x > lidx[n-1]][0] # end of data
    binsP = end - start # number of bins
    Edep = np.genfromtxt(file, delimiter=' ', usecols=(0,3,4), skip_header=start+1, max_rows=binsP) 
    df = pd.DataFrame(columns=['energy','cts','err'], data=Edep)
    return df