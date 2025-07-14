"""
Example reading OUTP type-4 tallies.
"""

import pathlib

import pymcnp

TALLY = '18'
CELL = '200'

# Reading tallies.
path = pathlib.Path(__file__).parent.parent / 'files' / 'outp' / 'example_01.outp'
outp = pymcnp.Outp.from_file(path)
tallies = outp.to_dataframe()
tally = tallies[TALLY]
tally = tally.loc[tally['cell'] == CELL]

print(tally)
