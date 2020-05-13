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

fileName = "Moon/png_moon_F4_V2.o"
dfet = io.read_output(fileName, tally=4, n=1, tally_type="et", particle="p")
dfet.drop(columns=0.0, inplace=True)

# sum over 5 time bins
dfet2 = pd.DataFrame(columns=["energy"], data=dfet.energy)
for i in range(dfet.shape[1]):
    sum_cols = dfet.iloc[:, 5 * i + 1 : 5 * i + 6].sum(axis=1).to_numpy()
    if sum_cols.sum() == 0:
        next
    else:
        df_tmp = pd.DataFrame(columns=[i], data=sum_cols)
        dfet2 = dfet2.join(df_tmp)

prompt = dfet2.iloc[:, 1:52].sum(axis=1)
delay = dfet2.iloc[:, 71:].sum(axis=1)

plt.figure()
plt.plot(dfet2.energy, prompt, label="prompt: 0 - 50 us")
plt.plot(dfet2.energy, delay, label="delay: 71 - 200 us")
plt.legend()
plt.title("skipping 20 seconds after end of burst")
plt.yscale("log")
plt.xlabel("Energy (MeV)")
