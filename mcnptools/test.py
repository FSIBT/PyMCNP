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
from pathlib import Path
import gammaSpect as gs

## Read non-pulsed MCNP output files
file = Path("test/MCNP-GEB-O.o")
file2 = Path("test/MCNP_F4_Al.o")

df1 = mcnpio.read_output(file, tally=8, n=1)
df2 = mcnpio.read_output(file, tally=8, n=2)
df3 = mcnpio.read_output(file2, tally=4, n=2)

plt.figure()
plt.plot(df1.energy, df1.cts, label="F8 - LaBr")
plt.plot(df2.energy, df2.cts, label="F8 - NaI")
plt.plot(df3.energy, df3.cts, label="F4")

plt.yscale("log")
plt.legend()

## Create input file

Ebins = np.array(df3.energy)
freq = np.array(df3.cts / df3.cts.sum())

cells = [
    "Detector response single carbon block",
    'c first step: create "photon source',
    "c written by Mauricio Ayllon",
    "c CELLS",
    "12 2 -1.75 -112 IMP:P,N=1 $ C-brick",
    "77 1 -0.00125 112 -999 IMP:P,N=1 $ air everywhere",
    "99 0 999 IMP:P,N=0  ",
]

surfaces = [
    "c SURFACES ",
    "112 RPP -7.2 7.2 -16.6 16.6 72 78 $ C-brick",
    "999 SO 200 $ world",
]

materials = [
    "c MATERIAL DEFINITIONS",
    "M1 8016 -0.21  7014 -0.78 018040 -0.01 $ air",
    "M2 6000.24c 0.333333 $ density = -1.75",
]

dataC = [
    "c DATA CARDS",
    "mode n p",
    "sdef erg=14 x=0 y=0 z=0 par=1 $ isotropic neutron source",
    "F4:n 12",
    "F14:P 12",
    "E14 .1 1000I 10",
    "VOL 2868.48 2j",
    "F5:p 0.0 0.0 75 5",
    "Fm4 52525579.2 2 -5 $ S[n/s]*n[atoms/cm*b]*vol[cm3], mat, reaction type",
    "nps 1e8 $ number of particles",
]


mcnpio.make_inp_DE(cells, surfaces, materials, dataC, "test_input.i", Ebins, freq)

## read FMESH tally

file_mesh = "test/meshtal10"
df_mesh = mcnpio.read_fmesh(file_mesh)
dfz_mesh = df_mesh[(df_mesh.Z > -1) & (df_mesh.Z < 1)]  # central slice
xx, mat = mcnpio.griddata(dfz_mesh.X, dfz_mesh.Y, dfz_mesh.Result, nbins=100)

plt.rc("font", size=14)
plt.figure(figsize=(8, 8))
plt.imshow(
    mat,
    extent=[0, dfz_mesh.X.max(), dfz_mesh.Y.min(), dfz_mesh.Y.max()],
    origin="lower",
    cmap="inferno",
)
plt.xlabel("Distance inside soil [cm]")
plt.ylabel("Surface [cm]")
clb = plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.2)
clb.ax.set_title("n/cm2/s")

## Smoothing techniques
# Moving average
mav = gs.moving_avg_smoothing(df1, num=8)
plt.figure()
plt.plot(df1.energy[80:], df1.cts[80:], lw=2, label="original")
plt.plot(df1.energy[80:], mav[80:], lw=2, alpha=0.8, label="smoothing MAV")
plt.legend()

# test F1 tally

f1file = Path("test/test-NASA/F1_Leeloo_run_1_1.o")
dff1 = mcnpio.read_output(f1file, tally=1, n=1)
dff2 = mcnpio.read_output(f1file, tally=1, n=2)
dff3 = mcnpio.read_output(f1file, tally=1, n=3)

# test time tally
file_t = Path("test/test-NASA/png_test.o")
dftime = mcnpio.read_output(file_t, tally=2, n=1, tally_type="t")
plt.figure()
plt.plot(dftime.time, dftime.cts / dftime.cts.max(), label="output")

# test time tally read input source
file_ti = "test/test-NASA/png_test.i"
dft1, dft2 = mcnpio.read_inp_source(file_ti)
plt.figure()
plt.plot(dft1.SI, dft1.SP, label="SP1")
plt.plot(dft2.SI, dft2.SP, label="SP2")
plt.xlabel("SI (time)")
plt.ylabel("SP")
plt.legend()

# Test read output with time
