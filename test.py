# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:13:34 2020

@author: mauricio

Testing script
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mcnpio

file = 'test/MCNP-GEB-O.o'
file2 = 'test/MCNP_F4_Al.o'

df1 = mcnpio.read_output(file, tally=8, n=1)
df2 = mcnpio.read_output(file, tally=8, n=2)
df3 = mcnpio.read_output(file2, tally=4, n=2)

plt.figure()
plt.plot(df1.energy, df1.cts, label='F8 - LaBr')
plt.plot(df2.energy, df2.cts, label='F8 - NaI')
plt.plot(df3.energy, df3.cts, label='F4')

plt.yscale('log')
plt.legend()

