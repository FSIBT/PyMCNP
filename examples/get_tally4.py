"""
Example reading OUTP type-4 tallies.
"""

import pathlib

import pymcnp

TALLY = '14'
CELL = '12'

# Reading tallies.
path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'F4.o'
outp = pymcnp.Outp.from_file(path)
tallies = outp.to_dataframe()
tally = tallies[TALLY]
tally = tally.loc[tally['cell'] == CELL]

print(tally)
