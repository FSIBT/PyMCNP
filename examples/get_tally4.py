"""
Example reading OUTP type-4 tallies.
"""

import pathlib

import pymcnp
import matplotlib.pyplot as plt

TALLY = '14'
CELL = '12'
BIN_WIDTH = 5

# Reading tallies.
path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'F4.o'
outp = pymcnp.Outp.from_file(path)
tallies = outp.to_dataframe()
tally = tallies[TALLY]
cell = tally.loc[tally['cell'] == CELL]

# Plotting tally.
plt.figure()
plt.bar(cell['bins'], cell['counts'], width=BIN_WIDTH)
plt.xlabel('Bins')
plt.ylabel('Counts')
plt.title('Type-4 Tally: Bins vs Counts')
plt.show()
