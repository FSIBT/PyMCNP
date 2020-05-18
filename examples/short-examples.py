"""
Short examples for mcnptools
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mcnptools.mcnpio as io
from pathlib import Path
import mcnptools.gammaSpect as gs

## Read non-pulsed MCNP output files (photons)
file = Path("../mcnp_runs/MCNP-example-F8-GEB.o")
file2 = Path("../mcnp_runs/MCNP-example-F4.o")

df1 = io.read_output(file, tally=8, n=1, tally_type="e", particle="p")
df2 = io.read_output(file, tally=8, n=2, tally_type="e", particle="p")
df3 = io.read_output(file2, tally=4, n=2, tally_type="e", particle="p")

plt.figure()
plt.plot(df1.energy, df1.cts, label="F8 - LaBr")
plt.plot(df2.energy, df2.cts, label="F8 - NaI")
plt.plot(df3.energy, df3.cts, label="F4")
plt.yscale("log")
plt.legend()


## read FMESH tally
file_mesh = Path("../mcnp_runs/meshtal-example")
df_mesh = io.read_fmesh(file_mesh)
dfz_mesh = df_mesh[(df_mesh.Z > -1) & (df_mesh.Z < 1)]  # central slice
xx, mat = io.griddata(dfz_mesh.X, dfz_mesh.Y, dfz_mesh.Result, nbins=100)

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
plt.title("Neutron Flux in Soil")

## Smoothing techniques
mav = gs.moving_avg_smoothing(df1, num=8)
plt.figure()
plt.plot(df1.energy[80:], df1.cts[80:], lw=2, label="original")
plt.plot(df1.energy[80:], mav[80:], lw=2, alpha=0.8, label="smoothing MAV")
plt.legend()

# F1 tally - Moon - photons
f1file = Path("../mcnp_runs/F1-example-moon.o")
dff1 = io.read_output(f1file, tally=1, n=1, tally_type="e", particle="p")
dff2 = io.read_output(f1file, tally=1, n=2, tally_type="e", particle="p")
dff3 = io.read_output(f1file, tally=1, n=3, tally_type="e", particle="p")

plt.figure()
plt.plot(dff1.energy, dff1.cts, label="Surface 6.1")
plt.plot(dff1.energy, dff2.cts, label="Surface 6.2")
plt.plot(dff1.energy, dff3.cts, label="Surface 6.3")
plt.legend()
plt.xlabel("Energy [MeV]")
plt.ylabel("cts")

# time tally
file_t = Path("../mcnp_runs/png_test.o")
dftime = io.read_output(file_t, tally=2, n=1, tally_type="t", particle="n")
plt.figure()
plt.plot(dftime.time, dftime.cts / dftime.cts.max(), label="output")
plt.xlabel("Time [us]")

# time tally read input source
file_ti = "../mcnp_runs/png_test.i"
dft1, dft2 = io.read_inp_source(file_ti)
plt.figure()
plt.step(dft1.SI / 100, dft1.SP, label="SP1")
plt.plot(dft2.SI / 100, dft2.SP, label="SP2")
plt.xlabel("SI (time [us])")
plt.ylabel("SP")
plt.legend()
