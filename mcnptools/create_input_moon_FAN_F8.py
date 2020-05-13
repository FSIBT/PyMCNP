# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:31:11 2020

@author: mauricio

Create input file for photon source distribution with detector response
and FAN composition for the surface of the Moon
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mcnpio as io

# read in source probability distribution
fileF4 = 'Moon/png_moon_V2.o'
df4 = io.read_output(fileF4, tally=4, n=1, tally_type='et', particle='p')

df4.drop(columns=0.0, inplace=True)

# sum over 5 time bins
df4V2 = pd.DataFrame(columns=['energy'], data=df4.energy)
tbins = 20
for i in range(df4.shape[1]):
    sum_cols = df4.iloc[:,tbins*i+1:tbins*i+(1+tbins)].sum(axis=1).to_numpy()
    if sum_cols.sum() == 0:
        next
    else:
        df_tmp = pd.DataFrame(columns=[i], data=sum_cols)
        df4V2 = df4V2.join(df_tmp)

prompt = df4V2.iloc[:,1:52].sum(axis=1)
delay = df4V2.iloc[:,51:].sum(axis=1)

prompt_prob = prompt/prompt.sum()
delay_prob = delay/delay.sum()
plt.figure();
plt.step(df4V2.energy, prompt_prob, label='prompt: 0 - 50 us')
plt.step(df4V2.energy, delay_prob, label='delay: 51 - 200 us')
plt.legend()
plt.title('Probability Distributions')
plt.yscale('log')
plt.xlabel('Energy (MeV)')

# create input file
cells = ['test']
surfaces = ['test']
materials = ['test']
dataC = ['test']

Ebin = np.array(df4V2.energy)
freq_delay = np.array(delay_prob)
freq_prompt = np.array(prompt_prob)

io.make_inp_DE(cells, surfaces, materials, dataC, 'F8-inp-delay.i', Ebin, freq_delay)
io.make_inp_DE(cells, surfaces, materials, dataC, 'F8-inp-prompt.i', Ebin, freq_prompt)

