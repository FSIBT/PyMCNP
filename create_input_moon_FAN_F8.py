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
#fileF4 = 'Moon/png_moon_V2.o'
fileF4 = 'Moon/test2-F4/png_moon_all_V3.o'
df4 = io.read_output(fileF4, tally=4, n=1, tally_type='et', particle='p')

df4.drop(columns=0.0, inplace=True)

df4V3 = df4.add_prefix('t')
first_tentry = df4.columns[1]
prompt = df4V3.loc[:,f't{first_tentry}':'t50.0'].sum(axis=1)
delay = df4V3.loc[:,'t51.0':].sum(axis=1)

prompt_prob = prompt/prompt.sum()
delay_prob = delay/delay.sum()
plt.figure();
plt.step(df4V3.tenergy, prompt_prob, label='prompt: 0 - 50 us')
plt.step(df4V3.tenergy, delay_prob, label='delay: 51 - 200 us')
plt.legend()
plt.title('Probability Distributions')
#plt.yscale('log')
plt.xlabel('Energy (MeV)')

# create input file
cells = ['test']
surfaces = ['test']
materials = ['test']
dataC = ['test']

Ebin = np.array(df4V3.tenergy)
freq_delay = np.array(delay_prob)
freq_prompt = np.array(prompt_prob)

io.make_inp_DE(cells, surfaces, materials, dataC, 'F8-inp-delay2.i', Ebin, freq_delay)
io.make_inp_DE(cells, surfaces, materials, dataC, 'F8-inp-prompt2.i', Ebin, freq_prompt)

