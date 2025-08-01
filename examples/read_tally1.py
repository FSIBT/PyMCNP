"""
Example reading OUTP type-1 tallies.
"""

import pathlib

import pymcnp

TALLY = '1'
SURFACE = '2.1'
ANGLE_FROM = '180.0'
BIN_WIDTH = 5

# Reading OUTP.
path = pathlib.Path(__file__).parent.parent / 'files' / 'outp' / 'example_00.outp'
outp = pymcnp.Outp.from_file(path)

# Reading tallies.
tallies = outp.to_dataframe()
tally = tallies[TALLY]
tally = tally.loc[tally['surface'] == SURFACE]
tally = tally.loc[tally['angle_from'] == ANGLE_FROM]

print(tally)
