# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:58:53 2020

@author: mauricio

Create input file for photon source distribution
and FAN composition for the surface of the Moon
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mcnpio as io

# composition
elem = ['Al', 'Ca', 'Fe', 'O', 'K', 'Mg', 'Na', 'Si', 'Th', 'Ti']
mass_frac = [0.1701, 0.1359, 0.0148, 0.456, 0.0002, 0.0051, 0.0045, 0.2066, 0.006, 0.0008]

sm = round(sum(mass_frac),2)

if sm != 1.0:
    print('Warning: Sum of mass fractions not equal to 1')
    
mat = []
for el, frac in zip(elem, mass_frac):
    tmp = io.make_material(el,frac)
    mat.append(tmp)

mat_flat = [item for sublist in mat for item in sublist]   

# Timing
burst = 50
period = 200
burst_packets = 1
long_wait = 0
sigma_packets = 1
S1, S2 = io.make_pulsed_source(burst, period, burst_packets, long_wait, sigma_packets)

plt.figure()
plt.title('Neutron Source Definition')
plt.step(S1[:,0]/100, S1[:,1], label='S1')
plt.plot(S2[:,0]/100, S2[:,1], label='S2')
plt.legend()
plt.xlabel('Time (us)')
plt.ylabel('Probability')


# create input file
tbin_width = 2 # time bin width in us
tbins = int(period*burst_packets*100/tbin_width)
f_to_read = 'Moon/png_moon_F4_V2.i'
f_time = 'png_moon_time_V3.i'
io.write_inp_pulsed_source(f_to_read, f_time, tbins, S1, S2)
f_final = 'png_moon_all_V3.i'
io.write_inp_materials(f_time, f_final, mat_flat, 100)


