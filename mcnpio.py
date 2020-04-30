# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:56:29 2020

@author: mauricio

Functions to create and read MCNP io files
"""

import numpy as np
import pandas as pd
from scipy.interpolate import griddata as gd

def read_output(file, tally=8, n=1, tally_type='e'):
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
    if tally_type == 't':
        key_word = 'time'
    else:
        key_word = 'energy'
    lidx = []
    endbin = [] 
    en = []
    surf = []
    print('Reading output file...')
    with open(file, 'r') as myfile:
        for i,l in enumerate(myfile):
            tmp = l.split()
            if 'tally' in tmp and 'type' in tmp and str(tally) in tmp:
                lidx.append(i)
            if key_word in tmp:
                en.append(i)
            if ('      total      ') in l:
                endbin.append(i)     
            if 'surface' in tmp:
                surf.append(i)
    first = [x for x in en if x > lidx[0]][0] # begining of data
    others = [x for x in surf if x > first] # rest of data
    if len(others) > 0: # this is usually necessary for F1 tally
        [lidx.append(x) for x in others]
    
    print(f'Found {len(lidx)} tallies')
    print(f'Output tally {n}') 
    start = [x for x in en if x > lidx[n-1]][0] # begining of data
    end = [x for x in endbin if x > lidx[n-1]][0] # end of data
    binsP = end - start # number of bins
    Edep = np.genfromtxt(file, delimiter=' ', usecols=(0,3,4), skip_header=start+1, max_rows=binsP-1) 
    df = pd.DataFrame(columns=[key_word,'cts','err'], data=Edep)
    return df

def read_inp_source(file, s1 =['SI1','SP1'], s2=['SI2','SP2'] ):
    data = []
    SI2 = 0
    SP2 = 0
    print('Reading output file...')
    with open(file, 'r') as myfile:
        for i,l in enumerate(myfile):
            tmp = l.split()
            if s1[0] in tmp and s1[1] in tmp:
                next
            try:
                tmp2 = [float(x) for x in tmp]
                data.append(tmp2)
            except ValueError:
                    pass
            if s2[0] in tmp:
                SI2 = [float(x) for x in tmp[1:]]
            if s2[1] in tmp:
                SP2 = [float(x) for x in tmp[1:]]
    source1 = [x for x in data if x != []] # remove empty list
    source2 = np.array([SI2,SP2])
    s1 = np.array(source1)
    s2 = source2.transpose()
    df1 = pd.DataFrame(columns=['SI','SP'], data=s1)
    df2 = pd.DataFrame(columns=['SI', 'SP'], data=s2)
    return df1, df2
    


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
    fileName: string or Path object
        file to write
        

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
    
def make_pulsed_source(B, P, BP, CG, SP):
    res = np.zeros((2*BP+2,2))
    res[1::2,1] = 1
    for i in range(int(res.shape[0]/2)):
        res[2*i][0] = int(i*P)
        res[2*i-1][0] = int((i-1)*P + B)
    res = res[:-1]
    res[-1][0] = res[-3][0] + CG + P
    res[:,0] = res[:,0]*1e2 # to shakes
    # SI2, SP2
    res2 = np.array([[0,res[-1][0]*SP],[0,1]])
    return res.astype(int), res2.astype(int)

# def write_inp_pulsed_source(file_to_read, file_to_write,B,P,BP,CG,SP):
#     with open(file_to_read,'r') as f: 
#        for i,l in enumerate(f):
#            tmp = l.split()
#            if 'SI'
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    