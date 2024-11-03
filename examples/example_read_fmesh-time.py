"""
Example read FMESH tally with additional time bins
"""

import pymcnp
import matplotlib.pyplot as plt
import numpy as np

file = 'data/output_files/meshtal-t'
out = pymcnp.outp.output.ReadFmesh(file)
df_info = out.df_info
# read and plot time series data
time_bins = df_info["tbins"][1:5]
for t in time_bins:
    df_mesh = out.read_data(time_bin=eval(t))
    xz, mat_xz = pymcnp.outp.output.griddata(df_mesh.X, df_mesh.Z, df_mesh.Result, nbins=15)
    plt.figure(figsize=(8, 8))
    plt.imshow(
        mat_xz,
        extent=[df_mesh.X.min(), df_mesh.X.max(), df_mesh.Z.min(), df_mesh.Z.max()],
        origin='lower',
        cmap='inferno',
    )
    plt.xlabel("X (cm)")
    plt.ylabel("Z (cm)")
    clb = plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.2)
    clb.ax.set_title("n/cm2/s")
    plt.title(f"Neutron Flux at t = {eval(t)*10} ns")
