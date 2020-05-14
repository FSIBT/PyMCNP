# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:14:05 2020

@author: mauricio
preliminary timeseries analysis
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mcnpio as io

fileName = 'Moon/png_moon_all_V3.o'
#fileName = 'Moon/test1-F4/png_moon_F4_V2.o'
dfet = io.read_output(fileName, tally=4, n=1, tally_type='et', particle='p')
dfet.drop(columns=0.0, inplace=True)

dfet2 = dfet.add_prefix('t')
first_tentry = dfet.columns[1]
prompt = dfet2.loc[:,f't{first_tentry}':'t50.0'].sum(axis=1)
delay = dfet2.loc[:,'t51.0':].sum(axis=1)

plt.figure();
plt.plot(dfet2.tenergy, prompt/prompt.sum(), label='prompt: 0 - 50 us')
plt.plot(dfet2.tenergy, delay/delay.sum(), label='delay: 51 - 200 us')
plt.legend()
plt.title('Gamma probability distribution at detector')
#plt.yscale('log')
plt.xlabel('Energy (MeV)')