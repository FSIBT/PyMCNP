"""
Example reading OUTP type-2 tallies.
"""

import pathlib

import pymcnp
import matplotlib.pyplot as plt

TALLY = '2'
SURFACE = '8'
BIN_WIDTH = 5

# Reading tallies.
path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'png_tmp.o'
outp = pymcnp.Outp.from_file(path)
tallies = outp.to_dataframe()
tally = tallies[TALLY]
surface = tally.loc[tally['surface'] == SURFACE]

# Plotting tally.
plt.figure()
plt.bar(surface['bins'], surface['counts'], width=BIN_WIDTH)
plt.xlabel('Bins')
plt.ylabel('Counts')
plt.title(f'Type-2 Tally: Bins vs Counts')
plt.show()
