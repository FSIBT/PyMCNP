"""
Example to read FMESH file
"""

import pymcnp
import matplotlib.pyplot as plt

file = 'data/output_files/meshtal'
out = pymcnp.outp.output.ReadFmesh(file)
df_info = out.df_info

# read data
df_mesh = out.read_data()

dfz_mesh = df_mesh[(df_mesh.Z > -1) & (df_mesh.Z < 1)]  # central slice
xx, mat = pymcnp.outp.output.griddata(dfz_mesh.X, dfz_mesh.Y, dfz_mesh.Result, nbins=100)

plt.rc('font', size=14)
plt.figure(figsize=(8, 8))
plt.imshow(
    mat,
    extent=[0, df_mesh.X.max(), df_mesh.Y.min(), df_mesh.Y.max()],
    origin='lower',
    cmap='inferno',
)
plt.xlabel('Distance inside soil [cm]')
plt.ylabel('Surface [cm]')
clb = plt.colorbar(orientation='horizontal', shrink=0.8, pad=0.2)
clb.ax.set_title('n/cm2/s')
plt.title('Neutron Flux in Soil')
