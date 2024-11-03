"""
Example read FMESH tally with additional time and energy bins
"""

import pymcnp
import matplotlib.pyplot as plt
import numpy as np

file = 'data/output_files/meshtal-te'
out = pymcnp.outp.output.ReadFmesh(file)
df_info = out.df_info
# all times, only 14 MeV
df14 = out.read_data(time_bin="Total", energy_bin=14)

# all times and energies
df_all = out.read_data(time_bin="Total", energy_bin="Total")

# specific times and energies
dfet = out.read_data(time_bin=2, energy_bin=3)

# when specifying the wrong parameters or if the file format is not 
# implemented, return the raw data
df_raw = out.read_data(time_bin=False, energy_bin=False)
