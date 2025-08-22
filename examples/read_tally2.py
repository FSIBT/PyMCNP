"""
Example reading OUTP type #2 tallies.

This example reads a tally type #2 tables card from `example_03.inp`. First, it
reads the OUTP file using `Outp.from_file`, and second it gets a dataframe
using  `to_dataframe`. Then it prints the resulting dataframe.
"""

import pathlib

import pymcnp

TALLY = '2'
SURFACE = '8'

# Reading tallies.
path = pathlib.Path('example_03.outp')
outp = pymcnp.Outp.from_file(path)
tallies = outp.to_dataframe()
tally = tallies[TALLY]
tally = tally.loc[tally['surface'] == SURFACE]

print(f'Reading tally #{TALLY} cell #{SURFACE} from `{path}`:')
print(tally)
