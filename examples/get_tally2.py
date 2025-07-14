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
path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'png_tmp.o'
outp = pymcnp.Outp.from_file(path)
tallies = outp.to_dataframe()
tally = tallies[TALLY]
tally = tally.loc[tally['surface'] == SURFACE]

print(tally)
