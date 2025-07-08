"""
Example reading OUTP type-1 tallies.
"""

import pathlib

import pymcnp
import matplotlib.pyplot as plt

TALLY = '1'
SURFACE = '2.1'
BIN_WIDTH = 5

# Reading OUTP.
path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'F1.o'
outp = pymcnp.Outp.from_file(path)

# Reading tallies.
tallies = outp.to_dataframe()
tally = tallies[TALLY]
surface = tally.loc[tally['surface'] == SURFACE]

# Plotting tally.
plt.figure()
plt.bar(surface['bins'], surface['counts'], width=BIN_WIDTH)
plt.xlabel('Bins')
plt.ylabel('Counts')
plt.title(f'Type-1 Tally: Bins vs Counts')
plt.show()
