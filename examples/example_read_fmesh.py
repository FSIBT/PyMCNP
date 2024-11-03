"""
Example to read FMESH file
"""

import pymcnp
import matplotlib.pyplot as plt
import numpy as np

file = 'data/output_files/meshtal'
out = pymcnp.outp.output.ReadFmesh(file)
df_info = out.df_info

# read data
df_mesh = out.read_data(time_bin=False, energy_bin=False)

xy, mat_xy = pymcnp.outp.output.griddata(df_mesh.X, df_mesh.Y, df_mesh.Result, nbins=5)
xz, mat_xz = pymcnp.outp.output.griddata(df_mesh.X, df_mesh.Z, df_mesh.Result, nbins=15)

plt.rc('font', size=14)
plt.figure(figsize=(8, 8))
plt.imshow(
    mat_xy,
    extent=[df_mesh.X.min(), df_mesh.X.max(), df_mesh.Y.min(), df_mesh.Y.max()],
    origin='lower',
    cmap='inferno',
)
plt.xlabel("X (cm)")
plt.ylabel("Y (cm)")
clb = plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.2)
clb.ax.set_title("n/cm2/s")
plt.title("Neutron Flux")

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
plt.title("Neutron Flux")

# Plotting the scatter plot with color mapping
plt.figure(figsize=(8, 6))
scatter = plt.scatter(df_mesh.X, df_mesh.Z, c=df_mesh.Result, cmap="magma")
plt.colorbar(scatter, label="Neutron flux")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

