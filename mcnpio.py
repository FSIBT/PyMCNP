# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:56:29 2020

@author: mauricio

Functions to create and read MCNP io files
"""

import numpy as np
import pandas as pd
from scipy.interpolate import griddata as gd

def read_output(file, tally=8, n=1, tally_type='e', particle='n'):
    ''' Read non-pulsed standard MCNP ouput file.
    

    Parameters
    ----------
    file : Path object.
        MCNP output file in plain text format
    tally: integer.
        tally type based on MCNP manual. Default is 8: pule-height tally
    n: integer.
        tally number to output. Defaul is the first one found.
    tally_type: string.
        either energy 'e', time 't', or both 'et'.
        

    Returns
    -------
    df : pandas dataframe.
        dataframe with columns: energy, cts, err

    '''
    flag = False
    if tally_type == 't':
        key_word = 'time'
    elif tally_type == 'e':
        key_word = 'energy'
    elif tally_type == 'et':
        flag = True
        
    if particle == 'n':
        particle = 'neutrons'
    elif particle == 'p':
        particle = 'photons'
    lidx = []
    endbin = [] 
    pidx = []
    en = []
    surf = []
    print('Reading output file...')
    with open(file, 'r') as myfile:
        for i,l in enumerate(myfile):
            tmp = l.split()
            if 'tally' in tmp and 'type' in tmp and str(tally) in tmp:
                lidx.append(i)
            if 'particle(s):' in tmp and particle in tmp:
                pidx.append(i)
            if key_word in tmp:
                en.append(i)
            if ('total') in tmp:
                endbin.append(i)     
            if 'surface' in tmp:
                surf.append(i)
    first = [x for x in en if x > pidx[0]][0] # begining of data
    others = [x for x in surf if x > first] # rest of data
    if len(others) > 0: # this is usually necessary for F1 tally
        [lidx.append(x) for x in others]
    
    print(f'Found {len(lidx)} tallies')
    print(f'Output tally number {n}') 
    
    if flag ==  True: # this is a time and energy tally
        erg = []
        cts = []
        err = []
        start = [x for x in en if x > pidx[n-1]][0] + 1
        totals = np.array([x for x in endbin if x > pidx[n-1]][:-1]) + 4
        idxall = np.append(start, totals)
        ebins = idxall[1] - idxall[0] - 4
        energy = np.genfromtxt(file, delimiter=' ', usecols=(0), skip_header=idxall[0],
                               max_rows=ebins)
        df = pd.DataFrame(columns=['energy'], data=energy)
        
        for ix in idxall:
            tme0 = np.genfromtxt(file, delimiter=' ', skip_header=ix-2, 
                                 max_rows=1)
            tme0 = tme0[~np.isnan(tme0)]
            cts0 = np.genfromtxt(file, delimiter=' ', usecols=(3,7,11,15,19), skip_header=ix, 
                                 max_rows=ebins)
            err0 = np.genfromtxt(file, delimiter=' ', usecols=(4,8,12,16,20), skip_header=ix, 
                                 max_rows=ebins)
            df0 = pd.DataFrame(columns=tme0, data=cts0)
            df = df.join(df0)
        with open(file, 'r') as f:
            for i,l in enumerate(f):
                tmp = l.split()
                if i == idxall[0]-2:
                    tme = [float(x) for x in tmp[1:]]
                if i >= idxall[0] and i < idxall[1]-4:
                    tmp_erg = float(tmp[0])
                    tmp_cts = [float(x) for x in tmp[1::2]]
                    tmp_err = [float(x) for x in tmp[2::2]]
                    erg.append(tmp_erg)
                    cts.append(tmp_cts)
                    err.append(tmp_err)
                    
        
    start = [x for x in en if x > pidx[n-1]][0] # begining of data
    end = [x for x in endbin if x > pidx[n-1]][0] # end of data
    binsP = end - start # number of bins
    Edep = np.genfromtxt(file, delimiter=' ', usecols=(0,3,4), skip_header=start+1, max_rows=binsP-1) 
    df = pd.DataFrame(columns=[key_word,'cts','err'], data=Edep)
    return df

def read_inp_source(file, s1 =['SI1','SP1'], s2=['SI2','SP2'] ):
    '''
    Parameters
    ----------
    file : str or file Path
        MCNP input file to read.
    s1 : list of strings, optional
        key words for start of SI1 and SP1. The default is ['SI1','SP1'].
    s2 : list of strings, optional
        key words for start of SI2 and SP2. The default is ['SI2','SP2'].

    Returns
    -------
    df1 : pandas DataFrame
        SI1 and SP1.
    df2 : pandas Data Frame
        SI2 and SP2.

    '''
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
    '''
    Parameters
    ----------
    B : integer
        burst time in microseconds.
    P : integer
        period in microseconds.
    BP : integer > 0
        burst packets.
    CG : integer
        capture gate in microseconds.
    SP : integer
        sigma packets.

    Returns
    -------
    numpy array
        [SI1,SP1], and [SI2,SP2].
    '''
    if BP <= 0:
        print('Burst packets must be greater than 0')
    if SP <= 0:
        print('Sigma packets must be greater than 0')
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
    return res.astype(int), res2.transpose().astype(int)

def write_inp_pulsed_source(file_to_read, file_to_write, tbins, S1, S2):
    idx_start = 0
    idx_end = 0
    # find important indices
    with open(file_to_read,'r') as rf: 
        for i,l in enumerate(rf):
            tmp = l.split()
            if 'Source' in tmp and 'definition' in tmp:
                idx_start = i
            if 'SI2' in tmp or 'SP2' in tmp:
                idx_end = i
            if 't0' in tmp:
                idx_tbin = i
    if idx_end > idx_tbin:
        print('ERROR: time bins must come after source definition')            
    with open(file_to_read, 'r') as rf:
        with open(file_to_write, 'w') as wf:
            for i,l in enumerate(rf):
                if i < idx_start:
                    wf.write(l)
                elif i == idx_start:
                    wf.write(l)
                    wf.write('sdef par=n erg=14 TME=D1<D2 \n')
                    wf.write('# SI1 SP1 \n')
                    wf.writelines(['{} {}\n'.format(s[0], s[1])  for s in S1])
                    wf.write('# SI2 SP2 \n')
                    wf.writelines(['{} {}\n'.format(s2[0], s2[1]) for s2 in S2])
                    str1 = 'c' + ' ' + 60*'=' + '\n'
                    str2 = 'c \n'
                    wf.writelines(str1)
                    wf.writelines(str2)
                    tstr = 't0 0 {}i {} \n'.format(tbins-1, S2[1,0])
                    wf.writelines(tstr)
                    next
                elif i > idx_tbin:
                    wf.write(l)
                    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    