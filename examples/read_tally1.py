"""
Example reading OUTP type #1 tallies.

This example reads a tally type #1 tables card from `example_00.inp`. First, it
reads the OUTP file using `Outp.from_file`, and second it gets a dataframe
using  `to_dataframe`. Then it prints the resulting dataframe.
"""

import pathlib

import pymcnp

TALLY = '1'
SURFACE = '2.1'
ANGLE_FROM = '180.0'

# Reading OUTP.
path = pathlib.Path('example_00.outp')
outp = pymcnp.Outp.from_file(path)

# Reading tallies.
tallies = outp.to_dataframe()
tally = tallies[TALLY]
tally = tally.loc[tally['surface'] == SURFACE]
tally = tally.loc[tally['angle_from'] == ANGLE_FROM]

print(f'Reading tally #{TALLY} cell #{SURFACE} from `{path}`:')
print(tally)
