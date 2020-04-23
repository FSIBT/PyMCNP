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
    Edep = np.genfromtxt(file, delimiter=' ', usecols=(0,3,4), skip_header=start+1, max_rows=binsP-1) 
    df = pd.DataFrame(columns=['energy','cts','err'], data=Edep)
    return df

def make_inp(cells, surfaces, materials, dataC, fileName):
    ''' Create MCNPinput file.
    

    Parameters
    ----------
    cells : List of strings.
        cell cards
    surfaces: List of strings.
        surface cards
    materials: List of strings.
        material cards
    dataC: List of strings.
        data cards
        

    Returns
    -------
    creates input file'''
    
    with open(fileName,'w') as f: 
       f.writelines(['%s\n' % c  for c in cells])
       f.writelines('\n')
       f.writelines('%s\n' % s for s in surfaces)
       f.writelines('\n')
       f.writelines(['%s\n' % m  for m in materials])
       f.writelines(['%s\n' % d for d in dataC])
       
       
def make_inp_DE(cells, surfaces, materials, dataC, fileName, Ebin, freq):
    '''Create input file with histogram photon source
    
    Parameters
    ----------
    cells : List of strings.
        cell cards
    surfaces: List of strings.
        surface cards
    materials: List of strings.
        material cards
    dataC: List of strings.
        data cards
    Ebin:
        energy bins
    freq: 
        normalized frequency
        

    Returns
    -------
    creates input file'''
        
    
    with open(fileName,'w') as f: 
       f.writelines(['%s\n' % c  for c in cells])
       f.writelines('\n')
       f.writelines(['%s\n' % s for s in surfaces])
       f.writelines('\n')
       f.writelines(['%s\n' % m  for m in materials])
       f.writelines(['%s\n' % d for d in dataC])
       f.writelines('SI1 ')
       f.writelines('%s &\n'%b for b in Ebin[:-1])
       f.writelines('%s\n'%Ebin[-1])
       f.writelines('SP1 0 &\n')
       f.writelines('%s &\n'%f for f in freq[1:-1])
       f.writelines('%s\n'%freq[-1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    