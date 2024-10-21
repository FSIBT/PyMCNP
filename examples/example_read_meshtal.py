"""
Example to read and plot FMESH tallies
"""
import pymcnp
import matplotlib.pyplot as plt

file_fmesh = "data/meshtal"
df = pymcnp.outp.output.read_fmesh(file_fmesh)
dfz = df[(df.Z > -1) & (df.Z < 1)]  # central slice
xx, mat = pymcnp.outp.output.griddata(dfz.X, dfz.Y, dfz.Result, nbins=100)

plt.rc("font", size=14)
plt.figure(figsize=(8, 8))
plt.imshow(
    mat,
    extent=[0, df.X.max(), df.Y.min(), df.Y.max()],
    origin="lower",
    cmap="inferno",
)
plt.xlabel("Distance inside soil [cm]")
plt.ylabel("Surface [cm]")
clb = plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.2)
clb.ax.set_title("n/cm2/s")
plt.title("Neutron Flux in Soil")

# Want F1, F4, F5, F8, Meshtal, ptrac, TME, FU+TAG