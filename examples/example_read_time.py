"""
Example to read a tally with time bins e.g. a pulsed neutron generator
"""

import pymcnp
import matplotlib.pyplot as plt

file = "data/output_files/png.o"
out = pymcnp.outp.ReadOutput(file)

# information about tallies found
dfi = out.df_info
df = out.read_tally(n=0, mode="t")
