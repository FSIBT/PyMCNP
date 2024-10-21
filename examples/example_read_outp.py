"""
Example for reading tally outputs
Note - for proper reading of the output file, the keyword 'print'
should be ommitted
"""

import pymcnp
import matplotlib.pyplot as plt

fileF1 = "data/F1.o"
out1 = pymcnp.outp.ReadOutput(fileF1)

# information about tallies found
dfi_F1 = out1.df_info

# read one of the three subtallies
df0 = out1.read_tally(n=0, tally_type="e")

# plot tally
plt.figure()
plt.plot(df0["energy"], df0["cts"])
plt.xlabel("Energy (MeV)")
plt.ylabel("Counts (a.u)")
plt.yscale("log")

