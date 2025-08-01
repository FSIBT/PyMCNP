"""
Example reading OUTP type-2 tallies.
"""

import pathlib

import pymcnp

TALLY = '2'
SURFACE = '8'
ANGLE = ''
BIN_WIDTH = 5

# Reading tallies.
path = pathlib.Path(__file__).parent.parent / 'files' / 'outp' / 'example_03.outp'
outp = pymcnp.Outp.from_file(path)
tallies = outp.to_dataframe()
tally = tallies[TALLY]
tally = tally.loc[tally['surface'] == SURFACE]

print(tally)
