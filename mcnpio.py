# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:56:29 2020

@author: mauricio

Functions to create and read MCNP io files
"""

import numpy as np
import pandas as pd
from scipy.interpolate import griddata as gd

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
    
def read_fmesh(file, mesh=False):
    '''
    
    Parameters
    ----------
    file : string
        meshtal file.
    mesh : boolean, optional
        if mesh points are desired. The default is False.

    Returns
    -------
    pandas dataframe
        dataframe columns: Energy, X, Y, Result, RelError

    '''
    endbin = 0
    with open(file, 'r') as myfile:
        for i,l in enumerate(myfile):
            if ('X direction') in l:
                x0 = l.split()
                x = np.asarray(x0[2:], dtype=float)
            if ('Y direction') in l:
                y0 = l.split()
                y = np.asarray(y0[2:], dtype=float)
            if ('Z direction') in l:
                z0 = l.split()
                z = np.asarray(z0[2:], dtype=float)
            if ('Energy bin boundaries') in l:
                endbin = i
    
    data = np.genfromtxt(file, skip_header=endbin+3)   
    df = pd.DataFrame(data=data, columns=['Energy', 'X', 'Y', 'Z', 'Result', 'RelError'])  
    if mesh == True:
        return x, y, z, df
    else:
        return df


    
def griddata(x, y, z, nbins, xrange=None, yrange=None):
    '''
    Parameters
    ----------
    x : numpy array or dataframe
        x-values.
    y : numpy array or dataframe
        y-values.
    z : numpy array or dataframe
        z-values.
    nbins : integer
        number of bins.
    xrange : list, optional
        with minimum and maximum values for x. The default is None.
    yrange : list, optional
        with minimum and maximum values for x. The default is None.

    Returns
    -------
    xx : numpy array
        mesh points.
    result : numpy array
        3D matrix better visualized with imshow.

    '''
    if xrange == None:
        lowx = x.min()
        highx = x.max()
    if yrange == None:
        lowy = y.min()
        highy = y.max()
    else:
        lowx = xrange[0]
        highx = xrange[1]
        lowy = yrange[0]
        highy = yrange[1]
        
    xx = np.linspace(lowx,highx,nbins)
    yy = np.linspace(lowy,highy,nbins)
    xg,yg = np.meshgrid(xx,yy)     
    
    result = gd((x, y), z, (xg,yg)) #, method='nearest')  
    return xx, result   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    