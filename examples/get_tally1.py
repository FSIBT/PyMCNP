"""
Example reading OUTP type-1 tallies.
"""

import pathlib

import pymcnp
import matplotlib.pyplot as plt

TALLY = '1'
SURFACE = '2.1'
ANGLE = '180.0        to  0.90000E+02 degrees'
BIN_WIDTH = 5

# Reading OUTP.
path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'F1.o'
outp = pymcnp.Outp.from_file(path)

# Reading tallies.
tallies = outp.to_dataframe()
tally = tallies[TALLY]
tally = tally.loc[tally['surface'] == SURFACE]
tally = tally.loc[tally['angle'] == ANGLE]

# Plotting tally.
plt.figure()
plt.step(tally['bins'], tally['counts'])
plt.xlabel('Bins')
plt.ylabel('Counts')
plt.title('Type-1 Tally: Bins vs Counts')
plt.show()
